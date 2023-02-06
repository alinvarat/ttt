let USR = 0
let USL = 0
let USC = 0
let count = 0
let ENCL = 0
basic.forever(function () {
    USC = Math.idiv(iBIT.ReadADC(ibitReadADC.ADC1), 10)
    USL = Math.idiv(iBIT.ReadADC(ibitReadADC.ADC0), 10)
    USR = Math.idiv(iBIT.ReadADC(ibitReadADC.ADC2), 10)
    ENCL = Math.idiv(iBIT.ReadADC(ibitReadADC.ADC3), 10)
    ENCL = 0
    ENCL = 0
    serial.writeValue("V", count)
})
