
import pyttsx3 as p
from pygame import mixer
from listas_de_frases import *
import random
from pysentimiento import create_analyzer
emotion_analyzer = create_analyzer(task="emotion", lang="es")

""""1.speak   2.   3.short_song   4.date   5.acciones   6.welcome   7.help   
    8.   9.   10.   11.   12.   13.  14."""
instruccion = ""
intr = ""
flag = True
# --------juegos ----------
from vosk import Model, KaldiRecognizer
import os
import pyaudio
from time import sleep
from listas_de_frases import *
import random
import datetime
from pysentimiento import create_analyzer
global model
global recognizer
global mic
global stream
global lista_song
model = Model("C:/cosas_de_python/Proyecto_de_titulo/vosk/vosk-model-small-es-0.42")
os.system('cls')
recognizer = KaldiRecognizer(model, 16000)
mic = pyaudio.PyAudio()
stream = mic.open(rate=16000, channels=1, format=pyaudio.paInt16, input=True, frames_per_buffer=8192)
#----------------------


def speak(text):
    engine = p.init()
    engine.setProperty('rate', 190)  # cambiar velocidad
    engine.say(text)  # entrada de voz
    engine.runAndWait()  # salida


def short_song(cancion,estado):
    mixer.init()
    if estado == 'welcome':
        mixer.music.load(f"C:\cosas_de_python\Proyecto_de_titulo\welcome\start_song\{cancion}.mp3")
    if estado == 'adios':
        mixer.music.load(f"C:\cosas_de_python\Proyecto_de_titulo\welcome\end_song\{cancion}.mp3")
    mixer.music.set_volume(0.7)
    mixer.music.play()



def acciones():
    speak(accioness)

def welcome():
    cancion = random.choice(song_list)
    short_song(cancion, 'welcome')
    hour=datetime.datetime.now().hour
    if hour >=3 and hour <12:
        speak(random.choice(buenos_dias))
    elif hour >=12 and hour <18:
        speak('Buenas tardes')
    elif hour >=18 and hour <21:
        speak('Buenas noches')
    elif hour >=21 and hour <24:
        speak('Buenas noches !')
    elif hour >=0 and hour <3:
        speak('Es tarde, creo que es hora de ir a dormir')
    speak("""Hola soy Carla, tu asistente de voz. Entre mis funciones esta:""")
    speak(accioness)



    # num = float(string_line)
    #print(f"respuesta: {string_line}")
    #print("\n")
def estado_animo():

    lista_palabras = ""
    resultado = ''
    speak("Hola, ¿estas ahi?")
    resp = input("resp:")
    if ('si' in resp) or ('aqui estoy' in resp) or ('que quieres' in resp):
        speak(
            "hacer una auto reflexion de como estuvo tu dia es bueno, nos hace darnos cuenta en como usamos el timpo, y muchas veces, no ayuda a darnos cuenta de como nos sentimos ¿Como te has sentido hoy?")
        resp = input("")
        emotion = emotion_analyzer.predict(resp)
        lista = []
        dic_emotion = {}
        h = f"{emotion}"
        for i in h:
            if i == '{':
                flag = True
            elif i == '}':
                flag == False
            if flag == True:
                lista_palabras += i
        y = lista_palabras[1:-2]
        t = y.split(',')
        print(t)
        for i in t:
            k = i.split(':')
            dic_emotion[k[0]] = float(k[1].strip())
        for i in dic_emotion.keys():
            lista.append(i)
        if lista[0] == 'others':
            resultado = lista[1]
        else:
            resultado = lista[0]
    else:
        resultado = ""
    if (resultado == 'joy'):
        pass
    elif (resultado == 'sadness') or (resultado == 'surprise') or (resultado == 'fear') or (
            resultado == 'anger') or (resultado == 'disgust'):
        print('enviar mensaje')
        speak("respuesta")



# ------------------------ Juegos ------------------

# ------------ Orden alfavetico --------------
# Se comienza con musica del juego.
from listas_de_frases import *
from random import choice
keys_list = []
lista_list = []
campo_rand = []
final = []

# --------------------- alfabeto --------------------------
def alfabeto():
    global final
    global campo_rand
    final.clear()
    campo_rand.clear()

    key_while_alf = True
    key_listo = True
    #speak(instrucciones_or_alfa)
    #speak(sugerencia)
    speak("Instrucciones")

    for x, y in campos.items():
        keys_list.append(x)
        lista_list.append(y)

    c = choice(keys_list)
    index_camp = keys_list.index(c)
    final = lista_list[index_camp]
    while len(campo_rand) != 3:
        h = choice(final)
        if h in campo_rand:
            pass
        else:
            campo_rand.append(h)

    while key_listo:
        speak("estas listo para jugar?")
        stream.stop_stream()
        resp = text_recognizer()
        stream.start_stream()
        if ("listo" in resp):
            speak(f"El campo es. {c}")
            speak(f"las palabras son. {campo_rand}")
            speak("Cuando estes listo para responder, solo di listo.")
            break
        if ("no" in resp) and ("jugar" in resp):
            key_while_alf = False
            break
        sleep(0.1)
    while key_while_alf:
        stream.stop_stream()
        resp = text_recognizer()
        stream.start_stream()
        if "repetir" in resp:
            speak(f"El campo es. {c}")
            speak(f"las palabras son. {campo_rand}")
            speak("Cuando estes listo para responder, solo di listo.")

        elif ("listo" in resp) or ("lista" in resp):
            orden = campo_rand.copy()
            orden.sort()
            print(orden)
            while key_while_alf:
                speak("¿Cuales tu respuesta?")
                resp = text_recognizer()
                try:
                    if "repetir" in resp:
                        speak(f"El campo es. {c}")
                        speak(f"las palabras son. {campo_rand}")
                        speak("Cuando estes listo para responder, solo di listo.")
                    if orden[0] in resp:
                        primero_ind = resp.index(orden[0])
                        print(f"primero: {primero_ind}")
                    if orden[1] in resp:
                        segundo_ind = resp.index(orden[1])
                        print(f"segundo: {segundo_ind}")
                    if orden[2] in resp:
                        tercero_ind = resp.index(orden[2])
                        print(f"tercero: {tercero_ind}")
                    if primero_ind < segundo_ind < tercero_ind:
                        print("ganaste!")
                        key_while_alf = False
                        speak("Esa es la respuesta correcta !!!")
                    else:
                        print("perdiste ")
                        key_while_alf = False
                        speak("No, esa no es")
                except:
                    speak("Creo que tu respuesta esta incompleta o he esuchado mal. ¿Me podrias repetir tu respuesta?")
                    print("Creo que tu respuesta esta incompleta o he esuchado mal. ¿Me podrias repetir tu respuesta?")
        speak("¿Te gustia volver a jugar?")
        while True:
            resp = text_recognizer()
            if ("sí" in resp) or ("si" in resp):
                alfabeto()
            elif ("no" in resp):
                break
# ----------------------- text_recognizer -----------------------------------
def text_recognizer():
    stream.start_stream()
    #speak("Te escucho")
    print('funcion text_recognizer')
    while True:
        data = stream.read(4096, exception_on_overflow=False)
        if len(data) == 0:
            break
        if recognizer.AcceptWaveform(data):
            text = recognizer.Result()[14:-3]
            print(text)
            if "" == text:
                speak('Disculpa, no te he escuchado bien')
            else:
                stream.stop_stream()
                return text
#------------------------- juegos matematicos ------------------------
def math_game():

    import random
    import sys
    import time
    from threading import Timer
    import tkinter
    from pynput.keyboard import Key, Controller

    key_resp = True
    lower = 1
    upper = 50

    tiempo = 60
    val = True
    val2 = True
    mathVal = True
    contSalirMath = 0
    res = 0
    answer = ""
    pts = 0
    answerInt = 0
    dictNumeros = {'cero': 0, 'uno': 1, 'dos': 2, 'tres': 3, 'cuatro': 4, 'cinco': 5, 'seis': 6, 'siete': 7,
                   'ocho': 8, 'nueve': 9, 'diez': 10, 'once': 11, 'doce': 12, 'trece': 13, 'catorce': 14, 'quince': 15,
                   'dieciseis': 16, 'diecisiete': 17, 'dieciocho': 18, 'diecinueve': 19, 'veinte': 20,
                   'veintiuno': 21, 'veintidos': 22, 'veintitres': 23, 'veinticuatro': 24, 'veinticinco': 25,
                   'veintiseis': 26, 'veintisiete': 27, 'veintiocho': 28, 'veintinueve': 29, 'treinta': 30,
                   'treinta y uno': 31, 'treinta y dos': 32, 'treinta y tres': 33, 'treinta y cuatro': 34,
                   'treinta y cinco': 35, 'treinta y seis': 36, 'treinta y siete': 37, 'treinta y ocho': 38,
                   'treinta y nueve': 39, 'cuarenta': 40, 'cuarenta y uno': 41, 'cuarenta y dos': 42,
                   'cuarenta y tres': 43,
                   'cuarenta y cuatro': 44, 'cuarenta y cinco': 45, 'cuarenta y seis': 46, 'cuarenta y siete': 47,
                   'cuarenta y ocho': 48, 'cuarenta y nueve': 49, 'cincuenta': 50}


    while mathVal:
        speak("¿Qué te gustaría jugar, sumas o adivina el número en el que esto pensado?")
        contSalirMath = contSalirMath + 1
        if contSalirMath % 2 == 0:
            speak("Recuerda que si no quieres jugar y quieres salir, solo dímelo")
        resp = text_recognizer()
        if ("sumas" in resp) or ("suma" in resp):
            speak("Bienvenido al Juego de sumas y restas, tendraás 20 segundos")
            speak("Estaás listo?")
            while key_resp:
                resp = text_recognizer()
                if ("si" in resp) or ("listo" in resp) or ("sí" in resp):
                    t_inicial = time.time()
                    key_resp = False
            while val:
                x = random.randrange(1, 20)
                y = random.randrange(1, 20)

                if x < y:
                    res = x + y
                    speak(f"¿Cuánto es  {x}  más  {y} ?")
                else:
                    res = x - y
                    speak(f"¿Cuánto es  {x}  menos  {y} ?")

                while val2:
                    answer = text_recognizer()

                    t_final = time.time()
                    if t_final - t_inicial > tiempo:
                        val2 = False
                        answerInt = -1
                    elif dictNumeros.keys() in answer:
                        answerInt = dictNumeros[answer]
                        val2 = False
                    else:
                        # val2 = True
                        pass

                val2 = True

                if answerInt == res:
                    speak("Excelente! 10 Puntos para Griffindor!")
                    pts = pts + 10
                elif answerInt == -1:
                    speak("Se ha acabado el tiempo")
                    break
                else:
                    speak("Esa no era la respuesta, intentalo denuevo!")

            speak(f"Tu puntaje fue: {pts} puntos")

        # ------------------ SEGUNDO JUEGO -----------------------------
        elif("adivina" in resp) or ("adivinar" in resp) or ("número" in resp):
            speak("Bienvenido al Juego de adivina el numero")
            speak("Estas listo?")

            resp = text_recognizer()

            if ("listo" in resp) or ("lista" in resp) or ("si" in resp) or ("sí" in resp):
                t_inicial = time.time()


                numAdivina = random.randint(lower, upper)
                count = 0

                speak("Debes adivinar el numero que se encuentra entre 1 y 50, di un numero para que partamos! Recuerda, solo debes decir el número")

                while val:

                    count += 1

                    while val2:
                        answer = text_recognizer()
                        t_final = time.time()
                        if t_final - t_inicial > tiempo:
                            answerInt = -1
                            val2 = False
                        elif answer in dictNumeros.keys():
                            answerInt = dictNumeros[answer]
                            val2 = False
                        else:
                            # val2 = True
                            pass

                    val2 = True

                    if numAdivina == answerInt:
                        speak(f"Felicidades, lo hiciste en  {count} intentos")
                        break
                    elif answerInt == -1:
                        speak("Se ha acabado el tiempo")
                        speak(f"El número era {numAdivina}")
                        break
                    elif numAdivina > answerInt:
                        speak("El numero es mayor")
                    elif numAdivina < answerInt:
                        speak("El numero es menor")


            else:
                speak("Adios")

            speak("Adios Final")
        # ------ SALIR ---------------
        elif ("sal" in resp) or ("salir" in resp):

                speak("Has salido de los juegos matemáticos")
                mathVal = False


#---------------------------- main -----------------------------------
def main():
    model = Model("C:/cosas_de_python/Proyecto_de_titulo/vosk/vosk-model-small-es-0.42")
    os.system('cls')
    recognizer = KaldiRecognizer(model, 16000)
    mic = pyaudio.PyAudio()
    stream = mic.open(rate=16000, channels=1, format=pyaudio.paInt16, input=True, frames_per_buffer=8192)

    game_key = True
    while True:
        stream.start_stream()
        speak("te escucho")
        while True:
            data = stream.read(4096, exception_on_overflow=False)
            if len(data) == 0:
                break
            if recognizer.AcceptWaveform(data):
                text = recognizer.Result()[14:-3]
                print(text)
                print('el tes escucho es del segundo while')
                if ("juegos" in text) or ("jugar" in text ) or ("juego" in text):
                    while game_key:
                        speak("¿Qué te gustaría jugar?, Juegos matematicos? o alfabeto?")
                        text = text_recognizer()
                        if ("matemático" in text) or ("matemática" in text) or ("matemáticos" in text) or ("matemáticas" in text):
                            stream.stop_stream()
                            math_game()
                            stream.start_stream()
                        elif ("alfabeto" in text):
                            stream.stop_stream()
                            alfabeto()
                            stream.start_stream()
                        elif ("salir" in text) or ("no quiero" in text):
                            game_key = False
                    speak("Adiós")