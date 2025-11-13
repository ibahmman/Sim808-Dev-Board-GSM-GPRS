from machine import UART
import time


class Sim808:
    BAUDRATE = 9600
    TIMEOUT = 2000
    SIM_ISP = 'mci'
    SMS_CENTER = {
        'mci': '+9891100500',
        'mtn': '+9893500005'
    }

    def __init__(self, tx: int, rx: int, baudrate: int=9600, timeout: int=2000):
        self.BAUDRATE = baudrate
        self.TIMEOUT = timeout
        self.TXD = tx
        self.RXD = rx

        self.SIM808 = UART(2, baudrate=self.BAUDRATE, tx=self.TXD, rx=self.RXD, timeout=self.TIMEOUT)


    def _safe_decode(self, data: bytes) -> str:
        allowed = []
        for b in data:
            if b in (9, 10, 13) or (32 <= b <= 126):
                allowed.append(b)
        return bytes(allowed).decode("ascii")
    
    def send_at(self, cmd, expected=""):
        self.SIM808.write((cmd + '\r\n').encode())
        t0 = time.ticks_ms()
        response = b""

        while time.ticks_diff(time.ticks_ms(), t0) < self.TIMEOUT:
            if self.SIM808.any():
                response += self.SIM808.read()
                if expected and expected.encode() in response:
                    break
        return self._safe_decode(response)

    
    def at_check(self):
        self.send_at("AT", "OK")

    def set_sms_mode(self, sms_mode=1):
        self.send_at(f"AT+CMGF={sms_mode}", "OK")
    
    def set_sms_center(self, isp=None, sms_center=None):
        self.SIM_ISP = 'mci' if isp.lower() in ['mci', 'hamrahaval', 'irmci'] else 'mtn' if isp.lower() in ['mtn', 'irancell', 'mtnirancell'] else 'mci'
        self.SMS_CENTER_NUMBER = sms_center
        
        if not sms_center:
            self.send_at(f'AT+CSCA="{self.SMS_CENTER[self.SIM_ISP]}"', "OK")
        else:
            self.send_at(f'AT+CSCA="{self.SMS_CENTER_NUMBER}"', "OK")

    def set_gps_power(self, pwr=1):
        self.send_at(f'AT+CGNSPWR={pwr}', "OK")



    def sms_send(self, mobile_number, message):
        self.at_check()
        self.set_sms_mode(1)

        mobile_number = f'+98{mobile_number[-10:]}'
        
        cmd = f'AT+CMGS="{mobile_number}"'
        if '>' in self.send_at(cmd, ">"):
            self.SIM808.write((message + "\x1A").encode())
            print("Message sent.")
            return True
        else:
            print('Faild to send message.')
            return False


    def sms_receive(self):
        self.at_check()
        self.set_sms_mode(1)
        response = self.send_at(f'AT+CMGL="REC UNREAD"')
        if "+CMGL" in response:
            messages = response.split("+CMGL:")
            for msg in messages[1:]:
                msg = msg.strip().split(',')
                d = {
                    'id': msg[0],
                    'status': msg[1],
                    'sender': msg[2],
                    'date': msg[4],
                    'time': msg[5].split('\r\n')[0],
                    'message': msg[5].split('\r\n')[1]
                }
                print('Received message data: ', d)
                return d


    def gps_get_location(self):
        self.set_gps_power(1)
        time.sleep(2)

        response = self.send_at('AT+CGNSINF')
        parts = response.split(",")
        if len(parts) > 4 and parts[3] and parts[4]:
            lat = parts[3]
            lon = parts[4]
            print(f"Latitude: {lat}, Longitude: {lon}")
            return lat, lon
        else:
            print("No GPS fix yet")
            return None, None
