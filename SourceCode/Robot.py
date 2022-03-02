
import serial, time

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


      target = 6800

        
      lsb = target & 0x74
      msb = (target >> 7) & 0x7F

# Explanation
# 0x01 is wheels?
# 0x02 is body
# 0x03 is the head
# 0x04 is 
      cmd = chr(0xaa) + chr(0xC) + chr(0x04) + chr(0x02) + chr(lsb) + chr(msb)
      self.maestro.write(cmd.encode('utf-8'))

