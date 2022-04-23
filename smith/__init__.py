from smith.capabilities.consume import consume as csm
from smith.capabilities.search import search, straight_search


def getNewModel():
    """
    Return a new fresh dictionary model that can be used in further testing.
    """
    return {}


def consume(model,location):
    """
    returns a tuple of status and either a error message or model
    return (bool, msg|model)
    """
    return csm(model,location)


def consumeWord(model,word):
    """
    Consumes a single word.
    Returns an updated model.
    """
    if not word in model.keys():
        print('Unknown Word: %s ->  Adding to model' % word)
        model[word] = {'word': word, 'definitions': {}, 'weight': 1}
    else:
        if not 'weight' in model[word].keys():
            model[word]['weight'] = 1
        else:
            model[word]['weight'] += 1
    return model


def WILD_Search(model, word):
    """
    Returns a model entry that is the WILD
    Search result.
    """
    return search(word,model)


def LD_Search(model,word):
    """
    Returns a model entry that is the LD
    Search result.
    """
    return straight_search(word, model)


