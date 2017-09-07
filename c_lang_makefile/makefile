CC=gcc
#CFLAGS=-Wall -std=gnu99
CFLAGS=-Wall -g

#目标文件
TARGET=t
SRCS = t.c \
       ./dir_t1/t1.c \
       ./dir_t2/t2.c \
       ./dir_t3/t3.c

INC = -I. -Idir_t1/ -Idir_t2/ -Idir_t3/

OBJS = $(SRCS:.c=.o)

$(TARGET):$(OBJS)
#@echo TARGET:$@
#@echo OBJECTS:$^
	$(CC) -o $@ $^

%.o:%.c
	$(CC) $(CFLAGS) $(INC) -c $< -o $@ 

clean:
	rm -rf $(TARGET) $(OBJS)
