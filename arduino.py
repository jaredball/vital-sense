
import serial

# Open serial port, adjust the port name to match the working port
ser = serial.Serial('portNameHere', 115200)

# Open a .txt file to write the data
with open('spo2_hr_data.txt', 'w') as file:
    while True:
        # Read a line from serial
        line = ser.readline().decode().strip()

        # Check if the line contains valid data
        if line.startswith("SPO2:") and "," in line and "HR:" in line:
            spo2, hr = line.split(",")
            spo2_value = spo2.split(":")[1].strip()
            hr_value = hr.split(":")[1].strip()

            # Write the data to the file
            file.write(f"SPO2: {spo2_value}, HR: {hr_value}\n")
            print(f"SpO2: {spo2_value}, Heart Rate: {hr_value}")
