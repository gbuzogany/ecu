from ecu import ECU
from ecu_message import ECU_Message
from table_11 import Table_11
from table_d1 import Table_D1

# 72 07 72 11 00 14 F0
packet = bytearray(b'\x72\x07\x72\x11\x00\x14\xF0')

msg = ECU_Message(packet)
msg.print()

msg = ECU_Message().read_request(0x11, 0x00, 0x14)
msg.print()

packet = bytearray(b'\x02\x1A\x72\x11\x00')
for i in range(0, 0x1A - 6):
    packet.append(0x00)

packet.append(0x61)

msg = ECU_Message(packet)
msg.print()

print('Read table D1:')
msg = ECU_Message().read_request(0xD1, 0x00, 0x05)
#      CMD,  LEN,  CMD,  DTAB, RAMK, RAMH, CHK
# OUT: 0x72, 0x07, 0x72, 0xD1, 0x00, 0x05, 0x3F
#      CMD,  LEN,  CMD,  RAMK, RAMH, NEUT, ????, ????, ????, ENG,  CHK
# ECU: 0x02, 0x0B, 0x72, 0xD1, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0xAF
msg.print()

print('Response:')
packet = bytearray(b'\x02\x0B\x72\xD1\x00\x00\x00\x00\x00\x01\xAF')
response = ECU_Message(packet)
response.print()
ECU_Message.print_bytes(response.payload)

if msg.response_length() == len(packet):
    print('Response length correct')
else:
    print('Response length incorrect')
    print(msg.response_length(), len(packet))

tab_d1 = Table_D1(response.payload)
# print(chr(27) + "[2J")
tab_d1.print()

print('Read table 11:')
msg = ECU_Message().read_request(0x11, 0x00, 0x0E)
# OUT: 0x72, 0x07, 0x72, 0x11, 0x00, 0x0E, 0xF6
# ECU: CMD,  LEN,  CMD,  RAML, RAMH, RPMH, RPML, TPSV, TPS%, ECTV, ECTC, IATH, IATL, MAPH, MAPL, ????, ????, BAT,  MPH,  CHK
# ECU: 0x02, 0x14, 0x72, 0x11, 0x00, 0x05, 0x5D, 0x19, 0x00, 0x2A, 0x7B, 0xAF, 0x36, 0x68, 0x45, 0xFF, 0xFF, 0x8B, 0x14, 0x18
msg.print()

print('response:')
packet = bytearray(b'\x02\x14\x72\x11\x00\x05\x5D\x19\x00\x2A\x7B\xAF\x36\x68\x45\xFF\xFF\x8B\x0F\x2c')
response = ECU_Message(packet)
response.print()
ECU_Message.print_bytes(response.payload)

tab_11 = Table_11(response.payload)
# print(chr(27) + "[2J")
tab_11.print()

gear = ECU.guess_gear(tab_11.speed, tab_11.rpm, tab_d1.neutral)
print('Gear:', gear)

if msg.response_length() == len(packet):
    print('Response length correct')
else:
    print('Response length incorrect')
    print(msg.response_length(), len(packet))