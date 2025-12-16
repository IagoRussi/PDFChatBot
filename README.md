# PDFChatBot
AsimoBot é um chatbot em Python que responde perguntas com base em informações extraídas de sites e PDFs fornecidos pelo usuário. Utiliza LangChain e Groq AI para processamento de conteúdo.

## Funcionalidades

- Conversa interativa no terminal
- Carrega informações diretamente de **sites** (URL)
- Carrega informações de **PDFs**
- Mantém histórico da conversa durante a execução

## Como usar

1. Clone o repositório:
git clone https://github.com/IagoRussi/PDFChatBot.git

2. Instale as dependências:
pip install -r requirements.txt

3. Rode o ChatBot
python app.py

## Aplicação

O chat solicitará que o usuário escolha se deseja conversar com um site ou com um arquivo PDF.

Caso escolha um site:
basta informar a URL desejada. Após isso, o usuário poderá fazer qualquer pergunta, e o chat responderá com base nas informações contidas no site informado.

Caso escolha um PDF:
será necessário informar o caminho do arquivo no computador:
Exemplo:
C:\caminho\para\arquivo.pdf (Certifique-se de que o caminho não esteja entre aspas.)

Em seguida, o usuário poderá fazer qualquer pergunta, e o chat responderá com base nas informações presentes no PDF fornecido.
