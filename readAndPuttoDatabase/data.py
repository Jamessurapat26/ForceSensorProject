import serial
import time
import requests

url = 'http://localhost:3000/sensor_data'

    # Set up the serial connection
ser = serial.Serial('COM3', 9600, timeout=1)
time.sleep(3)  # Give some time for the serial connection to initialize

    # Read data from serial port
while True:
    if ser.in_waiting > 0:
        line = ser.readline().decode('utf-8').rstrip()
        print(line)
        numbers = line.split()

        numbers = [int(num) for num in numbers]

        print(numbers)

        sensor_data = {
            "L1": numbers[0],
            "L2": numbers[1],
            "L3": numbers[2],
            "L4": numbers[3],
            "L5": numbers[4],
            "L6": numbers[5],
            "L7": numbers[6],
            "L8": numbers[7],
            "L9": numbers[8],
            "L10": numbers[9],
            "L11": numbers[10],
            "L12": numbers[11],
            "L13": numbers[12],
            "L14": numbers[13],
            "L15": numbers[14],
            "L16": numbers[15],
            "R1": numbers[16],
            "R2": numbers[17],
            "R3": numbers[18],
            "R4": numbers[19],
            "R5": numbers[20],
            "R6": numbers[21],
            "R7": numbers[22],
            "R8": numbers[23],
            "R9": numbers[24],
            "R10": numbers[25],
            "R11": numbers[26],
            "R12": numbers[27],
            "R13": numbers[28],
            "R14": numbers[29],
            "R15": numbers[30],
            "R16": numbers[31]
        }

        # Send POST request with JSON data
        response = requests.post(url, json=sensor_data)

        # Check response status
        if response.status_code == 200:
            print('Data posted successfully.')
            print('Response JSON:', response.json())
        else:
            print('Failed to post data. Status code:', response.status_code)
            print('Error:', response.text)


