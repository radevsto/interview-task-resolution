# The given task

```
Given an unsorted array A[]. The task is to print all unique pairs in the unsorted array with equal sum.

Note: Print the result in the format as shown in the below examples.

Examples:

Input: A[] = { 6, 4, 12, 10, 22, 54, 32, 42, 21, 11}

Output:

Pairs : ( 4, 12) ( 6, 10) have sum : 16

Pairs : ( 10, 22) ( 21, 11) have sum : 32

Pairs : ( 12, 21) ( 22, 11) have sum : 33

Pairs : ( 22, 21) ( 32, 11) have sum : 43

Pairs : ( 32, 21) ( 42, 11) have sum : 53

Pairs : ( 12, 42) ( 22, 32) have sum : 54

Pairs : ( 10, 54) ( 22, 42) have sum : 64

Input:A[]= { 4, 23, 65, 67, 24, 12, 86}

Output:

Pairs : ( 4, 86) ( 23, 67) have sum : 90
```

# Solution 1

Using built in data structures.

## Usage

```
> python equal_sum_collector.py --help              
usage: equal_sum_collector.py [-h] numbers [numbers ...]

Find unique pairs with equal sums in an array.

positional arguments:
  numbers     List of integers in the array, separated by spaces

options:
  -h, --help  show this help message and exit
```

## Example
```
> python equal_sum_collector.py 2 3 5 12 18 7 4 17 9        
Input: A[] = [2, 3, 5, 12, 18, 7, 4, 17, 9]
Pairs : ( 2, 5 ) ( 3, 4 ) have sum : 7
Pairs : ( 2, 12 ) ( 5, 9 ) have sum : 14
Pairs : ( 2, 18 ) ( 3, 17 ) have sum : 20
Pairs : ( 2, 7 ) ( 5, 4 ) have sum : 9
Pairs : ( 2, 17 ) ( 12, 7 ) have sum : 19
Pairs : ( 2, 9 ) ( 7, 4 ) have sum : 11
Pairs : ( 3, 18 ) ( 12, 9 ) ( 4, 17 ) have sum : 21
Pairs : ( 3, 9 ) ( 5, 7 ) have sum : 12
Pairs : ( 5, 17 ) ( 18, 4 ) have sum : 22
Pairs : ( 12, 4 ) ( 7, 9 ) have sum : 16
```

# Solution 2

Using numpy array.

## Usage

```
> python equal_sum_collector_with_numpy.py --help                                   
usage: equal_sum_collector_with_numpy.py [-h] numbers [numbers ...]                                                                                      
                                                                                                                                                         
Find unique pairs with equal sums in a numpy array.                                                                                                      

positional arguments:
  numbers     List of integers in the array, separated by spaces

options:
  -h, --help  show this help message and exit
```

## Example
```
> python equal_sum_collector_with_numpy.py 2 3 5 12 18 7 4 17 9
Input: A[] = [2, 3, 5, 12, 18, 7, 4, 17, 9]
Pairs : ( 2, 5 ) ( 3, 4 ) have sum : 7
Pairs : ( 2, 12 ) ( 5, 9 ) have sum : 14
Pairs : ( 2, 18 ) ( 3, 17 ) have sum : 20
Pairs : ( 2, 7 ) ( 5, 4 ) have sum : 9
Pairs : ( 2, 17 ) ( 12, 7 ) have sum : 19
Pairs : ( 2, 9 ) ( 7, 4 ) have sum : 11
Pairs : ( 3, 18 ) ( 12, 9 ) ( 4, 17 ) have sum : 21
Pairs : ( 3, 9 ) ( 5, 7 ) have sum : 12
Pairs : ( 5, 17 ) ( 18, 4 ) have sum : 22
Pairs : ( 12, 4 ) ( 7, 9 ) have sum : 16
```

# Testing

```
> pytest.exe --cov=.    
=============================================================================================== test session starts ===============================================================================================
platform win32 -- Python 3.12.8, pytest-7.4.4, pluggy-1.5.0
rootdir: C:\Users\Stoyan Radev\Desktop\interview-task-resolution
plugins: cov-6.0.0, django-4.10.0
collected 4 items                                                                                                                                                                                                  

tests\test_equal_sum_collector.py ..                                                                                                                                                                         [ 50%] 
tests\test_equal_sum_collector_with_numpy.py ..                                                                                                                                                              [100%]

---------- coverage: platform win32, python 3.12.8-final-0 -----------
Name                                           Stmts   Miss  Cover
------------------------------------------------------------------
__init__.py                                        0      0   100%
equal_sum_collector.py                            22      6    73%
equal_sum_collector_with_numpy.py                 24      7    71%
tests\test_equal_sum_collector.py                 19      0   100%
tests\test_equal_sum_collector_with_numpy.py      20      0   100%
------------------------------------------------------------------
TOTAL                                             85     13    85%


================================================================================================ 4 passed in 0.33s ================================================================================================ 
>
```

# Code standards and formatting
> No particular configuration has been added, just default behavior and 100 symbols line length

## flake8
```
> flake8 --max-line-length=100 .
>
```

## black
```
> black --check .
All done! ✨ 🍰 ✨
5 files would be left unchanged.
```