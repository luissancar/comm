import RPi.GPIO as GPIO
import time
from comm.codigos import  *




REC = 10
CLOCK = 9

GPIO.setmode(GPIO.BCM)
GPIO.setup(REC, GPIO.IN)
GPIO.setup(CLOCK, GPIO.IN)
cod = Codigos()
a = "b"

##primera, segunda =cod.getCodigoSecuencia(a)
##print(primera)
##print(segunda)

print(cod.getCaracter("00"))

print("Recibe")
while True:
    if GPIO.input(CLOCK) == GPIO.LOW:
        print("Recibe LOW")
    else:
        print("Recibe HIGH")
    time.sleep(1)

GPIO.cleanup()
