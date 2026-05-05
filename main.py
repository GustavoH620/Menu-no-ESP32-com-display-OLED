import machine, ssd1306, time, menu_principal
from machine import Pin, I2C
from menu_principal import menu_principal



btn1 = Pin(13, Pin.IN, Pin.PULL_UP)
btn2 = Pin(12, Pin.IN, Pin.PULL_UP)
btnEnter = Pin(14, Pin.IN, Pin.PULL_UP)
valorAnteriorEnter = 1
tempoEnterAnterior = time.ticks_ms()
enter = 1
index = 0
tempoAnterior = time.ticks_ms()

while True:
        valorBTN1 = btn1.value()
        valorBTN2 = btn2.value()
        valorBTNEnter = btnEnter.value()
        tempoAtual = time.ticks_ms()
        tempoEnterAtual = time.ticks_ms()
        
        if time.ticks_diff(tempoAtual, tempoAnterior) > 200:

            if valorBTN1 == 0 and index > 0:
                tempoAnterior = tempoAtual
                index -= 1
            if valorBTN2 == 0 and index < 3:
                tempoAnterior = tempoAtual
                index += 1
        if valorBTNEnter == 0 and valorAnteriorEnter == 1:
            enter = not enter
            valorAnteriorEnter = 0
            tempoEnterAnterior = tempoEnterAtual

        if time.ticks_diff(tempoEnterAtual, tempoEnterAnterior) > 1000 and valorBTNEnter == 1:
            valorAnteriorEnter = 1
        
        menu_principal(index, enter)

            
        #print(valorBTN1, " ", valorBTN2, " ", valorBTNEnter)
        print("Enter: ", enter)

    
