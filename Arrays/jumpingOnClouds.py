def jumpingOnClouds(c):
    jumps = 0
    while len(c) > 1:
        if len(c) == 2:
            jumps += 1
            break
        else:
            if c[2] == 0:
                c = c[2:]
            elif c[1] == 0:
                c = c[1:]
            jumps += 1
    return jumps