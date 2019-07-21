'''
CS 325 Algorithms
Derek Yang
Assignment 5

This program will implement breadth first search using the input from a
text file.  The user will input a text file name at runtime and the program
will go through and use breadth first search to categorize each
wrestler as a "baby face" or "heel".  Each wrestler is given
a pre-determined rivalry from the text file.  The program
will use BFS to check if this is possible or not.  All
results will be outputted into the terminal.
'''

class Vertex:
    def __init__(self):
        self.neighbor = []
        self.wrestler_name = ""
        self.type_of_wrestler = "baby face"
        self.visited = False
        self.length = 0
        self.possible = True

class Map:
    def __init__(self):
        self.length = 0
        self.verticies = {}
        self.possible = True

map = Map()

# builds a map of the wrestler pairs
def build_map(arr_wreslters_in,arr_pairs_in):
    for count in range(len(arr_wreslters_in)):
        x = Vertex()
        x.wrestler_name = arr_wreslters_in[count]
        map.verticies[x.wrestler_name] = x
        for i in range(len(arr_pairs_in)):
            # check if wrestlers are neighbors
            if x.wrestler_name == arr_pairs_in[i]:
                if i % 2 == 0 and arr_pairs_in[i+1] not in x.neighbor:
                    x.neighbor.append(arr_pairs_in[i+1])
                elif i % 2 != 0 and arr_pairs_in[i-1] not in x.neighbor:
                    x.neighbor.append(arr_pairs_in[i-1])

# Feed in the whole map, navigate map, thenadd it to the queue
def bfs(g, s):
    #initialize every vertex
    q = []

    #set verticies to map.verticies for ease of use
    verticies = map.verticies
    verticies[s].visited = True
    verticies[s].type_of_wrestler = "baby face"
    q.append(s)

    #set length of neighbors of s to +1
    for visited in verticies[s].neighbor:
        map.verticies[visited].length = verticies[s].length + 1

    '''
    start at the visited node, go through it's children and seeing if 
    they have been visited, if not add to queue
    '''
    while q:
        s = q.pop(0)
        for i in verticies[s].neighbor:
            node_neighbor = verticies[i]
            if not verticies[i].visited:
                verticies[i].visited = True
                q.append(i)
                if node_neighbor.length < verticies[s].length + 1:
                    node_neighbor.length = verticies[s].length + 1
                if node_neighbor.length %2 == 0:
                    node_neighbor.type_of_wrestler = "baby face"
                elif node_neighbor.length %2 != 0:
                    node_neighbor.type_of_wrestler = "heels"
            if node_neighbor.type_of_wrestler == verticies[s].type_of_wrestler:
                map.possible = False

# searches the map for a specific wrestler using bfs
def search_map(g,s):
    g = g.verticies
    bfs(g,s)
    for i in g:
        if g[i].length == 0 and g[i].wrestler_name != s:
            bfs(g,g[i].wrestler_name)

# prints all wrestlers in map
def print_all(g):
    g = g.verticies
    baby_face = []
    heels = []
    for i in g:
        if g[i].type_of_wrestler == "baby face":
            baby_face.append(g[i].wrestler_name)
        else:
            heels.append(g[i].wrestler_name)
    if map.possible:
        print("Yes Possible")
    else:
        print("Not Possible")
    print("babyfaces: ",end="")
    for b in baby_face:
        print(b+" ",end="")
    print("")
    print("heels: ",end="")
    for c in heels:
        print(c+" ",end="")
    print("")

# opens and processes data file
def process_wrestlers_file(f_in, wrestler_arr_in,pairs_arr_in):
    f = open(f_in,"r+")
    read_one = f.read().splitlines()
    arr_switch = 0
    len_wrester_arr = 0
    len_pairs_arr = 0
    for x in read_one:
        try:
            x = int(x)
            arr_switch = arr_switch + 1
            if arr_switch == 1:
                len_wrester_arr = x
            elif arr_switch == 2:
                len_pairs_arr = x
        except:
            if arr_switch == 1:
                wrestler_arr_in.append(x)
            elif arr_switch == 2:
                pairs_arr_in.append(x)
    pairs_arr_in = [words for strings in pairs_arr_in for words in strings.split()]
    pairs_arr_in = pairs_arr_in[:int(len_pairs_arr)*2]
    return pairs_arr_in


def main():
    arr_wrestlers = []
    arr_pairs = []
    map_wrestlers = []

    file_in = input("Enter Text File Name (include .txt):")
    arr_pairs = process_wrestlers_file(file_in,arr_wrestlers,arr_pairs)
    build_map(arr_wrestlers, arr_pairs)
    search_map(map, arr_wrestlers[0])
    print_all(map)

if __name__ == "__main__":
    main()