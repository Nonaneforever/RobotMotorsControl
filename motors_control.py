import RPi.GPIO as GPIO
import time

class MotorControl:
    def __init__(self, pin1, pin2):
        self.pin1 = pin1
        self.pin2 = pin2
        GPIO.setup(pin1, GPIO.OUT)
        GPIO.setup(pin2, GPIO.OUT)
        self.pwm = GPIO.PWM(pin1, 1000)  # Инициализация ШИМ на пине для управления скоростью
        self.pwm.start(0)

    def forward(self, speed):
        self.pwm.ChangeDutyCycle(speed)
        GPIO.output(self.pin2, GPIO.LOW)

    def backward(self, speed):
        self.pwm.ChangeDutyCycle(speed)
        GPIO.output(self.pin2, GPIO.HIGH)

    def stop(self):
        self.pwm.ChangeDutyCycle(0)

if __name__ == "__main__":
    try:
        GPIO.setmode(GPIO.BCM)
        motor1 = MotorControl(17, 18)
        motor2 = MotorControl(22, 23)

        while True:
            motor1.forward(50)  # Плавное движение вперёд
            motor2.forward(50)
            time.sleep(2)
            motor1.stop()
            motor2.stop()
            time.sleep(1)
            motor1.backward(50)  # Плавное движение назад
            motor2.backward(50)
            time.sleep(2)
            motor1.stop()
            motor2.stop()
            time.sleep(1)

    except KeyboardInterrupt:
        GPIO.cleanup()  # Очистка GPIO при прерывании программы Ctrl+C
