#Baktash Ansari 99521082 
# I made some changes in Algorithm.py --> get_path 
# get_path had some bug
# so please run my Algorithm.py


from collections import deque
from Utility import Node
from Algorithm import Algorithm


class BFS(Algorithm):
    def __init__(self, grid):
        super().__init__(grid)

    def bfs(self,snake) :
        queue = list()
        visited = list()
        start_state,end_state = self.get_initstate_and_goalstate(snake)
        queue.insert(0,start_state)
        while(len(queue)!=0) :
            global current
            current = queue.pop()
            if end_state.x == current.x and end_state.y==current.y:
                return self.get_path(current)
            if current not in visited :
                visited.append(current)
            for neighbor in self.get_neighbors(current) :
                if neighbor not in queue and neighbor not in visited and not self.outside_boundary(neighbor) and not self.inside_body(snake,neighbor) :
                    neighbor.parent = current
                    queue.insert(0,neighbor)
        return self.get_path(current)

    def run_algorithm(self, snake):
        
        #################################################################################
        if len(self.path)==0 :
            self.bfs(snake)
        return self.path.pop()
        #################################################################################
