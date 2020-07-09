import sys

# first argument is always the full path to the script file
print("number of cli args: " + str(len(sys.argv) - 1))

for arg in sys.argv:
    print(arg)

var1 = sys.argv[1]
var2 = sys.argv[2]
