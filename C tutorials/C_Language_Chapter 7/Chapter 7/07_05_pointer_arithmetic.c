#include<stdio.h>

int main(){
    // int i = 34;
    // int *ptr = &i;
    // printf("The value of ptr is %u\n", ptr);       int stored 4 bytes in my computer not all computer because it depends on compiler computer to computer architecture
    // // ptr = ptr - 1;
    // ptr = ptr + 1;
    // // ptr++;
    // // ptr++;
    // printf("The value of ptr is %u\n", ptr);

    // char c = '3';
    // char *ptr = &c;
    // printf("The value of ptr is %u\n", ptr);
    // // ptr = ptr - 1;
    // ptr = ptr + 1;
    // ptr = ptr + 1;                                // char stored 1 byte
    // // ptr++;
    // // ptr++;
    // printf("The value of ptr is %u\n", ptr);

    float f = 3.4;
    float *ptr = &f;
    printf("The value of ptr is %u\n", ptr);
    // ptr = ptr - 1;
    ptr = ptr + 1;
    // ptr = ptr + 1;                              // float will stored 4 bytes
    // ptr++;
    // ptr++;
    printf("The value of ptr is %u\n", ptr);


    return 0;
}