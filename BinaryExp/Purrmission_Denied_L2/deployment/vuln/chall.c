#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <openssl/sha.h>

void shell() {
    system("/bin/bash");
}

void to_hex_string(unsigned char *hash, char *output) {
    for (int i = 0; i < SHA256_DIGEST_LENGTH; i++) {
        sprintf(output + (i * 2), "%02x", hash[i]);
    }
    output[64] = '\0';
}

int main() {
    setbuf(stdout, NULL);
    unsigned char hash[SHA256_DIGEST_LENGTH];
    char hash_str[65];
    char password[65] = "78448ff2086a0d4ae279ba13b156cb8409f889288b6dfee347a0223656fc8abf";
    char input[100];

    printf("Why are you here? Kitty wants password\n");

    gets(input);

    SHA256((unsigned char *)input, strlen(input), hash);
    to_hex_string(hash, hash_str);
    
    if (strcmp(hash_str, password) == 0) {
        printf("Welcome home!\n");
        shell();
    } else {
        printf("You are lying. No access for you.\n");
    }

    return 0;
}
