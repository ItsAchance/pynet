#!/usr/bin/env python

"""You have the following three variables from the arp table of a router:

mac1 = "Internet  10.220.88.29           94   5254.abbe.5b7b  ARPA   FastEthernet4"
mac2 = "Internet  10.220.88.30            3   5254.ab71.e119  ARPA   FastEthernet4"
mac3 = "Internet  10.220.88.32          231   5254.abc7.26aa  ARPA   FastEthernet4"

Process these ARP entries and print out a table of "IP ADDR" to "MAC ADDRESS" mappings. The output should look like following:

             IP ADDR          MAC ADDRESS
-------------------- --------------------
        10.220.88.29       5254.abbe.5b7b
        10.220.88.30       5254.ab71.e119
        10.220.88.32       5254.abc7.26aa

Two columns, 20 characters wide, data right aligned, a header column."""


mac1 = "Internet  10.220.88.29           94   5254.abbe.5b7b  ARPA   FastEthernet4"

mac2 = "Internet  10.220.88.30            3   5254.ab71.e119  ARPA   FastEthernet4"

mac3 = "Internet  10.220.88.32          231   5254.abc7.26aa  ARPA   FastEthernet4"

mac1 = mac1.split()
ip_address1 = mac1[1]
mac_address1 = mac1[3]

mac2 = mac2.split()
ip_address2 = mac2[1]
mac_address2 = mac2[3]

mac3 = mac3.split()
ip_address3 = mac3[1]
mac_address3 = mac3[3]

print(f"{'IP ADDR' : ^20}{'MAC ADDRESS' : >20}")
print("-" *22, "-" *22)
print(f"{ip_address1 : ^20} {mac_address1 : >20} \n{ip_address2 : ^20} {mac_address2 : >20}\n{ip_address3 : ^20} {mac_address3 : >20}")