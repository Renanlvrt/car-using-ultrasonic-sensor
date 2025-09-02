"""

def obstacle_detected():

motobit.set_motor_speed(Motor.LEFT, MotorDirection.REVERSE, 60)

motobit.set_motor_speed(Motor.RIGHT, MotorDirection.REVERSE, 60)

pause(2000)

pins.servo_write_pin(AnalogPin.P15, 37)

pause(2000)

pins.servo_write_pin(AnalogPin.P15, 160)

motobit.set_motor_speed(Motor.LEFT, MotorDirection.REVERSE, 60)

motobit.set_motor_speed(Motor.RIGHT, MotorDirection.REVERSE, 60)

#TURN LEFT: pins.servo_write_pin(AnalogPin.P15, 37)

#TURN RIGHT: pins.servo_write_pin(AnalogPin.P15, 160)

#neutral: pins.servo_write_pin(AnalogPin.P15, 90)

motobit.invert(Motor.LEFT, True)

motobit.invert(Motor.RIGHT, True)

def enable_distance(distance):

motobit.enable(MotorPower.ON)

#led.enable(True)

#led.plot(0, 0)

if distance <= 3000:

led.plot(0, 1)

if distance <= 2500:

#here do things

led.plot(1, 1)

led.plot(2, 1)

led.plot(3, 1)

if distance <= 1500:

led.plot(1, 2)

led.plot(2, 2)

led.plot(3, 2)

if distance <= 1000:

led.plot(1, 3)

led.plot(2, 3)

led.plot(3, 3)

if distance <= 500:

led.plot(1, 4)

led.plot(2, 4)

led.plot(3, 4)

else:

led.unplot(1, 4)

led.unplot(2, 4)

led.unplot(3, 4)

else:

led.unplot(1, 3)

led.unplot(2, 3)

led.unplot(3, 3)

else:

led.unplot(1, 2)

led.unplot(2, 2)

led.unplot(3, 2)

obstacle_detected()

else:

led.unplot(1, 1)

led.unplot(2, 1)

led.unplot(3, 1)

motobit.set_motor_speed(Motor.LEFT, MotorDirection.FORWARD, 100)

motobit.set_motor_speed(Motor.RIGHT, MotorDirection.FORWARD, 100)

def on_forever():

distance = sonar.ping(DigitalPin.P12, DigitalPin.P14, PingUnit.MICRO_SECONDS)

if distance <= 1000:

enable_distance(distance)

else:

pins.servo_write_pin(AnalogPin.P15, 90)

motobit.set_motor_speed(Motor.LEFT, MotorDirection.FORWARD, 100)

motobit.set_motor_speed(Motor.LEFT, MotorDirection.FORWARD, 100)

#motobit.set_motor_speed(Motor.LEFT, MotorDirection.FORWARD, 50)

basic.clear_screen()

#serial.writeNumber(sonar.ping(DigitalPin.P12, DigitalPin.P14, PingUnit.MICRO_SECONDS));

pass

basic.forever(on_forever)

def button_a_pressed():

motobit.enable(MotorPower.ON)

motobit.set_motor_speed(Motor.LEFT, MotorDirection.FORWARD, 100)

motobit.set_motor_speed(Motor.RIGHT, MotorDirection.FORWARD, 100)

pass

input.on_button_pressed(Button.A, button_a_pressed)

def button_b_pressed():

pins.servo_write_pin(AnalogPin.P15, 90)

motobit.enable(MotorPower.OFF)

pass

input.on_button_pressed(Button.B, button_b_pressed)

#motobit.set_motor_speed(Motor.LEFT, MotorDirection.FORWARD, 100)

#motobit.set_motor_speed(Motor.LEFT, MotorDirection.FORWARD, 100)

"""

""""def on_button_pressed_a():
    global on
    motobit.enable(MotorPower.ON)
    motobit.set_motor_speed(Motor.LEFT, MotorDirection.FORWARD, 100)
    motobit.set_motor_speed(Motor.RIGHT, MotorDirection.FORWARD, 100)
    on = True
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    pins.servo_write_pin(AnalogPin.P15, 90)
    pause(1000)
    motobit.enable(MotorPower.OFF)
    led.unplot(0, 0)
input.on_button_pressed(Button.B, on_button_pressed_b)

on = False
manouvering = False
# TURN LEFT: pins.servo_write_pin(AnalogPin.P15, 37)
# TURN RIGHT: pins.servo_write_pin(AnalogPin.P15, 160)
# neutral: pins.servo_write_pin(AnalogPin.P15, 90)
motobit.invert(Motor.LEFT, True)
motobit.invert(Motor.RIGHT, True)
motobit.enable(MotorPower.OFF)
distance = sonar.ping(DigitalPin.P12, DigitalPin.P14, PingUnit.MICRO_SECONDS)
serial.write_value("distance", distance)
# serial.writeNumber(sonar.ping(DigitalPin.P12, DigitalPin.P14, PingUnit.MICRO_SECONDS));

def on_forever():
    global distance
    global manouvering
    distance = sonar.ping(DigitalPin.P12, DigitalPin.P14, PingUnit.MICRO_SECONDS)
    led.plot(0, 0)
    # serial.write_number(distance)
    serial.write_value("distance", distance)
    serial.write_line("" + str((on)))
    serial.write_line("" + str((manouvering)))
    if on:
        if not (manouvering):
            while distance < 2500:
                manouvering = True
                motobit.enable(MotorPower.ON)
                led.plot(2, 2)
                if distance < 1500:
                    led.plot(2, 1)
                    led.plot(2, 2)
                    led.plot(2, 3)
                    led.plot(1, 2)
                    led.plot(3, 2)
                    pins.servo_write_pin(AnalogPin.P15, 160)
                    pause(1000)
                    motobit.set_motor_speed(Motor.LEFT, MotorDirection.REVERSE, 100)
                    motobit.set_motor_speed(Motor.RIGHT, MotorDirection.REVERSE, 100)
                    pause(4000)
                    # pins.servo_write_pin(AnalogPin.P15, 37)
                    # motobit.set_motor_speed(Motor.LEFT, MotorDirection.FORWARD, 60)
                    # motobit.set_motor_speed(Motor.RIGHT, MotorDirection.FORWARD, 60)
                    # pause(1000)
                    led.unplot(2, 2)
                    led.unplot(2, 1)
                    led.unplot(2, 3)
                    led.unplot(1, 2)
                    led.unplot(3, 2)
                else:
                    pins.servo_write_pin(AnalogPin.P15, 37)
                    pause(1000)
                    motobit.set_motor_speed(Motor.LEFT, MotorDirection.FORWARD, 60)
                    motobit.set_motor_speed(Motor.RIGHT, MotorDirection.FORWARD, 60)
                    led.unplot(2, 2)
            ##manouvering2 = False
            pins.servo_write_pin(AnalogPin.P15, 90)
            motobit.set_motor_speed(Motor.LEFT, MotorDirection.FORWARD, 100)
            motobit.set_motor_speed(Motor.RIGHT, MotorDirection.FORWARD, 100)
            # motobit.set_motor_speed(Motor.LEFT, MotorDirection.FORWARD, 50)
            basic.clear_screen()
basic.forever(on_forever)"""


#################################################################
#################################################################

def on_button_pressed_a():
    global on
    motobit.enable(MotorPower.ON)
    motobit.set_motor_speed(Motor.LEFT, MotorDirection.FORWARD, 100)
    motobit.set_motor_speed(Motor.RIGHT, MotorDirection.FORWARD, 100)
    on = True

input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global on
    pins.servo_write_pin(AnalogPin.P15, 90)
    pause(100)
    motobit.enable(MotorPower.OFF)
    led.unplot(0, 0)
    on = False

input.on_button_pressed(Button.B, on_button_pressed_b)

on = False
manouvering = False
# TURN LEFT: pins.servo_write_pin(AnalogPin.P15, 37)
# TURN RIGHT: pins.servo_write_pin(AnalogPin.P15, 160)
# neutral: pins.servo_write_pin(AnalogPin.P15, 90)
motobit.invert(Motor.LEFT, True)
motobit.invert(Motor.RIGHT, True)
motobit.enable(MotorPower.OFF)
distance = sonar.ping(DigitalPin.P12, DigitalPin.P14, PingUnit.MICRO_SECONDS)
serial.write_value("distance", distance)
# serial.writeNumber(sonar.ping(DigitalPin.P12, DigitalPin.P14, PingUnit.MICRO_SECONDS));

def on_forever():
    motobit.invert(Motor.LEFT, True)
    motobit.invert(Motor.RIGHT, True)
    global distance
    global manouvering
    global on
    on = True
    distance = sonar.ping(DigitalPin.P12, DigitalPin.P14, PingUnit.MICRO_SECONDS)
    led.plot(0, 0)
    # serial.write_number(distance)
    serial.write_value("distance", distance)
    serial.write_line("" + str((on)))
    serial.write_line("" + str((manouvering)))
    if on:
        if not (manouvering):
            while distance < 3500:
                basic.clear_screen()
                serial.write_value("in the cycle", distance)
                led.unplot(0, 0)
                #not to forget to update distance in the while
                distance = sonar.ping(DigitalPin.P12, DigitalPin.P14, PingUnit.MICRO_SECONDS)
                manouvering = True
                motobit.enable(MotorPower.ON)
                led.plot(2, 2)
                if distance < 1500:
                    #led.plot(4,4)
                    led.plot(2, 1)
                    led.plot(2, 3)
                    led.plot(1, 2)
                    led.plot(3, 2)
                    #again same problem
                    motobit.enable(MotorPower.OFF)
                    pins.servo_write_pin(AnalogPin.P15, 160)
                    pause(300)
                    motobit.enable(MotorPower.ON)
                    motobit.set_motor_speed(Motor.LEFT, MotorDirection.REVERSE, 100)
                    motobit.set_motor_speed(Motor.RIGHT, MotorDirection.REVERSE, 100)
                    pause(1000)
                    # pins.servo_write_pin(AnalogPin.P15, 37)
                    # motobit.set_motor_speed(Motor.LEFT, MotorDirection.FORWARD, 60)
                    # motobit.set_motor_speed(Motor.RIGHT, MotorDirection.FORWARD, 60)
                    # pause(1000)
                    led.unplot(2, 2)
                    led.unplot(2, 1)
                    led.unplot(2, 3)
                    led.unplot(1, 2)
                    led.unplot(3, 2)
                    #led.unplot(4,4)
                    #manouvering = False
                else:
                    led.plot(2, 2)
                    #to avoid turning while going forward
                    #motobit.enable(MotorPower.OFF)
                    pins.servo_write_pin(AnalogPin.P15, 30)
                    #pause(300)
                    #motobit.enable(MotorPower.ON)
                    motobit.set_motor_speed(Motor.LEFT, MotorDirection.FORWARD, 70)
                    motobit.set_motor_speed(Motor.RIGHT, MotorDirection.FORWARD, 70)
                    pause(700)
                    led.unplot(2, 2)
            ##manouvering2 = False
            motobit.enable(MotorPower.OFF)
            pins.servo_write_pin(AnalogPin.P15, 90)
            motobit.enable(MotorPower.ON)
            motobit.set_motor_speed(Motor.LEFT, MotorDirection.FORWARD, 100)
            motobit.set_motor_speed(Motor.RIGHT, MotorDirection.FORWARD, 100)
            # motobit.set_motor_speed(Motor.LEFT, MotorDirection.FORWARD, 50)
            basic.clear_screen()
            #not to forget to update manouvering
            manouvering = False
basic.forever(on_forever)







