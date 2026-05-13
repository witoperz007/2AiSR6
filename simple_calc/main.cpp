#include <cstring>
#include <stdio.h>
#include <stdlib.h>
#include <iostream>
void usage(char *program_name) {
    printf("Usage: %s number1 operation number2\n",program_name);
    printf("Available operations:\n");
    printf("\tadd\n");
    printf("\n");
}
int main(int argc, char* argv[]) {

    int number1=0;
    int number2=0;
    int result=0;

    if (argc== 4) {
        number1 = atoi(argv[1]);
        number2 = atoi(argv[3]);

        if (!strcmp("add",argv[2])) {
            result=number1+number2;
            printf("%d + %d= %d\n",number1,number2,result);

        }
        else if (!strcmp("sub",argv[2])) {
            result=number1-number2;
            printf("%d - %d= %d\n",number1,number2,result);
        }
        else if (!strcmp("mul",argv[2])) {
            result=number1*number2;
            printf("%d * %d= %d\n",number1,number2,result);

        }
        else if (!strcmp("div",argv[2])) {
            result=number1/number2;
            printf("%d / %d= %d\n",number1,number2,result);

        }
        else if (!strcmp("mod",argv[2])) {
            result=number1%number2;
            printf("%d %% %d= %d\n",number1,number2,result);
        }

    }




    return 0;
}
