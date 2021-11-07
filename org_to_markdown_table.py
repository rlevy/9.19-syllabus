import sys, re

p = re.compile(r"^(.*?)\[\[([^\]]*)\]\[([^\]]*)\]\](.*)$")
for line in sys.stdin.readlines():
    line = line.rstrip()
    if re.match("^[0-9|<> ]*$",line) and re.match(".*\|.*",line):
        continue
    stillSearchingLine = True
    while stillSearchingLine:
        m = p.match(line)
        if m == None:
            stillSearchingLine = False
            continue
        line = m.group(1) + "[" + m.group(3) + "](" + m.group(2) + ")" + m.group(4)
    print(line)
        
