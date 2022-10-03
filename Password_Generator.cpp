//main concept: making a random selector function and an aaray .Will iterate in that for randomly selecting the characters.
#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;
//made an array of all characters that will be used in random password generator.
static const char alphabets[] = "0123456789"
                              "!@#$%^&*"
                              "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                              "abcdefghijklmnopqrstuvwxyz";
int strLen = sizeof(alphabets) - 1;

char GenRand()
//function for randomly generating any character from the array.
{
    return alphabets[rand() % strLen];
}
int main()
{
    int n, c = 0, s = 0;
    srand(time(0));
    //taking input from thee user of the length of password required 
    cout << "Enter the length of the password required:";
    cin >> n;
    cout << n << endl;
    cout << "Your Password is:";
N:
    char C;

    string D;

    for (int z = 0; z < n; z++)
    {
        //calling the function for randomly selceting a digit or character
        C = GenRand();
        D += C;
        //checking if the element is a digit or not
        if (isdigit(C))

        {
            c++;
            //first counter increment
        }
        if (C == '!' || C == '@' || C == '$' || C == '%' || C == '^' || C == '&' || C == '*' || C == '#')
        {
            s++;
            //second counter inncrement
        }
    }
    if (n > 2 && (s == 0 || c == 0))
    //checking if the passord generated is valid or not 
    {
        goto N;
    }
    cout << D;
    //printing the password
    return 0;
}
