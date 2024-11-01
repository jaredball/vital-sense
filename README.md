# VitalSense Blood Oxygen & Heart Rate Sensor

This project provides a simple SpO2 (Blood Oxygen Saturation) and heart rate monitoring system using an Arduino Uno board and a MAX30105 sensor. The Arduino code reads sensor data and sends it to a Python script via serial communication, where the data is logged to a .txt file.

## Arduino Setup

1. Connect the MAX30105 sensor to your Arduino Uno board according to the wiring diagram provided in the Arduino code.

2. Install the required libraries:
   - Wire library
   - MAX30105 library
   - LiquidCrystal library (if using an LCD)

3. Upload the provided Arduino code (`QUEST.ino`) to your Arduino Uno board using the Arduino IDE or any compatible IDE.

## Python Setup

1. Make sure you have Python installed on your computer. You can download Python from the official website: [Python.org](https://www.python.org/).

2. Install the PySerial library using pip:
   ```
   pip install pyserial
   ```

## Running the Project

1. Connect your Arduino Uno board to your computer via USB.

2. Open the Python script (`spo2_hr_monitor.py`) in your preferred Python editor or IDE (e.g., PyCharm, VS Code).

3. Modify the serial port name in the Python script to match the port your Arduino Uno board is connected to. You can find the port name in the Arduino IDE under `Tools > Port`.

4. Run the Python script. This will continuously read data from the Arduino board and log it to a .txt file.

5. Place your finger on the MAX30105 sensor to measure SpO2 and heart rate. The data will be logged to the .txt file.

## File Descriptions

- `QUEST.ino`: Arduino code for reading SpO2 and heart rate data from the MAX30105 sensor and sending it to the serial port.

- `arduino.py`: Python script for receiving SpO2 and heart rate data from the serial port and logging it to a .txt file.

## Additional Notes

- Make sure the Arduino and Python scripts are both running while collecting data.

- The MAX30102 sensor has had moments where it does not turn on and collect data, the solution to this issue was not found.

- The sensor's accuracy still fluctuates. Adjustments may be made to several variables to fix this, two of the most notable being the LED brightness and sample rate.

- For the breadboard set up (when using an LED display), the following configuration can be used:

![image](https://github.com/user-attachments/assets/24adf2ba-18e3-45f1-b302-bff1fd6d844b)

![image](https://github.com/user-attachments/assets/6326c2ba-9851-4090-ba82-c65a9a69c8b2)
