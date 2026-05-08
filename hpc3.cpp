// for execution 
// g++ hpc3.cpp -fopenmp -o hpc3
// ./hpc3

#include <iostream>
#include <vector>
#include <omp.h>
#include <climits>
using namespace std;
int main()
{
    int n;
    cout << "Enter number of elements: ";
    cin >> n;
    vector<int> arr(n);
    cout << "Enter elements:\n";
    for (int i = 0; i < n; i++)
        cin >> arr[i];
    int sum = 0;
    int min_val = INT_MAX;
    int max_val = INT_MIN;
    double start, end;
    start = omp_get_wtime();
    #pragma omp parallel for reduction(+ : sum) reduction(min : min_val) reduction(max : max_val)
    for (int i = 0; i < n; i++)
    {
        sum += arr[i];
        if (arr[i] < min_val)
            min_val = arr[i];
        if (arr[i] > max_val)
            max_val = arr[i];
    }
    end = omp_get_wtime();
    double avg = (double)sum / n;

    cout << "\nSum = " << sum;
    cout << "\nMinimum = " << min_val;
    cout << "\nMaximum = " << max_val;
    cout << "\nAverage = " << avg;
    cout << "\nExecution Time = " << (end - start) << " sec\n";
    return 0;
}

// Enter number of elements: 5
// Enter elements:
// 10
// 30
// 51
// 5
// 89

// Sum = 185
// Minimum = 5
// Maximum = 89
// Average = 37
// Execution Time = 0.00211347 sec
