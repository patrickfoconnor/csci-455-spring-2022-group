import serial


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

target = 6700

lsb = target & 0x74
msb = (target >> 7) & 0x7F

cmd = chr(0xaa) + chr(0xC) + chr(0x04) + chr(0x01) + chr(lsb) + chr(msb)

usb.write(cmd)

