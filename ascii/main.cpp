#include <stdio.h>
#include <string.h>

void to_lowercase(char *str) {
    while (*str) {
        if ('A' <= *str && *str <= 'Z') {
            *str += ('a' - 'A');
        }
        str++;
    }
}

void to_uppercase(char *str) {
    while (*str) {
        if ('a' <= *str && *str <= 'z') {
            *str += ('A' - 'a');
        }
        str++;
    }
}

int size_text(char *str) {
    int size = 0;
    while (*str) {
        size++;
        str++;
    }
    return size;
}




void usage(char *program_name) {
    printf("Usage: %s string\n", program_name);
}

int main(int argc, char* argv[]) {
    char str[80];

    if (argc != 2) {
        usage(argv[0]);
        return 1;
    }

    strcpy(str, argv[1]);


    printf("%s\n", str);

    to_lowercase(str);
    printf("%s\n", str);

    to_uppercase(str);
    printf("%s\n", str);

    printf("text size=%d\n", size_text(str));

    return 0;
}
