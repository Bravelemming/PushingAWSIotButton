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
# To email complex messages (including subject line)
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

# Board = BCM
GPIO.setmode(GPIO.BCM)
# No warnings, thanks!
GPIO.setwarnings(False)

# -- GPIO PIN SETUP --
button = 18 #GPIO 18 (PIN #12)
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def emailOnButton(toaddr, printer_id, location, subject):
    '''emailOnButton(): null -> null
    Expects nothing, returns nothing, has the side effects of
    sending an email to mlemos@humboldt.edu'''
    
    fromaddr = 'andthenraspi@gmail.com'
	
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = subject
    #msg['Subject'] = "Printer Help Request"
	
    body = "Send help to printer station " + printer_id + ' located: ' + location + ' has requested help!'
    msg.attach(MIMEText(body, 'plain'))
	
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr,'ghostinthemachine')
    text = msg.as_string()
	
    server.sendmail(fromaddr, toaddr,text)
    server.quit()

# -- -- -- -- -- --
# Listen for button click and call emailOnButton()
try:
    while True:
        input_value = GPIO.input(button)
        if input_value == False:
            print('The button has been pressed...')
            #emailOnButton('mlemos@humboldt.edu')
            emailOnButton('mlemos@humboldt.edu', '54b7894', 'Library floor 2', "We have pushed Dave's button.")
            emailOnButton('adam.carter@humboldt.edu', '54b7894', 'Library floor 2', "We have pushed Dave's button.")
            emailOnButton('kpa2@humboldt.edu', '54b7894', 'Library floor 2', "We have pushed Dave's button.")
            emailOnButton('dave@humboldt.edu', '54b7894', 'Library floor 2', "We have pushed Dave's button.")

            time.sleep(0.2)
finally:
    print("cleaning")
    # cleanup on normal exit
    GPIO.cleanup()
    print("cleaned")
