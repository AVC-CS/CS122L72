import random
def getRandom(N):
    """
    ########################################
    Code Your Program here
    ########################################
    """
    numbers = [random.randint(1, 100) for _ in range(N)]
    return numbers


def findMin(numbers):
    """
    ########################################
    Code Your Program here
    ########################################
    """
    minidx = numbers.index(min(numbers))
    numbers[0], numbers[minidx] = numbers[minidx], numbers[0]


def main():

    N = 5
    numbers = getRandom(N)
    print(f'The original list values : { numbers }')
    print('Finding the minimum value and swapping it with the first element...')
    findMin(numbers)
    print(f'The min value is now at the first index: { numbers[0] }')
    print(f'The list values after findMin() : { numbers }')


if __name__ == '__main__':
    main()
