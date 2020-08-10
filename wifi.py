import sys
import subprocess
import os
from decouple import config

# IP_NETWORK = "192.168.10.4"
# #config('IP_NETWORK')
# #config('IP_DEVICE')
# Mustafa = "192.168.10.4:"
# Sarrah = "192.168.10.5"

IP_NETWORK=""
Name = ""
print("Who To Check For .........  ")
input = input("1. Mustafa 2. Sarrah 3. Fatima 4. Muhammad  :")
if(input == "1"):
    IP_NETWORK =IP_NETWORK+"192.168.10.4"
    print(IP_NETWORK)
    Target = "192.168.10.4:"
    Name =Name+"Mustafa"

elif(input == "2"):
    IP_NETWORK =IP_NETWORK+"192.168.10.5"
    print(IP_NETWORK)
    Target = "192.168.10.5:"
    Name = "Sarrah"+Name

elif(input == "3"):
    IP_NETWORK =IP_NETWORK+"192.168.10.5"
    print(IP_NETWORK)
    Target = "192.168.10.5:"
    Name = "Fatima"+Name


elif(input == "4"):
    IP_NETWORK =IP_NETWORK+"192.168.10.8"
    print(IP_NETWORK)
    Target = "192.168.10.8:"
    Name = Name+"Muhammad"

proc = subprocess.Popen(["ping", IP_NETWORK],stdout=subprocess.PIPE)
while True:
  line = proc.stdout.readline()
  #print(line)
  if not line:
    break
  #the real code does filtering here
  connected_ip = line.decode('utf-8').split()[3]
  print(connected_ip)

  if connected_ip == Target:
      #subprocess.Popen(["say", "Mustafa just connected to the network"])
      print(Name+ " Has Connected")
