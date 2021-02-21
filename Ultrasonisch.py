# ---- Imports ----

from machine import UART

# ---- Setup ----

uart = UART(1)
uart.init(baudrate=9600, bits=8, parity=None, stop=1, timeout_chars=100,
pins=('P3', 'P4'))

# ---- Code ----

measure_count = 0
while True:
    measure_count = measure_count + 1

    header_bytes = uart.read(1)
    while(header_bytes != b'\xff'):
        header_bytes = uart.read(1)

    high = int(uart.read(1)[0])

    low = int(uart.read(1)[0])

    sum = int(uart.read(1)[0])

    # response time: 100-300ms, we toss away 9, show the 10th.
    if measure_count > 10:
        measure_count = 0

        distance = (high*256) + low

        if distance < 30:
            print("Below the lower limit")
        else:
            in_cm = distance / 10
            print("Distance: " + str(in_cm) + " cm")
