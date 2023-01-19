import time 

class Sudoku :

    def __init__(self,dim,fileDir):
        self.dim = dim
        self.expandedNodes = 0
        with open(fileDir) as f :
            content = f.readlines()
            self.grid = [list(x.strip()) for x in content]
        self.rv = self.getRemainingValues()
    
    def getNextLocation(self) :
        for i in range(len(self.grid)) :
            for j in range(len(self.grid)) :
                if self.grid[i][j]=='0' :
                    return [i,j]
        return [-1,-1]

    def isSafe(self,x,y,choice) :
        
        # check row :
        for i in range(self.dim) :
            if self.grid[x][i] == choice :
                return False

        # check column :
        for i in range(self.dim) :
            if self.grid[i][y] == choice :
                return False

        # check Box :
        x_index = x - x%3
        y_index = y - y%3
        for i in range(3) :
            for j in range(3) :
                if self.grid[i+x_index][j+y_index] == choice :
                    return False
        return True
    
    def getDomain(self,x,y) :
        RVCell = [str(i) for i in range(self.dim+1)]

        for i in range(self.dim) :
            if self.grid[x][i]!='0':
                if self.grid[x][i] in RVCell :
                    RVCell.remove(self.grid[x][i])


        for i in range(self.dim) :
            if self.grid[i][y]!='0':
                if self.grid[i][y] in RVCell :
                    RVCell.remove(self.grid[i][y])


        x_index = x - x%3
        y_index = y - y%3
        for i in range(3) :
            for j in range(3) :
                if self.grid[x_index + i][y_index + j]!='0' :
                    if self.grid[x_index + i][y_index + j] in RVCell :
                        RVCell.remove(self.grid[x_index + i][y_index + j])
        return RVCell


    def getRemainingValues(self) :
        RV = []
        for x in range(self.dim) :
            for y in range(self.dim) :
                if self.grid[x][y] != '0' :
                    RV.append(['x'])
                else :
                    RV.append(self.getDomain(x,y))
        return RV


    def solveSimpleBackTracking(self) :

        location = self.getNextLocation()
        if location[0]==-1 :
            return True
        else :
            self.expandedNodes +=1
            for choice in range(1,self.dim+1) :
                if self.isSafe(location[0],location[1],str(choice)) :
                    self.grid[location[0]][location[1]] = str(choice)
                    if self.solveSimpleBackTracking() :
                        return True
                    self.grid[location[0]][location[1]] = '0'
        return False

    def SCP(self) :

        location = self.getNextLocation()
        if location[0]==-1 :
            return True
        else :
            self.expandedNodes +=1
            for choice in self.rv[location[0]*9 + location[1]]:
                self.grid[location[0]][location[1]] = str(choice)
                self.rv = self.getRemainingValues()
                if self.solveSimpleBackTracking() :
                    return True
                self.grid[location[0]][location[1]] = '0'
        return False
                        
# grid = [
#     ["0","1","6","3","0","8","4","2","0"],
#     ["8","4","0","0","0","7","3","0","0"],
#     ["3","0","0","0","0","0","0","0","0"],
#     ["0","6","0","9","4","0","8","0","2"],
#     ["0","8","1","0","3","0","7","9","0"],
#     ["9","0","3","0","7","6","0","4","0"],
#     ["0","0","0","0","0","0","0","0","3"],
#     ["0","0","5","7","0","0","0","6","8"],
#     ["0","7","8","1","0","3","2","5","0"],
# ]



sdk1 = Sudoku(9,"./grid.txt")
start1 = time.time() 
sdk1.solveSimpleBackTracking()
end1 = time.time()
sdk2 = Sudoku(9,"./grid.txt")
start2 = time.time() 
sdk2.SCP()
end2 = time.time() 
print("Simple BackTracking :")
print("Number of expanded nodes : ",sdk1.expandedNodes)
print("The time of execution of above program is :",(end1-start1) * 10**3, "ms")
for i  in range(9) :
    print(sdk1.grid[i])
print("SCP :")
print("Number of expanded nodes : ",sdk2.expandedNodes)
for i  in range(9) :
    print(sdk2.grid[i])
print("The time of execution of above program is :",(end2-start2) * 10**3, "ms")

