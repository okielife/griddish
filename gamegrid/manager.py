from gamegrid.gridcell import GridCell
from gamegrid.character import Character


class GameManager(object):
    def __init__(self):
        # create a grid, place the character, place the treasure, handle buttons
        self.cella1 = GridCell(treasure_here=False)
        self.cella2 = GridCell(treasure_here=False)
        self.cellb1 = GridCell(treasure_here=True)
        self.cellb2 = GridCell(treasure_here=False)

        self.character = Character()
        self.character_position = "a1"

        keep_going = True
        while keep_going:
            print("Character position is: " + self.character_position)
            print("What to do?")
            print(" 1: Move left")
            print(" 2: Move right")
            print(" 3: Move up")
            print(" 4: Move down")
            print(" q: Quit")
            print("Make your selection:")
            key = raw_input("> ")
            if key == "1":
                print("Moving you left")
            elif key == "2":
                print("Moving you right")
            elif key == "3":
                print("Moving you up")
            elif key == "4":
                print("Moving you down")
            elif key == "q":
                keep_going = False
            else:
                print("Button not implemented yet")
