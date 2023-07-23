from numpy import random

def finished(env):
    m = len(env) 
    for i in range(m):
        for j in range(m):
            for k in  range(m):
                if env[i][j][k] == "-":
                    return False
    return True

def winner(m, string,player):
    res1 = "1" * int(m)
    res2 = "0" * int(m)
    if player == "1":
        if string == res1:
            return 1
        elif string == res2:
            return -1
        else:
            return 0
    else:
        if string == res2:
            return 1
        elif string == res1:
            return -1
        else:
            return 0

def check(env, location,player):
    i,j,k = location
    m = len(env)
    stringx = ""
    stringy = ""
    stringz = ""
    stringxy1 = ""  
    stringxy2 = ""
    stringxz1 = ""
    stringxz2 = ""
    stringyz1 = ""
    stringyz2 = ""
    stringxyz1 = ""
    stringxyz2 = ""
    stringxyz3 = ""
    stringxyz4 = ""
    for x in range(m):
        v = env[x][j][k]
        stringx += v
        
        v = env[i][x][k]
        stringy += v
        
        v = env[i][j][x]
        stringz += v
        
        v = env[x][x][k]
        stringxy1 += v

        v = env[x][m-(x+1)][k]
        stringxy2 += v
        
        v = env[x][j][x]
        stringxz1 += v

        v = env[x][j][m-(x+1)]
        stringxz2 += v
        
        v = env[i][x][x]
        stringyz1 += v

        v = env[i][x][m-(x+1)]
        stringyz2 += v
        
        v = env[x][x][x]
        stringxyz1 += v

        v = env[x][x][m-(x+1)]
        stringxyz2 += v

        v = env[x][m-(x+1)][m-(x+1)]
        stringxyz3 += v

        v = env[x][m-(x+1)][x]
        stringxyz4 += v
        
    w = winner(m, stringx,player)  
    if w != 0:
        return w
    w = winner(m, stringy,player)
    if w != 0:
        return w
    w = winner(m, stringz,player)
    if w != 0:
        return w
    w = winner(m, stringxy1,player)
    if w != 0:
        return w
    w = winner(m, stringxy2,player)
    if w != 0:
        return w
    w = winner(m, stringxz1,player)
    if w != 0:
        return w
    w = winner(m, stringxz2,player)
    if w != 0:
        return w
    w = winner(m, stringyz1,player)
    if w != 0:
        return w
    w = winner(m, stringyz2,player)
    if w != 0:
        return w
    w = winner(m, stringxyz1,player)
    if w != 0:
        return w
    w = winner(m, stringxyz2,player)
    if w != 0:
        return w
    w = winner(m, stringxyz3,player)
    if w != 0:
        return w
    w = winner(m, stringxyz4,player)
    if w != 0:
        return w
    

def minimax(env, mx:bool,location,player):
    score = check(env,location,player)
    
    if score == 1:
        return score
    elif score == -1:
        return score
    elif finished(env) == True:
        return 0
    
    if mx:
        return max_value(env,player)
    else:
        return min_value(env,player)

def max_value(env,player):
    value = -1000
    m = len(env)
    for i in range(m):
        for j in range(m):
            for k in range(m):
                if env[i][j][k] == "-":
                    env[i][j][k] = player
                    if value != 1:
                        value = max( value, minimax(env, False,(i,j,k), player))
                    env[i][j][k] = "-"
    return value

def min_value(env,player):
    m = len(env)
    value = +1000
    for i in range(m):
        for j in range(m):
            for k in range(m):
                if env[i][j][k] == "-":
                    env[i][j][k] = player
                    if value != -1:
                        value = min(value, minimax(env, True, (i,j,k),player))
                    env[i][j][k] = "-"
    return value

def findMinimax(env,player):
    m = len(env)
    value = -1000
    bestmove = (-1,-1,-1)
    for i in range(m):
        for j in  range(m):
            for k in range(m):
                if env[i][j][k] == "-":
                    env[i][j][k] = player
                    temp = minimax(env, False, (i,j,k),player)
                    env[i][j][k] = "-"
                    if temp > value:
                        bestmove = (i,j,k)
                        value = temp        
    return bestmove
# alpha beta
def minimaxAlphaBeta(env, mx:bool,location,player, alpha = -1000, beta = 1000):
    score = check(env,location,player)
    
    if score == 1:
        return score
    elif score == -1:
        return score
    elif finished(env) == True:
        return 0
    
    if mx:
        return max_valueAlphaBeta(env,player,alpha,beta)
    else:
        return min_valueAlphaBeta(env,player,alpha,beta)

def max_valueAlphaBeta(env,player,alpha,beta):
    value = -1000
    m = len(env)
    for i in range(m):
        for j in range(m):
            for k in range(m):
                if env[i][j][k] == "-":
                    env[i][j][k] = player
                    if value != 1:
                        value = max( value, minimaxAlphaBeta(env, False,(i,j,k), player,alpha,beta))
                        if value > beta:
                            return value
                        alpha = max(value,alpha)
                    env[i][j][k] = "-"
    return value

def min_valueAlphaBeta(env,player,alpha,beta):
    m = len(env)
    value = +1000
    for i in range(m):
        for j in range(m):
            for k in range(m):
                if env[i][j][k] == "-":
                    env[i][j][k] = player
                    if value != -1:
                        value = min(value, minimaxAlphaBeta(env, True, (i,j,k),player,alpha,beta))
                        if value<alpha:
                            return value
                        beta = min(value,beta)
                    env[i][j][k] = "-"
    return value

def findMinimaxAlphaBeta(env,player):
    m = len(env)
    value = -1000
    bestmove = (-1,-1,-1)
    for i in range(m):
        for j in  range(m):
            for k in range(m):
                if env[i][j][k] == "-":
                    env[i][j][k] = player
                    temp = minimaxAlphaBeta(env, False, (i,j,k),player)
                    env[i][j][k] = "-"
                    if temp > value:
                        bestmove = (i,j,k)
                        value = temp        
    return bestmove

def findRandom(env,player):
    m = len(env)
    while True:
        i,j,k = tuple(random.randint(m, size=m))
        if env[i][j][k] == "-":
            env[i][j][k] = player
            bestmove = (i,j,k)
            break
    return bestmove

def tictoctoe(m,algorithm0, algorithm1):
    env = [[["-" for i in range (m)] for j in range(m)]for k in range(m)]
    player0 = "0"
    player1 = "1"
    counter = 0
    while not finished(env):
        print(counter)
        counter +=1
        if algorithm1 == 1:
            bestMove= findMinimax(env,player1)
        elif algorithm1 == 2:
            bestMove = findMinimaxAlphaBeta(env,player1)
        else:
            bestMove = findRandom(env, player1)

        i,j,k = bestMove
        env[i][j][k] = player1
        if check(env, bestMove, player1)== 1:
            player = player1
            break
        if check(env, bestMove, player1)== -1:
            player = player0
            break
        if algorithm0 == 1:
            bestMove = findMinimax(env, player0)
        elif algorithm0 == 2:
            bestMove = findMinimaxAlphaBeta(env, player0)
        else:
            bestMove = findRandom(env, player0)

        i,j,k = bestMove
        env[i][j][k] = player0
        if check(env, bestMove, player0)== 1:
            player = player0
            break
        if check(env, bestMove, player0)== -1:
            player = player1
            break
    return player, env


if __name__== "__main__":
    while True :
        print("---tictoctoe---")
        m = int(input("dimension: "))
        print("choose algorithm for player0: 0 for random or 1 for minimax or 2 for minimaxAlphaBeta")
        algorithm0 = int(input("algoritm player0: "))
        print("choose algorithm for player1: 0 for random or 1 for minimax or 2 for minimaxAlphaBeta")
        algorithm1 = int(input("algoritm player1: "))
        player,env = tictoctoe(m,algorithm0, algorithm1)
        print(*env, sep = "\n")
        print("winner: player", player)
    