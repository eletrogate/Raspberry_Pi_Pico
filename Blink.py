#importa as classes a serem utilizadas
from machine import Pin, Timer

#instancia o pino 15 como uma saída para led
led = Pin(15, Pin.OUT)

#instancia timer como um objeto do tipo Timer()
timer = Timer()

#descreve a função blink
def blink(timer): #colocar timer como parâmetro é necessário para indicar que a função é callback deste objeto
    led.toggle()  #inverte o estado do led

#inicia o timer com frequencia de 1 Hz, modo periódico (não encerra após o primeiro ciclo) e callback para blink
timer.init(freq = 1, mode = Timer.PERIODIC, callback = blink)