import board
from analogio import AnalogIn
from digitalio import DigitalInOut, Pull
import usb_hid
from adafruit_hid.mouse import Mouse

mouse = Mouse(usb_hid.devices)
px = AnalogIn(board.GP26)
py = AnalogIn(board.GP27)
pc = DigitalInOut(board.GP6)
pc.switch_to_input(pull=Pull.UP)


sensitivity = 5
midpoint = 32768 # middle point value approximately of joystick
deadzone = 5000
invert = True # if true, it will invert the x and y values by multiplying them by -1.
debug = True 

def get_joystick_value(analog_input):
    value = analog_input.value - midpoint
    if abs(value) < deadzone:
        return 0
    return value / (midpoint - deadzone)

while True:
    x = get_joystick_value(px)
    y = get_joystick_value(py)
    clk = not pc.value

    if debug:
        print(f'px={px.value} | py={py.value} | x={x} | y={y} | clk={clk}')

    if invert:
        x = -x 
        y = -y 

    if clk :
        mouse.click(Mouse.LEFT_BUTTON)
        
    move_x = int(x * sensitivity)
    move_y = int(y * sensitivity)
    if move_x != 0 or move_y != 0:
        mouse.move(x=move_x, y=move_y)

