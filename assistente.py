# -*- coding: utf-8 -*-

# 1. Importação das bibliotecas necessárias
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import webbrowser
import os
from unidecode import unidecode

# Função para normalizar texto (remover acentos e colocar em minúsculo)
def normalizar(texto):
    """Remove acentos e converte para minúsculas."""
    return unidecode(texto.lower())

# 2. Módulo de Fala (Text-to-Speech) - Sem alterações
def falar(texto):
    print(f"Assistente: {texto}")
    try:
        tts = gTTS(text=texto, lang='pt-br')
        arquivo_audio_temporario = "resposta.mp3"
        tts.save(arquivo_audio_temporario)
        playsound(arquivo_audio_temporario)
        os.remove(arquivo_audio_temporario)
    except Exception as e:
        print(f"Ocorreu um erro ao tentar falar: {e}")

# 3. Módulo de Audição (Speech-to-Text) - *** A CORREÇÃO ESTÁ AQUI ***
def ouvir_comando():
    reconhecedor = sr.Recognizer()
    
    # ### MUDANÇA CRÍTICA: Aumentamos a tolerância à pausa ###
    # Agora, a assistente espera 1.5 segundos de silêncio antes de parar de ouvir.
    reconhecedor.pause_threshold = 1.5 

    with sr.Microphone() as source:
        print("Ajustando para o ruído do ambiente. Aguarde um momento...")
        reconhecedor.adjust_for_ambient_noise(source, duration=1)
        
        print("Pode falar. Estou ouvindo...")
        try:
            # Removemos o 'phrase_time_limit' para deixar o 'pause_threshold' ser o controlador principal
            audio = reconhecedor.listen(source)
            
            print("Reconhecendo...")
            comando = reconhecedor.recognize_google(audio, language='pt-BR')
            print(f"Você disse: {comando}\n")
            return comando
            
        except sr.UnknownValueError:
            print("Não consegui entender ou não detectei fala.")
            return None
        except sr.RequestError:
            falar("Desculpe, estou com problemas de conexão com o serviço de reconhecimento.")
            return None

# 4. Módulo Central de Comandos (O "Cérebro") - Sem alterações
def executar_comandos(comando):
    comando_normalizado = normalizar(comando)
    
    if 'wikipedia' in comando_normalizado and 'sobre' in comando_normalizado:
        try:
            termo_pesquisa = comando.lower().split('sobre')[-1].strip()
            if termo_pesquisa:
                url = f"https://pt.wikipedia.org/wiki/{termo_pesquisa.replace(' ', '_')}"
                webbrowser.open(url)
                falar(f"Pesquisando na Wikipedia sobre {termo_pesquisa}.")
            else:
                falar("Não entendi o que você quer pesquisar. Tente dizer: pesquise sobre [termo].")
        except Exception as e:
            falar("Ocorreu um erro ao tentar pesquisar na Wikipedia.")
            print(e)
        
    elif 'abra' in comando_normalizado and 'youtube' in comando_normalizado:
        webbrowser.open("https://www.youtube.com")
        falar("Abrindo o YouTube.")
        
    elif 'farmacia' in comando_normalizado and 'proxima' in comando_normalizado:
        url = "https://www.google.com/maps/search/farmácia+próxima"
        webbrowser.open(url)
        falar("Mostrando as farmácias mais próximas no Google Maps.")
        
    else:
        falar("Desculpe, não tenho um comando para isso. Pode tentar novamente?")

# 5. Loop Principal - Sem alterações
if __name__ == "__main__":
    falar("Olá! Sou sua assistente virtual. Como posso ajudar?")
    
    while True:
        comando_recebido = ouvir_comando()
        
        if comando_recebido:
            comando_normalizado = normalizar(comando_recebido)
            if any(palavra in comando_normalizado for palavra in ["desligar", "parar", "ate logo"]):
                falar("Até logo! Desligando.")
                break
            
            executar_comandos(comando_recebido)