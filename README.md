# Smart Waste Management System Using IoT

## 📌 Project Overview
This project aims to develop a **Smart Waste Management System** that enables real-time monitoring of garbage bin status using IoT technologies. The system utilizes multiple sensors, ESP32 microcontrollers, and cloud integration to provide efficient waste management through edge computing and wireless communication.

---

## 🧠 Key Features
- **Bin Fill Level Detection** using Ultrasonic Sensors
- **Waste Type Identification** using Moisture Sensors
- **Human Presence Detection** for interaction awareness
- **Wireless Communication** between End Nodes and Edge Node using ESP-NOW
- **Data Filtering and Processing** at Edge Node
- **Cloud Storage and Visualization** using Adafruit IO (via MQTT)
- **Local Server & Web UI** to fetch and display bin data (latest & average)
- **Visual Alerts** (Red/Yellow LEDs) for full bin or interaction detection

---

## 🏗️ System Architecture
- **End Nodes** (Bin 1 & Bin 2):
  - Arduino UNO + ESP32
  - Ultrasonic Sensor x2
  - Moisture Sensor
  - Red & Yellow LEDs

- **Edge Node**:
  - ESP32
  - ESP-NOW for local data reception
  - MQTT for cloud publishing

- **Cloud**:
  - Adafruit IO (Feeds: `bin1_level`, `bin2_level`)

- **Local Server**:
  - Python Flask App
  - REST API to pull data from Adafruit IO
  - Web UI with buttons for latest and average bin levels

---

## 🔗 Communication Flow

| Source      | Destination    | Protocol  | Description                              |
|-------------|----------------|-----------|------------------------------------------|
| End Nodes   | Edge Node      | ESP-NOW   | Sends raw sensor data                    |
| Edge Node   | Adafruit IO    | MQTT      | Publishes bin fill data to cloud         |
| Flask Server| Adafruit IO    | REST API  | Fetches latest/average values            |
| Web UI      | Flask Server   | HTTP/AJAX | Displays real-time bin levels            |

---

## 💻 Technologies Used
- **Hardware**: ESP32, Arduino UNO, Ultrasonic Sensor, Moisture Sensor, LEDs
- **Software**: Arduino IDE, Python (Flask), HTML/CSS/JS
- **Protocols**: ESP-NOW, MQTT, HTTP
- **Platforms**: Adafruit IO (Cloud), Localhost Web Server

---

## 🚀 How It Works
1. **ESP32 End Nodes** read sensor values and transmit data to the **Edge ESP32** using ESP-NOW.
2. The **Edge Node** filters and forwards only required data (e.g., bin level) to **Adafruit IO** via MQTT.
3. A **Flask-based server** fetches this data using Adafruit's REST API and displays it through a **web dashboard**.
4. The **UI** shows:
   - Latest bin levels
   - Average fill percentage
   - Visual alerts when bins are full

---

## 📊 Output Snapshots
- Dashboard UI displaying live bin data  
- Adafruit IO feed values for bin1 and bin2  
- Local Flask server running at `http://127.0.0.1:5000/`  
- Serial monitor output from ESP32 edge and end nodes  
- Hardware setup with bins, sensors, and LEDs  

---

## 📚 References
- [Adafruit IO API Docs](https://io.adafruit.com/api/docs/)
- [ESP-NOW Documentation](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/network/esp_now.html)
- [MQTT Protocol](https://mqtt.org/)
- [Flask Web Framework](https://flask.palletsprojects.com/)

---

## 👨‍💻 Developed By
**Name:** Cheppalli Naga Sai Varun Kumar Reddy  
**Roll No:** CB.EN.P2EBS24006  
**Institution:** Amrita School of Engineering, Coimbatore  

