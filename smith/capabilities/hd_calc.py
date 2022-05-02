from __future__ import print_function

def hd_calc(word1, word2):
    w1 = [x for x in word1]
    w2 = [x for x in word2]
    count = 0
    if len(w1) == len(w2):
        pass
    elif len(w1) < len(w2):
        for x in range(len(w2) - len(w1)):
            w1.append(None)
    elif len(w2) < len(w1):
        for x in range(len(w1) - len(w2)):
            w2.append(None)
    else:
        raise EOFError

    for x in range(len(w1)):
        if not w1[x] == w2[x]:
            count += 1
    return count



if __name__ == '__main__':
    print(hd_calc('something','soemthign'))
    print(hd_calc('something', 'something'))

