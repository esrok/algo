

def pseudo_polynomial_subset(numbers, target_sum=0):
    n = len(numbers)

    if n == 0:
        return False

    min_sum = sum([number for number in numbers if number < 0])
    max_sum = sum([number for number in numbers if number > 0])

    answer = {}

    # constructing [min_sum, max_sum] X (n + 1) matrix
    for i in xrange(min_sum, max_sum + 1):
        answer[i] = [False] * (n + 1)

    # with one number only one sum can be made
    answer[numbers[0]][1] = True

    for index, number in enumerate(numbers):
        for i in xrange(min_sum, max_sum + 1):
            result = False
            if answer[i][index - 1]:
                # sum was already made with previous item set
                result = True
            elif number == i:
                # sum can be made with current number
                result = True
            elif min_sum <= i - number <= max_sum:
                if answer[i - number][index - 1]:
                    # sum can be made with addition of number
                    # to some previous sum
                    result = True
            if result:
                answer[i][index] = True
                if i == target_sum:
                    return True
    return False
