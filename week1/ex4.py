#!/usr/bin/env python

"""Create a show_version variable that contains the following

 show_version = "*0        CISCO881-SEC-K9       FTX0000038X    " 

Remove all leading and trailing whitespace from the string.

Split the string and extract the model and serial_number from it.

Check if 'Cisco' is contained in the model string (ignore capitalization).

Check if '881' is in the model string.

Print out both the serial number and the model."""


show_version = "*0        CISCO881-SEC-K9       FTX0000038X    "

show_version = show_version.strip()
fields = show_version.split()

model = fields[1]
serial = fields[2]

vendor_cisco = 'cisco' in model.lower()
print(f"Is the word 'Cisco' in the model name?: {vendor_cisco}")

serial_number = '881' in serial
print(f"Is the numbers '881' in the model name?: {vendor_cisco}")

print(f"\nThe model model and serial number are: {model} & {serial}")