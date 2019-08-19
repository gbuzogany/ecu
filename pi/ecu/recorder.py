from ecu import ECU
import time

ecu = ECU(record=True)
ecu.connect()
result = ecu.handshake_ecu()
if result == False:
    print('Error sending message.')
    exit()

print('Handshake Successful!')

