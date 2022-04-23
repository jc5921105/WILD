INS_WEIGHT = 1
DEL_WEIGHT = 1
SUB_WEIGHT = 1

def med_calc(word1, word2):
    xs = word1; ys = word2
    tmp = [[0 for x in range(len(xs) + 1)] for x in range(len(ys) + 1)]
    for x in range(len(xs) + 1): tmp[0][x] = x
    for y in range(len(ys) + 1): tmp[y][0] = y
    for yinc in range(1, len(ys) + 1):
        for xinc in range(1, len(xs) + 1):
            if ys[yinc - 1] == xs[xinc - 1]:
                tmp[yinc][xinc] = tmp[yinc - 1][xinc - 1]
            else:
                delete = tmp[yinc - 1][xinc]
                insert = tmp[yinc][xinc - 1]
                sub = tmp[yinc - 1][xinc - 1]
                if (delete <= insert and delete <= sub): weight = DEL_WEIGHT
                elif (insert <= delete and insert <= sub): weight = INS_WEIGHT
                elif (sub <= delete and sub <= insert): weight = SUB_WEIGHT
                else: raise EOFError
                tmp[yinc][xinc] = min(delete, insert, sub) + weight
    #_pr(tmp)
    return tmp[-1][-1]

def _pr(m):
    for x in m:
        print(x)

if __name__ == '__main__':
    print(med_calc('language','lineage'))
