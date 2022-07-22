#importa as classes que serão utilizadas
from pico_i2c_lcd import I2cLcd
from machine import I2C, Pin, ADC
from time import sleep

#instancia o pino de entrada analógica
adc = ADC(Pin(26))

#instancia a conexão I2C, utilizando a interface 0
#o pino 1 como scl, o 0 como sda e a frequencia de
#medições como 100000 Hz
i2c = I2C(id=0,scl=Pin(1),sda=Pin(0),freq=100000)

#instancia o LCD com a conexão i2c iniciada anteriormente,
#o endereço 0x27 do barramento e 2 linhas de 16 caracteres
lcd = I2cLcd(i2c, 0x27, 2, 16)

#ciclo infinito
while True:
    lcd.putstr('V: ')                               #escreve a partir da primeira posição
    lcd.putstr(str(adc.read_u16()  * 3.3 / 65535))  #escreve a leitura do ADC convertida p/ tensão
    sleep(0.5)                                      #aguarda meio segundo
    lcd.clear()                                     #limpa o LCD e volta p/ primeira posição