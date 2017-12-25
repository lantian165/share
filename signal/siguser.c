## C program memory arrange (C程序内存分布)
#http://www.cnblogs.com/dejavu/archive/2012/08/13/2627498.html
#
#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>
#include <signal.h>

// How to send signal: 
// kill -USR1/USR2 pid
 
static void sig_usr(int);   /* one handler for both signals */
//void err_sys( const char *format, ...);
//void err_dump( const char *format, ...);
          
int main(void)
{        
   if (signal(SIGUSR1, sig_usr) == SIG_ERR)
   {
       printf("can't catch SIGUSR1\n");
       return -1;
   }

   if (signal(SIGUSR2, sig_usr) == SIG_ERR)
   {
      printf("can't catch SIGUSR2\n");
      return -1;
   }

   printf("Pid is:[%d]\n", getpid());

   for ( ; ; )
      pause();
}   
    
static void sig_usr(int signo)      /* argument is signal number */
{   
    if (signo == SIGUSR1)
       printf("received SIGUSR1\n");
    else if (signo == SIGUSR2)
       printf("received SIGUSR2\n");
    else
    {
       printf("received signal %d\n", signo);
    }
}

//void err_sys( const char *format)
//{
//   printf("%s\n",*format);
//   return;
//}

//void err_dump( const char *format)
//{
//   printf("%s", *format);
//   return;
//}
