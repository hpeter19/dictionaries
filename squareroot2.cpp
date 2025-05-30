//The fibonacci function is a recursive function that calculates the nth Fibonacci number:
//Base case: If n == 0 or n == 1, it returns n because the 0th Fibonacci number is 0, and the 1st Fibonacci number is 1.
//Recursive case: For values of n > 1, it calls the function recursively to compute fibonacci(n - 1) + fibonacci(n - 2).
//The main function asks the user how many terms of the Fibonacci sequence they want to print, and then it prints the sequence up to that number of terms.


#include<iostream>
using namespace std;

// Function to calculate the nth Fibonacci number using recursion
int fibonacci(int n) {
    // Base case: if n is 0 or 1, return n (since 0! = 0, and 1! = 1)
    if (n <= 1) {
        return n;
    }
    // Recursive case: Fibonacci of n is the sum of Fibonacci of (n-1) and Fibonacci of (n-2)
    else {
        return fibonacci(n - 1) + fibonacci(n - 2);
    }
}

int main() {
    int num;
    
    cout << "Enter the number of terms in Fibonacci sequence: ";
    cin >> num;

    cout << "Fibonacci sequence up to " << num << " terms is: ";

    // Generate Fibonacci sequence up to num terms
    for (int i = 0; i < num; i++) {
        cout << fibonacci(i) << " ";
    }

    cout << endl;

    return 0;
}
