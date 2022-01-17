import mido
import serial
import time


port='COM10' #порт midi устройства
arduino=serial.Serial(port, 115200)
time.sleep(2)

note = [35,37,38,41,44,45,47,48,49] #ноты midi устройства

mid = mido.MidiFile('song.mid')
for msg in mid.play():
    a = msg.bytes()
    if msg.type == 'note_on':
        print(a[1])
        if a[1] == note[0]:
            arduino.write(b'1')
            print('good1')
        if a[1] == note[1]:
            arduino.write(b'2')
            print('good2')
        if a[1] == note[2]:
            arduino.write(b'3')
            print('good3')
        if a[1] == note[3]:
            arduino.write(b'4')
            print('good4')
        if a[1] == note[4]:
            arduino.write(b'5')
            print('good5')
        if a[1] == note[5]:
            arduino.write(b'6')
            print('good6')
        if a[1] == note[6]:
            arduino.write(b'7')
            print('good7')
        if a[1] == note[7]:
            arduino.write(b'8')
            print('good8')
        if a[1] == note[8]:
            arduino.write(b'9')
            print('good9')
