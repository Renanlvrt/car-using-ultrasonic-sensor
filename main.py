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