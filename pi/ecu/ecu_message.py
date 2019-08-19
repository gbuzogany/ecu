import binascii

class ECU_Message():
    def __init__(self, message=None):

        self.destination = None
        self.length = None
        self.query_type = None
        self.table = None
        self.start_address = None
        self.stop_address = None
        self.checksum = None
        self.data = None
        self.payload = None
        self.assembled = False

        if message != None:
            self.data = message
            self.decode()

    def HANDSHAKE():
        return bytearray(b'\x72\x05\x00\xF0\x99')

    def WAKEUP():
        return bytearray(b'\xFE\x04\xFF\xFF')

    def ECU_HELLO():
        return bytearray(b'\x02\x04\x00\xFA')


    def decode(self):
        self.destination = self.data[0]
        self.length = self.data[1]

        if self.destination == 0x72:
            self.decode_outgoing()
        elif self.destination == 0x02:
            self.decode_incoming()
        else:
            print('Unknown destination: '+self.destination)

    def decode_incoming(self):
        self.query_type = self.data[2]
        self.table = self.data[3]
        self.start_address = self.data[4]
        self.payload = self.data[5:-1]
        self.checksum = self.data[-1]
        self.assembled = True
        self.validate_checksum()

    def decode_outgoing(self):
        self.query_type = self.data[2]
        self.table = self.data[3]
        self.start_address = self.data[4]
        self.stop_address = self.data[5]

        if len(self.data) == self.length-1:
            # just missing the checksum
            self.checksum = ECU_Message.calculate_checksum(self.data)
            if len(self.data) == self.length-1:
                self.data.append(self.checksum)
            elif len(self.data) == self.length:
                self.data[-1] = self.checksum

        elif len(self.data) == self.length:
            self.checksum = self.data[6]
            self.assembled = True
            if self.validate_checksum() == False:
                print('Checksum failed')
        else:
            print('Invalid message')

    def calculate_checksum(message):
        total = 0

        for i in range(0, len(message)):
            total += message[i]
        checksum = 0x100 - (total % 0x100)
        return checksum

    def validate_checksum(self):
        if self.assembled == False:
            self.assemble()

        checksum = ECU_Message.calculate_checksum(self.data[0:-1])
        if checksum == self.checksum:
            return True
        print('Checksum failed. Expected: '+hex(checksum))
        return False

    def assemble(self):
        if self.destination != None and self.length != None and self.query_type != None:
            if self.destination == 0x72 and self.query_type == 0x72:
                self.assemble_table_query()
            elif self.destination == 0x02 and self.query_type == 0x72:
                self.assemble_table_response()

    def assemble_table_query(self):
        if self.table != None and self.start_address != None and self.stop_address != None:
            data = bytearray()
            data.append(self.destination)
            data.append(self.length)
            data.append(self.query_type)
            data.append(self.table)
            data.append(self.start_address)
            data.append(self.stop_address)
            self.data = data
            checksum = ECU_Message.calculate_checksum(data)
            data.append(checksum)

    def assemble_table_response(self):
        if self.table != None and self.start_address != None and self.stop_address != None:
            data = bytearray()
            data.append(self.destination)
            data.append(self.length)
            data.append(self.query_type)
            data.append(self.table)
            data.append(self.start_address)
            data.append(self.stop_address)
            self.data = data
            checksum = ECU_Message.calculate_checksum(data)
            data.append(checksum)

    def print(self):
        if self.assembled == False:
            assembled = self.assemble()
            if assembled == False:
                return
        ECU_Message.print_bytes(self.data)

    def print_bytes(msg, caption=None):
        if msg != None:
            if caption != None:
                print(caption,  end='')
            decoded = msg.hex()
            for i in range(0, len(decoded)):
                print(decoded[i].upper(), end='')
                if (i-1)%2 == 0:
                    print(' ', end='')
            print('')

    def outgoing(self):
        self.destination = 0x72
        return self

    def incoming(self):
        self.destination = 0x02
        return self

    def read_request(self, data_table, start_register, end_register):
        self.destination = 0x72
        self.length = 0x07
        self.query_type = 0x72
        self.table = data_table
        self.start_address = start_register
        self.stop_address = end_register
        self.assemble()
        return self

    def data(self):
        return self.data

    def response_length(self):
        if self.query_type == 0x72:
            return 5 + self.stop_address - self.start_address + 1;
        else:
            return -1
