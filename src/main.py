from loaders import load_web_context
from chatbot import generate_response

URL = "https://pt.wikipedia.org/wiki/Inteligência_artificial"

print("AI Knowledge AssistantAI iniciado!\n")

while True:
    question = input("Você: ")

    if question.lower() in ["sair", "exit", "quit"]:
        print("Encerrando chatbot...")
        break

    try:
        context = load_web_context(URL)

        response = generate_response(context, question)

        print("\nAssistant:\n")
        print(response)
        print("\n" + "-"*50 + "\n")

    except Exception as error:
        print(f"\nErro: {error}")
