print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.tapdance import TapDance
from kmk.modules.layers import Layers
from kmk.modules.modtap import ModTap

keyboard = KMKKeyboard()

keyboard.debug_enabled = False
keyboard.modules.append(TapDance())
keyboard.modules.append(Layers())
keyboard.modules.append(ModTap())
TapDance.tap_time = 350

TD = KC.TD(KC.DF(1),KC.A, KC.B, KC.C, KC.D, KC.E, KC.F, KC.G, KC.H, KC.I, KC.J, KC.K, KC.L, KC.M, KC.N, KC.O, KC.P, KC.Q, KC.R, KC.S ,KC.T ,KC.U ,KC.V ,KC.W ,KC.X ,KC.Y ,KC.Z)
TD2 = KC.TD(KC.DF(0),KC.LSFT(KC.A),KC.LSFT(KC.B),KC.LSFT(KC.C),KC.LSFT(KC.D),KC.LSFT(KC.E),KC.LSFT(KC.F),KC.LSFT(KC.G),KC.LSFT(KC.H),KC.LSFT(KC.I),KC.LSFT(KC.J),KC.LSFT(KC.K),KC.LSFT(KC.L),KC.LSFT(KC.M),KC.LSFT(KC.N),KC.LSFT(KC.O),KC.LSFT(KC.P),KC.LSFT(KC.Q),KC.LSFT(KC.R),KC.LSFT(KC.S),KC.LSFT(KC.T),KC.LSFT(KC.U),KC.LSFT(KC.V),KC.LSFT(KC.W),KC.LSFT(KC.X),KC.LSFT(KC.Y),KC.LSFT(KC.Z))

keyboard.col_pins = (board.GP10,)
keyboard.row_pins = (board.GP13,)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
        [TD,],
        [TD2,],
]

if __name__ == '__main__':
    keyboard.go()
