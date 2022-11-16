from vosk import Model, KaldiRecognizer
#from funciones_apps import *
from funciones_finales import *
import pyaudio
import os
from listas_de_frases import *
import random
import serial
import time

espmin = serial.Serial("COM9", 115200)
espmin.flushInput() #limpia la entrada serial antes de leer cualquier dato
entrada = ""

while True:

    # recibe
    stringbytes = espmin.readline()  # lee datos que vengan por puerto serial
    string_line = stringbytes.decode('latin-1').strip()  # convierte los datos que llegan del esp32 a string

    print(f"respuesta: {string_line}")
    print("\n")
    if ("ENTRO" in string_line):
        break

def comunicacion_serie(orde):
    try:
            # ENVIA
            flagg = 0
            orden = orde.encode('latin-1')
            espmin.write(orden)
            if (orde == "h") or (orde == "g"):
                while True:
                    stringbytes = espmin.readline()  # lee datos que vengan por puerto serial
                    string_line = stringbytes.decode('latin-1').strip()  # convierte los datos que llegan del esp32 a string
                    if ("ENTRO" not in string_line):
                        # num = float(string_line)
                        respuesta = string_line
                        print(f"respuesta: {respuesta}")
                        return respuesta
                    elif ("ENTRO" in string_line):
                        flagg+=1
                    elif(flagg == 2):
                        break

    except KeyboardInterrupt:
        # cerrar programa con ctrl +c
            print("entro al except")


def date():
    today = comunicacion_serie("g")
    speak(today)

def text_recognizer():
    global model
    global recognizer
    global mic
    global stream
    global lista_song
    stream.start_stream()
    speak("Te escucho")
    print('funcion text_recognizer')
    while True:
        data = stream.read(4096, exception_on_overflow=False)
        if len(data) == 0:
            break
        if recognizer.AcceptWaveform(data):
            text = recognizer.Result()[14:-3]
            if " " == text:
                speak('Disculpa, no te he escuchado bien')
            else:
                stream.stop_stream()
                return text
def help():
    speak("¿Necesitas ayuda?")
    stream.stop_stream()
    resp = text_recognizer()
    print(resp)
    if ('si' in resp) or ('ayuda' in resp):
        speak("No te preocupes, pedire ayuda....")
        comunicacion_serie("a")
    elif ("" == resp):
        speak("No te he esuchado")
        help()
    elif("no" in resp) or ("No" in resp):
        pass


def time():
    Time = comunicacion_serie("h")
    speak('Son las ')
    speak(Time)

switch =False
model = Model("C:/cosas_de_python/Proyecto_de_titulo/vosk/vosk-model-small-es-0.42")
os.system('cls')
welcome()
recognizer = KaldiRecognizer(model, 16000)
mic = pyaudio.PyAudio()
stream = mic.open(rate=16000, channels=1, format=pyaudio.paInt16, input=True, frames_per_buffer=8192)

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
            if 'carla' in text:
                os.system('cls')
                stream.stop_stream()
                switch = True
                break
            if ('funciones' in text) or ('hacías' in text) or ('cosa haces' in text) or ('qué haces' in text):
                stream.stop_stream()
                acciones()
                stream.start_stream()
            if ("cómo te llamas" in text) or ('cuál es tu nombre' in text) or ("cómo te llamabas" in text):
                print('entro mellamo carla')
                stream.stop_stream()
                speak("Me llamo carla")
                stream.start_stream()
            if ('necesito ayuda' in text)or ('ayuda' in text) or ('fuego' in text) or ('me caí' in text) or ('me duele' in text ) or ('mareado' in text):
                os.system('cls')
                stream.stop_stream()
                help()
                stream.start_stream()




    if switch == True:
        print('entro')
        stream.start_stream()
        while switch:
            data = stream.read(4096, exception_on_overflow=False)
            if len(data) == 0:
                break
            if recognizer.AcceptWaveform(data):
                text = recognizer.Result()[14:-3]
                print(text)
                if ('necesito ayuda' in text) or ('ayuda' in text)  or ('fuego' in text) or ('me caí' in text) or ('me duele' in text) or ('mareado' in text):
                    os.system('cls')
                    stream.stop_stream()
                    help()
                    speak(f'¿Puedo hacer algo más por tí?')
                    stream.start_stream()
                if "hora" in text:
                    os.system('cls')
                    stream.stop_stream()
                    time()
                    speak(f'¿Puedo hacer algo más por tí?')
                    stream.start_stream()
                    print('')
                    print('listening ...')
                    print('')
                elif ("día es" in text) or ('fecha' in text):
                    os.system('cls')
                    stream.stop_stream()
                    date()
                    speak(f'¿Puedo hacer algo más por tí?')
                    stream.start_stream()
                    print('')
                    print('listening ...')
                    print('')
                elif ('funciones' in text) or ('funcione' in text) or ('hacias' in text) or ('cosa haces' in text):
                    stream.stop_stream()
                    acciones()
                    speak('¿Qué puedo hacer por ti?')
                    speak('Te escucho')
                    stream.start_stream()

                elif text in despedida:
                    stream.stop_stream()
                    print('entro adios')
                    cancion = random.choice(off)
                    short_song(cancion, 'adios')
                    speak(random.choice(desps))
                    switch = False
                    break
                elif ('colgar' in text):
                    stream.stop_stream()
                    comunicacion_serie("f")
                    speak('¿Qué puedo hacer por ti?')
                    speak('Te escucho')
                    stream.start_stream()
                elif ('prende' in text) or ('enciende' in text) and ('luz' in text):
                    stream.stop_stream()
                    comunicacion_serie("d")
                    speak('¿Qué puedo hacer por ti?')
                    speak('Te escucho')
                    stream.start_stream()
                elif ('apaga' in text) and ('luz' in text):
                    stream.stop_stream()
                    comunicacion_serie("e")
                    speak('¿Qué puedo hacer por ti?')
                    speak('Te escucho')
                    stream.start_stream()

                elif ('juegos' in text) or ('jugar' in text):
                    print("entro a juegos")
                    stream.stop_stream()
                    main()
                    speak('¿Qué puedo hacer por ti?')
                    speak('Te escucho')
                    stream.start_stream()
                os.system('cls')

                elif












