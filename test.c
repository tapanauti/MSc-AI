#include <stdio.h>
#include <conio.h>

int main()
{
    int i;
    float exam,lab,assignment, sum=0, avg;
    printf("Enter Marks obtained in 3 Subjects: ");
    for(i=0; i<3; i++)
    {
        scanf("%f", &exam);
        scanf("%f", &lab);
        scanf("%f", &assignment);

 

        sum = sum+(exam*0.50+lab*0.25+assignment*0.25);
    }
    avg = sum/3*100;
    printf("\nMarks Grade");
    if(avg>=70 && avg<=100)
        printf("A");
    else if(avg>=60 && avg<69)
        printf("B");
    else if(avg>= 50 & avg<59)
        printf("C");
    else if(avg>=40 && avg<49)
        printf("D");
    else if(avg<40)
        printf("E");
    else
        printf("Invalid!");
    getch();
    return 0;

}