# finder
simple grep wrapper

1. ```

finder() {
  set -f 
  command=`python ~/bin/finder.py $*`
  echo $command
  eval $command
  set +f 
}
``` to .bashrc
2. "finder.py" to "~/bin"
3. usage: 
  `finder -grep "doctype" -name "*.html"`
