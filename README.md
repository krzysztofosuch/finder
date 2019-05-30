# finder
simple grep wrapper

1. ```finder() {
  command=`python ~/bin/finder.py $*`
  eval $command
}``` to .bashrc
2. "finder.py" to "~/bin"
3. usage: 
  `finder -grep "doctype" -name "*.html"`
