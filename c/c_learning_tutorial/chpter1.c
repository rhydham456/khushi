// #include <stdio.h>
// int main(int argc, char const *argv[])
// {
//     printf("twinkle twinkle little star\nhow are wonder what you are\nup above the world so high\n like a diamond in the sky\n");
//     return 0;
// }
// #include<stdio.h>
// int main(int argc, char const *argv[])
// {
//     for (int i == ';'i < 11; i++)
//     {
//         printf("5x%d==%'\'",i,5*i);
//     }

//     return 0;
// }

#include <stdio.h>
int main(int argc, char const *argv[])
{
    float firstNumber, secondNumber;
    char oper;
    printf("enter your first number");
    scanf("%f", &firstNumber);
    printf("enter your second number");
    scanf("%f", &secondNumber);
    printf("enter your operator");
    scanf("%c", &oper);
    if (oper == '+')
    {
        printf("the sum of %f and %f is %f", firstNumber, secondNumber, firstNumber + secondNumber);
    }
    else if (oper == '-')
    {
        printf("the difference of %f and %f is %f", firstNumber, secondNumber, firstNumber - secondNumber);
    }
    else if (oper == '*')
    {
        printf("the product of %f and %f is %f", firstNumber, secondNumber, firstNumber * secondNumber);
    }
    else if (oper == '/')
    {
        printf("the difference of %f and %f is %f", firstNumber, secondNumber, firstNumber / secondNumber);
    }

    return 0;
}
