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

Create a `.env` file and add your API key:

```env
GROQ_API_KEY=your_api_key
```

---

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
