# Project Description

Proyek Monitoring Suhu dengan Arduino dan Flask

Proyek ini bertujuan untuk memonitor suhu menggunakan Arduino yang terhubung dengan sensor LM35. Data suhu yang terbaca akan disimulasikan menggunakan Proteus dan ditampilkan secara real-time melalui antarmuka web yang dibangun dengan Flask. Arduino akan mengirimkan data suhu melalui komunikasi serial virtual menggunakan VSPE (Virtual Serial Port Emulator).

Deskripsi Proyek

Proyek ini menggunakan Arduino Uno sebagai mikrokontroler utama yang terhubung dengan sensor suhu LM35. Data suhu yang diterima oleh Arduino akan dikonversi menjadi nilai tegangan dan kemudian ditampilkan pada LCD 16x2. Selain itu, nilai suhu juga akan dikirimkan melalui serial untuk diproses dan ditampilkan dalam bentuk antarmuka web menggunakan Flask.

Fitur Utama

Monitoring Suhu Real-Time: Memungkinkan pengguna untuk melihat nilai suhu aktual yang dikirim oleh Arduino.
Simulasi Proteus: Menyediakan simulasi perangkat keras menggunakan Proteus untuk memvalidasi pengiriman data suhu dari Arduino.
Antarmuka Web Responsif: Antarmuka web dibangun dengan Flask untuk menampilkan data suhu secara visual dan intuitif.
