from cmath import inf
from math import log, sqrt
from random import choice
import os
import copy


player, opponent = 'X', 'O'


#########################################################################################


class Node :

    def __init__(self,board,turn,parent=None):
        self.visited = 0.00
        self.score = 0.00
        self.parent = parent 
        self.children = []
        self.board = board
        self.turn= turn # x stand for player and o stand for agent
        self.position = (-1,-1)
        self.ucb = -inf
        # ucb = score/visited + sqrt(2)*sqrt(ln(parent.visited)/visited)
        if self.parent==None :
            for i in range(3):
                for j in range(3) :
                    if self.board[i][j]=="X" :
                        self.position = (i,j)
        # elif self.visited!=0: 
        #     self.ucb = self.score/self.visited + sqrt(2) * sqrt(log(self.parent.visited)/self.visited)
        self.find_all_children()

    def find_all_children(self) :
        
        for i in range(3) :
            for j in range(3) :
                if self.board[i][j]=="_" :
                    new_board = copy.deepcopy(self.board)
                    if(self.turn=="X") :
                        new_board[i][j] = "O"
                        child = Node(new_board,"O",self)
                        child.position = (i,j)
                        self.children.append(child)
                    else : 
                        new_board[i][j] = "X"
                        child = Node(new_board,"X",self)
                        child.position = (i,j)
                        self.children.append(child)

#mcst :
def check(current) :
    for child in current.children :
        if child.ucb == -inf :
            return (True,child)
    return (False,0)

def selection_expansion(current) :
    cur = current
    while(len(cur.children)!=0) :
        flag,child = check(cur)
        if flag :
            return child
        for child in cur.children :
            child.ucb = child.score/child.visited + sqrt(2) * sqrt(log(child.parent.visited)/child.visited)
        cur = max(cur.children,key = lambda key:key.ucb)
    return cur



def is_end(board) :
    for i in range(3) :
        for j in range(3) :
            if(board[i][j]=="_") :
                return False
    return True

def simulation(node) :
    current = node
    board = node.board
    current_turn = node.turn
    while(not checkWin(board)) :
        if(is_end(board)) :
            return "draw"
        current = choice(current.children)
        current_turn = current.turn
        board = current.board
    if(current_turn=="X") :
        return "X"
    return "O"

def back_propagation(node,result) :
    current = node
    while(current!=None) :
        current.visited+=1
        # if current.parent!=None:
        #     current.ucb = current.score/current.visited + sqrt(2) * sqrt(log(current.parent.visited)/current.visited)
        if current.turn == result :
            current.score+=1
        elif result!="draw" :
            current.score -=1
        # else :
        #     current.score-=1
        for child in current.children :
            if child.visited !=0 :
                child.ucb = child.score/child.visited + sqrt(2) * sqrt(log(child.parent.visited)/child.visited)
        current = current.parent

#########################################################################################


def findBestMove(board): 

    root = Node(board,"X")
    for i in range(1000) :
        node = selection_expansion(root)
        if not is_end(node.board) :
            result = simulation(node)
            back_propagation(node,result)

    return list(max(root.children,key = lambda item:item.ucb).position)


def findRandom(board):
    empty_spots = [i*3+j for i in range(3)
    for j in range(3) if board[i][j] == "_"]
    idx = choice(empty_spots)
    return[int(idx/3), idx % 3]


def isMovesLeft(board):
    return ('_' in board[0] or '_' in board[1] or '_' in board[2])


def checkWin(board):
    for row in range(3):
        if (board[row][0] == board[row][1] and board[row][1] == board[row][2] and not board[row][0] == '_'):
            return True
    for col in range(3):
        if (board[0][col] == board[1][col] and board[1][col] == board[2][col] and not board[0][col] == '_'):
            return True

    if (board[0][0] == board[1][1] and board[1][1] == board[2][2] and not board[0][0] == '_'):
        return True

    if (board[0][2] == board[1][1] and board[1][1] == board[2][0] and not board[0][2] == '_'):
        return True

    return False


def printBoard(board):
    os.system('cls||clear')
    print("\n Player : X , Agent: O \n")
    for i in range(3):
        print(" ", end=" ")
        for j in range(3):
            if(board[i][j] == '_'):
                print(f"[{i*3+j+1}]", end=" ")
            else:
                print(f" {board[i][j]} ", end=" ")

        print()
    print()


if __name__ == "__main__":
    board = [
            ['_', '_', '_'],
            ['_', '_', '_'],
            ['_', '_', '_']
    ]

    turn = 0
    
    while isMovesLeft(board) and not checkWin(board):
        if(turn == 0):
            printBoard(board)
            print(" Select Your Move :", end=" ")
            tmp = int(input())-1
            userMove = [int(tmp/3),  tmp % 3]
            while((userMove[0] < 0 or userMove[0] > 2) or (userMove[1] < 0 or userMove[1] > 2) or board[userMove[0]][userMove[1]] != "_"):
                print('\n \x1b[0;33;91m' + ' Invalid move ' + '\x1b[0m \n')
                print("Select Your Move :", end=" ")
                tmp = int(input())-1
                userMove = [int(tmp/3),  tmp % 3]
            board[userMove[0]][userMove[1]] = player
            
            print("Player Move:")
            printBoard(board)
            turn = 1
        else:
            bestMove = findBestMove(board)
            board[bestMove[0]][bestMove[1]] = opponent
            print("Agent Move:")
            printBoard(board)
            turn = 0

    if(checkWin(board)):
        if(turn == 1):
            print('\n \x1b[6;30;42m' + ' Player Wins! ' + '\x1b[0m')

        else:
            print('\n \x1b[6;30;42m' + ' Agent Wins! ' + '\x1b[0m')
    else:
        print('\n \x1b[0;33;96m' + ' Draw! ' + '\x1b[0m')

    input('\n Press Enter to Exit... \n')







