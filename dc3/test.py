HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

from dc3 import DC3

file = open("./data/bible.txt")
s = file.read()
print(s)
algorithm = DC3(s)
p = input("Pattern:")

while (p != ""):
    positions = algorithm.search(p)
    if len(positions) == 0:
        print("Pattern not found!")
    else:
        for i in positions:
            print("["+str(i)+"]  "+s[i-80:i]+OKGREEN+s[i:i+len(p)]+ENDC+s[i+len(p):i+len(p)+80])
    p = input("Pattern:")