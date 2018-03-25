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
GPIO.setwarnings(False)

# -- GPIO PIN SETUP --
button = 1
GPIO.setup(button, GPIO.IN)

#yellowled = 14
#GPIO.setup(yellowled, GPIO.OUT)

# -- -- -- -- -- --
# Listen for button click

try:
    while True:
        input_value = GPIO.input(button)
        if input_value == True:
            print('The button has been pressed...')
            # emailOnButton()
            while input_value == False:
                input_value = GPIO.input(button)
finally:
    print("cleaning")
    # cleanup on normal exit
    GPIO.cleanup()
    print("cleaned")

# emailOnButton(): null -> null
# Expects nothing, returns nothing, has the side effects of
# sending an email to nathan@humboldt.edu

def emailOnButton():
    # email to myself
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('andthenraspi@gmail.com','ghostinthemachine')
    msg = "Send help to printer station!"
    server.sendmail('andthenraspi@gmail.com','bravelemming@gmail.com','Printer Help Request')
    server.quit()

    # light up LED
    # GPIO.output(yellowled, 1)
    # time.sleep(5)
    # GPIO.output(yellowled, 0)
