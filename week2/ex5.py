#!/bin/usr/env python

"""Read the 'show_ip_bgp_summ.txt' file into your program. From this BGP output obtain the first and last lines of the output.

From the first line use the string .split() method to obtain the local AS number.

From the last line use the string .split() method to obtain the BGP peer IP address.

Print both local AS number and the BGP peer IP address to the screen."""

with open ("show_ip_bgp_summ.txt") as bgp_text:
	bgp_output = bgp_text.readlines()

bgp_output_first = bgp_output[0]
bgp_output_first = bgp_output_first.split(",")
bgp_output_first = bgp_output_first[1]

bgp_output_last = bgp_output[-1]
bgp_output_last = bgp_output_last.split()
bgp_output_last = bgp_output_last[0]

print(bgp_output_first)
print(bgp_output_last)