import copy
from last import *

def find_level(present):
    if present == None:
        return 0
    return( 1+ find_level(present.parent))

def print_children(root):
    if len(root.children) == 0:
        print('root children no =0')
        return
    lev1=[]
    lev2=[]
    lev3=[]
    games_list=[]
    wins_list=[]
    #loses_list=[]
    print("Root--> Lvl ", find_level(root))
    print_state(root.state)
    for child in root.children:
        lev1.append(child.state[0])
        lev2.append(child.state[1])
        lev3.append(child.state[2])
        games_list.append(child.games)
        wins_list.append(child.wins)
        #loses_list.append(child.loses)
    print("level",find_level(root)+1)
    print(lev1)
    print(lev2)
    print(lev3)
    print(*games_list,sep='           ')
    print(*wins_list, sep='           ')
    #print(*loses_list, sep='           ')
    for child in root.children:
        print_children(child)
    
def print_state(state):
        for i in range(3):
            for j in range(3):
                if state[i][j]==1 :
                    print('X',end="")
                elif state[i][j]==2 :
                    print('O',end="")
                else:
                    print('_',end="")
            print(" ")
        print(" ")


if __name__=="__main__":
    a=[[1,0,1],[1,2,0],[2,0,0]]
    #print(check_win(a,2))
    root=Node(a, None, 0,0, 1)
    print_state(a)
    cur_node =getMove(root,2)
    print_state(cur_node.state)
    print_children(root)
    '''
    list_games=[]
    for i in range(1000):
        list_games.append(simulate(root))
    print("wins=",list_games.count(2))
    print("loses=",list_games.count(-2))
    print("draws=",list_games.count(1))
    '''