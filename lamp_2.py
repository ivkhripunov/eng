import RPi.GPIO as GPIO
import time

dac = [26, 19, 13, 6, 5, 11, 9, 10]
bits = len(dac)
levels = 2 ** bits
max_voltage = 3.3

def decimal_to_binary(number):
    return [int(i) for i in bin(number)[2:].zfill(len(dac))]

def decimal_to_dac(value):
    signal = decimal_to_binary(value)
    GPIO.output(dac, signal)
    return signal

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT, initial = GPIO.LOW)

try:
    while True:

        for i in range(256):
            decimal_to_dac(i)
            time.sleep(0.002)
            print(i)
        
        for i in range(254, 0, -1):
            decimal_to_dac(i)
            time.sleep(0.002)
            print(i)

        
except KeyboardInterrupt:
    print('The program was stopped by the keyboatd')
else:
    print('No exceptions')
finally:
    GPIO.output(dac, GPIO.LOW)
    GPIO.cleanup(dac)
    print('Cleanup completed')