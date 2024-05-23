from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent
from langchain_openai import ChatOpenAI
import pandas as pd
import os
from langchain.agents.agent_types import AgentType

# Carregar o dataframe
data_path = os.path.join(os.path.dirname(__file__), 'data', 'df_rent.csv')
df = pd.read_csv(data_path)

# Criar o agente
agent = create_pandas_dataframe_agent(
    ChatOpenAI(model="gpt-3.5-turbo-0613"),
    df,
    verbose=True,
    agent_type=AgentType.OPENAI_FUNCTIONS,
)

# Invocar o agente com uma pergunta
response = agent.invoke("Quantas linhas há no conjunto de dados?")
print(response)