#include<stdio.h>
#include<stdlib.h>
#include<time.h>


int main() {
    int number, guess;
    char *secret = "Y3liZXJRdWVzdHt5MHVfNjA3XzE3LHIwMGsxMyFfN2JmMGE3NzM3Y2I3YTlmYTcxNWUyMWJlNWMzMTRjYzF9";
    srand(time(0));
    number = rand() % 10 + 1;

    printf("Welcome to the Guessing Game!\n");
    printf("I'm thinking of a number between 1 and 10.\n");

    printf("Guess a number between 1 and 10:");
    scanf("%d", &guess);
    if (guess == number) {
        printf("Correct! Here's a clue: The flag is hidden in this binary. Try using 'strings' with it.\n");
    } else {
        printf("Nope! Try again.\n\n");
    }
}