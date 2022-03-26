#
# Complete the 'aVeryBigSum' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER_ARRAY ar as parameter.
#

def aVeryBigSum(ar):
    sum_value = 0
    for i in range(0, len(ar)):
        if ar[i] <= 10 ** 10:
            sum_value += ar[i]
        else:
            sum_value = "Invalid Input"
            break
    print(sum_value)       

if __name__ == '__main__':
    ar_count = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    if ar_count <= 10:
        result = aVeryBigSum(ar)