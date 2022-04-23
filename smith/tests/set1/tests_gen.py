from __future__ import print_function
import pdb, os, json, random, string

LENGTH = 4

def get_random_letter():
    return random.choice(string.ascii_lowercase)

with open('words.txt','r') as fobj:
    words = fobj.readlines()


#Straigt Test
straight_test  = []
for word in words:
    word = word.strip()
    straight_test.append((word,word))

with open('straight_test.json','w') as fobj:
    json.dump(straight_test,fobj,sort_keys=True,indent=4)


#with open('straight_test','r') as fobj:
#    data = json.load(fobj)


#One Insert
one_insert = []
for word in words:
    word = word.strip()
    if len(word) >= LENGTH:

        tmp = [x for x in word]
        tmp.insert(random.randint(1,len(word)),get_random_letter())
        alt = ''.join(tmp)
        one_insert.append((word,alt))

with open('one_insert_test.json','w') as fobj:
    json.dump(one_insert, fobj, sort_keys=True, indent=4)


#Two Insert
two_insert = []
for word in words:
    word = word.strip()
    if len(word) >= LENGTH:
        tmp = [x for x in word]
        tmp.insert(random.randint(1,len(word)),get_random_letter())
        alt = ''.join(tmp)
        tmp = [x for x in alt]
        tmp.insert(random.randint(1,len(alt)),get_random_letter())
        alt = ''.join(tmp)

        two_insert.append((word,alt))

with open('two_insert_test.json','w') as fobj:
    json.dump(two_insert, fobj, sort_keys=True, indent=4)


#One Delete
one_delete = []
for word in words:
    word = word.strip()
    if len(word) >= LENGTH + 2:
        tmp = [x for x in word]
        tmp.pop(random.randint(1,len(word) - 1))
        alt = ''.join(tmp)
        one_delete.append((word,alt))

with open('one_delete_test.json','w') as fobj:
    json.dump(one_delete, fobj, sort_keys=True, indent=4)


#Two Delete
two_delete = []
for word in words:
    word = word.strip()
    if len(word) >= LENGTH + 2:
        tmp = [x for x in word]
        tmp.pop(random.randint(1,len(word) - 1))
        alt = ''.join(tmp)
        tmp = [x for x in alt]
        tmp.pop(random.randint(1,len(alt) - 1))
        alt = ''.join(tmp)
        two_delete.append((word,alt))

with open('two_delete_test.json','w') as fobj:
    json.dump(two_delete, fobj, sort_keys=True, indent=4)


#One Swap
one_swap = []
for word in words:
    word = word.strip()
    if len(word) >= LENGTH:
        tmp = [x for x in word]
        indx = random.randint(1,len(word) - 1)
        while True:
            ti = get_random_letter()
            if ti != tmp[indx] : tmp[indx] = ti; break
        alt = ''.join(tmp)
        one_swap.append((word,alt))

with open('one_swap_test.json','w') as fobj:
    json.dump(one_swap, fobj, sort_keys=True, indent=4)


#Two Swap
two_swap = []
for word in words:
    word = word.strip()
    if len(word) >= LENGTH:
        tmp = [x for x in word]
        indx = random.randint(1,len(word) - 1)
        while True:
            ti = get_random_letter()
            if ti != tmp[indx] : tmp[indx] = ti; break
        alt = ''.join(tmp)
        tmp = [x for x in alt]
        indx = random.randint(1,len(alt) - 1)
        while True:
            ti = get_random_letter()
            if ti != tmp[indx] : tmp[indx] = ti; break
        alt = ''.join(tmp)
        two_swap.append((word,alt))

with open('two_swap_test.json','w') as fobj:
    json.dump(two_swap, fobj, sort_keys=True, indent=4)







pdb.set_trace()