'''
Created on May 1, 2019

@author: ae
'''
import struct

class Loop2Packet:

    def __init__(self, raw_data):
        
        #copy data
        self.ack = struct.unpack('c', raw_data[0:1])[0]
        self.L = struct.unpack('c', raw_data[1:2])[0]
        self.O1 = struct.unpack('c', raw_data[2:3])[0]
        self.O2 = struct.unpack('c', raw_data[3:4])[0]
        
        trend = struct.unpack('b', raw_data[4:5])[0]
        trends = {-60: "Falling Rapidly", -20: "Falling Slowly", 0: "Steady", 20: "Rising Slowly", 60: "Rising Rapidly"}
        self.bar_trend = trends[trend]
        
        self.pkt_type = struct.unpack('B', raw_data[5:6])[0]
        
        self.barometer = struct.unpack('H', raw_data[8:10])[0] / 1000
        
        self.inside_temp = struct.unpack('h', raw_data[10:12])[0] / 10
        self.inside_hum = struct.unpack('B', raw_data[12:13])[0]
        
        self.wind_speed = struct.unpack('B', raw_data[15:16])[0]
        self.wind_dir = struct.unpack('H', raw_data[17:19])[0]
        self.ten_min_avg_wind_spd = struct.unpack('H', raw_data[23:25])[0] * 0.1

class LoopPacket:

    def __init__(self, raw_data):
        
        #copy data
        self.ack = struct.unpack('c', raw_data[0:1])[0]
        self.L = struct.unpack('c', raw_data[1:2])[0]
        self.O1 = struct.unpack('c', raw_data[2:3])[0]
        self.O2 = struct.unpack('c', raw_data[3:4])[0]
        
        trend = struct.unpack('b', raw_data[4:5])[0]
        trends = {-60: "Falling Rapidly", -20: "Falling Slowly", 0: "Steady", 20: "Rising Slowly", 60: "Rising Rapidly"}
        self.bar_trend = trends[trend]
        
        self.pkt_type = struct.unpack('B', raw_data[5:6])[0]
        self.next_record = struct.unpack('H', raw_data[6:8])[0]
        self.barometer = float(struct.unpack('H', raw_data[8:10])[0]) * 25.4 / 1000
        self.inside_temp = (float(struct.unpack('h', raw_data[10:12])[0]) - 320) * 5 / 90
        self.inside_hum = struct.unpack('B', raw_data[12:13])[0]
        self.outside_temp = struct.unpack('h', raw_data[13:15])[0] / 10
        self.outside_temp = (float(struct.unpack('h', raw_data[13:15])[0]) - 320) * 5 / 90
        self.wind_speed = float(struct.unpack('B', raw_data[15:16])[0]) * 1.60934
        self.ten_min_avg_wind_spd = float(struct.unpack('B', raw_data[16:17])[0]) * 1.60934
        self.wind_dir = struct.unpack('H', raw_data[17:19])[0]
        self.ex_temp_1 = struct.unpack('b', raw_data[19:20])[0] - 90
        self.ex_temp_2 = struct.unpack('b', raw_data[20:21])[0] - 90
        self.ex_temp_3 = struct.unpack('b', raw_data[21:22])[0] - 90
        self.ex_temp_4 = struct.unpack('b', raw_data[22:23])[0] - 90
        self.ex_temp_5 = struct.unpack('b', raw_data[23:24])[0] - 90
        self.ex_temp_6 = struct.unpack('b', raw_data[24:25])[0] - 90
        self.ex_temp_7 = struct.unpack('b', raw_data[25:26])[0] - 90
        self.soil_temp_1 = struct.unpack('b', raw_data[26:27])[0] - 90
        self.soil_temp_2 = struct.unpack('b', raw_data[27:28])[0] - 90
        self.soil_temp_3 = struct.unpack('b', raw_data[28:29])[0] - 90
        self.soil_temp_4 = struct.unpack('b', raw_data[29:30])[0] - 90
        self.leaf_temp_1 = struct.unpack('b', raw_data[30:31])[0] - 90
        self.leaf_temp_2 = struct.unpack('b', raw_data[31:32])[0] - 90
        self.leaf_temp_3 = struct.unpack('b', raw_data[32:33])[0] - 90
        self.leaf_temp_4 = struct.unpack('b', raw_data[33:34])[0] - 90
        self.out_hum = struct.unpack('B', raw_data[34:35])[0]
        self.ex_hum_1 = struct.unpack('B', raw_data[35:36])[0]
        self.ex_hum_2 = struct.unpack('B', raw_data[36:37])[0]
        self.ex_hum_3 = struct.unpack('B', raw_data[37:38])[0]
        self.ex_hum_4 = struct.unpack('B', raw_data[38:39])[0]
        self.ex_hum_5 = struct.unpack('B', raw_data[39:40])[0]
        self.ex_hum_6 = struct.unpack('B', raw_data[40:41])[0]
        self.ex_hum_7 = struct.unpack('B', raw_data[41:42])[0]
        self.rain_rate = struct.unpack('H', raw_data[42:44])[0] * 0.2
        self.uv = struct.unpack('B', raw_data[44:45])[0]
        self.solar_radiation = struct.unpack('H', raw_data[45:47])[0]
        self.storm_rain = struct.unpack('H', raw_data[47:49])[0] * 0.2
        self.storm_start_date = struct.unpack('H', raw_data[49:51])[0]
        self.day_rain = float(struct.unpack('H', raw_data[51:53])[0]) * 0.2
        self.month_rain = struct.unpack('H', raw_data[53:55])[0] * 0.2
        self.year_rain = struct.unpack('H', raw_data[55:57])[0] * 0.2
        self.day_et = struct.unpack('H', raw_data[57:59])[0] / 1000
        self.month_et = struct.unpack('H', raw_data[59:61])[0] / 100
        self.year_et = struct.unpack('H', raw_data[61:63])[0] / 100
        self.soil_moisture_1 = struct.unpack('B', raw_data[63:64])[0]
        self.soil_moisture_2 = struct.unpack('B', raw_data[64:65])[0]
        self.soil_moisture_3 = struct.unpack('B', raw_data[65:66])[0]
        self.soil_moisture_4 = struct.unpack('B', raw_data[66:67])[0]
        self.leaf_wetness_1 = struct.unpack('B', raw_data[67:68])[0]
        self.leaf_wetness_2 = struct.unpack('B', raw_data[68:69])[0]
        self.leaf_wetness_3 = struct.unpack('B', raw_data[69:70])[0]
        self.leaf_wetness_4 = struct.unpack('B', raw_data[70:71])[0]
        self.inside_alarms = struct.unpack('c', raw_data[71:72])[0]
        self.rain_alarms = struct.unpack('c', raw_data[72:73])[0]
        self.outside_alarms_1 = struct.unpack('c', raw_data[73:74])[0]
        self.outside_alarms_2 = struct.unpack('c', raw_data[74:75])[0]
        self.extra_temp_hum_alarm_1 = struct.unpack('c', raw_data[75:76])[0]
        self.extra_temp_hum_alarm_2 = struct.unpack('c', raw_data[76:77])[0]
        self.extra_temp_hum_alarm_3 = struct.unpack('c', raw_data[77:78])[0]
        self.extra_temp_hum_alarm_4 = struct.unpack('c', raw_data[78:79])[0]
        self.extra_temp_hum_alarm_5 = struct.unpack('c', raw_data[79:80])[0]
        self.extra_temp_hum_alarm_6 = struct.unpack('c', raw_data[80:81])[0]
        self.extra_temp_hum_alarm_7 = struct.unpack('c', raw_data[81:82])[0]
        self.extra_temp_hum_alarm_8 = struct.unpack('c', raw_data[82:83])[0]
        self.soil_leaf_alarm_1 = struct.unpack('c', raw_data[83:84])[0]
        self.soil_leaf_alarm_2 = struct.unpack('c', raw_data[84:85])[0]
        self.soil_leaf_alarm_3 = struct.unpack('c', raw_data[85:86])[0]
        self.soil_leaf_alarm_4 = struct.unpack('c', raw_data[86:87])[0]
        self.xmtr_battery_status = struct.unpack('?', raw_data[87:88])[0]
        self.console_battery_volts = ((struct.unpack('h', raw_data[88:90])[0] * 300) / 512) / 100.0
        icon = struct.unpack('b', raw_data[90:91])[0]
        icons = {2: "Cloud", 3: "Cloud + Rain", 6: "Partial Sun + Cloud", 7: "Partial Sun + Cloud + Rain", 
            8: "Sun", 18: "Partial Sun + Cloud + Rain", 19: "Cloud + Rain + Snow", 22: "Partial Sun + Cloud + Snow", 
            23: "Partial Sun + Cloud + Rain + Snow"}
        self.forecast_icons = icons[icon]
        self.forecast_rule = struct.unpack('c', raw_data[91:92])[0]
        self.sunrise = struct.unpack('h', raw_data[92:94])[0]
        self.sunset = struct.unpack('h', raw_data[94:96])[0]
        self.lf  = struct.unpack('c', raw_data[96:97])[0]
        self.cr  = struct.unpack('c', raw_data[97:98])[0]
        self.crc  = struct.unpack('h', raw_data[98:100])[0]