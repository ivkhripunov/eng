import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(22, GPIO.OUT)

p = GPIO.PWM(22, 1000)  
p.start(0)
try:
    while True:
        dc = input('Type the voltage percentage (type q to exit)>> ')
        
        if dc == 'q':
            break
        
        if not dc.isdigit():
            print('Type error. Try again')
            continue
        
        elif int(dc) > 100 or int(dc) < 0:
            print('Value is out of range :((')
            continue
        
        else:
            p.ChangeDutyCycle(int(dc))
            continue    
        

except KeyboardInterrupt:
    print('Program was interrupted by the keyboard')

finally:
    GPIO.cleanup()

p.stop()
GPIO.cleanup()
