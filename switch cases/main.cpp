#include <iostream>
#include <cstdio>
#include <time.h>
#define  SIZE 10
FILE * fptr;


void copy_array(int source[], int destination[], int size) {
    for (int i = 0; i < size; i++) {
        destination[i] = source[i];

    }
}

void copy_to_file(const char *file, int *numbers, int size) {
    FILE *fptr = fopen(file, "w");

    if (fptr == NULL) {
        printf("Error: Could not save to %s\n", file);
        return;
    }
    for (int i = 0; i < size; i++) {
        fprintf(fptr, "%d\n", numbers[i]);
    }
    fclose(fptr);
}
void restore_array(const char *file, int *numbers, int size) {
    FILE *fptr = fopen(file, "r");
    if (fptr == NULL) {
        printf("No snapshot found in %s!\n", file);
        return;
    }
    for (int i = 0; i < size; i++) {
        if (fscanf(fptr, "%d", &numbers[i]) != 1) break;
    }
    fclose(fptr);
}
void save_snapshot(const char *file, int *numbers, int size) {
    copy_to_file(file, numbers, size);
    time_t now = time(NULL);
    struct tm *tm_info = localtime(&now);
    FILE *info = fopen("snapshot_time.txt", "w");
    if (info) {
        fprintf(info, "%02d.%02d.%04d %02d:%02d:%02d",
                tm_info->tm_mday,
                tm_info->tm_mon + 1,
                tm_info->tm_year + 1900,
                tm_info->tm_hour,
                tm_info->tm_min,
                tm_info->tm_sec);
        fclose(info);
    }
}


// void copy_to_file(FILE *fptr,int *numbers,int size) {
//     fptr = fopen("array.txt", "w");
//     if (fptr == 0)
//     {
//         printf("Error with opening data.\n");
//         exit(1);
//     }
//     fseek(fptr,0,SEEK_SET);
//     for (int i = 0; i < size; i++) {
//         fprintf(fptr, "%d \n", numbers[i]);
//     }
//     fflush(fptr);
//     fclose(fptr);
// }
// void restore_array(FILE *fptr,int *numbers,int size) {
//     fptr = fopen("array.txt", "w");
//     if (fptr == 0)
//     {
//         printf("Error with opening data.\n");
//         exit(1);
//     }
//     for (int i = 0; i < size; i++) {
//         if (fscanf(fptr,"%d",&numbers[i]) != 1) {
//             printf("Error with reading data.\n");
//             exit(2);
//         }
//     }
    // fseek(fptr,0,SEEK_SET);
    // for (int i = 0; i < size; i++) {
    //     fscanf(fptr,"%d", &numbers[i]);
    // }
//     fclose(fptr);
// }

void Array_print(int *numbers,int size) {

    for (int i = 0; i < size; i++) {
        printf("number[%d]=%d\n",i,*(numbers+i));
    }

}
int max_array(int *numbers,int size) {
    int max = *numbers;
    for (int i = 0; i < size; i++) {
        if  (max < *(numbers+i )) {
            max = *(numbers+i );
        }
    }return max;
}
int min_array(int *numbers,int size) {

    int min = *numbers;
    for (int i = 0; i < size; i++) {
        if (min > *(numbers+i)) {
            min = *(numbers+i);
        }
    }return min;
}
int sum(int *numbers,int size) {
    int sum=0;
    for (int i = 0; i < size; i++) {
        sum += *(numbers+i);
    }return sum;
}
float average(int *numbers,int size) {

    float avg = (float)sum(numbers,size)/size;
    return avg;

}



void sort_array(int *arr, int size) {
    for (int i = 0; i < size - 1; i++) {
        for (int j = 0; j < size - i - 1; j++) {
            if (arr[j] > arr[j+1]) {
                int temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
        }
    }
}


double median(int *numbers, int size) {
    save_snapshot("snapshot.txt",numbers,SIZE);
    int temp_array[size];
    copy_array(numbers,temp_array,size);
    sort_array(temp_array,size);
    double median;
    if (size % 2 != 0) {
        median = (double)temp_array[size / 2];
        printf("median=%.2f\n", median);
    }else {


        median = (temp_array[size / 2 - 1] + temp_array[size / 2]) / 2.0;
        printf("median=%.2f\n", median);
    }
    return median;
}



void menu(){
    printf("\nMenu\n");
    printf("Type 1. to show numbers\n");
    printf("Type 2. to show max numbers\n");
    printf("Type 3. to show min number\n");
    printf("Type 4. to show sum number\n");
    printf("Type 5 to show average number\n");
    printf("Type 6 to show median number\n");
    printf("Type 7 to copy array\n");
    printf("Type 8 to restore array\n");
    printf("Type 9 to make snapshot\n");
    printf("Type 10 to restore snapshot\n");
    printf("Type 11 to restore to default\n");
    printf("Type 0 to exit\n");
}

int main() {


    int numbers[SIZE] = {1, 2, 3, 40, -5, 6, 7, 8, 9, 10};
    copy_to_file("defualt.txt",numbers,SIZE);
    int option;
    do {
        menu();
        scanf("%d",&option);
        switch (option) {
            case 1:
                Array_print(numbers,SIZE);
                break;
            case 2:
                printf("max=%d\n", max_array(numbers,SIZE));
                break;
            case 3:
                printf("min=%d\n", min_array(numbers,SIZE));
                break;
            case 4:
                printf("sum=%d\n", sum(numbers,SIZE));
                break;
            case 5:
                printf("average=%.2f\n", average(numbers,SIZE));
                break;
            case 6:
                save_snapshot("snapshot.txt",numbers,SIZE);
                printf("median=%.2f\n", median(numbers,SIZE));
                break;
            case 7:
                copy_to_file("array.txt",numbers,SIZE);
                printf("Array copied\n");
                break;
            case 8:
                printf("Restoring from the file\n");
                restore_array("array.txt",numbers,SIZE);
                break;
            case 9:
                printf("saving snapshot\n");
                save_snapshot("snapshot.txt",numbers,SIZE);
                break;
            case 10:
                printf("Loading snapshot\n");
                restore_array("snapshot.txt",numbers,SIZE);
                break;
            case 11:
                printf("Restoring to default\n");
                restore_array("default.txt",numbers,SIZE);
            case 0:
                printf("Goodbye!\n");
                break;


        }if (option >11 || option < 0) {
            printf("Type correct number...\n");
        }


    }
    while (option != 0);

}

