import RPi.GPIO as GPIO
import time


class Codigos:
    codigo = {'a': '00', 'b': '01'}

    def getCodigo(self, cod):
        return self.codigo[cod]

    def getCodigoSecuencia(self, cod):
        primera = self.codigo[cod][0]
        segunda = self.codigo[cod][1]
        return primera, segunda

    def getCaracter(self, cod):
        for secuencia in self.codigo:
            if cod == self.codigo[secuencia]:
                return secuencia
        return "error"


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
