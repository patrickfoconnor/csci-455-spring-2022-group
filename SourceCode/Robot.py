import sys

import serial


class Robot:
    def __init__(self):
        try:
            self.maestro = serial.Serial('/dev/ttyACM0')
            print(self.maestro.name)
            print(self.maestro.baudrate)

        except:
            try:
                self.maestro = serial.Serial('/dev/ttyACM1')
                print(self.maestro.name)
                print(self.maestro.baudrate)
            except:
                print("No servo serial ports")
                sys.exit(0)

        target = 5896

        lsb = target & 0x74
        msb = (target >> 7) & 0x7F


# Explanation
        # 0x00 or 0x01 = Wheels
        # 0x02 = Body
        # 0x03 = Head
        cmd = chr(0xaa) + chr(0xC) + chr(0x04) + chr(0x01) + chr(lsb) + chr(msb)

        self.maestro.write(cmd)

