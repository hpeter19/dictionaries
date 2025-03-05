#include<iostream>
#include<cmath>

using namespace std;

int main()
{
    float Number, squareroot;

    cout << "Enter a Number: ";
    cin >> Number; 

    // Check if the number is non-negative
    if (Number < 0) {
        cout << "Error: Cannot compute the square root of a negative number." << endl;
    } else {
        squareroot = sqrt(Number);
        cout << "The square root of " << Number << " is: " << squareroot << endl;
    }

    return 0;
}




}