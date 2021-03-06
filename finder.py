import sys

args = sys.argv
args.pop(0)
verbose = False
parsed = {
    "dir": [],
    "not": [
        "*node_modules/*", "*vendor/*", "*lib*", "*bower_components/*", "*site-packages/*" , "*build/*", "*venv/*", "*.swp", "*.pyc", "*.git*", "*dist/*", "*.cache/*", "*.log", "*/tmp/*", "*frontend/de*"
    ],
    "name": [],
    "iname": [],
    "grep": [],
    "igrep": [],
    "A": None, 
    "B": None
}
mode = "iname" 
specials = {
    "fgrep" : False
}
if '--all' in args:
    parsed['not'] = []
    args.remove('--all')
if '--v' in args:
    verbose = True
    args.remove('--v')
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
            if isinstance(parsed[mode],list):
                parsed[mode].append(arg)
            else:
                parsed[mode] = arg

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

grep_params = []
if parsed['A']:
    grep_params.append('-A%s'%(parsed['A']))
if parsed['B']:
    grep_params.append('-B%s'%(parsed['B']))

if parsed["igrep"]:
    grep_params.append('-i')
    parsed['grep'] = parsed['igrep']
    del parsed['igrep']

if parsed["grep"]:
    cmd.append('-exec grep --color=always %s -n "%s" {} /dev/null \;'%(" ".join(grep_params), " ".join(parsed["grep"])))

print(" ".join(cmd))
