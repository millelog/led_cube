import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM);

GPIO.setup(22, GPIO.OUT);
GPIO.setup(23, GPIO.OUT);
GPIO.setup(24, GPIO.OUT);
GPIO.setup(25, GPIO.OUT);
GPIO.setup(26, GPIO.OUT);
GPIO.setup(27, GPIO.OUT);

def led_on_only(num):
    num = num+22; #because the start of the gpio [pins is at 22]
    print("Turning on "+num)
    for i in range(22, 25):
        GPIO.output(i, GPIO.LOW)
    GPIO.output(num, GPIO.HIGH)

def toggle_level(level):
    print("Level: " level);
    if(level==0)
        GPIO.output(27, GPIO.LOW)
        GPIO.output(26, GPIO.HIGH)
        level==1:
    else:
        GPIO.output(26, GPIO.LOW)
        GPIO.output(27, GPIO.HIGH);
        level==0;
    return level;

level = 0;
led = 0;
while True:
    led_on_only(led);
    led++
    if(led>=3):
        led=0;
        level++;
    if(level>=1):
        level=0;
    time.sleep(1);
