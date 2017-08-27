def choose_max_up(triangle, row, pos):
    #print("Going up from {} {}".format(row,pos))
    if row == 1:
        return 0
    if row == pos:
        return pos - 1
    
    if pos - 1 >= 0:
        if triangle[row - 1][pos -1] > triangle[row - 1][pos]:
            return pos - 1
        else:
            return pos
    else:
        return pos

def do_path_up(triangle, row, pos):
    if row == 1:
        return [pos, 0]
    
    new_pos = choose_max_up(triangle, row, pos)
    return [pos] + do_path_up(triangle, row - 1, new_pos)

def do_paths(triangle_size):
    if triangle_size == 1:
        return [[0]]
       
    upper_paths = do_paths(triangle_size-1)
    new_paths = []
    for path in upper_paths:
        last_one = path[len(path)-1]
        new_paths.append(path + [last_one])
        new_paths.append(path + [last_one + 1])
    return new_paths

def test():
    rows = 4
    triangle = {0: [3], 1: [7, 4], 2: [2, 4, 6], 3: [8, 5, 9, 3]}

    paths = do_paths(4)
    for path in paths:
        print(path)
        suma = 0
        level = 0
        for i in path:
            suma += triangle[level][i]
            level += 1
        print(suma)
            
            
        
        
