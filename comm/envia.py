import time

import RPi.GPIO as GPIO
from codigos import  *


ENV=23
CLOCK=24

GPIO.setmode(GPIO.BCM)
GPIO.setup(ENV, GPIO.OUT)
GPIO.setup(CLOCK, GPIO.OUT)

def enviar(dato):
    cod=Codigos()
    first, second=cod.getCodigoSecuencia(dato)
    if first == "0":
        GPIO.output(ENV, GPIO.LOW)
        print("envio 0")
    else:
        GPIO.output(ENV, GPIO.HIGH)
        print("envio 1")
    GPIO.output(CLOCK, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(CLOCK, GPIO.LOW)
    if second == "0":
        GPIO.output(ENV, GPIO.LOW)
        print("envio 0")
    else:
        GPIO.output(ENV, GPIO.HIGH)
        print("envio 1")
    GPIO.output(CLOCK, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(CLOCK, GPIO.LOW)







while True:


    ## Python 2.7 raw_input
    ## Python 3 input
    dato=str(raw_input("introducir dato (a,b,c,d) f=fin -> "))
    ##dato = str(input("introducir dato (a,b,c,d) f=fin -> "))

    if dato == "f":
        break
    if dato in ("a","b","c","d"):
        enviar(dato)
    else:
        print("Introducia a,b,c,d o f")


GPIO.cleanup()
