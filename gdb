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
$ (gdb) s (steping into)
or
$ (gdb) n (steping over)

# print the value of var
$ (gdb) p str

# quit the gdb
$ (gdb) q

# change var value when running
$ (gdb) print var=value

# Get me 15 minutes & I'll change your view of GDB
# Command: what it will do
$ start: start running
$ list:  list the source code
$ backtrace(=bt): list the stack info
$ frame num: show the stack detail
#
# Graphy Mode:
$ gdb -tui or Ctrl+X+A
$ Ctrl+X+(Right small numbric key: 1 or 2 ): Separate screen to 2 part

# gdb Core file
$ gdb -c core_file_name
$ (gdb) bt

# break points, and commands:
$commands [range...]

... command-list ...

end
# Example:
break foo if x>0
commands       //指令集设置命令
silent         //断点触发时不打印断点信息
printf "x is %d\n",x
cont
end            //指令集设置结束时必须用end结束
