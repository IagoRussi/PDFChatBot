import os
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.document_loaders import WebBaseLoader

loader = WebBaseLoader("https://asimov.academy/")
lista_documentos = loader.load()
print(lista_documentos)
