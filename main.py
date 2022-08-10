from screen import Screen
import serial, os
from time import sleep


screen = Screen()
screen.run()

# porta = "COM10"
# velocidade = 9600

# con = serial.Serial(porta, velocidade)
# con.timeout = 1

# while True:
#     os.system('cls')
#     con.write(b'A')
#     print(con.readline().decode('ascii'))
#     sleep(1)
#     os.system('cls')
#     con.write(b'a')
#     print(con.readline().decode('ascii'))
#     sleep(1)
