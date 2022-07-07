To enable split:
rename each pico with L or R at the end of the drive name
connect pins 38-38 (VSYS - for power), 39-39(GND), 27-27 (GP21)
Put code on both halves

connect switches to 14 (GP10) and 17 (GP13)

GP21 is normally I2C but we use the PIO library to convert this to UART
