from serial import Serial
from ecu_message import ECU_Message
from table_11 import Table_11
from table_d1 import Table_D1
import time

class ECU():
    def __init__(self, config=None, record=None):
        self.config = config
        self.record = record
        self.ser = None

    def handshake_ecu(self):
        print('Starting handshake...')
        if self.ser == None:
            return False

        self.ser.setDTR(True)
        time.sleep(1.0)
        self.ser.setDTR(False)
        time.sleep(0.07)
        self.ser.setDTR(True)
        time.sleep(0.12)
        print('Sending WAKEUP...')
        result = self.send(ECU_Message.WAKEUP())
        time.sleep(0.2)
        print('Sending HANDSHAKE...')
        result = self.send(ECU_Message.HANDSHAKE())
        trail = self.ser.read(1)

        msg = self.ser.read(4)
        ECU_Message.print_bytes(msg, 'Received: ')
        if msg == ECU_Message.ECU_HELLO():
            return True
        else:
            return False

    def read_table_d1(self):
        msg = ECU_Message().read_request(0xD1, 0x00, 0x05)
        print('Requesting table D1')
        self.send(msg.data)
        resp_length = msg.response_length()
        if resp_length > 0:
            tab = self.ser.read(resp_length)
            ECU_Message.print_bytes(tab, 'Received: ')
            response = ECU_Message(tab)
            return Table_D1(response.payload)
        else:
            return False

    def read_table_11(self):
        msg = ECU_Message().read_request(0x11, 0x00, 0x0E)
        print('Requesting table 11')
        self.send(msg.data)
        resp_length = msg.response_length()
        if resp_length > 0:
            tab = self.ser.read(resp_length)
            ECU_Message.print_bytes(tab, 'Received: ')
            response = ECU_Message(tab)
            return Table_11(response.payload)
        else:
            return False

    def connect(self):
        if self.ser != None:
            self.disconnect()

        self.ser = Serial(port='/dev/ttyUSB0', baudrate=38400)
        return True

    def send(self, msg):
        ECU_Message.print_bytes(msg, 'Sent: ')
        self.ser.write(msg)
        buf_msg = self.ser.read(len(msg))
        if buf_msg == msg:
            return True
        return False


    def guess_gear(speed, rpm, neutral):
        if neutral != 0:
            return -1

        prim_reduction = 1.690
        final_reduction = 2.8
        tire_circumference = 1.98
        #                 1st,   2nd,   3rd,   4th,   5th,   6th
        gear_ratios = [ 3.071, 2.235, 1.777, 1.520, 1.333, 1.214 ]
        base_wheel_speed = rpm / prim_reduction;

        base = []
        delta = []

        for i in range(len(gear_ratios)):
            #           (             base wheel speed rpm                  ) / (s/min) * tire_circumference * (m/s to km/h)
            base.append((base_wheel_speed / gear_ratios[i] / final_reduction) /   60    * tire_circumference * 3.6)
            delta.append(abs(speed-base[i]))


        smallest_index = 0
        smallest_value = 9999999

        for i in range(len(delta)):
            if delta[i] < smallest_value:
                smallest_index = i
                smallest_value = delta[i]

        return smallest_index+1

    def disconnect(self):
        if self.ser != None:
            self.ser.close()
            self.ser = None
            return True
        return False
