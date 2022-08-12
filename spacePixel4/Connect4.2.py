import pygame
import os

WHITE = (255,255,255)
BLACK = (0,0,0)
FPS = 60 
VEL = 10
STOP = 508
WINNER = ""

WIDTH, HEIGHT = 1092, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

coordf = 0
Bkgnd_x = 0
Bkgnd_y = 0 
Board_y = 1464
Bkgnd_VEL = 0

Board_Dim = (2100*0.55, 1500*0.55)
Red_Piece_Width, Red_Piece_Height = 555*1.15, 400*1.15
Yellow_Piece_Width, Yellow_Piece_Height = 555*1.07, 400*1.07

Red_Top_Piece_Width = 210*3
Red_Bottom_Piece_Width = 210*3
Yellow_Top_Piece_Width = 210*3
Yellow_Bottom_Piece_Width = 210*3

Red_Top_Piece_Height = 150*3
Red_Bottom_Piece_Height = 150*3
Yellow_Top_Piece_Height = 150*3
Yellow_Bottom_Piece_Height = 150*3


Background_Red = pygame.image.load(os.path.join('Assets', 'Scroll_Background.png')).convert()
Background_Yellow = pygame.image.load(os.path.join('Assets', 'Scroll_Background_Yellow.png')).convert()

Background = Background_Red

Board = pygame.image.load(os.path.join('Assets', 'Board2.png')) .convert_alpha()
Red_Piece_Image = pygame.image.load(os.path.join('Assets', 'Red_Piece.png')).convert_alpha()
Yellow_Piece_Image = pygame.image.load(os.path.join('Assets', 'Yellow_Piece.png')).convert_alpha()

Red_Piece_Grey_Image = pygame.image.load(os.path.join('Assets', 'Red_Piece_Grey.png')).convert_alpha()
Yellow_Piece_Grey_Image = pygame.image.load(os.path.join('Assets', 'Yellow_Piece_Grey.png')).convert_alpha()

Yellow_Win_Top_Image = pygame.image.load(os.path.join('Assets', 'Yellow_Win_Top.png')).convert_alpha()
Yellow_Win_Bottom_Image = pygame.image.load(os.path.join('Assets', 'Yellow_Win_Bottom.png')).convert_alpha()
Red_Win_Top_Image = pygame.image.load(os.path.join('Assets', 'Red_Win_Top.png')).convert_alpha()
Red_Win_Bottom_Image = pygame.image.load(os.path.join('Assets', 'Red_Win_Bottom.png')).convert_alpha()



Board = pygame.transform.scale(Board,(Board_Dim))
Red_Piece = pygame.transform.scale(Red_Piece_Image,(Red_Piece_Width, Red_Piece_Height))
Yellow_Piece = pygame.transform.scale(Yellow_Piece_Image,(Yellow_Piece_Width, Yellow_Piece_Height))

Red_Piece_Grey = pygame.transform.scale(Red_Piece_Grey_Image,(Red_Piece_Width, Red_Piece_Height))
Yellow_Piece_Grey = pygame.transform.scale(Yellow_Piece_Grey_Image,(Yellow_Piece_Width, Yellow_Piece_Height))

Red_Top_Piece = pygame.transform.scale(Red_Win_Top_Image,(Red_Top_Piece_Width, Red_Top_Piece_Height))
Yellow_Top_Piece = pygame.transform.scale(Yellow_Win_Top_Image,(Yellow_Top_Piece_Width, Yellow_Top_Piece_Height))
Red_Bottom_Piece = pygame.transform.scale(Red_Win_Bottom_Image,(Red_Bottom_Piece_Width, Red_Bottom_Piece_Height))
Yellow_Bottom_Piece = pygame.transform.scale(Yellow_Win_Bottom_Image,(Yellow_Bottom_Piece_Width, Yellow_Bottom_Piece_Height))

Red_Piece_A1 = pygame.transform.scale(Red_Piece_Image,(Red_Piece_Width, Red_Piece_Height))

NumOfYellow, NumOfRed = 0,0
TURN = "R"
NumberArray = [0,0,0,0,0,0,0]


def CheckWin(Dict):
    global WINNER
    #Vertical win detection for Red
    for j in range(3,0,-1):
        for i in range(65,72):
            if Dict[chr(i)+str(j)] == Dict[chr(i)+str(j+1)] == Dict[chr(i)+str(j+2)] == Dict[chr(i)+str(j+3)] == 'R':
                Dict[chr(i)+str(j)] = 'RW'
                Dict[chr(i)+str(j+1)] = 'RW'
                Dict[chr(i)+str(j+2)] = 'RW'
                Dict[chr(i)+str(j+3)] = 'RW'
                WINNER = "R"

    #Vertical win detection for Yellow
    for j in range(3,0,-1):
        for i in range(65,72):
            if Dict[chr(i)+str(j)] == Dict[chr(i)+str(j+1)] == Dict[chr(i)+str(j+2)] == Dict[chr(i)+str(j+3)] == 'Y':
                Dict[chr(i)+str(j)] = "YW"
                Dict[chr(i)+str(j+1)] = "YW"
                Dict[chr(i)+str(j+2)] = "YW"
                Dict[chr(i)+str(j+3)] = "YW"
                WINNER = "Y"

    #Horizontal win detection for Red
    for j in range(6,0,-1):
        for i in range(65,69):
            if Dict[chr(i)+str(j)] == Dict[chr(i+1)+str(j)] == Dict[chr(i+2)+str(j)] == Dict[chr(i+3)+str(j)] == 'R':
                Dict[chr(i)+str(j)] = 'RW'
                Dict[chr(i+1)+str(j)]= 'RW'
                Dict[chr(i+2)+str(j)] = 'RW'
                Dict[chr(i+3)+str(j)] = 'RW'
                WINNER = "R"

    #Horizontal win detection for Yellow
    for j in range(6,0,-1):
        for i in range(65,69):
            if Dict[chr(i)+str(j)] == Dict[chr(i+1)+str(j)] == Dict[chr(i+2)+str(j)] == Dict[chr(i+3)+str(j)] == 'Y':
                Dict[chr(i)+str(j)] = 'YW'
                Dict[chr(i+1)+str(j)] = 'YW'
                Dict[chr(i+2)+str(j)] = 'YW'
                Dict[chr(i+3)+str(j)] = 'YW'
                WINNER = "Y"
    
    #Up-right diagonal win detection for Red
    for j in range(3,0,-1):
        for i in range(65,69):
            if Dict[chr(i)+str(j)] == Dict[chr(i+1)+str(j+1)] == Dict[chr(i+2)+str(j+2)] == Dict[chr(i+3)+str(j+3)] == 'R':
                Dict[chr(i)+str(j)] = 'RW'
                Dict[chr(i+1)+str(j+1)] = 'RW'
                Dict[chr(i+2)+str(j+2)] = 'RW'
                Dict[chr(i+3)+str(j+3)] = 'RW'
                WINNER = "R"

    #Up-right diagonal win detection for Yellow
    for j in range(3,0,-1):
        for i in range(65,69):
            if Dict[chr(i)+str(j)] == Dict[chr(i+1)+str(j+1)] == Dict[chr(i+2)+str(j+2)] == Dict[chr(i+3)+str(j+3)] == 'Y':
                Dict[chr(i)+str(j)] = 'YW'
                Dict[chr(i+1)+str(j+1)] = 'YW'
                Dict[chr(i+2)+str(j+2)] = 'YW'
                Dict[chr(i+3)+str(j+3)] = 'YW'
                WINNER = "Y"

    #Up-left diagonal win detection for Red
    for j in range(3,0,-1):
        for i in range(68,72):
            if Dict[chr(i)+str(j)] == Dict[chr(i-1)+str(j+1)] == Dict[chr(i-2)+str(j+2)] == Dict[chr(i-3)+str(j+3)] == 'R':
                Dict[chr(i)+str(j)] = 'RW'
                Dict[chr(i-1)+str(j+1)] = 'RW'
                Dict[chr(i-2)+str(j+2)] = 'RW'
                Dict[chr(i-3)+str(j+3)] = 'RW'
                WINNER = "R"

    #Up-left diagonal win detection for Yellow
    for j in range(3,0,-1):
        for i in range(68,72):
            if Dict[chr(i)+str(j)] == Dict[chr(i-1)+str(j+1)] == Dict[chr(i-2)+str(j+2)] == Dict[chr(i-3)+str(j+3)] == 'Y':
                Dict[chr(i)+str(j)] = 'YW'
                Dict[chr(i-1)+str(j+1)] = 'YW'
                Dict[chr(i-2)+str(j+2)] = 'YW'
                Dict[chr(i-3)+str(j+3)] = 'YW'
                WINNER = "Y"

def Height_finder(Dict,letter):
    global coordf
    number = 7
    Height = 0
    for key in Dict:
        if (key[0] == letter) and Dict[key] == "O":
            number -= 1
            coordf+=1

    if number == 1: 
        Height = 508
    if number == 2: 
        Height = 439
    if number == 3: 
        Height = 370
    if number == 4: 
       Height = 302
    if number == 5: 
        Height = 233
    if number == 6: 
        Height = 164
    return(Height)
        
def piece():
    WIN.blit(Red_Piece_Image)

def cursor_func(cursor):
    cursor = pygame.mouse.get_pos()
    x = 0
    if cursor[0]<359:
        x = 297
    elif cursor[0]<427:
        x = 365
    elif cursor[0]<496:
        x = 433
    elif cursor[0]<564:
        x = 502
    elif cursor[0]<633:
        x = 571
    elif cursor[0]<702:
        x = 639
    elif cursor[0]>702:
        x = 708
    return (x)

def initialize_board(): 
    Dict = {}
    for j in range(6,0,-1):
        for i in range(65,72):
            Dict [chr(i)+str(j)] = "O"
    return(Dict)
    
def coord_finder_red(let_num):
    global coordf
    x = list(let_num)
    if x[0] == "A":
        x[0] = 297
    if x[0] == "B":
        x[0] = 365
    if x[0] == "C":
        x[0] = 433
    if x[0] == "D":
        x[0] = 502
    if x[0] == "E":
        x[0] = 571
    if x[0] == "F":
        x[0] = 639
    if x[0] == "G":
        x[0] = 708
    if x[1] == "1": 
        x[1] = 508
    if x[1] == "2": 
        x[1] = 439
    if x[1] == "3": 
        x[1] = 370
    if x[1] == "4": 
        x[1] = 302
    if x[1] == "5": 
        x[1] = 233
    if x[1] == "6": 
        x[1] = 164
    return(x)

def coord_finder_yellow(let_num):   
    x = list(let_num)
    if x[0] == "A":
        x[0] = 297
    if x[0] == "B":
        x[0] = 365
    if x[0] == "C":
        x[0] = 433
    if x[0] == "D":
        x[0] = 502
    if x[0] == "E":
        x[0] = 571
    if x[0] == "F":
        x[0] = 639
    if x[0] == "G":
        x[0] = 708
    if x[1] == "1": 
        x[1] = 508
    if x[1] == "2": 
        x[1] = 439
    if x[1] == "3": 
        x[1] = 370
    if x[1] == "4": 
        x[1] = 302
    if x[1] == "5": 
        x[1] = 233
    if x[1] == "6": 
        x[1] = 164
    return(x)

def print_board(Dict):
    i = 1
    for key in Dict:
        if i == 8:
            print("")
            i = 1
        print(Dict[key], end="")
        i+=1
    print("")
    print("")

def Board_Check(Dict):
    global TURN
    global NumOfRed
    global NumOfYellow

    if NumOfRed != NumOfYellow:
            TURN = "Y"
    if NumOfRed == NumOfYellow:
            TURN = "R"

x = True
def draw_window(red, yellow):
    global x
    global Bkgnd_x
    global Bkgnd_y
    global Bkgnd_VEL
    global Board_y
    global WINNER
    global Red_Top_Piece_Width
 
    WIN.blit(Background,(Bkgnd_x,Bkgnd_y))
    if Bkgnd_y == -1445:
        Bkgnd_VEL = 0
    
    Bkgnd_y -= Bkgnd_VEL
    Board_y -= Bkgnd_VEL
    

    if TURN == "Y" and WINNER == "" and Bkgnd_y == -1445:
        WIN.blit(Yellow_Piece, (yellow.x, yellow.y))
    if TURN == "R" and WINNER == "" and Bkgnd_y == -1445:
        WIN.blit(Red_Piece, (red.x,red.y))
    if WINNER == "R":
        WIN.blit(Red_Top_Piece, (425,45))
        WIN.blit(Red_Bottom_Piece, (377,640))
    if WINNER == "Y":
        WIN.blit(Yellow_Top_Piece, (293,45))
        WIN.blit(Yellow_Bottom_Piece, (377,640))

    for key in Dict:
        if (Dict[key] == "R") and WINNER =="": 
            WIN.blit(Red_Piece, ((coord_finder_red(key)[0]),coord_finder_red(key)[1]))
        if (Dict[key] == "R") and WINNER != "":
            WIN.blit(Red_Piece_Grey, ((coord_finder_red(key)[0]),coord_finder_red(key)[1]))
        if (Dict[key] == "RW") and WINNER != "":
            WIN.blit(Red_Piece, ((coord_finder_red(key)[0]),coord_finder_red(key)[1]))
        if (Dict[key] == "Y") and WINNER =="": 
            WIN.blit(Yellow_Piece, ((coord_finder_yellow(key)[0]),coord_finder_yellow(key)[1]))
        if (Dict[key] == "Y") and WINNER != "":
            WIN.blit(Yellow_Piece_Grey,  ((coord_finder_yellow(key)[0]),coord_finder_yellow(key)[1]))
        if (Dict[key] == "YW") and WINNER != "":
            WIN.blit(Yellow_Piece,  ((coord_finder_yellow(key)[0]),coord_finder_yellow(key)[1]))
    WIN.blit(Board,(-8,Board_y))

    pygame.display.update()

def Drop_Piece(red,yellow,Height,event,Dict):
    number = "1"
    NumberArrayPos = 7
    global NumOfRed
    global NumOfYellow
    global TURN
    EmptySpace = True
    n = False
    if TURN == "R":
        letter = ""
        cursor = pygame.mouse.get_pos()
        if cursor[0]<359:
            red.x = 297
            letter = "A"
            NumberArrayPos = 0
            if NumberArray[NumberArrayPos] == 6:
                EmptySpace = False  
        elif cursor[0]<427:
            red.x = 365
            letter = "B"
            NumberArrayPos = 1
            if NumberArray[NumberArrayPos] == 6:
                EmptySpace = False 
        elif cursor[0]<496:
            red.x = 433
            letter = "C"
            NumberArrayPos = 2
            if NumberArray[NumberArrayPos] == 6:
                EmptySpace = False 
        elif cursor[0]<564:
            red.x = 502
            letter = "D"
            NumberArrayPos = 3
            if NumberArray[NumberArrayPos] == 6:
                EmptySpace = False 
        elif cursor[0]<633:
            red.x = 571
            letter = "E"
            NumberArrayPos = 4
            if NumberArray[NumberArrayPos] == 6:
                EmptySpace = False 
        elif cursor[0]<702:
            red.x = 639
            letter = "F"
            NumberArrayPos = 5
            if NumberArray[NumberArrayPos] == 6:
                EmptySpace = False 
        elif cursor[0]>702:
            red.x = 708
            letter = "G"
            NumberArrayPos = 6
            if NumberArray[NumberArrayPos] == 6:
                EmptySpace = False 
        if event.type == pygame.MOUSEBUTTONDOWN and EmptySpace:
            n = True 
            
        
        

        
        while n == True:
 
            Height = Height_finder(Dict,letter)

            if red.y == Height:
                NumberArray[NumberArrayPos]+=1
                number = str(NumberArray[NumberArrayPos])
                n = False
                red.y = 0
                red.x = cursor_func(cursor)
                Dict[letter + number] = TURN
                CheckWin(Dict)
                NumOfRed +=1

            if red.y + VEL > Height:
                red.y +=  VEL - ((VEL + red.y) - Height)
            
            else:
                red.y += VEL
            yellow.y = red.y
            yellow.x = red.x
            draw_window(red, yellow)

    if TURN == "Y":
        letter = ""
        cursor = pygame.mouse.get_pos()
        if cursor[0]<359:
            yellow.x = 296
            letter = "A"
            NumberArrayPos = 0
            if NumberArray[NumberArrayPos] == 6:
                EmptySpace = False  
        elif cursor[0]<427:
            yellow.x = 365
            letter = "B"
            NumberArrayPos = 1
            if NumberArray[NumberArrayPos] == 6:
                EmptySpace = False 
        elif cursor[0]<496:
            yellow.x = 433
            letter = "C"
            NumberArrayPos = 2
            if NumberArray[NumberArrayPos] == 6:
                EmptySpace = False 
        elif cursor[0]<564:
            yellow.x = 502
            letter = "D"
            NumberArrayPos = 3
            if NumberArray[NumberArrayPos] == 6:
                EmptySpace = False 
        elif cursor[0]<633:
            yellow.x = 571
            letter = "E"
            NumberArrayPos = 4
            if NumberArray[NumberArrayPos] == 6:
                EmptySpace = False 
        elif cursor[0]<702:
            yellow.x = 639
            letter = "F"
            NumberArrayPos = 5
            if NumberArray[NumberArrayPos] == 6:
                EmptySpace = False 
        elif cursor[0]>702:
            yellow.x = 708
            letter = "G"
            NumberArrayPos = 6
            if NumberArray[NumberArrayPos] == 6:
                EmptySpace = False 

        if event.type == pygame.MOUSEBUTTONDOWN and EmptySpace:
            n = True 
            
        while n == True:
            Height = Height_finder(Dict,letter)
            if yellow.y == Height:
                NumberArray[NumberArrayPos]+=1
                number = str(NumberArray[NumberArrayPos])
                Dict[letter + number] = TURN
                CheckWin(Dict)
                NumOfYellow +=1
                yellow.y = 0
                yellow.x = cursor_func(cursor)
                n = False  
            if yellow.y + VEL > Height:
                yellow.y +=  VEL - ((VEL + yellow.y) - Height)
            
            else:
                yellow.y += VEL
            red.x = yellow.x
            red.y = yellow.y
            draw_window(red, yellow)

def HomeScreen(event):
    global Bkgnd_VEL
    global Background
    cursor = pygame.mouse.get_pos()
    if event.type == pygame.MOUSEBUTTONDOWN and cursor[0] > 478 and cursor[0] < 616 and cursor[1]>460 and cursor[1]<535:
        Background = Background_Yellow
    if event.type == pygame.MOUSEBUTTONUP and cursor[0] > 478 and cursor[0] < 616 and cursor[1]>460 and cursor[1]<535:
        Background = Background_Red
        Bkgnd_VEL =5

def main():
    red = pygame.Rect(251,40, Red_Piece_Width, Red_Piece_Height)
    yellow = pygame.Rect(251,40,Yellow_Piece_Width, Yellow_Piece_Height) 
    pygame.display.set_caption ("Connect 4")
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        Height = 508
        draw_window(red, yellow)
        if Board_y != 19:
            HomeScreen(event)

        if WINNER == "" and Bkgnd_y == -1445:
            draw_window(red, yellow)
            Drop_Piece(red,yellow,Height,event,Dict)
            Board_Check(Dict)
    pygame.quit()
Dict = initialize_board()

if __name__ == "__main__":
    main()