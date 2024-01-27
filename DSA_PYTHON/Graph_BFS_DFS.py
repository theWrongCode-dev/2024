from collections import defaultdict
from queue import Queue


class Graph():
    def __init__(self,n) -> None:
        #create a adjMatrix Sq. of size n
        self.n = n+1  #size of graph
        self.adjMatrix = [[0]*n for _ in range(self.n)] # 2D matrix
    
    def addEdge(self,u,v,wt=1):
        #it's  undirected graph
        self.adjMatrix[u][v] =wt
        #self.adjMatrix[v][u] =1
    
    def display(self):
        for row in self.adjMatrix:
            print(row)

class  graphAdj():
    def __init__(self) -> None:
        self.adjList = defaultdict()
        self.adjList.default_factory=list  #set default valud to []
        

    def addEdge(self,u,v,wt=1):
        self.adjList[u] += [(v,wt)]
        self.adjList[v] += [(u,wt)] #comment if directed
    
    def display(self):
        for i in self.adjList.keys():
            print(i,[_ for _,i in self.adjList[i]])
    
    def bfsTraversal(self,ch):
        q = Queue()
        #vis = defaultdict(default_factory=0)
        
        q.put(ch)
        vis[ch]=1

        while not q.empty():
            frntNode = q.get()
            print(frntNode,end=" ")

            for nbrNode in self.adjList[frntNode]:
                nbr = nbrNode[0]
                if nbr not in vis:
                    q.put(nbr)
                    vis[nbr]=1

    def dfsTraversal(self,ch):
        stack =[]
        stack.append(ch)
        vis[ch]=1

        while len(stack)>0:
            top = stack.pop()
            print(top,end=" ")

            for nbrNode in self.adjList[top]:
                nbr =nbrNode[0]
                if nbr not in vis:
                    stack.append(nbr)
                    vis[nbr]=1

            




vis = defaultdict(default_factory=0)  #this is visited bool

if __name__ == "__main__":
    gp =  graphAdj()
    vis = defaultdict(default_factory=0)
    gp.addEdge(1,2)
    gp.addEdge(1,4)
    gp.addEdge(3,1)
    gp.addEdge(3,2)
    gp.addEdge(3,4)

    gp.display()
    
    for node in range(1,5):
        if node not in vis:
            gp.dfsTraversal(node)
            print("\n")
    
    

