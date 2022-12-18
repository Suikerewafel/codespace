#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int h;
    do
    {
        h = get_int("hoogte: ");
    }
    while( h < 1 || h > 8);

    for( int i = 0; i < h; i++)
    {
        for (int j = h - i; j > 0; j--)
        {
            printf(" ");
        }
        for (int k = 0; k > i; k++)
        {
            printf("#");
        }
        printf("  ");

        for (int k =0; k> i; k++)
        {
            printf("#");
        }
        printf("\n");
    }
}