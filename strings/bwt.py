

def build_bwt_matrix(text):
    matrix = []
    length = len(text)
    for i in xrange(length):
        matrix.append(text[i:] + text[:i])
    matrix.sort()
    return matrix


def bwt(text):
    matrix = build_bwt_matrix(text)
    result = [s[-1] for s in matrix]
    return ''.join(result)


def get_occurrence(text, index):
    result = 0
    symbol = text[index]
    for i in xrange(index + 1):
        curr_symbol = text[i]
        if curr_symbol == symbol:
            result += 1
    return result


def last_first_index(first_col, last_col, index):
    last_symbol = last_col[index]
    occurrence = get_occurrence(last_col, index)

    for curr_index, curr_symbol in enumerate(first_col):
        if curr_symbol == last_symbol:
            occurrence -= 1
            if occurrence == 0:
                return curr_index


def inverse_bwt(bwt_str):
    last_col = list(bwt_str)
    first_col = sorted(bwt_str)
    length = len(last_col)
    result = []
    curr_index = 0
    for i in xrange(length):
        result.append(first_col[curr_index])
        curr_index = last_first_index(first_col, last_col, curr_index)
    return ''.join(reversed(result))
