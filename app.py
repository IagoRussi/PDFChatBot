from langchain_community.document_loaders import WebBaseLoader, PyPDFLoader
import os
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

api_key = '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'
os.environ['GROQ_API_KEY'] = api_key

chat = ChatGroq(model="llama-3.3-70b-versatile")


def resposta_do_bot(lista_mensagens, documento):
    mensagem_system = "Você é um assistente útil chamado AsimoBot. Você utiliza as seguintes informações para as suas respostas : {informacoes}"
    mensagens_modelo = [("system", mensagem_system)]
    mensagens_modelo += lista_mensagens
    template = ChatPromptTemplate.from_messages(mensagens_modelo)
    chain = template | chat
    return chain.invoke({'informacoes': documento}).content


def carrega_site():
    url_site = input('Digite a URL do site que você quer carregar: ')
    loader = WebBaseLoader(url_site)
    lista_documentos = loader.load()
    documento = ''
    for doc in lista_documentos:
        documento = documento + doc.page_content
    return documento


def carrega_pdf():
    caminho = input('Digite o caminho completo do PDF: ')

    loader = PyPDFLoader(caminho)
    lista_documentos = loader.load()

    documento = ''
    for doc in lista_documentos:
        documento = documento + doc.page_content
    return documento


print('Bem-vindo ao ChatBot da Asimo! (Digite x se você quiser sair!)\n')

texto_selecao = '''Digite 1 se você quiser conversar com um site
Digite 2 se você quiser conversar com um pdf
'''

while True:
    selecao = input(texto_selecao)
    if selecao == '1':
        documento = carrega_site()
        break
    if selecao == '2':
        documento = carrega_pdf()
        break

    print('Seleção inválida. Por favor, tente novamente.\n')

mensagens = []
while True:
    pergunta = input('Usuario:')
    if pergunta.lower() == 'x':
        break
    mensagens.append(('user', pergunta))
    resposta = resposta_do_bot(mensagens, documento)
    mensagens.append(('assistant', resposta))
    print(f'Bot: {resposta}')

print('\nMuito obrigado por utilizar o AsimoBot!')


