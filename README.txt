Weighted Implementation of Levenshtein Distance <W.I.L.D>

Code developed for CSCI 538 Artificial Intelligence Final Poject
Author_1) Krystal Jordan
Author_2) Juan Cota


Installation:
    Chose a location to copy the smith module to.

    Windows EX: C:\users\someone\Desktop
    Linux EX: /home/someone/Desktop

    WINDOWS:
    The location at which you install the code will need to be added to the PATH variable.


Running the Code:
    To execute the smith agent, run the following commands from the folder that you copied the code to from the terminal.
        "python -m smith" | "python2 -m smith" | "python3 -m smith"

Importing the Code:
    WILD can be used by importing the "smith" module. EX: 'import smith'.
    Once imported, the user will have access to the functions available
    through the interface. 


    FUNCTIONS
        LD_Search(model, word)
            Returns a model entry that is the LD
            Search result.
        
        WILD_Search(model, word)
            Returns a model entry that is the WILD
            Search result.
        
        consume(model, location)
            returns a tuple of status and either a error message or model
            return (bool, msg|model)
        
        consumeWord(model, word)
            Consumes a single word.
            Returns an updated model.
        
        getNewModel()
            Return a new fresh dictionary model that can be used in further testing.

Further Notes:
    For the smith agent to properly train itself, the host computer must have an active connection to the internet. Agent
    training will cause the agent to try to access the Miraim Webster website.
