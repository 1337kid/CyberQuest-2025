#include<stdio.h>
#include<stdlib.h>

void shell() {
    char cmd[]="/bin/bash";
    system(cmd);
}

int main() {
    int tmp = 1234;
    char text[20];
    printf("Why are you here?\n");
    gets(text);
    if(tmp == 5678) {
        printf("Welcome home!\n");
        shell();
    }
    else {
        printf("You are lying. No access for you.\n");
    }
    return 0;
}
