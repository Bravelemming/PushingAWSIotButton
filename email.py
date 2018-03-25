# Generate Email from Raspberry Pi GPIO button press
#

# Standard time library
import time
# GPIO Control
import RPi.GPIO as GPIO
# Email
import smtplib

# Board = BCM
GPIO.setmode(GPIO.BCM)
# No warnings, thanks!
GPIO.setwarnings(False)

# -- GPIO PIN SETUP --

yellowled = 14
GPIO.setup(yellowled, GPIO.OUT)

# -- ---  -- -- -- --


def emailOnButton():
    # email to myself
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('andthenraspi@gmail.com','ghostinthemachine')
    msg = "Send help to printer station!"
    server.sendmail('andthenraspi@gmail.com','bravelemming@gmail.com','Printer Help Request')
    server.quit()

    # light up LED
    GPIO.output(yellowled, 1)
    time.sleep(5)
    GPIO.output(yellowled, 0)

# cleanup on normal exit
    GPIO.cleanup()
