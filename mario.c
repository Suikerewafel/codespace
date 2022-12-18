#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // ask user for size between 1 and 8
int n;
do
{
    n = get_int("geef een hoogte in tussen 1 en 8: ");
}
while (n < 1 || n > 8 );

    // pyramide maken
for (int i = 0; i < n; i++)
{
    printf("#");
}
}