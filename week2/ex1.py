"""Open the "show_version.txt" file for reading. Use the .read() method to read in the entire file contents to a variable. Print out the file contents to the screen. Also print out the type of the variable (you should have a string at this point).

Close the file.

Open the file a second time using a Python context manager (with statement). Read in the file contents using the .readlines() method. Print out the file contents to the screen. Also print out the type of the variable (you should have a list at this point)."""

cfg = open("show_run.txt")
config = cfg.read()

print(config)
print(type(config))

cfg.close()

with open ("show_run.txt") as cnfg:
	sh_cnfg = cnfg.readlines()

print(sh_cnfg)
print(type(sh_cnfg))