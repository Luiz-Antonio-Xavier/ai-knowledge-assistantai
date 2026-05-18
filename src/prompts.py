from langchain_core.prompts import ChatPromptTemplate

chat_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
You are an intelligent AI assistant.

Answer the user's questions clearly and objectively.

Use the provided context whenever possible.
"""
    ),

    (
        "user",
        """
Context:
{context}

Question:
{question}
"""
    )
])
