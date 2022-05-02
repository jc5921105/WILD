

def jaro_calc(word1, word2):
    if word1 == word2: return 1.0
    if len(word1) == 0 or len(word2) == 0: return 0.0
 
    md = (max(len(word1), len(word2)) / 2 ) - 1
    if not type(md) == type(0): md = int(md)
    match = 0
    hash_1 = [0 for x in word1]
    hash_2 = [0 for x in word2]
    for i in range(len(word1)):
        for j in range(max(0, i - md),min(len(word2), i + md + 1)):
            if word1[i] == word2[j] and hash_2[j] == 0:
                hash_1[i] = 1
                hash_2[j] = 1
                match += 1
                break
         
    if match == 0: return 0.0
    trans = 0
    point = 0
    for i in range(len(word1)):
        if hash_1[i]:
            while hash_2[point] == 0: point += 1
            if word1[i] != word2[point]:
                point += 1
                trans += 1
            else:
                point += 1
    t = trans/2
    return ((float(match) / len(word1)) + (float(match) / len(word1)) + (float(match - t)/ len(word2))) / 3.0


def jw_calc(word1, word2):
    jd = jaro_calc(word1, word2)
    if jd > 0.7:
        prefix = 0
        for i in range(min(len(word1), len(word2))):
            if word1[i] == word2[i]: prefix += 1
            else: break
        prefix = min(4, prefix)
        jd = jd + ( 0.1 * prefix * (1 - jd))
    return jd

