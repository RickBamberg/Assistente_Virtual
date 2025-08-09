## Projeto: Assistente Virtual em Python
Este projeto é a implementação de uma assistente virtual de linha de comando desenvolvida em Python, como parte do desafio de projeto do curso de Machine Learning. O sistema é capaz de ouvir comandos de voz em português, processá-los utilizando técnicas de Processamento de Linguagem Natural (PLN) e executar tarefas simples, respondendo também com áudio.
## Funcionalidades
- Reconhecimento de Voz: Captura áudio do microfone e transcreve para texto.
- Síntese de Voz (Text-to-Speech): Responde aos comandos com uma voz sintetizada.
- Comandos Ativados por Voz:
    - Abrir o site do YouTube.
    - Realizar pesquisas na Wikipedia.
    - Encontrar a farmácia mais próxima no Google Maps.
- Controle de Execução: Pode ser encerrada com um comando de voz ("desligar", "parar").
## Tecnologias Utilizadas
- Linguagem: Python 3.11
- Gerenciador de Ambiente: Anaconda (conda)
- Bibliotecas Principais:
    - SpeechRecognition: Para a conversão de fala em texto (Speech-to-Text).
    - gTTS (Google Text-to-Speech): Para a conversão de texto em fala (Text-to-Speech).
    - PyAudio: Essencial para o acesso ao microfone.
    - playsound==1.2.2: Versão estável para reprodução de áudio no Windows.
    - unidecode: Para normalização de texto (remoção de acentos), tornando os comandos mais robustos.
    - webbrowser: Para abrir links no navegador padrão.
## Configuração do Ambiente
Para executar este projeto, é necessário ter o Anaconda instalado. Siga os passos abaixo:
Clone o Repositório
code
```bash
git clone https://github.com/RickBamberg/Assistente_Virtual.git
cd Assistente_Virtual
```
Crie o Ambiente Conda
O projeto foi desenvolvido e testado com Python 3.11. Crie um novo ambiente com o seguinte comando:
code
```bash
conda create --name assistente_env python=3.11 -y
```
Ative o Ambiente
code
```bash
conda activate assistente_env
```
Instale as Dependências
A instalação é feita em duas etapas para garantir a compatibilidade:
code
```bash
# 1. Instale o PyAudio usando o canal conda-forge
conda install -c conda-forge pyaudio

# 2. Instale as outras bibliotecas com pip
pip install gTTS SpeechRecognition playsound==1.2.2 wikipedia-api unidecode
```
Como Usar
Certifique-se de que seu ambiente assistente_env está ativo.
Execute o script principal no seu terminal:
code
```bash
python assistente.py
```  

- A assistente irá cumprimentá-lo. Quando ela disser "Pode falar. Estou ouvindo...", diga um dos comandos, por exemplo:
    - "Abra o YouTube"
    - "Pesquise na Wikipedia sobre Inteligência Artificial"
    - "Qual a farmácia mais próxima?"
    - "Desligar"
---
## Estrutura do Projeto e as 3 Etapas do Desafio
O código foi estruturado de forma modular para cumprir os três requisitos principais do desafio:
### Etapa 1: Módulo Text-to-Speech (Saída de Áudio)
Este módulo é responsável por fazer a assistente "falar".

- Função Principal: falar(texto)
- Como Funciona:
    - Recebe uma string de texto como argumento.
    - Utiliza a biblioteca gTTS para se comunicar com a API do Google e converter essa string em um arquivo de áudio (.mp3).
    - A biblioteca playsound é então utilizada para reproduzir o arquivo de áudio gerado, permitindo que o usuário ouça a resposta da assistente.
### Etapa 2: Módulo Speech-to-Text (Entrada de Voz)
Este módulo permite que a assistente "ouça" e "entenda" os comandos do usuário.
- Função Principal: ouvir_comando()
- Como Funciona:
    - Utiliza a biblioteca SpeechRecognition em conjunto com a PyAudio para acessar o microfone.
    - O parâmetro pause_threshold foi ajustado para 1.5 segundos, permitindo que o usuário faça pausas naturais ao falar sem ser interrompido.
    - O áudio capturado é enviado para a API de reconhecimento de fala do Google.
    - A API retorna a transcrição do áudio, que a função entrega como uma string de texto.
### Etapa 3: Acionamento de Funções por Comando de Voz (Lógica Central)
Este é o "cérebro" da assistente, que conecta as etapas de ouvir e falar para executar ações.
- Função Principal: executar_comandos(comando)
- Como Funciona:
    - Recebe o texto transcrito da função ouvir_comando().
    - Normaliza o texto: Utiliza a biblioteca unidecode para remover acentos e converter tudo para letras minúsculas. Isso torna a detecção de comandos muito mais robusta (ex: "Wikipédia" e "wikipedia" são tratados da mesma forma).
    - Usa uma estrutura condicional (if/elif/else) para procurar por palavras-chave no comando normalizado (ex: "youtube", "wikipedia", "farmacia").
    - Se uma correspondência for encontrada, ele executa a ação associada, como chamar a biblioteca webbrowser para abrir uma URL.
    - Ao final, chama a função falar() para dar um feedback em áudio ao usuário sobre a ação que foi realizada.