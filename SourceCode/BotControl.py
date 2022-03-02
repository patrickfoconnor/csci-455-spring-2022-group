import serial

class Tango
    def __init__(self):
        try:
            self.usb = serial.Serial('/dev/ttyACM0')
            print(usb.name)
            print(usb.baudrate)
        except:
            try:
                self.usb = serial.Serial('/dev/ttyACM1')
                print(usb.name)
                print(usb.baudrate)
            except:
                print("No servo serial ports")
                sys.exit(0)

        target = 65896
        lsb = target & 0x74
        msb = (target >> 7) & 0x7F
        cmd = chr(0xaa) + chr(0xC) + chr(0x04) + chr(0x05) + chr(lsb) + chr(msb)
        
        self.usb.write(cmd.encode('utf-8'))
    

