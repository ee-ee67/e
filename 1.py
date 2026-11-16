#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
int main(void)
{
    pid_t pid = fork();
    if (pid < 0)
    {
        perror("Fork failed");
        return 1;
    }
    else if (pid == 0)
    {
        // Child Process
        printf("\nChild Process\n");
        printf("Child PID : %d\n", (int)getpid());
        printf("Parent PID : %d\n", (int)getppid());
    }
    else
    {
        // Parent Process
        printf("\nParent Process\n");
        printf("Parent PID : %d\n", (int)getpid());
        printf("Child PID : %d\n", (int)pid);

        wait(NULL);
    }
    return 0;
}