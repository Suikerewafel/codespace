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
        for (int j= h - i; j = h; j++)
        {
            printf("#");
        }
        printf("\n");
    }
}