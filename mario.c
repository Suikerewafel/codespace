#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // ask user for size



    // reprompt when not between 1-8
   do
   {
    int n = get_int("Hoogte: ")
   }
   while (n => 8)

    //print de hoogte
    for(int i = 0; i < n; i++)
    {
    //print de breedte
        for(int j = 0; j < n; j++)
        {
        printf("#");
        }
    printf("\n");
    }
}