
from rc_car_gpio_side_functions import Car

from evdev import InputDevice, categorize, ecodes



# Reading the button selections on the controller
gamepad = InputDevice("/dev/input/event5")

pad_left = 18
pad_right = 33
pad_up = 46
pad_down = 32


# Creating the *Car* object which will house all info
# related to the car
car = Car()

# Creating the motors inside the Car class, and tying the
# pins to their respective motor
# First pin is positive, second is negative
car.set_motor(1, 29, 31)
car.set_motor(2, 29, 31)
car.set_motor(3, 18, 16)
car.set_motor(4, 18, 16)

# Initialize the GPIO pins that the motors are connected to
car.init_board()

# Actual Control Code
try:
    while True:
        for event in gamepad.read_loop():
            if event.type == ecodes.EV_KEY:
                 if event.value == 1:
                         
                     elif event.code == pad_up:
                         car.left_forward()
                         car.right_forward()
                     elif event.code == pad_down:
                         car.left_reverse()
                         car.right_reverse()
                     elif event.code == pad_left:
                         car.left_reverse()
                         car.right_forward()
                     elif event.code == pad_right:
                         car.left_forward()
                         car.right_reverse()


except KeyboardInterrupt:
    print("you ended the program early :(")
    
except:
    print("Another error occurred")
    
finally:
    car.cleanUp()        
    
        

