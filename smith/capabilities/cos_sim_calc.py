from __future__ import print_function


def cos_sim_calc(word1, word2):
    w1 = [ord(x) for x in word1]
    w2 = [ord(x) for x in word2]

    if len(w1) == len(w2):
        pass
    elif len(w1) < len(w2):
        for x in range(len(w2) - len(w1)):
            w1.append(0)
    elif len(w2) < len(w1):
        for x in range(len(w1) - len(w2)):
            w2.append(0)
    else:
        raise EOFError

    #ab_dot_prod = _get_dot_prod(w1,w2)
    #mag_w1 = _get_magnitude(w1)
    #mag_w2 = _get_magnitude(w2)
    return _get_dot_prod(w1,w2) / (_get_magnitude(w1) * _get_magnitude(w2))


def _get_dot_prod(one,two):
    prod = 0.00
    for x in range(len(one)):
        prod += (one[x] * two[x])
    return prod


def _get_magnitude(tmp):
    return (sum([x**2 for x in tmp]))**.5


if __name__ == '__main__':
    print(cos_sim_calc('somethingasdf','soemthingxxx'))
    print(cos_sim_calc('ant','not'))
