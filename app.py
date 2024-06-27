from flask import Flask, render_template_string
import random
import threading
import time
import serial

app = Flask(__name__)

# Konfigurasi port serial virtual dari VSPE
serial_port = 'COM2'  # Sesuaikan dengan port yang Anda buat di VSPE
baud_rate = 9600

# Inisialisasi koneksi serial
ser = serial.Serial(serial_port, baud_rate, timeout=1)

# Variabel global untuk menyimpan nilai suhu
temperature = 0.0

# Fungsi untuk mensimulasikan pembacaan nilai analog
def read_analog(pin):
    return random.randint(0, 1023)

# Fungsi untuk mengonversi nilai analog ke suhu (misalnya, dari LM35)
def convert_to_temperature(sensor_value):
    voltage = sensor_value * (5.0 / 1023.0)
    temperature = voltage * 100.0
    return temperature

# Fungsi untuk mensimulasikan pengiriman data suhu ke serial
def send_to_serial(temperature):
    print(f"Temperature: {temperature} °C")
    ser.write(f"{temperature}\n".encode())  # Mengirimkan data suhu ke serial

# Fungsi utama untuk mensimulasikan pembacaan nilai dan tampilan
def simulate_sensor_readings():
    global temperature
    while True:
        sensor_value = read_analog('A0')  # Simulasi bacaan dari pin analog A0
        temperature = convert_to_temperature(sensor_value)
        
        # Tampilkan suhu di console (simulasi untuk LCD)
        print(f"Suhu: {temperature} C")

        # Kirim suhu melalui serial (simulasi)
        send_to_serial(temperature)

        time.sleep(1)  # Tunda selama 1 detik sebelum membaca nilai berikutnya

# Thread untuk memulai simulasi
simulate_thread = threading.Thread(target=simulate_sensor_readings)
simulate_thread.daemon = True
simulate_thread.start()

# Route untuk menampilkan data suhu pada halaman web
@app.route('/')
def home():
    global temperature
    return render_template_string('''
    <!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <title>Suhu Arduino</title>
    <style>
      body {
        font-family: Arial, sans-serif;
        margin: 40px;
        background-color: #f0f0f0;
      }
      .container {
        max-width: 600px;
        margin: 0 auto;
        background-color: #ffffff;
        padding: 20px;
        border-radius: 8px;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
      }
      h1 {
        color: #333;
        text-align: center;
      }
      .temperature {
        font-size: 2em;
        text-align: center;
        margin-top: 30px;
        margin-bottom: 30px;
      }
      footer {
        text-align: center;
        margin-top: 20px;
        color: #666;
      }
    </style>
  </head>
  <body>
    <div class="container">
      <h1>Suhu Arduino</h1>
      <p class="temperature">Temperature: {{ temperature }} °C</p>
    </div>
    <footer>
      <p>© 2024 By Ragil Lingga Aditya</p>
    </footer>
  </body>
</html>
    ''', temperature=temperature)

if __name__ == '__main__':
    app.run(debug=True)
