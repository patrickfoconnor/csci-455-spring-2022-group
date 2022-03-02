import serial, time


try:
    usb = serial.Serial('/dev/ttyACM0')
    print(usb.name)
    print(usb.baudrate)

except:
    try:
        usb = serial.Serial('/dev/ttyACM1')
        print(usb.name)
        print(usb.baudrate)

    except:
        print("No servo serial ports")

target = 6800

lsb = target & 0x74
msb = (target >> 7) & 0x7F


# 0x01 is wheels?
# 0x02 is body
# 0x03 is the head
# 0x04 is 
cmd = chr(0xaa) + chr(0xC) + chr(0x04) + chr(0x02) + chr(lsb) + chr(msb)

usb.write(cmd.encode('utf-8'))

