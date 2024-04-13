# Отчет

В данном проекте ***RobotMotorsControl*** представлен скрипт на Python для управления двигателями робота.

### Описание скрипта

Для данного примера управления двигателями используется библиотека RPi.GPIO, которая позволяет управлять GPIO пинами на Raspberry Pi (предполагается, что используется Raspberry Pi). 

Для более плавного изменения скорости двигателей на роботе в его аппаратной реализации используется ШИМ (Широтно-Импульсную Модуляцию). В програмной реализации для этого добавлен класс MotorControl, который содержит методы для управления направлением движения, скоростью и т.д. 

### Описание работы с Git

1. Создание и клонирование репозитория

Репозиторий с названием _RobotMotorsControl_ , содержащий пустые файлы README.md и motors_control.py, был создан на GitHub и далее клонирован в на компьтер с использованием SSH командой:

``` git clone git@github.com:Nonaneforever/RobotMotorsControl.git ```

2. Процесс сохранения изменений

После того, как в файл motors_control.py был вставлен код для управления двигателями робота и описание в README.md, были выполнены команды для добавления, фиксации и отправки изменений: 

``` git add . ```

``` git commit -m "Initial commit" ```

``` git push origin master ```


3. Взаимодействие с ветками

Далее была создана ветка для внесения улучшений:

``` git checkout -b feature_branch_name ```

Проверка текущей ветки:

``` git branch ```

После внесения изменений в код (функции плавного изменения скорости) были выполнены теже операции для добавления, фиксации и отправки изменений, но уже с новой веткой. Изменения отобразились на GitHub - добавилась новая ветка feature_branch_name. 


4. Пул-реквесты

Пул-реквест был создан изначально коряво - не закрыт. Потом осмыслен и закрыт нормально. История изменений видна на GitHub.

5. Основные изменения и улучшения в коде: кратко опишите ключевые добавленные или модифицированные функции и их назначение.

Первичный код:

```
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
```


Измененный код:

```
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
```


### Заключение

Да всё норм. Что тут излагать впечатления от работы с Git. Планов тоже нет...



