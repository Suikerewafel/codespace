#include <cs50.h>
#include <stdio.h>
#include <math.h>

int main(void)
{
    float cash;
    do
    {
        cash = get_float("change owed: ");
    }
    while(cash < 0);

    int cents = round(cash * 100);

    if(cents >= 25)
}


