from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser

from config import MODEL_NAME
from prompts import chat_prompt

llm = ChatGroq(model=MODEL_NAME)

parser = StrOutputParser()

chain = chat_prompt | llm | parser

def generate_response(context, question):

    return chain.invoke({
        "context": context,
        "question": question
    })
