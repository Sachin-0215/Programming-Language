#include<stdio.h>
void goodMorning();
void goodAfternoon();
void goodNight();

int main(){
    goodMorning();
    return 0;
}

void goodMorning(){
    printf("Good Morning Sir\n");
    goodAfternoon();
}

void goodAfternoon(){
    printf("Good Afternoon Sir\n");
    goodNight();
}

void goodNight(){
    printf("Good Night Sir\n");
}