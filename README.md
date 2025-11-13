# SIM808 MicroPython Driver

A lightweight and easy-to-use MicroPython driver for the **SIM808 GSM/GPS module**, providing simple methods to send/receive SMS, control GPS, and communicate using AT commands.

---

## 📦 Features

* ✅ Send and receive SMS messages
* 📡 Get GPS coordinates (latitude & longitude)
* ⚙️ Set SIM center number automatically based on ISP (MCI / MTN)
* 🦭 Turn GPS on/off
* 🔧 Simple AT command wrapper

---

## 🧠 Requirements

* MicroPython board (e.g. ESP32, ESP8266, etc.)
* SIM808 GSM/GPS module
* Proper UART connection between board and SIM808

  ```
  TX (board) → RXD (SIM808)
  RX (board) → TXD (SIM808)
  GND (board) → GND (SIM808)
  ```

---

## ⚙️ Installation

Simply copy the file `sim808.py` to your MicroPython board.

Example using [ampy](https://github.com/scientifichackers/ampy):

```bash
ampy put sim808.py
```

Then import and use it in your MicroPython script.

---

## 🚀 Usage Example

```python
from sim808 import Sim808
import time

# Initialize SIM808 (TX=17, RX=16 for example)
sim = Sim808(tx=17, rx=16)

# Check connection
sim.at_check()

# Set SMS mode
sim.set_sms_mode(1)

# Send SMS
sim.sms_send("09123456789", "Hello from SIM808!")

# Receive unread messages
msg = sim.sms_receive()
if msg:
    print("New message:", msg)

# Enable GPS and get location
lat, lon = sim.gps_get_location()
if lat and lon:
    print("GPS:", lat, lon)
```

---

## 🛰️ GPS Notes

* It may take **30–60 seconds** to get a GPS fix the first time.
* Ensure the module has a clear view of the sky.
* You can turn off GPS to save power:

  ```python
  sim.set_gps_power(0)
  ```

---

## 🧹 Class Overview

| Method                                 | Description                               |
| -------------------------------------- | ----------------------------------------- |
| `send_at(cmd, expected="")`            | Send raw AT command and wait for response |
| `at_check()`                           | Check communication with SIM808           |
| `set_sms_mode(mode=1)`                 | Set SMS mode (1 = text)                   |
| `set_sms_center(isp, sms_center=None)` | Configure SMS service center              |
| `sms_send(number, message)`            | Send an SMS message                       |
| `sms_receive()`                        | Read unread SMS messages                  |
| `set_gps_power(pwr=1)`                 | Enable/disable GPS power                  |
| `gps_get_location()`                   | Retrieve current GPS coordinates          |

---

## 🗞️ License

This project is licensed under the MIT License.
Feel free to use and modify it for your own projects!

---

## 👤 Author

**Sobhan Bahman Rashnu**
📧 [bahmanrashnu@gmail.com](mailto:bahmanrashnu@gmail.com)
💡 Contributions and pull requests are welcome!
