'''
Created on May 1, 2019

@author: ae
'''
import socket
from WeatherLink import *

WEATHERLINK_IP = "192.168.55.225"
WEATHERLINK_PORT = 22222


weatherlink_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
weatherlink_socket.connect((WEATHERLINK_IP, WEATHERLINK_PORT))
weatherlink_socket.sendall(b"LOOP 1\n")

data = weatherlink_socket.recv(1024)

loop = LoopPacket(data)

weatherlink_socket.sendall(b"LPS 2 1\n")

data = weatherlink_socket.recv(1024)

loop2 = Loop2Packet(data)

weatherlink_socket.close()



# print(loop.pkt_type)
print "Bar Trend:", (loop.bar_trend)
print "Weather icon:", (loop.forecast_icons)
print "Barometr: %3.2f" % (loop.barometer)
print "Temp Inside C: %2.2f" % (loop.inside_temp)
print "Inside Hum %:", (loop.inside_hum)
print "Temp Outside C: %2.2f" % (loop.outside_temp)
print "Wind Speed km/h: %2.2f" % (loop.wind_speed)
print "Wind Direction", (loop.wind_dir)
print "Outside Hum %:", (loop.out_hum)
print "Dayly raim, mm: %3.2f" % (loop.day_rain)

print('LOOP2')
print(loop2.pkt_type)
print(loop2.bar_trend)
print(loop2.barometer)
print(loop2.inside_temp)
