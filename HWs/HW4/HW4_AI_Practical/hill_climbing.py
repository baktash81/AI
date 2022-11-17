import sys

def hill_climbing(problem,state):
    ''' Returns a state as the solution of the problem '''
    min = state
    for new_state in problem.neighbors(state) :
        if problem.value(new_state)<=problem.value(min) :
            min = new_state
    return min

def hill_climbing_random_restart(problem, limit = 10):
    state = problem.initial()
    cnt = 0
    while problem.goal_test(state) == False and cnt < limit:
        state = hill_climbing(problem,state)
        cnt += 1
    return state
