# Generate Email from Raspberry Pi GPIO button press
# HSU LumberHacks Hackathon
# Team: Pressing Dave's button
# Contributors: Jack Kinne, Sam Alston, Max Lemos, Nathan Ortolan
# Last Modified: 3/24/18

# Standard time library
import time
# GPIO Control
import RPi.GPIO as GPIO
# Email
import smtplib

# Board = BCM
GPIO.setmode(GPIO.BCM)
# No warnings, thanks!
GPIO.setwarnings(True)

# -- GPIO PIN SETUP --
button = 18 #GPIO 18 (PIN #12)
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def emailOnButton():
    '''emailOnButton(): null -> null
    Expects nothing, returns nothing, has the side effects of
    sending an email to nathan@humboldt.edu
    email to myself'''

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('andthenraspi@gmail.com','ghostinthemachine')
    msg = "Send help to printer station!"
    server.sendmail('andthenraspi@gmail.com','mlemos@humboldt.edu','Printer Help Request')
    server.quit()

    # light up LED
    # GPIO.output(yellowled, 1)
    # time.sleep(5)
    # GPIO.output(yellowled, 0)

#yellowled = 14
#GPIO.setup(yellowled, GPIO.OUT)

# -- -- -- -- -- --
# Listen for button click

try:
    while True:
        input_value = GPIO.input(button)
        if input_value == False:
            print('The button has been pressed...')
            emailOnButton()
            time.sleep(0.2)
finally:
    print("cleaning")
    # cleanup on normal exit
    GPIO.cleanup()
    print("cleaned")
