import sys

args = sys.argv
args.pop(0)

parsed = {
    "dir": [],
    "not": [
        "*node_modules*", "*vendor*", "*lib*", "*bower_components*", "*site-packages*" , "*build*", "*venv*", "*.swp", "*.pyc", "*.git*" 
    ],
    "name": [],
    "iname": [],
    "grep": [],
    "igrep": []
}
mode = "iname" 
specials = {
    "fgrep" : False
}
if '--all' in args:
    parsed['not'] = []
    args.remove('--all')
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
    cmd.append("-and -not -wholename '%s'"%(n))
cmd.append("-and")

iname = []
for n in parsed["iname"]: 
    iname.append("-iname '%s'"%(n))
if iname: 
    cmd.append("\( " +  (" -or ".join(iname)) + ' \)') 

name = []
for n in parsed["name"]: 
    name.append("-name '%s'"%(n))
if name: 
    cmd.append("\( " +  (" -or ".join(name)) + " \)") 

if parsed["igrep"]:
    cmd.append('-exec grep --color -ni "%s" {} /dev/null \;'%(" ".join(parsed["igrep"])))
else: 
    if parsed["grep"]:
        cmd.append('-exec grep --color -n "%s" {} /dev/null \;'%(" ".join(parsed["grep"])))

print(" ".join(cmd))
