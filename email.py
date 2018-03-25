# SQL ENQUIRY + GPIO LED DISPLAY.  Jack Daniel Kinne.
# THis SQL Enquiry searches for any mention of "cats" 
# across multiple sub reddits with at least 15 likes.
# It outputs title and subreddit as an automated email 
# and updates the SQL DB entry emailed = "yes"

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