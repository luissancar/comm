import RPi.GPIO as GPIO
import time
import codigos

ENV=23
CLOCK=24

GPIO.setmode(GPIO.BCM)
GPIO.setup(ENV, GPIO.OUT)
GPIO.setup(CLOCK, GPIO.OUT)



print("Envia")
while True:
	
    GPIO.output(CLOCK, GPIO.HIGH)
    print("Envia HIGH")
    time.sleep(1)
    GPIO.output(CLOCK, GPIO.LOW)
    print("Envia LOW")
    time.sleep(1)
   

GPIO.cleanup()
