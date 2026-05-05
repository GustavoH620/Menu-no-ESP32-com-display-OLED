import machine, ssd1306, time
from machine import Pin, I2C

i2c = I2C(scl=Pin(21), sda=Pin(22))


# Precisa ser renomeada para "Telas"
estado = 0

oled_width=128
oled_height=64

oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)
indexAnterior = 5

def menu_principal(index, enter):
    global estado
    if enter == 0:
        estado = index + 1
    else:
        estado = 0
    if estado == 0:
        
        Px = 1
        Py = 10
        contadorY = 0
        global indexAnterior
        tempoAnterior = time.ticks_ms()

        for i in range (4):  
            for p in range (60):
                oled.pixel(Px, Py, 1)
                Px += 1
            contadorY += 1
            Px += 4
            if contadorY == 2:
                Py += 30
                contadorY = 50
                Px = 0

        oled.text("Dados", 0, 15)
        oled.text("Coleta", 60, 15)
        oled.text("Som", 0, 45)
        oled.text("Scan", 60, 45)


        if indexAnterior != index:
            if index == 0:
                Px = 30
                Py = 5
                for i in range (5):
                    oled.pixel(i + 90, 5, 0)
                for i in range (5):
                    oled.pixel(i + 30, 35, 0)
                for i in range (5):
                    oled.pixel(i + 90, 35, 0)

                    
            elif index == 1:
                Px = 90
                Py = 5
                for i in range (5):
                    oled.pixel(i + 30, 5, 0)
                for i in range (5):
                    oled.pixel(i + 30, 35, 0)
                for i in range (5):
                    oled.pixel(i + 90, 35, 0)
            elif index == 2:
                Px = 30
                Py = 35
                for i in range (5):
                    oled.pixel(i + 90, 5, 0)
                for i in range (5):
                    oled.pixel(i + 30, 5, 0)
                for i in range (5):
                    oled.pixel(i + 90, 35, 0)
            elif index == 3:
                Px = 90
                Py = 35
                for i in range (5):
                    oled.pixel(i + 90, 5, 0)
                for i in range (5):
                    oled.pixel(i + 30, 35, 0)
                for i in range (5):
                    oled.pixel(i + 30, 5, 0)


            for i in range (5):
                oled.pixel(i + Px, Py, 1)
            indexAnterior = index

        

    elif estado == 1:
        
        oled.fill(0)
        oled.text("Dados", 10, 30)
        oled.show()
        if enter == 0:
            oled.fill(0)
            indexAnterior = 5
            estado = 0
            return
    elif estado == 2:
        
        oled.fill(0)
        oled.text("Coleta", 10, 30)
        oled.show()
        if enter == 0:
            oled.fill(0)
            indexAnterior = 5
            estado = 0
            return
    elif estado == 3:
        
        oled.fill(0)
        oled.text("Som", 10, 30)
        oled.show()
        if enter == 0:
            oled.fill(0)
            indexAnterior = 5
            estado = 0
            return
    elif estado == 4:
        
        oled.fill(0)
        oled.text("Scan", 10, 30)
        oled.show()
        if enter == 0:
            oled.fill(0)
            indexAnterior = 5
            estado = 0
            return
                
        
    print("Estado: ", estado)
    oled.show()
