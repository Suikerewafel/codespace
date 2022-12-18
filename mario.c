#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // ask user for size

int n = get_int("Hoogte: ");

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