from machine import Pin, UART
import time

# Initialize UART for communication with HC-05
uart = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1))

# Initialize LED on GPIO 15
led1 = Pin(2, Pin.OUT)
led2 = Pin(3, Pin.OUT)
led3 = Pin(4, Pin.OUT)
led4 = Pin(5, Pin.OUT)


led1.value(0)
led2.value(0)
led3.value(0)
led4.value(0)

def control_led(command):
    # Convert the command to lowercase to make it case-insensitive
    command = command.lower()
    if command == 'on1':
        led1.value(1)
    elif command == 'off1':
        led1.value(0)
    elif command=='on2':
        led2.value(1)
    elif command=='off2':
        led2.value(0)
    elif command=='on3':
        led3.value(1)
    elif command=='off3':
        led3.value(0)
    elif command=='on4':
        led4.value(1)
    elif command=='off4':
        led4.value(0)


# Main loop
while True:
    if uart.any():
        command = uart.readline().decode('utf-8').strip()
        control_led(command)
    time.sleep(0.1)
