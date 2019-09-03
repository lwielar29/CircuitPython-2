import time
import board
import pulseio
from digitalio import DigitalInOut, Direction

# PWM (fading) LEDs are connected on D0 (PWM not avail on D1)
pwm_leds = board.D0
pwm = pulseio.PWMOut(pwm_leds, frequency=1000, duty_cycle=0)

# digital LEDs connected on D2
digital_leds = DigitalInOut(board.D2)
digital_leds.direction = Direction.OUTPUT
brightness = 0  # how bright the LED is
fade_amount = 1285  # 2% steping of 2^16
counter = 0  # counter to keep track of cycles

while True:

    # And send to LED as PWM level
    pwm.duty_cycle = brightness

    # change the brightness for next time through the loop:
    brightness = brightness + fade_amount

    print(brightness)
    time.sleep(0.1)
    # reverse the direction of the fading at the ends of the fade:
    if brightness <= 0:
        fade_amount = -fade_amount
        counter += 1
    elif brightness >= 65535:
        fade_amount = -fade_amount
        counter += 1