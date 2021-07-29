#include<stdio.h>
int sum (int a, int b);
int main(){
    int a=4, b=7;
    printf("The value of x and y is %d and %d\n", a,b);
    printf("The value of 4+7 is %d\n", sum(a, b));
    printf("The value of x and y after function call is %d and %d\n", a, b);
    return 0;
}
int sum (int a, int b){
    int c;
    c = a + b;
    b =3434,a = 23432;   // No Change with changing the value of a and b kyuki function k value se main function ki value change nai kar sakte.
    return c;
}