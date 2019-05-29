import sys

args = sys.argv
args.pop(0)

parsed = {
    "dir": [],
    "not": [
        "*node_modules*", "*vendor*", "*lib*", "*bower_components*", "*site-packages*"
    ],
    "name": [],
    "iname": [],
    "grep": []
}
mode = "dir"
specials = {
    "fgrep" : False
}
while args:
    arg = args.pop(0)
    if arg.startswith('-'):
        arg = arg[1:]
        if arg in parsed:
            mode = arg
        if arg in specials:
            specials[arg] = True
    else:
        if mode in parsed:
            parsed[mode].append(arg)

cmd = [
    "find -L "
]
if not parsed["dir"]:
    parsed["dir"].append(".")

for d in parsed["dir"]:
    cmd.append(d)

cmd.append("-type f")
for n in parsed["not"]:
    cmd.append("-not -wholename '%s'"%(n))

for n in parsed["iname"]:
    cmd.append("-iname '%s'"%(n))

for n in parsed["name"]:
    cmd.append("-name '%s'"%(n))

if parsed["grep"]:
    cmd.append('-exec grep -ni "%s" {} /dev/null \;'%("|".join(parsed["grep"])))

print(" ".join(cmd))
