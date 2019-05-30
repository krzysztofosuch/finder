# finder
simple grep wrapper

1. 

    finder() {
      set -f 
      command=\`python ~/bin/finder.py $*\`
      echo $command
      eval $command
      set +f 
    }
 to .bashrc
 
2. "finder.py" to "~/bin"


3. usage: 
  `finder -igrep "doctype" -name "*.html"` - looks for "doctype" phrase (case-insensitive) in .html files in current directory 
  `finder ~/ -iname "*.rb" -grep " < ApplicationRecord"` - looks for " < ApplicationRecord" phrase in all Ruby files (.rb, case insensitive) in home directory 
  `finder -name '*.json' -not "*backup*" -grep "foo"` - looks for "foo" phrase in all jsons except for files with "backup" in path (so "./backup/file.json" will be ommited, ./scr/test/backup.json" too)
  
"igrep" is case-insensitive "grep", "iname" is case-insensitive "name". 
