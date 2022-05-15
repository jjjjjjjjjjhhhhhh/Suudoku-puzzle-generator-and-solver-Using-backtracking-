import random
base = 3
side = base*base

#building 9*9 2D array with random numbers

def pattern(r, c):
    return (base*(r % base)+r//base+c) % side

def shuffle(s):
    return random.sample(s, len(s))


rBase = range(base)

rows = []
for g in shuffle(rBase):
    for r in shuffle(rBase):
        rows.append(g*base + r)

cols = []
for g in shuffle(rBase):
    for c in shuffle(rBase):
        cols.append(g*base + c)

nums = shuffle(range(1, base*base+1))

board = [[nums[pattern(r, c)] for c in cols] for r in rows]

for line in board:
    print(line)

#removing numbers from the 2D array

def remove_numbers(board,amount):
  h, w, r = len(board), len(board[0]), []
  print(w)
  spaces = [[x, y] for x in range(h) for y in range(w)]
  for k in range(amount):
      r = random.choice(spaces)
      board[r[0]][r[1]] = 0
      spaces.remove(r)
  return board

remove_numbers(board, 50)
print(board)
sudoku = board

#inserting into the board

def expandLine(line):
  return line[0]+line[5:9].join([line[1:5]*(base-1)]*base)+line[9:13]


line0 = expandLine("╔═══╤═══╦═══╗")
line1 = expandLine("║ . ║ . ║ . ║")
line2 = expandLine("╟===║===╪===╢")
line3 = expandLine("╠═══║═══╬═══╣")
line4 = expandLine("╚═══╧═══╩═══╝")

#or
#line0 = expandLine("╔═══╤═══╦═══╗")
#line1 = expandLine("║ . │ . ║ . ║")
#line2 = expandLine("╟───┼───╫───╢")
#line3 = expandLine("╠═══╪═══╬═══╣")
#line4 = expandLine("╚═══╧═══╩═══╝")

symbol = " 1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"
nums = [[""]+[symbol[n] for n in row] for row in board]
print(line0)
for r in range(1, side+1):
  print("".join(n+s for n, s in zip(nums[r-1], line1.split("."))))
  print([line2, line3, line4][(r % side == 0)+(r % base == 0)])
