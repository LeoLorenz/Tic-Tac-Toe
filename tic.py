marks = {'TL' : ' ', 'TC' : ' ', 'TR' : ' ', 'ML' : ' ', 'MC' : ' ', 'MR' : ' ',\
  'BL' : ' ', 'BC' : ' ', 'BR' : ' '}

player_db = {'Player 1' : 'X', 'Player 2' : 'O'}

def draw_board(marks):
    board = (f"     L       C       R\n\
      |----|----|----|\n\
    T |--{marks['TL']}-|--{marks['TC']}-|--{marks['TR']}-|\n\
      |----|----|----|\n\
    M |--{marks['ML']}-|--{marks['MC']}-|--{marks['MR']}-|\n\
      |----|----|----|\n\
    B |--{marks['BR']}-|--{marks['BC']}-|--{marks['BR']}-|\n\
      |----|----|----|\n")
    print(board)

move = ''

for turn in range (9):
  if turn % 2 == 0:
    player = 'Player 1'
  else:
    player = 'Player 2'
  draw_board(marks)
  while move not in (marks.keys()):
    print(f'{player}: please enter your move')
    move = input()
  marks[move] = player_db[player]
  move = ''


