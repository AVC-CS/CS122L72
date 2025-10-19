import main
import pytest

@pytest.mark.basic
def test_main_1():
    N = 5
    numbers = main.getRandom(N)

    minval = min(numbers)
    minidx = numbers.index(minval)
    firstelm = numbers[0]

    print(f'The original list values {numbers}')
    main.findMin(numbers)
    print(f'Min val: {numbers[0]}, Swapped with {numbers[minidx]}')
    print(f'The list values  after findMin() {numbers}')

    assert numbers[0] == minval
    assert numbers[minidx] == firstelm

@pytest.mark.edge
def test_main_2():
    N = 10
    numbers = main.getRandom(N)

    minval = min(numbers)
    minidx = numbers.index(minval)
    firstelm = numbers[0]

    print(f'The original list values {numbers}')
    main.findMin(numbers)
    print(f'Min val: {numbers[0]}, Swapped with {numbers[minidx]}')
    print(f'The list values  after findMin() {numbers}')

    assert numbers[0] == minval
    assert numbers[minidx] == firstelm

@pytest.mark.bonus
def test_main_3():
    
    N = 1
    numbers = main.getRandom(N)

    minval = min(numbers)
    minidx = numbers.index(minval)
    firstelm = numbers[0]

    print(f'The original list values {numbers}')
    main.findMin(numbers)
    print(f'Min val: {numbers[0]}, Swapped with {numbers[minidx]}')
    print(f'The list values  after findMin() {numbers}')

    assert numbers[0] == minval
    assert numbers[minidx] == firstelm