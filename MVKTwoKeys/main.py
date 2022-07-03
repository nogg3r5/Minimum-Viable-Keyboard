print("Starting...I never actually got htis to work because one of my switches was connected ot two GPIO pins and not a GPIO and Ground. Oops")

import board

import MyKeyboard
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.tapdance import TapDance

keyboard = MyKeyboard.MyKeyboard()

keyboard.debug_enabled = True

keyboard.modules.append(TapDance())

TapDance.tap_time = 350

TD = KC.TD(KC.A, KC.B, KC.C, KC.D, KC.E, KC.F, KC.G, KC.H, KC.I, KC.J, KC.K, KC.L, KC.M, KC.N, KC.O, KC.P, KC.Q, KC.R, KC.S ,KC.T ,KC.U ,KC.V ,KC.W ,KC.X ,KC.Y, KC.Z, KC.SPACE)
TD2 = KC.TD(KC.LSFT(KC.A),KC.LSFT(KC.B),KC.LSFT(KC.C),KC.LSFT(KC.D),KC.LSFT(KC.E),KC.LSFT(KC.F),KC.LSFT(KC.G),KC.LSFT(KC.H),KC.LSFT(KC.I),KC.LSFT(KC.J),KC.LSFT(KC.K),KC.LSFT(KC.L),KC.LSFT(KC.M),KC.LSFT(KC.N),KC.LSFT(KC.O),KC.LSFT(KC.P),KC.LSFT(KC.Q),KC.LSFT(KC.R),KC.LSFT(KC.S),KC.LSFT(KC.T),KC.LSFT(KC.U),KC.LSFT(KC.V),KC.LSFT(KC.W),KC.LSFT(KC.X),KC.LSFT(KC.Y),KC.LSFT(KC.Z), KC.SPACE)


keyboard.keymap = [
        [TD,TD2],
]

if __name__ == '__main__':
    keyboard.go()
