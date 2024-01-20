from datetime import datetime
import random
import math

#Tournament code is preliminary.

#import bots here

bot_list=[]

def Game(bot_list, init_copy, round_count):
    date=datetime.now().strftime('%Y-%m%d-%H%M')
    num_bot = len(bot_list)
    #populate bot pool
    bot_counts=[]
    round_score=[]
    pool_size = len(bot_list) * init_copy
    bot_names = list(map(lambda x: x.__name__ , bot_list))
    bot_data = [[]]
    for i in range(num_bot):
        bot_data.append([])
        bot_data[0].append(0)
        bot_counts.append(init_copy)
        for j in range(num_bot):
            bot_data[i+1].append([])#M, [S, P]

    #run rounds
    file = open(date + " Copies.csv" ,"a+")
    
    file.write("Round,")
    for b in range(num_bot):
        file.write("%s," % bot_names[b])

    file.write("\n") 
        
    file.write("0,") 
    for b in range(num_bot):
        file.write("%s," % bot_counts[b])
    file.write("\n") 
    file.close()
    
    for ROUND in range(round_count):
        
        match_turns = Get_Turns(64)
        print("R:%s/%s T:%s" %(ROUND, round_count, match_turns))
        bot_pool = Get_Pool(bot_list, bot_counts)
        bot_data = Round(bot_list, bot_pool, bot_data, match_turns)
        bot_counts = Judge(bot_list, bot_data[0], pool_size)
        
        file = open(date + " Copies.csv" ,"a+")
        file.write("%s," % (ROUND+1)) 
        for c in bot_counts:
            file.write("%s," % c)
        file.write("\n")
        file.close()
        
    for bot in range(num_bot):
        print("%s : %s" %(bot_names[bot], bot_counts[bot]))


    file = open(date + " Stats.csv" ,"a+")
    
    file.write("Matches,")
    for b in range(num_bot):
        file.write("%s," % bot_names[b])

    file.write(",Avg Shares,")
    for b in range(num_bot):
        file.write("%s," % bot_names[b])

    file.write(",Avg Points,")
    for b in range(num_bot):
        file.write("%s," % bot_names[b])
            
    file.write("\n")
    
    for i in range(num_bot):
        row_match =[]
        row_share =[]
        row_point =[]
        for j in range(num_bot):
            num_match = len(bot_data [i+1][j])
            if(num_match > 0):
                sum_share = sum(stat[0] for stat in bot_data [i+1][j])
                sum_point = sum(stat[1] for stat in bot_data [i+1][j])
                avg_share = sum_share / num_match
                avg_point = sum_point / num_match
            else:
                avg_share = 0
                avg_point = 0

            row_match.append(num_match)
            row_share.append(round(avg_share,2))
            row_point.append(round(avg_point,2))
            
        file.write("%s," % bot_names[i])
        for b in range(num_bot):
            file.write("%s," % row_match[b])
        file.write(",")
            
        file.write("%s," % bot_names[i])
        for b in range(num_bot):
            file.write("%s," % row_share[b])
        file.write(",")
            
        file.write("%s," % bot_names[i])
        for b in range(num_bot):
            file.write("%s," % row_point[b])
        file.write(",")      
        file.write("\n")
    file.close()

    #output data




def Round (bot_list, bot_pool, bot_data, match_turns):
    
    #clear previous point tally
    for i in range(len(bot_list)):
        bot_data[0][i]=0
        
    for k in range(0, len(bot_pool),2):

        #setup addresses
        A_add = bot_pool[k]
        B_add = bot_pool[k+1]
        
        #setup matches
        A_bot = bot_list[A_add]
        B_bot = bot_list[B_add]

        #run matches
        match_data = Match(A_bot, B_bot, match_turns)

        #score matches
        bot_data[0][A_add] += match_data[0][1]
        bot_data[0][B_add] += match_data[1][1]

        #stat tracking
        bot_data[A_add+1][B_add].append(match_data[0])
        bot_data[B_add+1][A_add].append(match_data[1])

    for i in range(len(bot_list)):
        if (bot_data [0][i] < 0):
            bot_data [0][i] = 0
    #print(bot_data[0])
    return bot_data

    
def Match (A_bot, B_bot, match_turns):
    #bots start match with 1 share each
    #match start with empty pot
    P_score = 0
    A_share = 1
    B_share = 1
    A_moves = []
    B_moves = []

    while (match_turns>0):
        match_turns -= 1

        #get bot moves based on existing move lists
        A_move=Limit(A_bot(A_moves, B_moves))
        B_move=Limit(B_bot(B_moves, A_moves))

        #payoff matrix. 0 is Cooperate, 1 is Defect
        if (A_move == 0 and B_move == 0):
            P_score += 3
            
        if (A_move == 1 and B_move == 0):
            P_score += 1
            A_share += 1

        if (A_move == 0 and B_move == 1):
            P_score += 1
            B_share += 1

        if (A_move == 1 and B_move == 1):
            A_share += 1
            B_share += 1
 
        #append move lists            
        A_moves.append(A_move)
        B_moves.append(B_move)

    #Sum of shares becomes divisor
    S_share = A_share + B_share
    
    #Assign final score by fraction of shares taken
    #With only two bots, rounding is always fair
    A_point = round(P_score * A_share / S_share) - A_share
    B_point = round(P_score * B_share / S_share) - B_share 
    
    return [[A_share, A_point],[B_share, B_point]]


def Judge (bot_list, bot_points, pool_size):
    #inputs: bots, bot points, total pool size
    #outputs: new bot counts
    bot_counts = []
    rem_points = []
    sum_points = sum(bot_points)
    
    #zero contingency
    if(sum_points==0):
        for i in range(len(bot_list)):
            bot_counts.append(pool_size // len(bot_list))
            #even distribution
        return(bot_counts)
        
    for j in range(len(bot_list)):
        #first bot count as fraction of total points, rounded down
        #keep point remainder to determine remaining bot addiitons
     
        bot_counts.append((pool_size * bot_points[j]) // sum_points)
        rem_points.append((pool_size * bot_points[j]) % sum_points)

        #determine bot with highest remainder
        #add one copy of that bot to the pool
        #set that bot's remainder to zero
        #repeat until pool is filled

    for i in range(pool_size - sum(bot_counts)):
        bot_index = rem_points.index(max(rem_points))
        bot_counts[bot_index] +=1
        rem_points[bot_index] = 0
    
    return bot_counts

def Limit(move):
    if (move == 0 or move == 1):
        return move
    else:
        return 0

def Get_Turns(base):
    turns = 0
    count = True
    while (count):
        turns += 1
        if(turns >= base and random.randint(0,base) == 0):
            count = False
    return turns

def Get_Pool(bot_list, bot_counts):
    pool=[]
    for i in range (len(bot_list)):
        for j in range(bot_counts[i]):
            pool.append(i)
    #shuffle bot pool      
    pool = random.sample(pool,len(pool))
    return pool


Game(bot_list, 256, 256)
