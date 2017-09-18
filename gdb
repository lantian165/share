################################################## 
# 
# Advance GDB Usage: 
# 
################################################## 

gcc -g a.c -o a

gdb 
file execute_file

# 1
help layout
# Show with assembly code and src code
layout split

# 2
#Show with Assembly code
help disassemble
With a /m modifier, source lines are included (if available).
With a /r modifier, raw instructions in hex are included.
disas start,end
disas start,length

disassemble /m
disas /m main

# 3
# Print the valus of Extended Stack Pointer
p $esp

# 4
# See where the function main starts and ends
(gdb) info line main
Line 4 of "a.c" starts at address 0x40052d <main> and ends at 0x40053c <main+15>.

# 5
# Search source file
forward-search regexp --> for regexp
search regexp
reverse-search regexp --> rev regexp

# 6 
# x 
Examine memory: x/FMT ADDRESS.
Format letters are o(octal), x(hex), d(decimal), u(unsigned decimal),
  t(binary), f(float), a(address), i(instruction), c(char) and s(string).

Example: Use "x/i" to see the instruction of specify address
p c (print the value of array c[20])
p &c (print the address of c)
x/10i 0x7fffffffde10 (Examin address)
x/15i main ( the number: 15 represen 15 lines to shown 

$pc: the current running address of program
x/10i $pc





################################################## 
# 
# Basic GDB Usage: 
# 
################################################## 
# 
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
