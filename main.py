import random
import time

def measure_blood_pressure():
    # Simulate systolic (normal range: 90 to 120)
    systolic = random.randint(90, 120)
    
    # Simulate diastolic (normal range: 60 to 80)
    diastolic = random.randint(60, 80)
    
    return systolic, diastolic

def display_blood_pressure(systolic, diastolic):
    print(f"Blood Pressure: {systolic}/{diastolic} mmHg")

if __name__ == "__main__":
    print("Blood Pressure Monitor Simulation")
    while True:
        systolic, diastolic = measure_blood_pressure()
        display_blood_pressure(systolic, diastolic)
        time.sleep(5)  # wait 5 seconds before taking the next reading