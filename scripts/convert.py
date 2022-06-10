import pyttsx3
import time
import speech_recognition as sr
import subprocess

def convertAudio(resposta):
    engine = pyttsx3.init()
    engine. say(resposta)
    engine.runAndWait()
convertAudio("Iniciando meu sistema, aguarde um momento!")

while True:

    def convertVoz():
        
        print("Pode Falar")
        # def convertAudio(resposta):
        #     engine = pyttsx3.init()
        #     engine. say(resposta)
        #     engine.runAndWait()
        # convertAudio("Sistema atualizado!")
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)
            print("áudio capturado")
            try:
                text = r.recognize_google(audio, language='pt-br')
                print(text)
                
                #Comandos Melina
                #----------------------------------------------------------------------------------
                if text == "Melina":
                    def convertAudio(resposta):
                        engine = pyttsx3.init()
                        engine. say(resposta)
                        engine.runAndWait()
                    convertAudio("Olá Fábio, como posso ajudar?")
                #----------------------------------------------------------------------------------
                
                #Interação com aplicativos
                #----------------------------------------------------------------------------------
                elif text == "Abrir Google":
                    comando = (r'start %windir%\explorer.exe "C:\Program Files\Google\Chrome\Application\chrome.exe"')
                    print(subprocess.getoutput(comando))
                    def convertAudio(resposta):
                        engine = pyttsx3.init()
                        engine. say(resposta)
                        engine.runAndWait()
                    convertAudio("Tudo certo, estou abrindo o google!")
                
                elif text == "Abrir Photoshop":
                    comando = (r'start %windir%\explorer.exe "C:\Photoshop CS6 COMPLETO PT-BR - @iliesio22\PSCS6.exe"')
                    print(subprocess.getoutput(comando))
                    def convertAudio(resposta):
                        engine = pyttsx3.init()
                        engine. say(resposta)
                        engine.runAndWait()
                    convertAudio("Ta bom Fábio, estou abrindo o photoshop!")
                
                elif text == "Abrir Steam":
                    comando = (r'start %windir%\explorer.exe "C:\Program Files (x86)\Steam\steam.exe"')
                    print(subprocess.getoutput(comando))
                    def convertAudio(resposta):
                        engine = pyttsx3.init()
                        engine. say(resposta)
                        engine.runAndWait()
                    convertAudio("Tudo certo, estou abrindo a Steam!")
                    
                elif text == "gravar tela":
                    comando = (r'start %windir%\explorer.exe "C:\Program Files\obs-studio\bin\64bit\obs64.exe"')
                    print(subprocess.getoutput(comando))
                    def convertAudio(resposta):
                        engine = pyttsx3.init()
                        engine. say(resposta)
                        engine.runAndWait()
                    convertAudio("Ta bom, estou iniciando o OBS estúdio!")    


                #comandos pastas windows
                #-------------------------------------------------------------------------------
                elif text == "Abrir documentos":
                    comando = (r'start %windir%\explorer.exe "c:\users\Inicode Dev\Documents"')
                    print(subprocess.getoutput(comando))
                    def convertAudio(resposta):
                        engine = pyttsx3.init()
                        engine. say(resposta)
                        engine.runAndWait()
                    convertAudio("Pronto! Aqui está sua pasta de documentos.")
                    
                elif text == "Abrir desktop":
                    comando = (r'start %windir%\explorer.exe "c:\users\Inicode Dev\desktop"')
                    print(subprocess.getoutput(comando))
                    def convertAudio(resposta):
                        engine = pyttsx3.init()
                        engine. say(resposta)
                        engine.runAndWait()
                    convertAudio("Pronto! Sua área de trabalho está sendo aberta.")
                
                elif text == "Abrir downloads":
                    comando = (r'start %windir%\explorer.exe "c:\users\Inicode Dev\downloads"')
                    print(subprocess.getoutput(comando))
                    def convertAudio(resposta):
                        engine = pyttsx3.init()
                        engine. say(resposta)
                        engine.runAndWait()
                    convertAudio("Pronto! A pasta downloads foi aberta.")
                
                #---------------------------------------------------------------------------------


                #Entretenimento
                #---------------------------------------------------------------------------------  
                elif text == "conte uma piada":
                    def convertAudio(resposta):
                        engine = pyttsx3.init()
                        engine. say(resposta)
                        engine.runAndWait()
                    convertAudio("Sabe o que o melão estava fazendo de mãos dadas com o mamão perto de Copacabana?\
                    Levando o mamão papaya.")
                #----------------------------------------------------------------------------------
                
                
                #Comandos de encerramento
                #----------------------------------------------------------------------------------
                elif text == "encerrar":
                    def convertAudio(resposta):
                        engine = pyttsx3.init()
                        engine. say(resposta)
                        engine.runAndWait()
                    convertAudio("Ok, te vejo mais tarde!")
                    time.sleep(3)
                    exit()
                #----------------------------------------------------------------------------------
                
                #Comando de entendimento
                #----------------------------------------------------------------------------------
                else:
                    def convertAudio(resposta):
                        engine = pyttsx3.init()
                        engine. say(resposta)
                        engine.runAndWait()
                    convertAudio("Não entendi, pode falar novamente?")
                #----------------------------------------------------------------------------------
                
                
                
                
            except sr.UnknownValueError:
                print("Sphinx não conseguiu entender o audio")
            except sr.RequestError as e:
                print("Sphinx error; {0}".format(e))

    convertVoz()
    
