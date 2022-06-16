"""Create a list of five IP addresses.

Use the .append() method to add an IP address onto the end of the list. Use the .extend() method to add two more IP addresses to the end of the list.

Use list concatenation to add two more IP addresses to the end of the list.

Print out the entire list of ip addresses. Print out the first IP address in the list. Print out the last IP address in the list.

Using the .pop() method to remove the first IP address in the list and the last IP address in the list.

Update the new first IP address in the list to be '2.2.2.2'. Print out the new first IP address in the list."""

ip_addresses = ["10.0.0.1", "10.0.1.2", "10.0.0.3", "172.16.0.1", "172.16.1.2"]

ip_addresses.append("172.16.100.1")


print(ip_addresses)
print(f"{ip_addresses[0]}")
print(f"{ip_addresses[-1]}")