<h1 align="center">
  <br>
  <a href="#"><img src="https://github.com/IMNascimento/DVR/assets/28989407/84028706-5a9e-4d00-af2c-2935e5604035" alt="Nascimento" width="200"></a>
  <br>
  NAI
  <br>
</h1>

## Visão geral

NAI (Nascimento Assistente Intelligence) é um assistente avançado de IA projetado para processar e analisar dados usando a biblioteca Pandas do Python. O projeto apresenta uma estrutura robusta para garantir escalabilidade, facilidade de manutenção e organização, tornando-o adequado para aplicações de grande escala. Inclui funcionalidades para gravação de voz, transcrição, análise de dados e respostas interativas.

## Índice

- [Visão geral](#visão_geral)
- [Recursos](#features)
- [Estrutura do Projeto](#estrutura_do_projeto)
- [Configuração e instalação](#configuração_e_instalação)
- [Uso](#uso)
   - [Executando o AI Assistant](#running_the_ai_assistant)
   - [Configuração](#configuração)
   - [Comandos de voz](#comandos_de_voz)
- [Contribuindo](#contribuindo)
- [Licença](#licença)
- [Agradecimentos](#agradecimentos)

## Características

- **Gravação e transcrição de voz**: grave entradas de áudio e transcreva-as usando o Whisper.
- **Análise de dados**: analise e manipule dados usando dataframes do Pandas.
- **Respostas interativas**: obtenha respostas em tempo real do assistente de IA.
- **Design Modular**: Estrutura de projeto organizada para escalabilidade e fácil manutenção.
- **Configurável**: configure facilmente caminhos e configurações usando variáveis de ambiente e arquivos de configuração.

## Estrutura do Projeto

```md
projeto_base/
│
├── core/
│ ├── init.py
│ ├── nai_llm.py
│ ├── nai_agent.py
│ ├── config/
│ │ ├── init.py
│ │ ├── nai_context.txt
│ │ └── settings.py
│ └── data/
│    ├── init.py
│    └── df_rent.csv
| 
|──audio/
│   └── input/
│       ├── init.py
│       └── fala.wav
├── .env
├── venv/
├── LICENÇA
├── README.md
└── requisitos.txt
```

## Configuração e instalação

### Pré-requisitos

-Python 3.10+
- Ambiente virtual (`venv`)
- Conexão com a Internet para acesso API
- Chave API

### Etapas de instalação

1. **Clone o repositório**:
     ```sh
     clone do git https://github.com/IMNascimento/NAI.git
     cd NAI
     ```

2. **Configure um ambiente virtual**:
     ```sh
     python -m venv venv
     source venv/bin/activate # No Windows use `venv\Scripts\activate`
     ```

3. **Instale os pacotes necessários**:
     ```sh
     pip install -r requeriments.txt
     ```

4. **Configure variáveis de ambiente**:
     - Crie um arquivo `.env` no diretório raiz do projeto com as variáveis de ambiente necessárias.
     - Para isso deixamos um arquivo .env.example para você criar ele da mesma forma e inserir sua chave de API.

## Uso

### Executando o Assistente de IA

1. **Ative o ambiente virtual**:
     ```sh
     source venv/bin/activate # No Windows use `venv\Scripts\activate`
     ```

2. **Execute o script `nai_llm.py`**:
     ```sh
     python ./core/nai_llm.py
     ```

### Configuração

- **Arquivo de configuração**: Modifique `core/config/settings.py` e `core/config/nai_context.txt` para ajustar as configurações e o contexto do assistente de IA.
- **Arquivo de dados**: Coloque seus arquivos de dados CSV no diretório `core/data` e atualize os caminhos de acordo em seus scripts.

### Comandos de voz

- **Iniciar/Parar Gravação**: Pressione a barra de espaço para iniciar ou parar a gravação de voz.
- **Sair do programa**: Pressione `Ctrl + Alt + E` para sair do programa com segurança.

## Contribuindo

Aceitamos contribuições para o projeto NAI! Contribuir:

1. Bifurque o repositório.
2. Crie um novo branch (`git checkout -b feature/your-feature`).
3. Confirme suas alterações (`git commit -am 'Adicione algum recurso'`).
4. Envie para o branch (`git push origin feature/your-feature`).
5. Crie uma nova solicitação pull.

## Licença

Este projeto está licenciado sob a licença GPL - consulte o arquivo [LICENSE](LICENSE) para obter detalhes.

## Agradecimentos

- Obrigado à equipe OpenAI por fornecer o poderoso modelo GPT-3.5 turbo. Pré treinado a um preço acessivel.
- Agradecimentos especiais aos colaboradores das bibliotecas Whisper e LangChain por suas excelentes ferramentas e documentação.
- Agradeço a Deus e minha família por me apoiar neste novo desenvolvimento.
- Antecipadamente agradeço também a todos os desenvolvedores que colaboraram com esse projeto diretamente e indiretamente.
