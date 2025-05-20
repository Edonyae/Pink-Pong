import serial

def getByte(input_byte, pos):
    return (input_byte >> pos) & 0b00000001

def interpret_joystick_direction(input_byte):
    input_byte = input_byte[0]
    directions = {
        "haut": getByte(input_byte, 0),
        "gauche": getByte(input_byte, 1),
        "droite": getByte(input_byte, 2),
        "bas": getByte(input_byte, 3)
    }
    return directions

ser = serial.Serial("/dev/ttyACM0", baudrate=9600)

while True:
    if ser.in_waiting > 0:
        input_byte = ser.read(1)
        joystick_direction = interpret_joystick_direction(input_byte)

        print("Joystick direction:", joystick_direction)
