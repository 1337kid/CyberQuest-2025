#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void win() {
    FILE *fp = fopen("flag.txt", "r");
    if (fp == NULL) {
        perror("Error opening flag.txt");
        exit(1);
    }

    char flag[100];
    fgets(flag, sizeof(flag), fp);
    printf("%s\n", flag);
    fclose(fp);
}

int main() {
    setbuf(stdout, NULL);
    int whatIWant = 0xBAADF00D;
    char whatYouGot[45];

    printf("You got any burgers for me?\n");
    gets(whatYouGot);
    if(whatIWant == 0xBAADF00D) {
        printf("HAHAHA... I can eat %zu burgers all day long\n", strlen(whatYouGot));        
    } else {
        printf("Bruhh.. that's too much for meee..\nHere is your flag\n");
        win();
    }
    return 0;
}
