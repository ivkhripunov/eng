import RPi.GPIO as GPIO

dac = [26, 19, 13, 6, 5, 11, 9, 10]
bits = len(dac)
levels = 2 ** bits
max_voltage = 3.3

def decimal_to_binary(number):
    return [int(i) for i in bin(number)[2:].zfill(len(dac))]

def bin_to_dac(value):
    signal = decimal_to_binary(value)
    GPIO.output(dac, signal)
    return signal

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT, initial = GPIO.LOW)

try:
    while True:
        input_string = input('Enter a value betweeen 0 and 255 (type q to exit) >> ')

        if input_string.isdigit() == True:
            value = int(input_string)

            if value >= levels:
                print('The value is out of range :((')
                continue
                
            signal = bin_to_dac(value)
            voltage = value / levels * max_voltage
            print('Entered value = {:^3} -> {}, output voltage = {:.2f}'.format(value, signal, voltage))

        elif input_string == 'q':
            break
        else:
            print('Unappropriate input')
        
except KeyboardInterrupt:
    print('The program was stopped by the keyboatd')
else:
    print('No exceptions')
finally:
    GPIO.output(dac, GPIO.LOW)
    GPIO.cleanup(dac)
    print('Cleanup completed')