import RPi.GPIO as GPIO
import time

# Установка режима нумерации GPIO пинов
GPIO.setmode(GPIO.BCM)

# Определение пинов, к которым подключены двигатели
motor1_pin1 = 17
motor1_pin2 = 18
motor2_pin1 = 22
motor2_pin2 = 23

# Установка пинов как выходы
GPIO.setup(motor1_pin1, GPIO.OUT)
GPIO.setup(motor1_pin2, GPIO.OUT)
GPIO.setup(motor2_pin1, GPIO.OUT)
GPIO.setup(motor2_pin2, GPIO.OUT)

# Функция для движения вперёд
def forward():
    GPIO.output(motor1_pin1, GPIO.HIGH)
    GPIO.output(motor1_pin2, GPIO.LOW)
    GPIO.output(motor2_pin1, GPIO.HIGH)
    GPIO.output(motor2_pin2, GPIO.LOW)

# Функция для движения назад
def backward():
    GPIO.output(motor1_pin1, GPIO.LOW)
    GPIO.output(motor1_pin2, GPIO.HIGH)
    GPIO.output(motor2_pin1, GPIO.LOW)
    GPIO.output(motor2_pin2, GPIO.HIGH)

# Функция для остановки двигателей
def stop():
    GPIO.output(motor1_pin1, GPIO.LOW)
    GPIO.output(motor1_pin2, GPIO.LOW)
    GPIO.output(motor2_pin1, GPIO.LOW)
    GPIO.output(motor2_pin2, GPIO.LOW)

# Пример использования функций
try:
    while True:
        forward()
        time.sleep(2)  # Движение вперёд на 2 секунды
        stop()
        time.sleep(1)  # Пауза 1 секунда
        backward()
        time.sleep(2)  # Движение назад на 2 секунды
        stop()
        time.sleep(1)  # Пауза 1 секунда

except KeyboardInterrupt:
    GPIO.cleanup()  # Выполнить очистку GPIO при прерывании программы Ctrl+C
