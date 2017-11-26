import RPi.GPIO as GPIO
import time
from codigos import  *




REC = 10
CLOCK = 9

GPIO.setmode(GPIO.BCM)
GPIO.setup(REC, GPIO.IN)
GPIO.setup(CLOCK, GPIO.IN)
cod = Codigos()


##primera, segunda =cod.getCodigoSecuencia(a)
##print(primera)
##print(segunda)



print("Recibe")
while True:
    caracter=""
    while GPIO.input(CLOCK) == GPIO.LOW:
        pass
    for i in range(2):
        if GPIO.input(REC) == GPIO.LOW:
            caracter+="0"
            print("Recibe 0")
        else:
            caracter += "1"
            print("Recibe 1")
        while GPIO.input(CLOCK) == GPIO.HIGH:
            pass
    print(cod.getCaracter(caracter))



GPIO.cleanup()
