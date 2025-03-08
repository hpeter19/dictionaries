#include<iostream>
using namespace std;
//git
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
