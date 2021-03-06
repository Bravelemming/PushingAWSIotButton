# AWS IOT Button OR Raspberry Pi Button to send email on click

## AWS IOT Button
**Follow this [guide](https://docs.aws.amazon.com/iot/latest/developerguide/iot-device-sdk-node.html)**.
---This may require setting up a new AWS account---
1. Use the AWS Lambda Function Console to create a new trigger and function
   * Input the Device Serial Number (DSN) found on the back of the IOT button
   * Download the generated certificate and private key
2. Hold the IOT Button down for 5 seconds to start configuration mode
3. Connect to the IOT Button's network on your computer (Button ConfigureMe - XXX)
4. Navigate to [198.162.0.1](198.162.0.1) to view the Button Configuration Page
5. Input the Button information generated by trigger creation and Network information
6. Submit the form and watch the light on the IOT Button. It should flash blue repeatedly and then flash solid green
7. Re-connect to the original WiFi Network that was used in the IOT Button Configuration
8. *(Optional)* Use the AWS Lambda Function Console to create a test (Hello World is a good test template for this use case)
   * Run the test
   * Check for a subscription confirmation email from AWS
   * Confirm the subscription
   * Re-run the test
   * Check for the generated email
9. Click the IOT Button and watch the light. It should flash blue repeatedly and then flash solid green
10. Check for the generated email!

## Raspberry Pi Button
Using:
   * Pi 2 Model B Rev 1.1 running Raspbian
   * Breadboard
   * 2 GPIO Jumper Wires (Power and Ground)
   * 1 GPIO Breadboard 4-Pin Button
   * Python 2.7
   * Libraries:
      * time - Python time
      * RPi.GPIO - GPIO Control
      * smtplib - Python email
      * MIMEMultipart - More complete emails (subject line)
      * MIMEText - More complete emails (subject line)

### Hardware Setup
1. Attach the Jumper Wires from GPIO Pins to Breadboard
  * Power - GPIO \#18 (PIN \#12) -> Breadboard \#1B
  * Ground - GPIO \#39 (PIN GND) -> Breadboard \#2B
  * *Use this [guide](http://www.raspberry-projects.com/pi/pi-hardware/raspberry-pi-2-model-b/rpi2-model-b-io-pins) for GPIO Pins*
2. Attach the 4-Pin Button to Breadboard Pins \#1C, \#1F, \#3C, \#3F
3. Power on the Raspberry Pi

### Software Setup
1. Use VNC/SSH to connect to the Raspberry Pi
2. Clone the [repository](https://github.com/Bravelemming/PushingAWSIotButton) into the Raspberry Pi
3. Create a Gmail account and set it up for SMTP
5. Replace the *to* and *from* email addresses in *email_button.py*
3. Run the script *email_button.py* with Python 2.7 as super user
   * `sudo python email_button.py`
   * DO NOT rename the file to *email.py* as this name is reserved by the SMTP Library.
4. Click the button! You shoud see a terminal message saying that the button has been pressed and receive an email!
