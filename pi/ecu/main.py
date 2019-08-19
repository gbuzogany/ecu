from ecu import ECU
import time

ecu = ECU()
ecu.connect()
result = ecu.handshake_ecu()
if result == False:
    print('Error sending message.')
    exit()

print('Handshake Successful!')

while True:
#    print(chr(27) + "[2J")
    t11 = ecu.read_table_11()
    t11.print()
    td1 = ecu.read_table_d1()
    td1.print()
    gear = ECU.guess_gear(t11.speed, t11.rpm, td1.neutral)
    print('Gear:', gear)
    time.sleep(0.5)
