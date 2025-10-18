from parts import Board

game = Board()
game.display()
game.make_move(1, 1, 'X')
game.make_move(0, 0, 'O')
print('Ход сделан!')
game.display()
