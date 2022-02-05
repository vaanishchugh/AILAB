def print_b(src):
    state = src.copy()
    state[state.index(-1)] = ' '
    print(f"""
{state[0]} {state[1]} {state[2]}
{state[3]} {state[4]} {state[5]}
{state[6]} {state[7]} {state[8]}
        """)

def h(state, target):
    count=0
    i=0
    for j in state:
        if state[i]!= target[i]:
            count=count+1
    return count

def astar(state,target):
    states = [src]
    g = 0
    visited_states =[]
    while len(states):
        print(f"Level: {g}")
        moves = []
        for state in states:
            visited_states.append(state)
            print_b(state)
            if state == target:
                print("Success")
                return
            moves += [move for move in possible_moves(state, visited_states) if move not in moves]
        costs = [g + h(move, target) for move in moves]
        states = [moves[i] for i in range(len(moves)) if costs[i] == min(costs)]
        g += 1
    print("Fail")
def possible_moves(state,visited_state):
    b = state.index(-1);
    
    d = []
                                    
    if b - 3 in range(9): 
        d.append('u')
    if b not in [0,3,6]: 
        d.append('l')
    if b not in [2,5,8]: 
        d.append('r')
    if b + 3 in range(9): 
        d.append('d')
    
    pos_moves = []
    
    for m in d:
        pos_moves.append(gen(state, m, b))
    
    return [move for move in pos_moves if move not in visited_state]

def gen(state,m, b):
    temp = state.copy()                              
    
    if m == 'u': temp[b-3] , temp[b] = temp[b], temp[b-3]
    if m == 'l': temp[b-1] , temp[b] = temp[b], temp[b-1]
    if m == 'r': temp[b+1] , temp[b] = temp[b], temp[b+1]
    if m == 'd': temp[b+3] , temp[b] = temp[b], temp[b+3]   
    
    return temp

src = [1,2,3,-1,4,5,6,7,8]
target = [1,2,3,4,5,-1,6,7,8]  

       


astar(src, target) 
