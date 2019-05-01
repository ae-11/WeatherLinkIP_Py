'''
Created on Feb 12, 2014

@author: Joseph
'''
import socket
from WeatherLink import *

WEATHERLINK_IP = "192.168.1.245"
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



print(loop.pkt_type)
print(loop.bar_trend)
print(loop.barometer)
print(loop.inside_temp)
print(loop.inside_hum)
print(loop.outside_temp)
print(loop.wind_speed)
print(loop.wind_dir)
print(loop.out_hum)
print(loop.day_rain)

print('LOOP2')
print(loop2.pkt_type)
print(loop2.bar_trend)
print(loop2.barometer)
print(loop2.inside_temp)