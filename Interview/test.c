#include <stdio.h>


#include <conio.h>



void main()

{
int number;
float average;
int counter=0;
float sum=0;

while(1)
{

printf("Enter number:%d:",counter);
scanf_s("%d",&number);
if (number==9999)
break;
else
sum=(sum+number);
counter++;

}
average=sum/counter;
printf("Average=:%d",average);
getch();

}