#Baktash Ansari 99521082


# I wrote some function for each part
# horizontal,vertical and diameter are functions that check for attacking or defending in # game
# if flag be false function check for specific index where lead to winning 
# and when it is true function check for defending against enemy winning
# put function put the cross in vital index of game's state

# link of video : 
#   https://drive.google.com/file/d/1yWx75_nGESfv4b-YTfeoxg1giQqgtAwo/view?usp=sharing

#################################################################################
def horizontal(game_state,flag) :
    for i in range(5) :
        ## two ways :
        if(game_state[i*5+1]==flag and game_state[i*5+2]==flag and flag==True) :
            if game_state[i*5+3]==None :
                return 5*i+3
        elif(game_state[i*5+1]==flag and game_state[i*5+3]==flag and flag==True) :
            if game_state[i*5+2]==None :
                return 5*i+2
        elif(game_state[i*5+2]==flag and game_state[i*5+3]==flag and flag==True) :
            if game_state[i*5+1]==None :
                return 5*i+1
        ################################
        elif(game_state[i*5+0]==flag and  game_state[i*5+1]==flag and  game_state[i*5+2]==flag) :
            if game_state[i*5+3]==None :
                return 5*i+3
        elif( game_state[i*5+1]==flag and  game_state[i*5+2]==flag and  game_state[i*5+3]==flag) :
            if game_state[i*5+4]==None :
                return 5*i+4
            elif game_state[i*5+0]==None :
                return 5*i+0
        elif( game_state[i*5+2]==flag and  game_state[i*5+3]==flag and  game_state[i*5+4]==flag) :
            if game_state[i*5+1]==None :
                return 5*i+1
        elif( game_state[i*5+0]==flag and  game_state[i*5+2]==flag and  game_state[i*5+3]==flag) :
            if game_state[i*5+1]==None :
                return 5*i+1
        elif( game_state[i*5+0]==flag and  game_state[i*5+1]==flag and  game_state[i*5+3]==flag) :
            if game_state[i*5+2]==None :
                return 5*i+2
        elif( game_state[i*5+1]==flag and  game_state[i*5+3]==flag and  game_state[i*5+4]==flag) :
            if game_state[i*5+2]==None :
                return 5*i+2
        elif( game_state[i*5+1]==flag and  game_state[i*5+2]==flag and  game_state[i*5+4]==flag) :
            if game_state[i*5+3]==None :
                return 5*i+3
    return -1

def vertical(game_state,flag) :
    for i in range(5) :
        ## two ways :
        if(game_state[1*5+i]==flag and game_state[2*5+i]==flag and flag==True) :
            if game_state[3*5+i]==None :
                return 5*3+i
        elif(game_state[1*5+i]==flag and game_state[3*5+i]==flag and flag==True) :
            if game_state[2*5+i]==None :
                return 5*2+i
        elif(game_state[2*5+i]==flag and game_state[3*5+i]==flag and flag==True) :
            if game_state[1*5+i]==None :
                return 5*1+i
        ################################
        elif( game_state[0*5+i]==flag and  game_state[1*5+i]==flag and  game_state[2*5+i]==flag) :
            if game_state[3*5+i]==None :
                return 5*3+i
        elif( game_state[1*5+i]==flag and  game_state[2*5+i]==flag and  game_state[3*5+i]==flag) :
            if game_state[4*5+i]==None :
                return 5*4+i
            elif game_state[0*5+i]==None :
                return 5*0+i
        elif( game_state[2*5+i]==flag and  game_state[3*5+i]==flag and  game_state[4*5+i]==flag) :
            if game_state[1*5+i]==None :
                return 5+i
        elif( game_state[0*5+i]==flag and  game_state[2*5+i]==flag and  game_state[3*5+i]==flag) :
            if game_state[1*5+i]==None :
                return 5+i
        elif( game_state[0*5+i]==flag and  game_state[1*5+i]==flag and  game_state[3*5+i]==flag) :
            if game_state[2*5+i]==None :
                return 5*2+i
        elif( game_state[1*5+i]==flag and  game_state[3*5+i]==flag and  game_state[4*5+i]==flag) :
            if game_state[2*5+i]==None :
                return 5*2+i
        elif( game_state[1*5+i]==flag and  game_state[2*5+i]==flag and  game_state[4*5+i]==flag) :
            if game_state[3*5+i]==None :
                return 5*3+i
    return -1

def diameter(game_state,flag) :

# Asli ha(2) :
    ## two ways :
    if(game_state[3*5+1]==flag and game_state[2*5+2]==flag and flag==True) :
        if game_state[1*5+3]==None :
            return 8
    elif(game_state[1*5+3]==flag and game_state[3*5+1]==flag and flag==True) :
        if game_state[2*5+2]==None :
            return 5*2+2
    elif(game_state[2*5+2]==flag and game_state[1*5+3]==flag and flag==True) :
        if game_state[3*5+1]==None :
            return 5*3+1
    ################################
    elif( game_state[4*5+0]==flag and  game_state[3*5+1]==flag and  game_state[2*5+2]==flag) :
        if game_state[1*5+3]==None :
                return 5+3
    elif( game_state[3*5+1]==flag and  game_state[2*5+2]==flag and  game_state[1*5+3]==flag) :
        if game_state[0*5+4]==None :
                return 4
        elif game_state[4*5+0]==None :
                return 20
    elif( game_state[2*5+2]==flag and  game_state[1*5+3]==flag and  game_state[0*5+4]==flag) :
        if game_state[3*5+1]==None :
                return 5*3+1
    elif( game_state[4*5+0]==flag and  game_state[2*5+2]==flag and  game_state[1*5+3]==flag) :
        if game_state[3*5+1]==None :
                return 5*3+1
    elif( game_state[4*5+0]==flag and  game_state[3*5+1]==flag and  game_state[1*5+3]==flag) :
        if game_state[2*5+2]==None :
                return 5*2+2
    elif( game_state[1*5+3]==flag and  game_state[0*5+4]==flag and  game_state[3*5+1]==flag) :
        if game_state[2*5+2]==None :
                return 5*2+2
    elif( game_state[3*5+1]==flag and  game_state[2*5+2]==flag and  game_state[0*5+4]==flag) :
        if game_state[1*5+3]==None :
                return 5+3
    ###############################################################################
    ## two ways :
    elif(game_state[3*5+3]==flag and game_state[2*5+2]==flag and flag==True) :
        if game_state[1*5+1]==None :
            return 6
    elif(game_state[1*5+1]==flag and game_state[3*5+3]==flag and flag==True) :
        if game_state[2*5+2]==None :
            return 5*2+2
    elif(game_state[2*5+2]==flag and game_state[1*5+1]==flag and flag==True) :
        if game_state[3*5+3]==None :
            return 5*3+3
    ################################
    elif( game_state[4*5+4]==flag and  game_state[3*5+3]==flag and  game_state[2*5+2]==flag) :
        if game_state[1*5+1]==None :
                return 5+1
    elif( game_state[3*5+3]==flag and  game_state[2*5+2]==flag and  game_state[1*5+1]==flag) :
        if game_state[0*5+0]==None :
                return 0
        elif game_state[4*5+4]==None :
                return 5*4+4
    elif( game_state[2*5+2]==flag and  game_state[1*5+1]==flag and  game_state[0*5+0]==flag) :
        if game_state[3*5+3]==None :
                return 5*3+3
    elif( game_state[4*5+4]==flag and  game_state[2*5+2]==flag and  game_state[1*5+1]==flag) :
        if game_state[3*5+3]==None :
                return 5*3+3
    elif( game_state[4*5+4]==flag and  game_state[3*5+3]==flag and  game_state[1*5+1]==flag) :
        if game_state[2*5+2]==None :
                return 5*2+2
    elif( game_state[0*5+0]==flag and  game_state[1*5+1]==flag and  game_state[3*5+3]==flag) :
        if game_state[2*5+2]==None :
                return 5*2+2
    elif( game_state[0*5+0]==flag and  game_state[2*5+2]==flag and  game_state[3*5+3]==flag) :
        if game_state[1*5+1]==None :
                return 5+1
#Farei ha(4) :
#1:
    elif( game_state[0*5+1]==flag and  game_state[1*5+2]==flag and  game_state[2*5+3]==flag) :
        if game_state[3*5+4]==None :
                return 5*3+4
    elif( game_state[1*5+2]==flag and  game_state[2*5+3]==flag and  game_state[3*5+4]==flag) :
        if game_state[0*5+1]==None :
                return 1
    elif( game_state[0*5+1]==flag and  game_state[1*5+2]==flag and  game_state[3*5+4]==flag) :
        if game_state[2*5+3]==None :
                return 5*2+3
    elif( game_state[0*5+1]==flag and  game_state[2*5+3]==flag and  game_state[3*5+4]==flag) :
        if game_state[1*5+2]==None :
                return 5*1+2
#2:
    elif( game_state[1*5+0]==flag and  game_state[2*5+1]==flag and  game_state[3*5+2]==flag) :
            if game_state[4*5+3]==None :
                    return 5*4+3
    elif( game_state[2*5+1]==flag and  game_state[3*5+2]==flag and  game_state[4*5+3]==flag) :
        if game_state[1*5+0]==None :
                return 1
    elif( game_state[1*5+0]==flag and  game_state[2*5+1]==flag and  game_state[4*5+3]==flag) :
        if game_state[3*5+2]==None :
                return 5*3+2
    elif( game_state[1*5+0]==flag and  game_state[3*5+2]==flag and  game_state[4*5+3]==flag) :
        if game_state[2*5+1]==None :
                return 5*2+1
#3: 
    elif( game_state[3*5+0]==flag and  game_state[2*5+1]==flag and  game_state[1*5+2]==flag) :
            if game_state[0*5+3]==None :
                    return 3
    elif( game_state[2*5+1]==flag and  game_state[1*5+2]==flag and  game_state[0*5+3]==flag) :
        if game_state[3*5+0]==None :
                return 5*3
    elif( game_state[1*5+2]==flag and  game_state[0*5+3]==flag and  game_state[3*5+0]==flag) :
        if game_state[2*5+1]==None :
                return 5*2+1
    elif( game_state[2*5+1]==flag and  game_state[3*5+0]==flag and  game_state[0*5+3]==flag) :
        if game_state[1*5+2]==None :
                return 5*1+2
#4 :
    elif( game_state[4*5+1]==flag and  game_state[3*5+2]==flag and  game_state[2*5+3]==flag) :
                if game_state[1*5+4]==None :
                        return 5+4
    elif( game_state[3*5+2]==flag and  game_state[2*5+3]==flag and  game_state[1*5+4]==flag) :
        if game_state[4*5+1]==None :
                return 5*4+1
    elif( game_state[2*5+3]==flag and  game_state[1*5+4]==flag and  game_state[4*5+1]==flag) :
        if game_state[3*5+2]==None :
                return 5*3+2
    elif( game_state[3*5+2]==flag and  game_state[4*5+1]==flag and  game_state[1*5+4]==flag) :
        if game_state[2*5+3]==None :
                return 5*2+3
    return -1

def put(game_state) :
    if game_state[2*5+2]==None : 
        return 12
    else :
        for i in range(1,4) :
            for j in range(1,4) :
                if(i==2 and j==2 ):
                    continue
                if game_state[i*5+j]==None :
                    return i*5+j
        for i in range(5) :
            for j in range(5) :
                if game_state[i*5+j]==None :
                    return i*5+j
#################################################################################


def ai_action(game_state):
    ''' Generate and play move from tic tac toe AI'''
    # first check for win : 
    result  = vertical(game_state,False)
    if result !=-1 :
        return result
    result  = horizontal(game_state,False)
    if result !=-1 :
        return result
    result  = diameter(game_state,False)
    if result !=-1 :
        return result
    # seccond check for defend :
    result  = vertical(game_state,True)
    if result !=-1 :
        return result
    result  = horizontal(game_state,True)
    if result !=-1 :
        return result
    result  = diameter(game_state,True)
    if result !=-1 :
        return result
    # third put in vital areas :
    return put(game_state)