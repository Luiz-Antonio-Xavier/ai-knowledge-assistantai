# Prompt Engineering

## Objective

The objective of the prompt is to guide the AI assistant to provide clear, contextualized and objective responses.

---

## System Prompt Strategy

The chatbot uses a system prompt designed to:

- maintain conversational clarity
- provide concise answers
- use contextual information
- avoid generic responses
- simulate an intelligent assistant behavior

---

## Context Injection

The application retrieves contextual information from web sources and injects the retrieved content into the user prompt before sending it to the LLM.

---

## Prompt Structure

```text
System Prompt
      ↓
Retrieved Context
      ↓
User Question
      ↓
LLM Response
```

---

## Current Limitations

- Limited context window
- No conversational memory
- Possible hallucinations
- Dependence on external web sources

---

## Future Improvements

- Better context filtering
- Semantic retrieval
- Memory support
- Prompt optimization
- Multi-step reasoning
