running_config = open("show_run.txt")
show_version = running_config.read()

print(show_version)

running_config.close()

# The more proper way of doing this

with open ("show_run.txt") as running_config:
	show_version = running_config.read()
