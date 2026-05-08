// for execution 
// g++ hpc2.cpp -fopenmp -o hpc2
// ./hpc2

#include <bits/stdc++.h>
#include <omp.h>
using namespace std;

void bubbleSortSeq(vector<int> &arr)
{
    int n = arr.size();
    for (int i = 0; i < n - 1; i++)
    {
        for (int j = 0; j < n - i - 1; j++)
        {
            if (arr[j] > arr[j + 1])
                swap(arr[j], arr[j + 1]);
        }
    }
}
void bubbleSortPar(vector<int> &arr)
{
    int n = arr.size();
    for (int i = 0; i < n; i++)
    {
        #pragma omp parallel for
        for (int j = 0; j < n - 1; j += 2)
        {
            if (arr[j] > arr[j + 1])
                swap(arr[j], arr[j + 1]);
        }
        #pragma omp parallel for
        for (int j = 1; j < n - 1; j += 2)
        {
            if (arr[j] > arr[j + 1])
                swap(arr[j], arr[j + 1]);
        }
    }
}

void merge(vector<int> &arr, int l, int m, int r)
{
    vector<int> temp;
    int i = l, j = m + 1;
    while (i <= m && j <= r)
    {

        if (arr[i] < arr[j])
            temp.push_back(arr[i++]);
        else
            temp.push_back(arr[j++]);
    }
    while (i <= m)
        temp.push_back(arr[i++]);
    while (j <= r)
        temp.push_back(arr[j++]);
    for (int k = l; k <= r; k++)
        arr[k] = temp[k - l];
}
void mergeSortSeq(vector<int> &arr, int l, int r)
{
    if (l >= r)
        return;
    int m = (l + r) / 2;
    mergeSortSeq(arr, l, m);
    mergeSortSeq(arr, m + 1, r);
    merge(arr, l, m, r);
}
void mergeSortPar(vector<int> &arr, int l, int r)
{
    if (l >= r)
        return;
    int m = (l + r) / 2;
    #pragma omp parallel sections
    {
        #pragma omp section
        mergeSortPar(arr, l, m);
        #pragma omp section
        mergeSortPar(arr, m + 1, r);
    }
    merge(arr, l, m, r);
}


int main()
{
    int n;
    cout << "Enter number of elements: ";
    cin >> n;

    vector<int> arr(n);
    cout << "Enter elements:\n";
    for (int i = 0; i < n; i++)
        cin >> arr[i];
    vector<int> arr1 = arr, arr2 = arr, arr3 = arr, arr4 = arr;

    double start, end;
    start = omp_get_wtime();
    bubbleSortSeq(arr1);
    end = omp_get_wtime();
    cout << "\nSequential Bubble Sort Time: " << (end - start) << " sec";

    start = omp_get_wtime();
    bubbleSortPar(arr2);
    end = omp_get_wtime();
    cout << "\nParallel Bubble Sort Time: " << (end - start) << " sec";

    start = omp_get_wtime();
    mergeSortSeq(arr3, 0, n - 1);
    end = omp_get_wtime();
    cout << "\nSequential Merge Sort Time: " << (end - start) << " sec";

    start = omp_get_wtime();
    mergeSortPar(arr4, 0, n - 1);
    end = omp_get_wtime();
    cout << "\nParallel Merge Sort Time: " << (end - start) << " sec";

    cout << "\n\nSorted Array:\n";
    for (int x : arr4)
        cout << x << " ";
    cout << endl;
    return 0;
}



// Enter number of elements: 5
// Enter elements:
// 5 4 1 2 3

// Sequential Bubble Sort Time: 3.36004e-07 sec
// Parallel Bubble Sort Time: 0.0041331 sec
// Sequential Merge Sort Time: 6.16e-06 sec
// Parallel Merge Sort Time: 3.6746e-05 sec

// Sorted Array:
// 1 2 3 4 5 
