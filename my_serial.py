import serial
import threading
import time
# from manage import main


class MySerial:
    def __init__(self, portx, bps, timeout):
        self.get_str = ''
        while 1:
            try:
                self.ser = serial.Serial(portx, bps, bytesize=8, parity='N', stopbits=1, timeout=timeout)
                print("串口启动成功")
                break
            except Exception as e:
                print("--异常--: ", e)

    def read_data(self):
        if self.ser.in_waiting:
            self.get_str = self.ser.read(self.ser.in_waiting).decode("gbk")
            print(self.get_str)
        return self.get_str

    def send_data(self, text):
        result = self.ser.write(text.encode("gbk"))
        return result

    def close_port(self):
        self.ser.close()


if __name__ == "__main__":
    my_serial = MySerial("COM4", 9600, None)
    # main()
    while 1:
        msg = my_serial.read_data()
        if msg == "hello pc\n":
            print("get the message")
        time.sleep(1)
        my_serial.send_data("hello stm32")
        time.sleep(1)
