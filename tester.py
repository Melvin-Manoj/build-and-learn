from TicTacO import *
def gameplay():
    board=[[0,0,0],[0,0,0],[0,0,0]]
    print("hello")
    while( not is_draw(board)):
        while(True):
            inp=input("enter coordinate of X  ")
            i,j=[int(ele) for ele in inp.split()]
            if  i>2 or j>2 or board[i][j]!=0 :
                print("invalid coordinates")
            else:
                board[i][j]=1
                break
        start_node = Node(board, None, 0,0, 1 )
        print("Your move")
        print_state(board) #board after X moved
        if check_win(board, 1): 
            print("player X has won")
            break
        returned_node=getMove(start_node,2)
        if returned_node == None :
            if is_draw:
                print("game draw")
                break
        else:
            board=returned_node.state
        print("AI's move")
        print_state(board) # board after O moved
        
        if check_win(board, 2): 
            print("player O has won")
            break
        if is_draw(board):
            print("Draw")
        
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


def is_draw(board):
    for  row in board:
        for ele in row:
            if ele==0 :
                return False
    return True

if __name__=="__main__":
    gameplay()
        
    


