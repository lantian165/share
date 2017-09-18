CC=gcc
#CFLAGS=-Wall -std=gnu99
CFLAGS=-Wall -g

#目标文件
TARGET=siguser
SRCS = siguser.c 

INC = -I. 

OBJS = $(SRCS:.c=.o)

$(TARGET):$(OBJS)
#@echo TARGET:$@
#@echo OBJECTS:$^
	$(CC) -o $@ $^

%.o:%.c
	$(CC) $(CFLAGS) $(INC) -c $< -o $@ 

clean:
	rm -rf $(TARGET) $(OBJS)
