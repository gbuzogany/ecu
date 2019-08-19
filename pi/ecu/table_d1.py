class Table_D1():
    def __init__(self, data):
        self.neutral = self.parse_neutral(data)
        self.neutral_txt = self.parse_neutral_txt(data)
        self.engine_running = self.parse_engine_running(data)

    def parse_neutral(self, data):
        return data[0]

    def parse_neutral_txt(self, data):
        if data[0] == 0:
            return 'gear'
        elif data[0] == 1:
            return 'neutral/clutch'
        elif data[0] == 3:
            return 'kickstand'
        return -1

    def parse_engine_running(self, data):
        return data[4] == 0x01

    def print(self):
        print('Neutral:\t', self.neutral)
        print('Neutral (txt):\t', self.neutral_txt)
        print('Engine Running: ', self.engine_running)