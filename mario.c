#include <cs50.h>
#include <stdio.h>

void pyramide (int n);

int main(void)
{
    // ask user for size between 1 and 8
int n;
do
{
    n = get_int("geef een hoogte in tussen 1 en 8: ");
}
while (n < 1 || n > 8 );
}

    // pyramide maken
void pyramide (int n)
{
    for (int i = 0; i < n; i++)
    {
        for ( int k = n - i - 2; k <= 0; k--)
    {
        printf(" ");
    }
    for(int j = 0; j < (i + 1); j++)
    {
        printf("#");
    }
    printf("\n");
    }
}