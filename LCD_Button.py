import time

import board
import digitalio
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface

from lcd.lcd import CursorMode

button_a = digitalio.DigitalInOut(board.BUTTON_A)
button_a.direction = digitalio.Direction.INPUT
button_a.pull = digitalio.Pull.DOWN

# Talk to the LCD at I2C address 0x27.
# The number of rows and columns defaults to 4x20, so those
# arguments could be omitted in this case.
lcd = LCD(I2CPCF8574Interface(0x27), num_rows=2, num_cols=16)

lcd.print("abc ")
lcd.print("This is quite long and will wrap onto the next line automatically.")

lcd.clear()

# Start at the second line, fifth column (numbering from zero).
lcd.set_cursor_pos(1, 4)
lcd.print("Here I am")

# Make the cursor visible as a line.
lcd.set_cursor_mode(CursorMode.LINE)

while True:
    if button_a.value:
        print((1,))
    else:
        print((0,))
    time.sleep(0.1)