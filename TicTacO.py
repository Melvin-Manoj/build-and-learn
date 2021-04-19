import copy
import random
import math

#throughtout the game player X=1 and O=2
def check_win(a,player):
    #player is an int representing X=1,O=2
    for row in a:
        if row.count(player)==3:
            return True
    for i in range(3):
        if a[0][i]==a[1][i] and a[1][i]==a[2][i] and a[0][i]==player :
            return True
    if a[0][0]==a[1][1] and a[1][1]==a[2][2] and a[1][1]==player :
        return True
    if a[0][2]==a[1][1] and a[1][1]==a[2][0] and a[1][1]==player :
        return True
    return False

def is_draw(board):
    for  row in board:
        for ele in row:
            if ele==0 :
                return False
    return True

class Node:
    #X=1,O=2   always used to find O's movement
    def __init__(self,state,parent,games,wins,player_no):
        self.parent=parent
        self.state=state
        self.games=games
        self.wins=wins
        self.children=[]
        self.player_no=player_no
        
    def get_children(self):
        if len(self.children) != 0 :
            return
        cur_state=self.state
        for i in range(3):
            for j in range(3):
                if cur_state[i][j] == 0 :
                    cur_state[i][j]=3-self.player_no
                    self.children.append(Node(copy.deepcopy(cur_state), self, 0,0,3-self.player_no))
                    cur_state[i][j]=0

    def find_children(self):
        list_child=[]
        cur_state=self.state
        for i in range(3):
            for j in range(3):
                if cur_state[i][j] == 0 :
                    cur_state[i][j]=3-self.player_no
                    list_child.append(Node(copy.deepcopy(cur_state), self, 0,0, 3-self.player_no))
                    cur_state[i][j]=0
        return list_child

def select_promising_node(root_node):
    '''it runs the UCT and returns the best node'''
    if len(root_node.children)==0 :
        return root_node
    max,max_child_index=0,0
    for index,child in enumerate(root_node.children):
        if child.games==0 :
            select_param=math.inf
        else:
            select_param= child.wins/child.games + math.sqrt( 2*math.log(root_node.games)/child.games)
        
        if select_param>max :
            max=select_param
            max_child_index=index
    best_node=root_node.children[max_child_index]
    return best_node

#to expand the node, use the get_children method 

def simulate(root_node):
    children=root_node.find_children()
    if check_win(root_node.state, 2) :
        return 2
    elif check_win(root_node.state, 1) :
        return -2
    elif is_draw(root_node.state) :
        return 1
    else:
        random_index=random.randint(0,len(children)-1)
        root_node=children[random_index]
        return simulate(root_node)

def backpropagate(result, cur_node):
    cur_node.games += 1
    if result==2 :
        if cur_node.player_no==2:
            cur_node.wins += 1
    elif result==-2 :
        if cur_node.player_no==1:
            cur_node.wins += 1
    else:
        cur_node.wins += 0.5
    cur_node=cur_node.parent
    if cur_node != None :
        backpropagate(result, cur_node)

def getMove(root_node, reqd_player_move):
    #root_node=Node(board, None, 0,0, 3-reqd_player_move)
    '''
    This method is called to get the best move
    '''
    for iterations in range(1000):    
        
        promising_node = select_promising_node(root_node)
        #checking if the promising_node is a leaf
        while len(promising_node.children) != 0 :
            promising_node = select_promising_node(promising_node)
        #print(f"len={len(promising_node.children)} but should be 0") #debugging line
        if promising_node.games==0 :
            result= simulate(promising_node)
            backpropagate(result, promising_node)
        else:
            
            #i have to check if a player has already won the game (code added at 8pm)
            # in that case don't make furthur children
            if check_win(promising_node.state,2) or check_win(promising_node.state,1):
                #print("'''''''''   hello")
                #print(promising_node.state)
                result= simulate( promising_node )
                backpropagate(result, promising_node)
            else:
                promising_node.get_children()
            if len( promising_node.children )==0 :
                result= simulate( promising_node )
                backpropagate(result, promising_node)
            else:
                result= simulate( promising_node.children[0] )
                backpropagate(result, promising_node.children[0])
            
    return select_promising_node(root_node) #finally it returns the best move possible