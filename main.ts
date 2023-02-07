let USC = 0
basic.forever(function () {
    USC = iBIT.ReadADC(ibitReadADC.ADC1)
    serial.writeValue("USC", USC)
})
