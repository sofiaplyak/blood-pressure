from microbit import *
from micropython import const
import bluetooth
from ble_uart import BLEUART

# Ініціалізація Bluetooth
ble = bluetooth.BLE()
uart = BLEUART(ble)

# Функція для введення віку
def get_age():
    display.scroll("AGE?")
    age = 0
    while True:
        display.show(age)
        if button_a.was_pressed():
            age += 1
            if age > 120:
                age = 0  # Скидання, якщо вік занадто великий
        if button_b.was_pressed():
            break  # Завершення введення
        sleep(200)
    return age

# Функція для розрахунку тиску
def calculate_bp(age, pulse):
    sat = 100 + (age / 2) + (pulse / 10)  # Систолічний тиск
    dat = sat - (pulse / 2)  # Діастолічний тиск
    return int(sat), int(dat)

# Основний цикл
display.scroll("Waiting BT...")  # Очікуємо підключення
age = get_age()  # Запит віку

while True:
    if uart.any():  # Читаємо вхідні дані через Bluetooth
        data = uart.read().decode().strip()
        if data.isdigit():  # Якщо отримано число (пульс)
            pulse = int(data)
            sat, dat = calculate_bp(age, pulse)  # Розрахунок тиску
            
            # Відображення результату на micro:bit
            display.scroll("BP:{}-{}".format(sat, dat))
            
            # Надсилаємо відповідь назад на телефон
            uart.write("BP:{}-{}".format(sat, dat))
            
            sleep(5000)  # Затримка перед наступним прийомом даних
