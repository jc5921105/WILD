import pdb
from smith.controller import Controller
from smith.model import Model
import smith.view as view


def main():
    pass
    model = Model()
    app = Controller(model,view)



if __name__ == '__main__':
    main()