USC = int(0)

def on_forever():
    global USC
    USC = iBIT.read_adc(int(ibitReadADC.ADC1))
    serial.write_value("USC", int(USC))
basic.forever(on_forever)
