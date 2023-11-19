import pygame, time

def scrolling_text(n):
    '''
        input : a string(n)
        output : print the same inputted string but in a format that will make it scroll across as it is printed
    '''
    #make sure n is a string
    n = str(n)
    for i in n:
        print(i)
        time.sleep(0.5)

# scrolling_text("This text should be scrolling, see?")

class example():
    def __init__(self):
        self.size = self.height, self.width = 500, 500

a = example()

# print(a.size, a.height)
x1 = 10
width1 = 20
y1 = 10
height1 = 30
x2 = x1 + width1
y2 = y1 + height1

x3 = 40
width2 = 10
y3 = 40
height2 = 30
x4 = x3 + width2
y4 = y3 + height2

# player1coords = (x1, x2, y1, y2)


class Enemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    
new_list = []
i = 0
x = 0
while i < 7:
    new_list.append("enemy_" + str(i))
    new_list[i] = Enemy(x, 20)
    x += 10
    i += 1

def spawn_enemies(i):
    #define the variables
    enemy_list = []
    x = 30
    while i < (i+6):
        #create the class name 
        enemy_list.append("enemy_" +str(i))
        enemy_list[i] = Enemy(x, 30)
        #update x and the counter
        x += 100
        i += 1
    return(enemy_list, i)

def test():
    return 5, 6

List_of_Lists = []
i = 0
n = 0
while i <= 7:
    while n <= 4:
        new_list.append(n)
        n+=1
    n = 0
    List_of_Lists.append(new_list)
    new_list = []
    i += 1

list_example = []
list_example.append("a")
list_example[0] = "b"

print(list_example[0])