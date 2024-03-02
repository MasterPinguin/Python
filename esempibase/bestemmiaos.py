from machine import Pin, PWM, I2C
import utime
from ssd1306 import SSD1306_I2C
import framebuf
from buzzer_music import music

song = '0 E4 1 8;0 G4 1 8;8 A4 1 8;8 D5 1 8;16 F#4 1 8;16 A4 1 8;24 A4 1 8;24 C#5 1 8;32 E4 1 8;32 G4 1 8;32 B4 1 8;40 A4 1 8;40 D5 1 8;40 F#5 1 8;48 F#4 1 8;48 A4 1 8;48 C#5 1 8;56 A4 1 8;56 C#5 1 8;56 E5 1 8;64 E4 1 8;64 G4 1 8;64 B4 1 8;72 A4 1 8;72 D5 1 8;72 F#5 1 8;80 F#4 1 8;80 A4 1 8;80 C#5 1 8;88 A4 1 8;88 C#5 1 8;88 E5 1 8;96 E4 1 8;96 G4 1 8;96 B4 1 8;100 A5 1 8;102 B5 1 8;104 A4 1 8;104 D5 1 8;104 F#5 1 8;110 D5 1 8;111 E5 1 8;112 F#4 1 8;112 A4 1 8;112 C#5 1 8;118 F#5 1 8;119 A5 1 8;120 A4 1 8;120 C#5 1 8;120 E5 1 8;128 E4 1 8;128 G4 1 8;128 B4 1 8;130 D6 1 8;132 B5 1 8;134 A5 1 8;136 A4 1 8;136 D5 1 8;136 F#5 1 8;142 D5 1 8;143 E5 1 8;144 F#4 1 8;144 A4 1 8;144 C#5 1 8;150 A5 1 8;151 F#5 1 8;152 A4 1 8;152 C#5 1 8;152 E5 1 8;160 E4 1 8;160 G4 1 8;160 B4 1 8;164 A5 1 8;166 B5 1 8;168 D5 1 8;168 F#5 1 8;168 D6 1 8;174 D5 1 8;174 F#6 1 8;175 E5 1 8;175 E6 1 8;176 D5 1 8;176 C#6 1 8;182 F#5 1 8;182 D6 1 8;183 C#6 1 8;184 A4 1 8;184 C#5 1 8;184 E5 1 8;184 A5 1 8;192 E4 1 8;192 G4 1 8;192 B4 1 8;196 B5 1 8;198 A5 1 8;200 A4 1 8;200 D5 1 8;200 F#5 1 8;206 D5 1 8;207 E5 1 8;208 F#4 1 8;208 A4 1 8;208 C#5 1 8;214 F#5 1 8;215 A5 1 8;216 A4 1 8;216 C#5 1 8;216 E5 1 8;224 E4 1 8;224 G4 1 8;224 B4 1 8;228 A5 1 8;230 B5 1 8;232 A4 1 8;232 D5 1 8;232 F#5 1 8;238 D5 1 8;239 E5 1 8;240 F#4 1 8;240 A4 1 8;240 C#5 1 8;244 F#6 1 8;246 F#5 1 8;247 A5 1 8;248 A4 1 8;248 C#5 1 8;248 E5 1 8;256 B4 1 8;256 D5 1 8;256 F#5 1 8;262 B5 1 8;263 A5 1 8;264 G#4 1 8;264 B4 1 8;264 E5 1 8;268 E5 1 8;270 D5 1 8;272 E4 1 8;272 A4 1 8;272 C#5 1 8;278 D5 1 8;279 E5 1 8;280 D4 1 8;280 G4 1 8;280 B4 1 8;288 B4 1 8;288 D5 1 8;288 F#5 1 8;288 D6 1 8;294 B5 1 8;295 A5 1 8;296 G#4 1 8;296 B4 1 8;296 E5 1 8;300 E5 1 8;302 D5 1 8;302 E6 1 8;304 E4 1 8;304 A4 1 8;304 C#5 1 8;304 C#6 1 8;308 D6 1 8;310 F#6 1 8;312 B4 1 8;312 B5 1 8;0 E3 1 8;4 F#3 1 8;8 G3 1 8;12 B3 1 8;16 A3 1 8;20 G3 1 8;24 D3 1 8;32 E3 1 8;36 F#3 1 8;40 G3 1 8;44 B3 1 8;48 A3 1 8;52 G3 1 8;56 D3 1 8;64 E3 1 8;68 F#3 1 8;72 G3 1 8;76 B3 1 8;80 A3 1 8;84 G3 1 8;88 D3 1 8;96 E3 1 8;100 F#3 1 8;104 G3 1 8;108 B3 1 8;112 A3 1 8;116 G3 1 8;120 D3 1 8;128 E3 1 8;132 F#3 1 8;136 G3 1 8;140 B3 1 8;144 A3 1 8;148 G3 1 8;152 D3 1 8;160 E3 1 8;164 F#3 1 8;168 G3 1 8;168 A4 1 8;172 B3 1 8;176 A3 1 8;176 F#4 1 8;176 A4 1 8;180 G3 1 8;184 D3 1 8;192 E3 1 8;196 F#3 1 8;200 G3 1 8;204 B3 1 8;208 A3 1 8;212 G3 1 8;216 D3 1 8;224 E3 1 8;228 F#3 1 8;232 G3 1 8;236 B3 1 8;240 A3 1 8;244 G3 1 8;248 D3 1 8;256 B2 1 8;256 B3 1 8;264 E3 1 8;264 E4 1 8;272 A2 1 8;272 A3 1 8;280 G2 1 8;280 G3 1 8;288 B2 1 8;288 B3 1 8;296 E3 1 8;296 E4 1 8;304 A2 1 8;304 A3 1 8;312 G2 1 8;312 D4 1 8;312 G4 1 8;312 B4 1 8;0 E4 1 26;0 G4 1 26;8 A4 1 26;8 D5 1 26;16 F#4 1 26;16 A4 1 26;24 A4 1 26;24 C#5 1 26;32 E4 1 26;32 G4 1 26;32 B4 1 26;40 A4 1 26;40 D5 1 26;40 F#5 1 26;48 F#4 1 26;48 A4 1 26;48 C#5 1 26;56 A4 1 26;56 C#5 1 26;56 E5 1 26;64 E4 1 26;64 G4 1 26;64 B4 1 26;72 A4 1 26;72 D5 1 26;72 F#5 1 26;80 F#4 1 26;80 A4 1 26;80 C#5 1 26;88 A4 1 26;88 C#5 1 26;88 E5 1 26;96 E4 1 26;96 G4 1 26;96 B4 1 26;100 A5 1 26;102 B5 1 26;104 A4 1 26;104 D5 1 26;104 F#5 1 26;110 D5 1 26;111 E5 1 26;112 F#4 1 26;112 A4 1 26;112 C#5 1 26;118 F#5 1 26;119 A5 1 26;120 A4 1 26;120 C#5 1 26;120 E5 1 26;128 E4 1 26;128 G4 1 26;128 B4 1 26;130 D6 1 26;132 B5 1 26;134 A5 1 26;136 A4 1 26;136 D5 1 26;136 F#5 1 26;142 D5 1 26;143 E5 1 26;144 F#4 1 26;144 A4 1 26;144 C#5 1 26;150 A5 1 26;151 F#5 1 26;152 A4 1 26;152 C#5 1 26;152 E5 1 26;160 E4 1 26;160 G4 1 26;160 B4 1 26;164 A5 1 26;166 B5 1 26;168 D5 1 26;168 F#5 1 26;168 D6 1 26;174 D5 1 26;174 F#6 1 26;175 E5 1 26;175 E6 1 26;176 D5 1 26;176 C#6 1 26;182 F#5 1 26;182 D6 1 26;183 C#6 1 26;184 A4 1 26;184 C#5 1 26;184 E5 1 26;184 A5 1 26;192 E4 1 26;192 G4 1 26;192 B4 1 26;196 B5 1 26;198 A5 1 26;200 A4 1 26;200 D5 1 26;200 F#5 1 26;206 D5 1 26;207 E5 1 26;208 F#4 1 26;208 A4 1 26;208 C#5 1 26;214 F#5 1 26;215 A5 1 26;216 A4 1 26;216 C#5 1 26;216 E5 1 26;224 E4 1 26;224 G4 1 26;224 B4 1 26;228 A5 1 26;230 B5 1 26;232 A4 1 26;232 D5 1 26;232 F#5 1 26;238 D5 1 26;239 E5 1 26;240 F#4 1 26;240 A4 1 26;240 C#5 1 26;244 F#6 1 26;246 F#5 1 26;247 A5 1 26;248 A4 1 26;248 C#5 1 26;248 E5 1 26;256 B4 1 26;256 D5 1 26;256 F#5 1 26;262 B5 1 26;263 A5 1 26;264 G#4 1 26;264 B4 1 26;264 E5 1 26;268 E5 1 26;270 D5 1 26;272 E4 1 26;272 A4 1 26;272 C#5 1 26;278 D5 1 26;279 E5 1 26;280 D4 1 26;280 G4 1 26;280 B4 1 26;288 B4 1 26;288 D5 1 26;288 F#5 1 26;288 D6 1 26;294 B5 1 26;295 A5 1 26;296 G#4 1 26;296 B4 1 26;296 E5 1 26;300 E5 1 26;302 D5 1 26;302 E6 1 26;304 E4 1 26;304 A4 1 26;304 C#5 1 26;304 C#6 1 26;308 D6 1 26;310 F#6 1 26;312 B4 1 26;312 B5 1 26;0 E3 1 26;4 F#3 1 26;8 G3 1 26;12 B3 1 26;16 A3 1 26;20 G3 1 26;24 D3 1 26;32 E3 1 26;36 F#3 1 26;40 G3 1 26;44 B3 1 26;48 A3 1 26;52 G3 1 26;56 D3 1 26;64 E3 1 26;68 F#3 1 26;72 G3 1 26;76 B3 1 26;80 A3 1 26;84 G3 1 26;88 D3 1 26;96 E3 1 26;100 F#3 1 26;104 G3 1 26;108 B3 1 26;112 A3 1 26;116 G3 1 26;120 D3 1 26;128 E3 1 26;132 F#3 1 26;136 G3 1 26;140 B3 1 26;144 A3 1 26;148 G3 1 26;152 D3 1 26;160 E3 1 26;164 F#3 1 26;168 G3 1 26;168 A4 1 26;172 B3 1 26;176 A3 1 26;176 F#4 1 26;176 A4 1 26;180 G3 1 26;184 D3 1 26;192 E3 1 26;196 F#3 1 26;200 G3 1 26;204 B3 1 26;208 A3 1 26;212 G3 1 26;216 D3 1 26;224 E3 1 26;228 F#3 1 26;232 G3 1 26;236 B3 1 26;240 A3 1 26;244 G3 1 26;248 D3 1 26;256 B2 1 26;256 B3 1 26;264 E3 1 26;264 E4 1 26;272 A2 1 26;272 A3 1 26;280 G2 1 26;280 G3 1 26;288 B2 1 26;288 B3 1 26;296 E3 1 26;296 E4 1 26;304 A2 1 26;304 A3 1 26;312 G2 1 26;312 D4 1 26;312 G4 1 26;312 B4 1 26'

button2 = Pin(16, Pin.IN, Pin.PULL_UP)
button3 = Pin(17, Pin.IN, Pin.PULL_UP)
button1 = Pin(18, Pin.IN, Pin.PULL_UP)
buzzer = PWM(Pin(15))
buzzer.freq(980)
scelta = 1
WIDTH  = 128
HEIGHT = 64
i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=400000)
oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)
menu = 0
enter = 0
sensor_temp = machine.ADC(4)
conversion_factor = 3.3 / (65535)
led = Pin(25, Pin.OUT)

while True:
    b1 = button1.value()
    b2 = button2.value()
    b3 = button3.value()
    if not b1:
        print('Button pressed!')
        buzzer.duty_u16(1000)
        utime.sleep(0.20)
        buzzer.duty_u16(0)
        scelta -= 1 #diminuisci scelta scelta
    elif not b2:
        print('Button 2 pressed!')
        buzzer.duty_u16(1000)
        utime.sleep(0.20)
        buzzer.duty_u16(0)
        scelta += 1 #aumenta scelta scelta
    elif not b3:
        print('Button 3 pressed!')
        buzzer.duty_u16(1000)
        utime.sleep(0.20)
        buzzer.duty_u16(0)
        enter = 1
        print(enter)
    elif scelta == 0:
        scelta = 1
    elif scelta > 4:
        scelta = 0

    elif (scelta == 1) and (menu == 0):
        oled.fill(0)
        oled.text("Bestemmio OS",20,3)
        oled.text("Music",20,13)
        oled.text("Temperatura",20,23)        
        oled.text(">",12,13)
        oled.text("Power on led",20,33)
        oled.text("Power off led",20,43)
        oled.show()
    elif (scelta == 2) and (menu == 0):
        oled.fill(0)
        oled.text("Bestemmio OS",20,3)
        oled.text("Music",20,13)
        oled.text("Temperatura",20,23) 
        oled.text(">",12,23)
        oled.text("Power on led",20,33)
        oled.text("Power off led",20,43)
        oled.show()
    elif (scelta == 3) and (menu == 0):
        oled.fill(0)
        oled.text("Bestemmio OS",20,3)
        oled.text("Music",20,13)
        oled.text("Temperatura",20,23) 
        oled.text(">",12,33)
        oled.text("Power on led",20,33)
        oled.text("Power off led",20,43)
        oled.show()
    elif (scelta == 4) and (menu == 0):
        oled.fill(0)
        oled.text("Bestemmio OS",20,3)
        oled.text("Music",20,13)
        oled.text("Temperatura",20,23) 
        oled.text(">",12,43)
        oled.text("Power on led",20,33)
        oled.text("Power off led",20,43)
        oled.show()
    if (scelta == 2 and menu == 0 and enter == 1):
        print(menu)
        enter = 0
        menu = 2
    elif menu == 2:
        reading = sensor_temp.read_u16() * conversion_factor 
        temperature = 27 - (reading - 0.706)/0.001721
        oled.fill(0)
        oled.text("Temperature is:",10,3)
        oled.text(str(temperature),35,13)
        oled.show()
        utime.sleep(5)
        menu = 0
    if (scelta == 1 and menu == 0 and enter == 1):
        print(menu)
        enter = 0
        menu = 1
    elif menu == 1:
        mySong = music(song, pins=[Pin(15)])
        oled.fill(0)
        oled.text("Bestemmio OS",20,3)
        oled.text("Calm minecraft",12,13)
        oled.text("Press stop icon to stop",2,32) 
        oled.show()
        while True:
            print(mySong.tick())
            utime.sleep(0.04)
    elif (scelta == 3 and menu == 0 and enter == 1):
        print(menu)
        enter = 0
        oled.fill(0)
        oled.text("Led is On",0,15)
        oled.show()
        led.on()
        utime.sleep(1)
    elif (scelta == 4 and menu == 0 and enter == 1):
        print(menu)
        enter = 0
        oled.fill(0)
        oled.text("Led is Off",0,15)
        oled.show()
        led.off()
        utime.sleep(1)
        
        


