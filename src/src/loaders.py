from langchain_community.document_loaders import WebBaseLoader

def load_web_context(url: str):

    loader = WebBaseLoader(url)

    docs = loader.load()

    content = " ".join([doc.page_content for doc in docs])

    return content[:9000]
