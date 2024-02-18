import RPi.GPIO as GPIO


class Car:
    
    def __init__(self):
        self.motor1 = Motor(0, 0)
        self.motor2 = Motor(0, 0)
        self.motor3 = Motor(0, 0)
        self.motor4 = Motor(0, 0)
        
        
    def set_motor(self, motor_number, pin1, pin2):
        if(motor_number == 1): self.motor1.changePinNumber(pin1, pin2)
        elif(motor_number == 2): self.motor2.changePinNumber(pin1, pin2)
        elif(motor_number == 3): self.motor3.changePinNumber(pin1, pin2)
        elif(motor_number == 4): self.motor4.changePinNumber(pin1, pin2)            
        else:
            print("You didnt enter a valid motor number(1-4) shithead")
    
    def init_board(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup((self.motor1).getPin1(), GPIO.OUT)
        GPIO.setup((self.motor1).getPin2(), GPIO.OUT)

        GPIO.setup((self.motor3).getPin1(), GPIO.OUT)
        GPIO.setup((self.motor3).getPin2(), GPIO.OUT)
        
    # Actions/Directions
    def left_forward(self):
        GPIO.output((self.motor3).getPin1(), 1)
        GPIO.output((self.motor3).getPin2(), 0)
    def left_reverse(self):
        GPIO.output((self.motor3).getPin1(), 0)
        GPIO.output((self.motor3).getPin2(), 1)
        
    def right_forward(self):
        GPIO.output((self.motor1).getPin1(), 0)
        GPIO.output((self.motor1).getPin2(), 1)
    def right_reverse(self):
        GPIO.output((self.motor1).getPin1(), 1)
        GPIO.output((self.motor1).getPin2(), 0)
        
    def cleanUp(self):
        GPIO.cleanup()


class Motor:
    def __init__(self, pin1, pin2):
        self.pin1 = pin1
        self.pin2 = pin2
        
    def getPin1(self):
        return self.pin1
    def getPin2(self):
        return self.pin2
            
    def changePinNumber(self, new_pin1, new_pin2):
        self.pin1 = new_pin1
        self.pin2 = new_pin2
    