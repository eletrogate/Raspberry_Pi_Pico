#importa as classes que serão utilizadas
from machine import Pin, PWM
from time import sleep

#instancia o pino 15 como saída PWM
pwm = PWM(Pin(15))

#define a frequencia, em Hz, da saída
pwm.freq(1000)

#ciclo infinito
while True:
    for duty in range(65025): #varia duty de 0 a 2^16
        pwm.duty_u16(duty)    #define o duty-cicle como igual a duty
        sleep(0.0001)         #delay de 100 us
    for duty in range(65025, 0, -1): #realiza o mesmo processo
        pwm.duty_u16(duty)           #do ciclo anterior, mas com
        sleep(0.0001)                #duty variando decrescentemente