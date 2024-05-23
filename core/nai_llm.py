import openai
from dotenv import load_dotenv, find_dotenv
from pynput import keyboard
import sounddevice as sd
import wave
import os
import numpy as np
import whisper
from langchain_openai import OpenAI, ChatOpenAI
from queue import Queue
import io
import soundfile as sf
import threading
from config.settings import get_agent_prompt_prefix
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent
import pandas as pd
from langchain.agents.agent_types import AgentType

load_dotenv(find_dotenv())
client = openai.Client()

class NAILLM():
    def __init__(self, model="gpt-3.5-turbo-0613", whisper_size="small"):
        self.is_recording = False
        self.audio_data = []
        self.samplerate = 44100
        self.channels = 1
        self.dtype = 'int16'
        self.input_device = 6
        self.whisper = whisper.load_model(whisper_size)
        self.llm = ChatOpenAI(model=model)
        self.llm_queue = Queue()
        self.create_agent()
        self.listener = None
        self.running = True

    def start_or_stop_recording(self):
        if self.is_recording:
            self.is_recording = False
            self.save_and_transcribe()
            self.audio_data = []
        else:
            print("Starting record")
            self.audio_data = []
            self.is_recording = True

    def create_agent(self):
        agent_prompt_prefix = get_agent_prompt_prefix()

        data_path = os.path.join(os.path.dirname(__file__), 'data', 'df_rent.csv')
        df = pd.read_csv(data_path)
        self.agent = create_pandas_dataframe_agent(
            self.llm,
            df,
            prefix=agent_prompt_prefix,
            verbose=True,
            agent_type=AgentType.OPENAI_FUNCTIONS,
        )

    def save_and_transcribe(self):
        print("Saving the recording...")
        output_dir = os.path.join(os.path.dirname(__file__), '..', 'audio', 'input')
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        output_path = os.path.join(output_dir, 'fala.wav')
        if os.path.exists(output_path):
            os.remove(output_path)
        
        wav_file = wave.open(output_path, 'wb')
        wav_file.setnchannels(self.channels)
        wav_file.setsampwidth(2)  # Corrigido para usar a largura de amostra para int16 diretamente
        wav_file.setframerate(self.samplerate)
        wav_file.writeframes(np.array(self.audio_data, dtype=self.dtype))
        wav_file.close()

        result = self.whisper.transcribe(output_path, fp16=False)
        print("Usuário:", result["text"])

        response = self.agent.invoke(result["text"])
        self.llm_queue.put(response["output"])

    def convert_and_play(self):
        tts_text = ''
        while self.running:
            tts_text += self.llm_queue.get()

            if '.' in tts_text or '?' in tts_text or '!' in tts_text:
                print(tts_text)

                spoken_response = client.audio.speech.create(model="tts-1",
                                                             voice='alloy',
                                                             response_format="opus",
                                                             input=tts_text
                                                             )

                buffer = io.BytesIO()
                for chunk in spoken_response.iter_bytes(chunk_size=4096):
                    buffer.write(chunk)
                buffer.seek(0)

                with sf.SoundFile(buffer, 'r') as sound_file:
                    data = sound_file.read(dtype='int16')
                    sd.play(data, sound_file.samplerate)
                    sd.wait()
                tts_text = ''

    def get_input_device(self):
        return sd.query_devices()

    def run(self):
        t1 = threading.Thread(target=self.convert_and_play)
        t1.start()

        def callback(indata, frame_count, time_info, status):
            if self.is_recording:
                self.audio_data.extend(indata.copy())

        with sd.InputStream(samplerate=self.samplerate,
                            device=self.input_device,
                            channels=self.channels,
                            dtype=self.dtype,
                            callback=callback):
            def on_activate_space():
                self.start_or_stop_recording()

            def on_activate_exit():
                self.running = False
                if self.listener is not None:
                    self.listener.stop()
                os._exit(0)

            def for_canonical(f):
                return lambda k: f(l.canonical(k))

            hotkey_space = keyboard.HotKey(
                keyboard.HotKey.parse('<space>'),
                on_activate_space)
            hotkey_exit = keyboard.HotKey(
                keyboard.HotKey.parse('<ctrl>+<alt>+e'),
                on_activate_exit)

            with keyboard.Listener(
                    on_press=for_canonical(hotkey_space.press),
                    on_release=for_canonical(hotkey_space.release)) as l:
                self.listener = l
                with keyboard.Listener(
                        on_press=for_canonical(hotkey_exit.press),
                        on_release=for_canonical(hotkey_exit.release)) as l_exit:
                    l_exit.join()

if __name__ == "__main__":
    talking_llm = NAILLM()
    talking_llm.run()