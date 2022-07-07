print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.tapdance import TapDance
from kmk.modules.layers import Layers
from kmk.modules.modtap import ModTap
from kmk.modules.split import *
from kmk.extensions.LED import AnimationModes, LED

keyboard = KMKKeyboard()
led_ext = LED(led_pin=[board.LED,board.GP15],brightness=50)

split = Split(
    split_flip=True,
    split_side=None,
    split_type=SplitType.UART,
    uart_flip=True,
    data_pin=board.GP21,
    data_pin2=None,
    use_pio=True,
    )

keyboard.debug_enabled = True
keyboard.modules.append(TapDance())
keyboard.modules.append(Layers())
keyboard.modules.append(ModTap())
keyboard.extensions.append(led_ext)
keyboard.modules.append(split)

TapDance.tap_time = 350


TD = KC.TD(KC.A, KC.B, KC.C, KC.D, KC.E, KC.F, KC.G, KC.H, KC.I, KC.J, KC.K, KC.L, KC.M, KC.N, KC.O, KC.P, KC.Q, KC.R, KC.S ,KC.T ,KC.U ,KC.V ,KC.W ,KC.X ,KC.Y ,KC.Z)
TD2 = KC.TD(KC.LSFT(KC.A),KC.LSFT(KC.B),KC.LSFT(KC.C),KC.LSFT(KC.D),KC.LSFT(KC.E),KC.LSFT(KC.F),KC.LSFT(KC.G),KC.LSFT(KC.H),KC.LSFT(KC.I),KC.LSFT(KC.J),KC.LSFT(KC.K),KC.LSFT(KC.L),KC.LSFT(KC.M),KC.LSFT(KC.N),KC.LSFT(KC.O),KC.LSFT(KC.P),KC.LSFT(KC.Q),KC.LSFT(KC.R),KC.LSFT(KC.S),KC.LSFT(KC.T),KC.LSFT(KC.U),KC.LSFT(KC.V),KC.LSFT(KC.W),KC.LSFT(KC.X),KC.LSFT(KC.Y),KC.LSFT(KC.Z))
LEDS = KC.TD(KC.LED_TOG(),KC.LED_SET(100),KC.LED_SET(0),KC.LED_MODE_BREATHE)


keyboard.col_pins = (board.GP10,)
keyboard.row_pins = (board.GP13,)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
        [TD,TD2,]
        ]

if __name__ == '__main__':
    keyboard.go()
