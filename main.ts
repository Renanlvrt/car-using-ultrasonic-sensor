function obstacle_detected() {
    // motobit.invert(Motor.LEFT, False)
    // motobit.invert(Motor.RIGHT, False)
    motobit.setMotorSpeed(Motor.Left, MotorDirection.Reverse, 60)
    motobit.setMotorSpeed(Motor.Left, MotorDirection.Reverse, 60)
    pause(2000)
    pins.servoWritePin(AnalogPin.P15, 37)
    pause(2000)
    pins.servoWritePin(AnalogPin.P15, 160)
    motobit.setMotorSpeed(Motor.Left, MotorDirection.Reverse, 60)
    motobit.setMotorSpeed(Motor.Left, MotorDirection.Reverse, 60)
}

// TURN LEFT: pins.servo_write_pin(AnalogPin.P15, 37)
// TURN RIGHT: pins.servo_write_pin(AnalogPin.P15, 160)
// neutral: pins.servo_write_pin(AnalogPin.P15, 90)
function enable_distance(distance: number) {
    // led.enable(True)
    // led.plot(0, 0)
    if (distance <= 3000) {
        led.plot(0, 1)
        if (distance <= 2500) {
            // here do things
            led.plot(1, 1)
            led.plot(2, 1)
            led.plot(3, 1)
            if (distance <= 1500) {
                led.plot(1, 2)
                led.plot(2, 2)
                led.plot(3, 2)
                if (distance <= 1000) {
                    led.plot(1, 3)
                    led.plot(2, 3)
                    led.plot(3, 3)
                    if (distance <= 500) {
                        led.plot(1, 4)
                        led.plot(2, 4)
                        led.plot(3, 4)
                    } else {
                        led.unplot(1, 4)
                        led.unplot(2, 4)
                        led.unplot(3, 4)
                    }
                    
                } else {
                    led.unplot(1, 3)
                    led.unplot(2, 3)
                    led.unplot(3, 3)
                }
                
            } else {
                led.unplot(1, 2)
                led.unplot(2, 2)
                led.unplot(3, 2)
            }
            
            obstacle_detected()
        } else {
            led.unplot(1, 1)
            led.unplot(2, 1)
            led.unplot(3, 1)
            motobit.setMotorSpeed(Motor.Left, MotorDirection.Forward, 100)
            motobit.setMotorSpeed(Motor.Left, MotorDirection.Forward, 100)
        }
        
    }
    
}

basic.forever(function on_forever() {
    let distance = sonar.ping(DigitalPin.P12, DigitalPin.P14, PingUnit.MicroSeconds)
    if (distance <= 4000) {
        enable_distance(distance)
    } else {
        // motobit.set_motor_speed(Motor.LEFT, MotorDirection.FORWARD, 50)
        basic.clearScreen()
    }
    
    // serial.writeNumber(sonar.ping(DigitalPin.P12, DigitalPin.P14, PingUnit.MICRO_SECONDS));
    
})
input.onButtonPressed(Button.A, function button_a_pressed() {
    motobit.setMotorSpeed(Motor.Left, MotorDirection.Forward, 100)
    motobit.setMotorSpeed(Motor.Left, MotorDirection.Forward, 100)
    
})
input.onButtonPressed(Button.B, function button_b_pressed() {
    pins.servoWritePin(AnalogPin.P15, 90)
    motobit.enable(MotorPower.Off)
    
})
