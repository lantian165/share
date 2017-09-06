# Using -g to add debug info to the execute file
$gcc -g -o t t.c

# start gdb
$ gdb

# load execute file
$ (gdb) file t

# set break points to function main
$ (gdb) b main

# set break points to line 8
$ (gdb) b 8

# start the program
$ (gdb) r

# continue
$ (gdb) c

# run a line 
$ (gdb) s
or
$ (gdb) n

# print the value of var
$ (gdb) p str

# quit the gdb
$ (gdb) q

