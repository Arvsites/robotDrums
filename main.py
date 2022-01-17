import mido
import serial
import time

list=['COM1','COM2','COM3','COM4','COM5','COM6','COM7','COM8','COM9','COM10','COM11','COM12','COM13','COM14','COM15','COM16','COM17','COM18',]



COM1='COM1'
COM2='COM2'
COM3='COM3'
COM4='COM4'
COM5='COM5'
COM6='COM6'
COM7='COM7'
COM8='COM8'
COM9='COM9'
COM10='COM10'
COM11='COM11'
COM12='COM12'
COM13='COM13'
COM14='COM14'
COM15='COM15'
COM16='COM16'
COM17='COM17'
COM18='COM18'
COM19='COM19'
time.sleep(1)
arduino = serial.Serial()

arduino.baudrate = 115200

i=1

while True:
    time.sleep(.2)
    print(i)
    arduino.port = list[i]
    try:

        arduino.open()
        if arduino.isOpen()==True:
            print('connected')
            #print('arduino is on COMPORT'.join(i))
            break
        break

    except:
        print('waiting')
        i=i+1
        if i==18:
            print('Kindly remove usb cable and try again')
            break

print('here we go')
print(i+1)


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
