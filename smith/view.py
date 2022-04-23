from __future__ import print_function
import sys, time, pdb, os


def introduction():
    _print('I am Agent Smith')


def prompt_user():
    _print('\n\nWhat Can I Do For You?')
    try:
        tmp = raw_input('<Me>: ')
    except:
        #print('caught some type of error')
        tmp = str(input('<Me>: '))
    if(os.name == 'posix'): os.system('clear')
    else: os.system('cls')
    print('<Me>: ' + tmp)
    return tmp


def _print(tmp = ''):
    for x in (y for y in tmp):
        sys.stdout.write(x)
        sys.stdout.flush()
        time.sleep(.01)
    print('')


def s_print(txt):
    _print(txt)


def print_entity(ent):
    _print('Word: %s' % ent['word'])
    _print('Current Weight: %s' % ent['weight'])
    _print('Definitions: ')
    for x in range(len(ent['definitions'])):
        _print('\t%s) %s' % (x + 1,ent['definitions'][str(x + 1)]))
    #print(ent)


def print_spelling_entity(ent):
    _print('\n\nI believe the word that you are looking for is:\n\t\"%s\"' % ent['word'])
    _print('Probability:')
    _print('\t{:.4f}%'.format(ent['probability'] * 100))
    _print('Edit Distance:\n\t%s' % ent['edit_distance'])


def print_possible_spellings(model,word):
    _print('\n\nPossible Spellings for the word \"%s\" are:' % word)
    for x in model:
        ent = model[x]
        #_print()
        _print('\tWord:\"%s\"' % ent['word'])
        _print('\t\tProbability: {:.4f}%'.format(ent['probability'] * 100))
        _print('\t\tEdit Distance: %s' % ent['edit_distance'])
        _print('')


if __name__ == '__main__':
    introduction()
    print(prompt_user())