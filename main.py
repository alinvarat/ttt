USR = 0
USL = 0
USC = 0
ENCL = 0
count = 0

def on_forever():
    global USC, USL, USR, ENCL, count
    USC = Math.idiv(iBIT.read_adc(ibitReadADC.ADC1), 10)
    USL = Math.idiv(iBIT.read_adc(ibitReadADC.ADC0), 10)
    USR = Math.idiv(iBIT.read_adc(ibitReadADC.ADC2), 10)
    ENCL = Math.idiv(iBIT.read_adc(ibitReadADC.ADC3), 10)
    ENCL = 0
    ENCL = 0
    for ENCL in range (400):
        if ENCL > 56:
            count += 1
    serial.write_value("V", count)
basic.forever(on_forever)
