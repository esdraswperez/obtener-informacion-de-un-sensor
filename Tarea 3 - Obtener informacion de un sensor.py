from machine import I2C,Pin
from time import sleep
from pico_i2c_lcd import I2cLcd
from dht import DHT11

pin = Pin(20, Pin.IN, Pin.PULL_UP)
dht11 = DHT11(pin, None, dht11 = True)

# Raspberry Pi Pico
i2c = I2C(0, sda=Pin(8), scl=Pin(9), freq=400000)

#Dirección del I2C y tamaño del LCD
direccion = i2c.scan()[0]

#Configuración LCD
lcd = I2cLcd(i2c,direccion,2,16)

while True:
    T, H = dht11.read()
    try:
        lcd.move_to(0,0)
        lcd.putstr(f"Temperatura {T}°C")
        lcd.move_to(0,1)
        lcd.putstr(f"Humedad {H}%")
        print(f"Temperatura {T}°C")
        print(f"Humedad {H}%")
    except:
        print("Error...")
    sleep(2)
    lcd.clear()