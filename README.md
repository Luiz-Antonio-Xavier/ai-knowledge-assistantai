# Assistente de Conhecimento de IA

Assistente de IA conversacional desenvolvido com Python, LangChain e Groq para responder perguntas gerais e fornecer respostas contextuais.

Projeto acadêmico desenvolvido para explorar conceitos de Inteligência Artificial Conversacional, Engenharia de Prompts e integração com Modelos de Linguagem de Grande Escala (LLMs).

---

# Visão Geral

O Assistente de Conhecimento de IA (AI Knowledge Assistant) é um chatbot conversacional desenvolvido com Python, LangChain e Groq.

O projeto foi criado com foco acadêmico para estudar como funcionam assistentes de IA modernos, utilizando recuperação de contexto, engenharia de prompts e pipelines de LLM.

O sistema é capaz de responder perguntas gerais sobre diversos assuntos diretamente pelo terminal.

---

# Características

- Assistente de IA conversacional  
- Respostas para perguntas gerais  
- Recuperação de contexto a partir da web  
- Fluxo de engenharia de prompts  
- Integração com API da Groq  
- Interface via terminal  
- Estrutura modular de projeto  
- Projeto com fins educacionais  

---

# Tecnologias Utilizadas

- Python  
- LangChain  
- API da Groq  
- Llama 3.3 70B  
- WebBaseLoader  
- Engenharia de Prompts  
- Injeção de Contexto  
- Pipelines de IA  

---

# Arquitetura

```text
Pergunta do Usuário
        ↓
Processamento da Pergunta
        ↓
Recuperação de Contexto na Web
        ↓
Engenharia de Prompt
        ↓
Processamento pelo LLM (Groq + Llama)
        ↓
Resposta da IA
```

---

# Como Funciona

1. O usuário envia uma pergunta pelo terminal  
2. O sistema processa a pergunta  
3. Informações relevantes são buscadas na web  
4. O conteúdo é inserido no prompt  
5. O modelo de IA gera a resposta  
6. A resposta é exibida no terminal  

---

# Estrutura do Projeto

```txt
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
├── examples/
├── requirements.txt
├── README.md
└── LICENSE
```

---

# Instalação

### 1. Clonar o repositório

```bash
git clone https://github.com/yourusername/ai-knowledge-assistantai.git
```

### 2. Acessar a pasta

```bash
cd ai-knowledge-assistantai
```

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

---

# Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto:

```env
GROQ_API_KEY=sua_chave_aqui
USER_AGENT=AIKnowledgeAssistant/1.0
```

---

# Como criar a chave da API da Groq

### 1. Criar uma conta

Acesse:

```text
https://console.groq.com/
```

Crie sua conta ou faça login.

---

### 2. Acessar API Keys

No painel:

- Vá até o menu lateral  
- Clique em **API Keys**

---

### 3. Criar chave

Clique em:

```text
Create API Key
```

Copie a chave gerada (exemplo):

```text
gsk_xxxxxxxxxxxxxxxxxxxxx
```

---

### 4. Configurar no projeto

Cole a chave no arquivo `.env`.

---

# Executar o projeto

```bash
python src/main.py
```

---

# Exemplo de uso

### Usuário:
```text
O que é Python?
```

### Assistente:
```text
Python é uma linguagem de programação de alto nível conhecida por sua simplicidade e legibilidade.
```

---

# Objetivos de Aprendizado

Este projeto foi desenvolvido para estudar:

- Inteligência Artificial Conversacional  
- Fundamentos do LangChain  
- Engenharia de Prompts  
- Integração com LLMs  
- Recuperação de contexto  
- Organização de projetos em Python  
- Arquitetura de software  

---

# Limitações Atuais

- Interface apenas via terminal  
- Memória conversacional limitada  
- Dependência de conteúdo da web  
- Limite de contexto do modelo  
- Possíveis respostas imprecisas  

---

# Melhorias Futuras

- Interface web  
- Memória conversacional  
- Suporte a voz  
- Múltiplas fontes de contexto  
- Busca semântica  
- Histórico de chat  

---

# Contexto Acadêmico

Este projeto foi desenvolvido com fins educacionais para estudo de Inteligência Artificial e Desenvolvimento de Software.

O objetivo é entender como sistemas de IA funcionam na prática utilizando ferramentas modernas.

---

# Licença

Este projeto está sob a licença MIT.

---

# Autor

Luiz Antonio Xavier  
Estudante de tecnologia com foco em desenvolvimento de software.
