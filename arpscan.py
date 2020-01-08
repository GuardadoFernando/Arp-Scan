#!/usr/bin/python3
from os import system, name 
from scapy.all import ARP, Ether, srp
import socket
import platform
import subprocess

#Creating a device object
class Device:
      def __init__(self,Mac, Ip):
        self.Mac = Mac
        self.Ip = Ip

def main():
    #Prints pc information
    print("Computer information: \n Host Name: " + socket.gethostname()+
    "\n Platform: "+platform.platform()+
    "\n Processor: "+platform.processor()
    +"\n")

    ip = input("Enter target IP address in cidr format (Example 192.168.1.0/24)\n")
    if ip == "":
        print("You must enter target IP address...")
    else:
        try:
            print("Scanning: " + ip + "...\n")
            arp = ARP(pdst=ip)
            ether = Ether(dst="ff:ff:ff:ff:ff:ff")
            packet = ether/arp
            result = srp(packet, timeout=3, verbose=0)[0]

            device_list = []
            for sent, received in result:
                device_obj = Device(received.hwsrc,received.psrc)
                device_list.append({'MAC':device_obj.Mac, 'IP': device_obj.Ip})

            print("Results: ")
            for device in device_list:
                print("MAC Address: "+ device['MAC'] + " || Ip Address: " + device['IP'])
        except Exception as e:
            raise
if __name__ == "__main__":
    main()