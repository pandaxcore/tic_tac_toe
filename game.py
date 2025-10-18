from gameparts.parts import Board


def main():
    game = Board()
    game.display()
    game.make_move(1, 1, 'X')
    game.make_move(0, 0, 'O')
    print('Ход сделан!')
    game.display()


if __name__ == '__main__':
    main()
