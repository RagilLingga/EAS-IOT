#include <LiquidCrystal.h>

// Inisialisasi pin untuk LCD
LiquidCrystal lcd(7, 8, 9, 10, 11, 12);

int sensorPin = A0;  // Pin analog dimana LM35 terhubung
float temperature = 0;  // Variabel untuk menyimpan nilai suhu

void setup() {
  lcd.begin(16, 2);  // Inisialisasi layar LCD 16x2
  Serial.begin(9600);  // Inisialisasi komunikasi serial dengan baud rate 9600
}

void loop() {
  int sensorValue = analogRead(sensorPin);  // Membaca nilai analog dari sensor LM35
  temperature = (sensorValue * 5.0 * 100.0) / 1024.0;  // Konversi nilai analog ke suhu (Celcius)
  
  lcd.clear();
  lcd.print("Suhu: ");
  lcd.print(temperature);  // Menampilkan suhu pada LCD
  lcd.print(" C");
  
  Serial.println(temperature);  // Mengirim nilai suhu melalui serial
  delay(1000);  // Delay 1 detik
}
