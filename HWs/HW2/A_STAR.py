#Baktash Ansari
#99521082

from sys import flags
from Utility import Node
from Algorithm import Algorithm

# open is frontier and close is explored_set 
class A_STAR(Algorithm):
    def __init__(self, grid):
        super().__init__(grid)

    def run_algorithm(self, snake) :
        start,end = self.get_initstate_and_goalstate(snake)
        open = [start]
        close = []
        self.path = []
        while(len(open)>0):
            global current
            current = min(open,key = lambda l:l.f)
            open.remove(current)
            if current.equal(end) :
                return self.get_path(current)            
            for neighb in self.get_neighbors(current) :
                if  not self.inside_body(snake,neighb) and  not self.outside_boundary(neighb):
                    flag = True
                    cost = current.g +1
                    neighb.h = self.manhattan_distance(neighb,end)
                    func = cost + neighb.h
                    for node in open :
                        if node.x==neighb.x and node.y==neighb.y and node.f<func :
                            flag = False
                            
                        elif node.x==neighb.x and node.y==neighb.y:
                            open.remove(node)
                            
                    # if not flag :
                    #     for node in close :
                    #         if node.x==neighb.x and node.y==neighb.y and node.f<func :
                    #             flag = False
                                
                    #         elif node.x==neighb.x and node.y==neighb.y:
                    #             close.remove(node)
                                
                    if(neighb not in close and flag==True):
                        neighb.parent = current
                        neighb.g = cost
                        neighb.f = func
                        open.append(neighb)
            close.append(current)
        return None


