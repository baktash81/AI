#Baktash Ansari 99521082 
# I made some changes in Algorithm.py --> get_path 
# get_path had some bug
# so please run my Algorithm.py


from Utility import Node
from Algorithm import Algorithm


class DFS(Algorithm):
    def __init__(self, grid):
        super().__init__(grid)


    def dfs(self,snake) :
        stack = list()
        visited = list()
        start_state,end_state = self.get_initstate_and_goalstate(snake)
        stack.append(start_state)
        while(len(stack)!=0) :
            global current
            current = stack.pop()
            if end_state.x == current.x and end_state.y==current.y:
                return self.get_path(current)
            if current not in visited :
                visited.append(current)
            for neighbor in self.get_neighbors(current) :
                if neighbor not in stack and neighbor not in visited and not self.outside_boundary(neighbor) and not self.inside_body(snake,neighbor) :
                    neighbor.parent = current
                    stack.append(neighbor)
        return self.get_path(current)

    def run_algorithm(self, snake):
        
        #################################################################################
        if len(self.path)==0 :
            self.dfs(snake)
        return self.path.pop()
        #################################################################################
