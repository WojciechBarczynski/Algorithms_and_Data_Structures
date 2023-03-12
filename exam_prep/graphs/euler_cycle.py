def check_if_euler_cycle_exist(adjacency_list):
    # + spojnosc
    for vertex in adjacency_list:
        if len(vertex) % 2 != 0:
            return False
    return True
