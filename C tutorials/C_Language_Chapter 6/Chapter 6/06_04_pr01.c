// WAP to print the address of a varibale. Use this address to get the value of the variable

#include<stdio.h>

int main(){
    int a=6;
    int *ptr;
    ptr = &a;
    printf("The value of variable a is %d\n", a);
    printf("The address of variable a is %u\n", ptr);
    printf("The value of variable a is %d\n", *ptr);
    printf("The address of variable a is %u\n", &a);

    return 0;
}