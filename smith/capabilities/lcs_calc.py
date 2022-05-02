import pdb
WEIGHT = 1


def _pr(m):
    for x in m:
        print(x)


def lcs_calc(word1, word2):
    xs = word1; ys = word2
    tmp = [[0 for x in range(len(xs) + 1)] for x in range(len(ys) + 1)]
    for yinc in range(1, len(ys) + 1):
        for xinc in range(1, len(xs) + 1):
            if ys[yinc - 1] == xs[xinc - 1]:
                tmp[yinc][xinc] = tmp[yinc - 1][xinc - 1] + WEIGHT
            else:
                tmp[yinc][xinc] = max(tmp[yinc][xinc - 1],tmp[yinc - 1][xinc])
    #_pr(tmp)
    return tmp[-1][-1]
