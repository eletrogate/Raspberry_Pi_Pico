#importa as classes que serão utilizadas
from machine import Pin
from time import sleep

#instancia led como saida digital
#e button como entrada digital
led = Pin(15, Pin.OUT)
button = Pin(16, Pin.IN)

#ciclo infinito
while True:
    if not button.value(): #se o botao não estiver em nível alto
                           #e, portanto, estiver apertado
                           #já que liga a entrada ao GND
        led.toggle()       #inverte o valor do led
        sleep(0.5)         #delay para debounce