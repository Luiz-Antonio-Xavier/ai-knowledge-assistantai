# AI Knowledge AssistantAI

Conversational AI assistant built with Python, LangChain and Groq for general question answering and contextual responses.

> Projeto acadêmico desenvolvido para explorar conceitos de Inteligência Artificial Conversacional, Prompt Engineering e integração com Large Language Models (LLMs).

---

## Overview

AI Knowledge AssistantAI is a conversational chatbot developed using Python, LangChain and Groq.

The project was created as a college study project focused on understanding how modern AI assistants work using contextual information retrieval, prompt engineering and LLM pipelines.

The assistant is capable of answering general questions about different topics directly from the terminal.

---

## Visão Geral

O AI Knowledge AssistantAI é um chatbot conversacional desenvolvido com Python, LangChain e Groq.

O projeto foi criado como um projeto acadêmico com foco no estudo de Inteligência Artificial Conversacional, engenharia de prompts e integração com modelos de linguagem modernos.

O assistente é capaz de responder perguntas gerais sobre diversos assuntos diretamente pelo terminal.

---

## Features

- Conversational AI assistant
- General-purpose question answering
- Context retrieval from web sources
- Prompt engineering workflow
- Integration with Groq API
- Terminal-based interaction
- Modular project structure
- Educational AI project

---

## Technologies

- Python
- LangChain
- Groq API
- Llama 3.3 70B
- WebBaseLoader
- Prompt Engineering
- Context Injection
- AI Pipelines

---

## Architecture

```text
User Question
      ↓
Question Processing
      ↓
Web Context Retrieval
      ↓
Prompt Engineering
      ↓
LLM Processing (Groq + Llama)
      ↓
AI Response
```

---

## How It Works

1. The user sends a question through the terminal.
2. The chatbot processes the question.
3. Relevant contextual information is retrieved from web sources.
4. The retrieved content is injected into the prompt.
5. The LLM generates a contextualized response.
6. The final answer is displayed to the user.

---

## Como Funciona

1. O usuário envia uma pergunta pelo terminal.
2. O chatbot processa a pergunta.
3. Informações contextuais são buscadas na web.
4. O conteúdo encontrado é inserido no prompt.
5. O modelo de IA gera uma resposta contextualizada.
6. A resposta final é exibida ao usuário.

---

## Project Structure

```text
ai-knowledge-assistantai/
│
├── src/
│   ├── main.py
│   ├── chatbot.py
│   ├── prompts.py
│   ├── loaders.py
│   └── config.py
│
├── docs/
│
├── assets/
│
├── examples/
│
├── requirements.txt
├── README.md
└── LICENSE
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/ai-knowledge-assistantai.git
```

Enter the project folder:

```bash
cd ai-knowledge-assistantai
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Environment Variables

## Como criar a chave da API Groq

Siga os passos abaixo para configurar a API utilizada pelo chatbot.

---

### 1. Criar uma conta na Groq

Acesse o site oficial:

```text
https://console.groq.com/
```

Crie sua conta ou faça login.

---

### 2. Acessar o painel da API

Após entrar na plataforma:

- Abra o menu lateral
- Vá até:

```text
API Keys
```

---

### 3. Gerar uma nova chave

Clique em:

```text
Create API Key
```

A plataforma irá gerar uma chave parecida com:

```text
gsk_xxxxxxxxxxxxxxxxxxxxxxxxx
```

Copie essa chave.

---

### 4. Criar o arquivo `.env`

Na raiz do projeto, crie um arquivo chamado:

```text
.env
```

A estrutura do projeto deve ficar assim:

```text
ai-knowledge-assistantai/
│
├── src/
├── docs/
├── .env
├── README.md
└── requirements.txt
```

---

### 5. Adicionar a chave da API

Dentro do arquivo `.env`, coloque:

```env
GROQ_API_KEY=sua_chave_aqui
USER_AGENT=AIKnowledgeAssistant/1.0
```

Substitua:

```text
sua_chave_aqui
```

pela chave gerada na Groq.

---

### 6. Instalar as dependências

Abra o terminal e execute:

```bash
pip install -r requirements.txt
```

---

### 7. Executar o chatbot

Inicie o projeto com:

```bash
python src/main.py
```

---

### 8. Utilizar o chatbot

Exemplo:

```text
Você: O que é Python?

Assistant:
Python é uma linguagem de programação de alto nível conhecida por sua simplicidade e legibilidade.
```

---

### 9. Encerrar o chatbot

Para fechar o programa digite:

```text
sair
```

ou

```text
exit
```
## Running the Project

```bash
python src/main.py
```

---

## Example Usage

```text
You: What is Artificial Intelligence?

AssistantAI:
Artificial Intelligence (AI) refers to systems capable of performing tasks that normally require human intelligence, such as reasoning, learning and decision-making.
```

---

## Learning Objectives

This project was developed to study:

- Conversational AI
- LangChain fundamentals
- Prompt engineering
- LLM integrations
- Context retrieval workflows
- Python project organization
- AI application architecture

---

## Current Limitations

- Terminal-only interface
- Limited conversational memory
- Depends on external web content
- Context size limitations
- Possible hallucinations from AI responses

---

## Future Improvements

- Web interface
- Conversational memory
- Voice interaction
- Multi-source context retrieval
- Better prompt optimization
- Semantic search
- Chat history support

---

## Academic Context

This project was developed as part of academic studies focused on Artificial Intelligence and Software Development.

The main objective is to understand how conversational AI systems work using modern AI frameworks and prompt engineering techniques.

---

## License

This project is licensed under the MIT License.

---

## Author

Luiz  
Technology Student focused on AI and Software Development
