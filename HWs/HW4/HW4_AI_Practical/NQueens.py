from operator import truediv
from random import randrange


class NQueens:
    def __init__(self, N):
        self.N = N

    def initial(self):
        ''' Returns a random initial state '''
        return tuple(randrange(self.N) for i in range(self.N))

    def goal_test(self, state):
        ''' Returns True if the given state is a goal state 
            I assume that the goal state is when 
        '''
        if self.value(state)==0 :
            return True
        return False

    def value(self, state):
        ''' Returns the value of a state. The higher the value, the closest to a goal state '''
        value = 0
        for i in range(len(state)) :
            for j in range(i+1,len(state)) :
                if state[i] == state[j] :
                    value +=1
                elif abs(state[j]-state[i]) == abs(j-i) :
                    value+=1
        return value 


    def neighbors(self, state):
        ''' Returns all possible neighbors (next states) of a state '''
        neighb = []
        for i in range(len(state)) :
            state_list = list(state)
            for j in range(len(state)) :
                if j==state[i] :
                    continue
                state_list[i] = j
                neighb.append(tuple(state_list))
        return neighb
