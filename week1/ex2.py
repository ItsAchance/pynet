#!/usr/bin/env python

"""Prompt a user to enter in an IP address from standard input. Read the IP address in and break it up into its octets. Print out the octets in decimal, binary, and hex.

Your program output should look like the following:

​ $ python exercise2.py 
Please enter an IP address: 80.98.100.240

    Octet1         Octet2         Octet3         Octet4     
------------------------------------------------------------
      80             98             100            240      
   0b1010000      0b1100010      0b1100100     0b11110000   
     0x50           0x62           0x64           0xf0      
------------------------------------------------------------

Four columns, fifteen characters wide, a header column, data centered in the column."""

ip_addr1 = "172.16.0.1"
ip_addr2 = "192.168.0.1"
ip_addr3 = "10.0.0.1"

print("\n")
print("{:^20}{:^20}{:^20}".format("Octet1", "Octet2", "Octet3"))
print("-" * 60)
print("{:^20}{:^20}{:^20}".format(ip_addr1, ip_addr2, ip_addr3))

print("{:^20}{:^20}{:^20}".format(ip_addr1, ip_addr2, ip_addr3))
print("-" * 60)
# Tråkig, inte klar