class Table_11():
    def __init__(self, data):
        self.rpm = self.parse_rpm(data)
        self.tps_volt = self.parse_tps_volt(data)
        self.tps_perc = self.parse_tps_perc(data)
        self.ect_volt = self.parse_ect_volt(data)
        self.ect_deg_c = self.parse_ect_deg_c(data)
        self.iat_volt = self.parse_iat_volt(data)
        self.iat_deg_c = self.parse_iat_deg_c(data)
        self.map_volt = self.parse_map_volt(data)
        self.map_kpa = self.parse_map_kpa(data)
        self.batt_volt = self.parse_batt_volt(data)
        self.speed = self.parse_speed(data)
        self.fuel_inj = self.parse_fuel_inj(data)

    def parse_rpm(self, data):
        rpm = bytearray()
        rpm.append(data[1])
        rpm.append(data[0])
        return int.from_bytes(rpm, byteorder='little', signed=False)

    def parse_tps_volt(self, data):
        return data[2] * (5.0/256.0)

    def parse_tps_perc(self, data):
        return data[3] / 16.0

    def parse_ect_volt(self, data):
        return data[4] * (5.0 / 256.0)

    def parse_ect_deg_c(self, data):
        return data[5] - 40.0

    def parse_iat_volt(self, data):
        return data[6] * (5.0 / 256.0)

    def parse_iat_deg_c(self, data):
        return data[7] - 40.0

    def parse_map_volt(self, data):
        return data[8] * (5.0 / 256.0)

    def parse_map_kpa(self, data):
        return data[9]

    def parse_batt_volt(self, data):
        return data[12] / 10.0

    def parse_speed(self, data):
        return data[13]

    def parse_fuel_inj(self, data):
        return 0

    def print(self):
        print('RPM:\t\t', self.rpm, 'rpm')
        print('TPS Voltage:\t', self.tps_volt, 'V')
        print('TPS %:\t\t', self.tps_perc, '%')
        print('ECT Voltage:\t', self.ect_volt, 'V')
        print('ECT Temp:\t', self.ect_deg_c, 'C')
        print('IAT Voltage:\t', self.iat_volt, 'V')
        print('IAT Temp:\t', self.iat_deg_c, 'C')
        print('MAP Voltage:\t', self.map_volt, 'V')
        print('MAP Pressure:\t', self.map_kpa, 'kPa')
        print('Battery Voltage:', self.batt_volt, 'V')
        print('Speed:\t\t', self.speed, 'km/h')
        # print('Fuel Injectors:\t', self.fuel_inj)

