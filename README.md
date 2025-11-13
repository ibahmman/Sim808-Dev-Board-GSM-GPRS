# SIM808 MicroPython Driver / درایور MicroPython برای SIM808

A lightweight and easy-to-use MicroPython driver for the **SIM808 GSM/GPS module**, providing simple methods to send/receive SMS, control GPS, and communicate using AT commands.

کتابخانه‌ای سبک و ساده برای **ماژول SIM808** که امکان ارسال و دریافت پیامک، کنترل GPS و کار با دستورات AT را در محیط MicroPython فراهم می‌کند.

---

## 📦 Features / ویژگی‌ها

* ✅ Send and receive SMS messages / ارسال و دریافت پیامک‌ها
* 📡 Get GPS coordinates (latitude & longitude) / دریافت موقعیت مکانی (طول و عرض جغرافیایی)
* ⚙️ Set SIM center number automatically based on ISP (MCI / MTN) / تنظیم خودکار مرکز پیام بر اساس اپراتور
* 🧭 Turn GPS on/off / روشن یا خاموش کردن GPS
* 🔧 Simple AT command wrapper / رابط ساده برای ارسال دستورات AT

---

## 🧠 Requirements / پیش‌نیازها

* MicroPython board (e.g. ESP32, ESP8266, etc.) / برد مبتنی بر MicroPython (مثل ESP32 یا ESP8266)
* SIM808 GSM/GPS module / ماژول SIM808
* Proper UART connection between board and SIM808 / اتصال صحیح UART بین برد و ماژول

  ```
  TX (board) → RXD (SIM808)
  RX (board) → TXD (SIM808)
  GND (board) → GND (SIM808)
  ```

---

## ⚙️ Installation / نصب

Simply copy the file `sim808.py` to your MicroPython board.
فایل `sim808.py` را به برد MicroPython خود منتقل کنید.

Example using [ampy](https://github.com/scientifichackers/ampy):

```bash
ampy put sim808.py
```

Then import and use it in your MicroPython script.
سپس در کد خود آن را ایمپورت و استفاده کنید.

---

## 🚀 Usage Example / نمونه استفاده

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

📘 **توضیح:**

* متد `sms_send()` برای ارسال پیامک استفاده می‌شود.
* متد `sms_receive()` پیامک‌های خوانده‌نشده را بازمی‌گرداند.
* متد `gps_get_location()` مختصات جغرافیایی فعلی را می‌خواند.

---

## 🛰️ GPS Notes / نکات GPS

* It may take **30–60 seconds** to get a GPS fix the first time.
  ممکن است دریافت موقعیت GPS برای بار اول بین **۳۰ تا ۶۰ ثانیه** طول بکشد.
* Ensure the module has a clear view of the sky.
  اطمینان حاصل کنید که ماژول دید مستقیم به آسمان دارد.
* You can turn off GPS to save power:
  می‌توانید برای صرفه‌جویی در انرژی، GPS را خاموش کنید:

  ```python
  sim.set_gps_power(0)
  ```

---

## 🧩 Class Overview / مرور متدها

| Method / متد                           | Description / توضیح                                             |
| -------------------------------------- | --------------------------------------------------------------- |
| `send_at(cmd, expected="")`            | Send raw AT command / ارسال مستقیم دستور AT                     |
| `at_check()`                           | Check communication with SIM808 / بررسی ارتباط با ماژول         |
| `set_sms_mode(mode=1)`                 | Set SMS mode (1 = text) / تنظیم حالت پیامک                      |
| `set_sms_center(isp, sms_center=None)` | Configure SMS service center / تنظیم مرکز پیامک                 |
| `sms_send(number, message)`            | Send an SMS message / ارسال پیامک                               |
| `sms_receive()`                        | Read unread SMS messages / دریافت پیامک‌های خوانده‌نشده         |
| `set_gps_power(pwr=1)`                 | Enable/disable GPS power / روشن یا خاموش کردن GPS               |
| `gps_get_location()`                   | Retrieve current GPS coordinates / دریافت موقعیت جغرافیایی فعلی |

---

## 🧾 License / مجوز

This project is licensed under the MIT License.
این پروژه تحت مجوز MIT منتشر شده است و می‌توانید آزادانه از آن استفاده یا آن را ویرایش کنید.

---

## 👤 Author / نویسنده

**Sobhan Bahman Rashnu**
📧 [bahmanrashnu@gmail.com](mailto:bahmanrashnu@gmail.com)
💡 Contributions and pull requests are welcome!
💬 از پیشنهادها و بهبودهای شما استقبال می‌شود!

سبحان بهمن رشنو
