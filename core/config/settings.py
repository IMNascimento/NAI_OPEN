import os

def get_agent_prompt_prefix():
    config_path = os.path.join(os.path.dirname(__file__), 'nai_context.txt')
    with open(config_path, 'r', encoding='utf-8') as file:
        agent_prompt_prefix = file.read()
    return agent_prompt_prefix