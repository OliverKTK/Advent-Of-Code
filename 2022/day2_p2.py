f = '2022\day2.txt'
strategyGuide2 = open(f, 'r')

rock = ['A Y', 'B X', 'C Z']
paper = ['A Z', 'B Y', 'C X']
scissors = ['A X', 'B Z', 'C Y']
my_total_score_p2 = 0

def play_rock(self):
    global my_total_score_p2
    for i in range(3):
        if self == rock[i]:
            my_total_score_p2 += 1
            return True
    return False
            
def play_paper(self):
    global my_total_score_p2
    for i in range(3):
        if self == paper[i]:
            my_total_score_p2 += 2
            return True
    return False            

def play_scissors(self):
    global my_total_score_p2
    for i in range(3):
        if self == scissors[i]:
            my_total_score_p2 += 3
            return True
    return False
            
def result_value(self):
    global my_total_score_p2
    match self:
        case 'X':
            my_total_score_p2 += 0
        case 'Y':
            my_total_score_p2 += 3
        case 'Z':
            my_total_score_p2 += 6

for lines in strategyGuide2:
    lines = lines.rstrip()
    if lines == '':
        break
    elif play_rock(lines):
        result_value(lines[-1:])
    elif play_paper(lines):
        result_value(lines[-1:])
    elif play_scissors(lines):
        result_value(lines[-1:])
    else:
        print('erro')
strategyGuide2.close()

print(f"For the second part: {my_total_score_p2}")


# Rock : 1 Point
# Paper : 2 Points
# Scissors : 3 Points
# 0 lose
# 3 draw
# 6 win

#Part Two
# X lose
# Y draw
# Z win

#rock == 'A Y', 'B X', 'C Z'
#paper ==  'A Z', 'B Y', 'C X'
#Scissors == 'A X', 'B Z', 'C Y'