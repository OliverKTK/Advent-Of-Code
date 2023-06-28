f = '2022\day2.txt'
strategyGuide1 = open(f, 'r')

lose = ['A Z', 'B X', 'C Y']
draw = ['A X', 'B Y', 'C Z']
win = ['A Y', 'B Z', 'C X']
my_total_score_p1 = 0

def play_value(self):
    global my_total_score_p1
    match self:
        case 'X':
            my_total_score_p1 += 1
        case 'Y':
            my_total_score_p1 += 2
        case 'Z':
            my_total_score_p1 += 3

def lose_value(self):
    for i in range(3):
        if self == lose[i]:
            return True
    return False

def draw_value(self):
    global my_total_score_p1
    for i in range(3):
        if self == draw[i]:
            my_total_score_p1 += 3
            return True
    return False

def win_value(self):
    global my_total_score_p1
    for i in range(3):
        if self == win[i]:
            my_total_score_p1 += 6
            return True
    return False

for line in strategyGuide1:
    line = line.rstrip()
    if line == '':
        break
    elif lose_value(line):
        play_value(line[-1:])
    elif draw_value(line):
        play_value(line[-1:])
    elif win_value(line):
        play_value(line[-1:])
    else:
        print('erro')
strategyGuide1.close()


print(f"For the first part: {my_total_score_p1}")


# Rock : 1 Point
# Paper : 2 Points
# Scissors : 3 Points
# 0 lose
# 3 draw
# 6 win

#Part One
# A,X Rock
# B,Y Paper
# C,Z Scissors

# lose == 'A Z', 'B Y', 'C Y'
# draw =='A X', 'B Y', 'C Z'
#win == 'A Y', 'B Z', 'C X'

