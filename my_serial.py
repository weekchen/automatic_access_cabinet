import serial
import threading
import time
# from manage import main

boxes_pos = {
        'box_100': "0#0", 'box_101': "125#0", 'box_102': "\r\n255#0\r\n",
        'box_200': "\r\n0#100\r\n", 'box_201': "\r\n125#100\r\n", 'box_202': "\r\n255#100\r\n",
        'box_300': "\r\n0#200\r\n", 'box_301': "\r\n125#200\r\n", 'box_302': "\r\n255#200\r\n",
        'box_400': "\r\n0#300\r\n", 'box_401': "\r\n125#300\r\n", 'box_402': "\r\n255#300\r\n",
        }


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
            # self.get_str = self.ser.read(self.ser.in_waiting)
            # print(self.get_str)
        return self.get_str

    def send_data(self, text):
        result = self.ser.write(text.encode("gbk"))
        # result = self.ser.write(0x0d)
        # result = self.ser.write(0x0a)

    def close_port(self):
        self.ser.close()


if __name__ == "__main__":
    my_serial = MySerial("COM3", 9600, None)
    # main()
    while 1:
        msg = my_serial.read_data()
        if len(msg) > 1:
            print(msg)
            print("###########")
            print("###########")
        if msg == "hello pc\n":
            print("get the message")
        time.sleep(1)
        # my_serial.send_data("hello stm32\r\n")
        my_serial.send_data(boxes_pos['box_101']+"\r\n")
        # time.sleep(1)
        # my_serial.send_data("\r\n")
        break
