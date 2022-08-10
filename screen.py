from time import sleep
from tkinter import Tk, Button
import serial


class Screen:
    def __init__(self) -> None:
        self.door = "COM10"
        self.velocity = 9600
        self.serial_connection = serial.Serial(self.door, self.velocity)
        self.serial_connection.timeout = 1

        self.window = Tk()
        self.window.geometry("300x300")
        self.window.title("Controle de led")
        self.window.resizable(False, False)

        self.led_state = False

        self.turn_led_on = Button(self.window, {'text': 'Turn on', 'bg': 'yellow', 'fg': 'black'},
                                command=lambda: self.change_led_state('A'), width=20)
        self.turn_led_on.pack({'pady': 10})

        self.turn_led_off = Button(self.window, {'text': 'Turn off', 'bg': 'red', 'fg': 'white'},
                                command=lambda: self.change_led_state('a'), width=20)
        self.turn_led_off.pack(pady=5)

    def change_led_state(self, state: str) -> None:
        if self.led_state and state == 'a':
            self.serial_connection.write(state.encode())
            print(self.serial_connection.readline().decode())
        else:
            self.serial_connection.write(state.encode())
            print(self.serial_connection.readline().decode())

    def run(self) -> None:
        self.window.mainloop()
