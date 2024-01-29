from collections import defaultdict
from queue import Queue


class  graphAdj():
    def __init__(self) -> None:
        self.adjList = defaultdict(list) #default adjacency list of  new node is []
        

    def addEdge(self,u,v,wt=1):
        self.adjList[u] += [(v,wt)]
        self.adjList[v] += [(u,wt)] #comment if directed
    
    def display(self):
        for i in self.adjList.keys():
            print(i,[_ for _,i in self.adjList[i]])
    
    def bfsTraversal(self,ch,vis=None):
        q = Queue()
        if vis ==None:
            vis = dict() # function level visted array, if global nt given
    
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

    def dfsTraversal(self,ch,vis=None):
        stack =[]
        if vis ==None:
            vis = dict() # function level visted array, if global nt given
        stack.append(ch)
        vis[ch]=1

        while stack:
            top = stack.pop()
            print(top,end=" ")

            for nbrNode in self.adjList[top]:
                nbr =nbrNode[0]
                if nbr not in vis:
                    stack.append(nbr)
                    vis[nbr]=1

    






if __name__ == "__main__":
    gp =  graphAdj()
    vis =dict()
    gp.addEdge(1,2)
    gp.addEdge(1,4)
    gp.addEdge(3,1)
    gp.addEdge(3,2)
    gp.addEdge(3,4)

    gp.display()
    
    for node in range(1,5):
        if node not in vis:
            gp.dfsTraversal(node,vis)
            
            print("\n")
    
    

