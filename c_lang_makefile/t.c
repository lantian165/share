#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

#include "./dir_t1/t1.h"
#include "./dir_t2/t2.h"
#include "./dir_t3/t3.h"

int main()
{
  //int large_list[100000000];

  //int a=1;

  int c[20], cnt=0;

  for( cnt=0;cnt < sizeof(c)/sizeof(int);cnt++)
  { 
     c[cnt]=cnt;
  }

  for( cnt=0;cnt < sizeof(c)/sizeof(int);cnt++)
  { 
     printf("the value of c[%d] is : %d\n", cnt, *(c+cnt));
  }

  // print 
 
  (void)print_hello_t1();
  (void)print_hello_t2();
  (void)print_hello_t3();
  
  //while ( 1 )
  //{
  //   a=getpid();
  //   printf("==============the pid is: [%d]==============\n", a);
  //}

  return 0;
}
