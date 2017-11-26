import time

import RPi.GPIO as GPIO
from comm.codigos import  *


ENV=23
CLOCK=24

GPIO.setmode(GPIO.BCM)
GPIO.setup(ENV, GPIO.OUT)
GPIO.setup(CLOCK, GPIO.OUT)

def enviar(dato):
    cod=Codigos()
    first, second=cod.getCodigoSecuencia(dato)
    print("envio "+first)
    if first == "0":
        GPIO.output(ENV, GPIO.LOW)
    else:
        GPIO.output(ENV, GPIO.HIGH)
    GPIO.output(CLOCK, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(CLOCK, GPIO.LOW)
    print("envio "+second)
    if second == "0":
        GPIO.output(ENV, GPIO.LOW)
    else:
        GPIO.output(ENV, GPIO.HIGH)
    GPIO.output(CLOCK, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(CLOCK, GPIO.LOW)







while True:
    dato=input("introducir dato (a,b,c,d) f=fin -> ")
    if dato == "f":
        break
    if dato in ("a","b","c","d"):
        enviar(dato)
    else:
        print("Introducia a,b,c,d o f")
   

GPIO.cleanup()
