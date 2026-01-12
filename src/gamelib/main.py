class Console:
    # Constructeur
    def __init__(self):
        self.name = None
        self.manufacturer = None

    def launch_game(self, game: Game):
        print("Running video game: ", game.name)

class Game:
    # Constructeur
    def __init__(self):
        self.name = None
        self.studio = None
        self.year = 0
    

def main():
    game1 = Game()
    game1.name = "Driven"
    game1.studio = "RaceStudio"

    game2 = Game()
    game2.name = "Le Roi Scorpion"

    gba = Console()
    gba.launch_game(game1)

    print(game1.name)
    print(game2.name)

if (__name__ == "__main__"):
    main()
