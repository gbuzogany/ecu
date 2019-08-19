from ecu_sim import ECU_Sim

class Serial(object):
    def __init__(self, port='/dev/ttyUSB0', baudrate=9600, dsrdtr=False):
        self.buffer = bytearray()
        self.sim = ECU_Sim()
        pass

    def close(self):
        return True

    def setDTR(self, value=True):
        if value == True:
            self.sim.setLow()
        else:
            self.sim.setHigh()
        return True

    def write(self, msg):
        self.sim.write(msg)
        self.buffer += msg
        return True

    def read(self, length=1):
        if len(self.buffer) > 0:
            b = self.buffer[0:length]
            self.buffer = self.buffer[length+1:]
            return b
        else:
            return self.sim.read(length)