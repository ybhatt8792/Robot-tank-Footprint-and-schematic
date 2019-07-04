
import RPi.GPIO as gpio
import time
##import picamera
import sys
import termios
import tty
from time import sleep #new

temp1=1

gpio.setmode(gpio.BOARD) #Enable the all gpio pins
#gpio.setmode(gpio.BCM) #new
gpio.setwarnings(False) # Clear gpio pins
gpio.setup(12,gpio.OUT)	 # setup particular pin for PWM
gpio.setup(10,gpio.OUT)	# setup particular pin for PWM

p=gpio.PWM(10,50)	# set the duty cycle to 50% (Pan)
p.start(100)            # intially set the servo angle at the middle by 90 degree

q=gpio.PWM(12,50)	# set the duty cycle to 50% (tilt)	
q.start(100)            # intially set the servo angle at the middle by 90 degree

gpio.setup(11,gpio.OUT)    #EN1
gpio.setup(22,gpio.OUT)    #EN2
gpio.setup(13,gpio.OUT)    #IN1
gpio.setup(15,gpio.OUT)    #IN2
gpio.setup(16,gpio.OUT)    #IN3
gpio.setup(18,gpio.OUT)    #IN4  


p1=gpio.PWM(11,50)
p1.start(100)

p2=gpio.PWM(22,50)
p2.start(100)

def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

# FUNCTION      :	gpioInit
# DESCRIPTION   :	The initialize gpio pins
# PARAMETERS    :	void
# RETURNS       :	Nothing		
	
def gpioInit():
    gpio.setmode(gpio.BOARD)
    ##camera = picamera.PiCamera()
    gpio.setup(11,gpio.OUT)    #EN1
    gpio.setup(22,gpio.OUT)    #EN2
    gpio.setup(13,gpio.OUT)    #IN1
    gpio.setup(15,gpio.OUT)    #IN2
    gpio.setup(16,gpio.OUT)    #IN3
    gpio.setup(18,gpio.OUT)    #IN4  


# FUNCTION      :	pwmUpperStart
# DESCRIPTION   :	controlling the forward speed of the servo motors
# PARAMETERS    :	duty cycle
# RETURNS       :	change in duty cycle		
	
def pwmUpperStart(dutyCycle):
    pwmInit()
    duty=dutyCycle
    q.ChangeDutyCycle(duty)

# FUNCTION      :	pwmLowerStart
# DESCRIPTION   :	controlling the backward speed of the servo motors
# PARAMETERS    :	duty cycle
# RETURNS       :	change in duty cycle		
	
def pwmLowerStart(dutyCycle):
    pwmInit()
    duty=dutyCycle
    p.ChangeDutyCycle(duty)

# FUNCTION      :	pwmInit
# DESCRIPTION   :	Enables the pulse width modulation pulse
# PARAMETERS    :	void
# RETURNS       :	Nothing		
	
def pwmInit():
    gpio.setmode(gpio.BOARD)
    gpio.setup(12,gpio.OUT)
    gpio.setup(10,gpio.OUT)

# FUNCTION      :	reset
# DESCRIPTION   :	All peripherals going back to default condition
# PARAMETERS    :	void
# RETURNS       :	Nothing		
	
def reset():
    time.sleep(.01)

# FUNCTION      :	stop
# DESCRIPTION   :	To stop servo motors from rotation
# PARAMETERS    :	Integer type value that raise the the signal to low for stop rotating servo motor
# RETURNS       :	Nothing		
	
def stop():
    gpioInit()
    gpio.output(11,0)   #EN1
    gpio.output(22,0)   #EN2
    gpio.output(13,0)   #IN1
    gpio.output(15,0)   #IN2
    gpio.output(16,0)   #IN3
    gpio.output(18,0)   #IN4
 
    print("stop")

# FUNCTION      :	forward
# DESCRIPTION   :	The forward servo motors start rotating
# PARAMETERS    :	Integer type value that raise the the signal to hight for rotating servo motor
# RETURNS       :	Nothing		
	
def forward():
    gpioInit()
    gpio.output(13,1)
    gpio.output(15,0)
    gpio.output(16,1)
    gpio.output(18,0)
    print("forward")
    time.sleep(1.0)
    stop()
	
# FUNCTION      :	backward
# DESCRIPTION   :	The backward servo motors start rotating
# PARAMETERS    :	Integer type value that raise the the signal to hight for rotating servo motor
# RETURNS       :	Nothing		

def backward():
    gpioInit()
    gpio.output(13,0)
    gpio.output(15,1)
    gpio.output(16,0)
    gpio.output(18,1)
    print("backward")
    time.sleep(1.0)
    stop()

# FUNCTION      :	right
# DESCRIPTION   :	The right side of servo motors start rotating
# PARAMETERS    :	Integer type value that raise the the signal to hight for rotating servo motor
# RETURNS       :	Nothing		
	
def right():
    gpioInit()
    gpio.output(13,1)
    gpio.output(15,0)
    gpio.output(16,0)
    gpio.output(18,1)
    print("right")
    time.sleep(0.1)
    stop()

# FUNCTION      :	left
# DESCRIPTION   :	The left side of servo motors start rotating
# PARAMETERS    :	Integer type value that raise the the signal to hight for rotating servo motor
# RETURNS       :	Nothing	
	
def left():
    gpioInit()
    gpio.output(13,0)
    gpio.output(15,1)
    gpio.output(16,1)
    gpio.output(18,0)
    print("left")
    time.sleep(0.1)
    stop()

	
# FUNCTION      :	lowerServoMiddle
# DESCRIPTION   :	The lower middle servo motor work begins
# PARAMETERS    :	Integer type value that provide  servo for some moment to particular angle
# RETURNS       :	Nothing

def lowerServoMiddle():
    pwmLowerStart(7.5)
    print("lowerServoMiddle")

# FUNCTION      :	lowerServoLeft
# DESCRIPTION   :	The lower left servo motor work begins
# PARAMETERS    :	Integer type value that provide servo some moment to particular angle
# RETURNS       :	Nothing	
	
def lowerServoLeft():
    pwmLowerStart(12.5)
    print("lowerServoLeft")

# FUNCTION      :	lowerServoRight
# DESCRIPTION   :	The lower right servo motor work begins
# PARAMETERS    :	Integer type value that provide servo some moment to particular angle
# RETURNS       :	Nothing	
	
def lowerServoRight():
    pwmLowerStart(2.5)
    print("lowerServoRight")

# FUNCTION      :	upperServoMiddle
# DESCRIPTION   :	The upper middle servo motor work begins
# PARAMETERS    :	Integer type value that provide servo some moment to particular angle
# RETURNS       :	Nothing	
	
def upperServoMiddle():
    pwmUpperStart(7.5)
    print("upperServoMiddle")

# FUNCTION      :	upperServoLeft
# DESCRIPTION   :	The upper left servo motor work begins
# PARAMETERS    :	Integer type value that provide servo some moment to particular angle
# RETURNS       :	Nothing	
	
def upperServoLeft():
    pwmUpperStart(12.5)
    print("upperServoLeft")

# FUNCTION      :	upperServoRight
# DESCRIPTION   :	The upper right servo motor work begins
# PARAMETERS    :	Integer type value that provide servo some moment to particular angle
# RETURNS       :	Nothing	
	
def upperServoRight():
    pwmUpperStart(2.5)
    print("upperServoRight")

bol=True;      #if condition is true proceed
try:		   # To handle the exceptions
##    stop()
    while bol:
        direct=getch()		#getting the commands from the ASCI keyboard

        if direct=='w':		#getting the forward commands from the ASCI keyboard word 'w'
            forward()
        elif direct=='s':	#getting the backward commands from the ASCI keyboard word 's'
            backward()
        elif direct=='a':	#getting the left commands from the ASCI keyboard word 'a'
            left()
        elif direct=='d':	#getting the right commands from the ASCI keyboard word 'd'
            right()
        elif direct=='i':	#getting the upper left commands from the ASCI keyboard word 'i' for the servo motor 
            upperServoLeft()
        elif direct=='o':	#getting the upper middle commands from the ASCI keyboard word 'o' for the servo motor
            upperServoMiddle()
        elif direct=='p':	#getting the upper right commands from the ASCI keyboard word 'p' for the servo motor
            upperServoRight()
        elif direct=='j':	#getting the lower left commands from the ASCI keyboard word 'j' for the servo motor
            lowerServoLeft()
        elif direct=='k':	#getting the lower middle commands from the ASCI keyboard word 'k' for the servo motor
            lowerServoMiddle()
        elif direct=='l':	#getting the lower right commands from the ASCI keyboard word 'l' for the servo motor
            lowerServoRight()
        elif direct=='c':	#getting the capture mode commands from the ASCI keyboard word 'c' 
          camera.capture('group1.jpg')
        elif direct=='b':	#getting the reset commands from the ASCI keyboard word 'b' 
            gpio.cleanup()
            bol=False
        elif direct=='v':	#getting the camera preview commands from the ASCI keyboard word 'v' 
            camera.start_preview()	#start the preview of the camera
            sleep(15)
            camera.stop_preview()	#stop the preview of the camera
except KeyboardInterrupt:			#if any other ASCI character press it interrupts the command
    gpio.cleanup()
