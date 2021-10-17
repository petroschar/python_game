import paixnidi1 as p1
import paixnidi2 as p2
print("Game start...")

num_pextes = 0
num_pextes = int(input("Dwse arithmo pextwn : "))

while (num_pextes == 0) or (num_pextes >= 3):
    print("O arithmos twn pextwn prepei na einai 1 h 2!")
    num_pextes = int(input("Dwse arithmo pextwn : "))

if num_pextes == 1:
    p1.start()
else:
    p2.start()

    


