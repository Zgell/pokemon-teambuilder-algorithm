# Pokemon Teambuilder Algorithm V2 - Started on Jan. 6th, 2020

TYPE_LIST = ['Normal', 'Fighting', 'Flying', 
            'Poison', 'Ground', 'Rock',
            'Bug', 'Ghost', 'Steel',
            'Fire', 'Water', 'Grass',
            'Electric', 'Psychic', 'Ice',
            'Dragon', 'Dark', 'Fairy']
TYPE_ABUNDANCES = [33/400, 33/400, 36/400, 26/400, 40/400, 24/400, 35/400, 39/400, 26/400, 23/400, 60/400, 41/400, 24/400, 44/400, 30/400, 28/400, 34/400, 32/400]
TYPE_MATRIX = [[1.0, 2.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
               [1.0, 1.0, 2.0, 1.0, 1.0, 0.5, 0.5, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 2.0, 1.0, 1.0, 0.5, 2.0],
               [1.0, 0.5, 1.0, 1.0, 0.0, 2.0, 0.5, 1.0, 1.0, 1.0, 1.0, 0.5, 2.0, 1.0, 2.0, 1.0, 1.0, 1.0],
               [1.0, 0.5, 1.0, 0.5, 2.0, 1.0, 0.5, 1.0, 1.0, 1.0, 1.0, 0.5, 1.0, 0.5, 1.0, 1.0, 1.0, 0.5],
               [1.0, 1.0, 1.0, 0.5, 1.0, 0.5, 1.0, 1.0, 1.0, 1.0, 2.0, 2.0, 0.0, 1.0, 2.0, 1.0, 1.0, 1.0],
               [0.5, 2.0, 0.5, 0.5, 2.0, 1.0, 1.0, 1.0, 2.0, 0.5, 2.0, 2.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
               [1.0, 0.5, 2.0, 1.0, 0.5, 2.0, 1.0, 1.0, 1.0, 2.0, 1.0, 0.5, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
               [0.0, 0.0, 1.0, 0.5, 1.0, 1.0, 0.5, 2.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 2.0, 1.0],
               [0.5, 2.0, 0.5, 0.0, 2.0, 0.5, 0.5, 1.0, 0.5, 2.0, 1.0, 0.5, 1.0, 0.5, 0.5, 0.5, 1.0, 0.5],
               [1.0, 1.0, 1.0, 1.0, 2.0, 2.0, 0.5, 1.0, 0.5, 0.5, 2.0, 0.5, 1.0, 1.0, 0.5, 1.0, 1.0, 0.5],
               [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.5, 0.5, 0.5, 2.0, 2.0, 1.0, 0.5, 1.0, 1.0, 1.0],
               [1.0, 1.0, 2.0, 2.0, 0.5, 1.0, 2.0, 1.0, 1.0, 2.0, 0.5, 0.5, 0.5, 1.0, 2.0, 1.0, 1.0, 1.0],
               [1.0, 1.0, 0.5, 1.0, 2.0, 1.0, 1.0, 1.0, 0.5, 1.0, 1.0, 1.0, 0.5, 1.0, 1.0, 1.0, 1.0, 1.0],
               [1.0, 0.5, 1.0, 1.0, 1.0, 1.0, 2.0, 2.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.5, 1.0, 1.0, 2.0, 1.0],
               [1.0, 2.0, 1.0, 1.0, 1.0, 2.0, 1.0, 1.0, 2.0, 2.0, 1.0, 1.0, 1.0, 1.0, 0.5, 1.0, 1.0, 1.0],
               [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.5, 0.5, 0.5, 0.5, 1.0, 2.0, 2.0, 1.0, 2.0],
               [1.0, 2.0, 1.0, 1.0, 1.0, 1.0, 2.0, 0.5, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0, 1.0, 1.0, 0.5, 2.0],
               [1.0, 0.5, 1.0, 2.0, 1.0, 1.0, 0.5, 1.0, 2.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0, 0.5, 1.0]]

weakness_pool = []
wlist = []
type_breakdown = {}

def weaknesses_1(typeinput):
    x = TYPE_LIST.index(typeinput)
    i = 0
    wk = []
    while (i < 18):
        if (TYPE_MATRIX[x][i] == 2.0): #It's a weakness
            wk.append(TYPE_LIST[i]) #Add weakness to list
        i = i + 1
    return wk

def weaknesses_2(type1, type2):
    x = TYPE_LIST.index(type1)
    y = TYPE_LIST.index(type2)
    i = 0
    wk = []
    while (i < 18):
        type_matchup = TYPE_MATRIX[x][i] * TYPE_MATRIX[y][i]
        if (type_matchup == 2.0):
            wk.append(TYPE_LIST[i])
        elif (type_matchup == 4.0): #4x weakness, add to pool twice
            wk.append(TYPE_LIST[i])
            #wk.append(TYPE_LIST[i]) (Remove this for now)
        i = i + 1
    return wk    

# ===== MAIN =====
print("Please choose your first type:")
input1 = input('--> ')
print("Please choose your second type:")
input2 = input('--> ')
#input1 = 'Rock'             # TEMPORARY
#input2 = 'Ground'            # TEMPORARY
weakness_pool = weakness_pool + weaknesses_2(input1, input2) #Add weaknesses to weakness pool
for x in weakness_pool:
    wlist = wlist + weaknesses_1(x)
    wlist.sort()
type_breakdown = {i:wlist.count(i) for i in wlist}
#Multiply each type by some number correlating to the type's abundance (to make it so there's no ties/equal values)
i = 0
while (i < len(TYPE_LIST)): #Iterate through all the types
    if TYPE_LIST[i] in type_breakdown: #If one of the types is in the weakness list...
        #MULTIPLY BY ABUNDANCE FACTOR
        type_breakdown[TYPE_LIST[i]] = type_breakdown[TYPE_LIST[i]] * TYPE_ABUNDANCES[i]
        type_breakdown[TYPE_LIST[i]] = type_breakdown[TYPE_LIST[i]] / len(weaknesses_1(TYPE_LIST[i])) #Divide by number of weaknesses of cover
        ###############print(TYPE_LIST[i])
    i = i + 1

#Pick the top type(s)
max_type_factor_1 = max(type_breakdown.keys(), key=(lambda k: type_breakdown[k]))
################print(type_breakdown)
wlist = []
type_breakdown = {}
#Run through weakness pool, remove any that are now covered, run through everything again with wlist/type_breakdown
i = 0
while (i < len(weakness_pool)):
    if max_type_factor_1 in weaknesses_1(weakness_pool[i]): #If the type is already covered...
        weakness_pool.remove(weakness_pool[i]) #Remove the type
    i = i + 1

for x in weakness_pool:
    wlist = wlist + weaknesses_1(x)
    wlist.sort()
type_breakdown = {i:wlist.count(i) for i in wlist}
#Multiply each type by some number correlating to the type's abundance (to make it so there's no ties/equal values)
i = 0
while (i < len(TYPE_LIST)): #Iterate through all the types
    if TYPE_LIST[i] in type_breakdown: #If one of the types is in the weakness list...
        #MULTIPLY BY ABUNDANCE FACTOR
        type_breakdown[TYPE_LIST[i]] = type_breakdown[TYPE_LIST[i]] * TYPE_ABUNDANCES[i]
        type_breakdown[TYPE_LIST[i]] = type_breakdown[TYPE_LIST[i]] / len(weaknesses_1(TYPE_LIST[i])) #Divide by number of weaknesses of cover
        ###############print(TYPE_LIST[i])
    i = i + 1

try:
    max_type_factor_2 = max(type_breakdown.keys(), key=(lambda k: type_breakdown[k]))
except ValueError:
    max_type_factor_2 = max_type_factor_1

#print(wlist)
###########print(type_breakdown)
if (max_type_factor_1 == max_type_factor_2):
    print("The Best Counter: " + max_type_factor_1)
if (max_type_factor_1 != max_type_factor_2):
    print("The Best Counter: " + max_type_factor_1 + " / " + max_type_factor_2)
print("Press anything to continue.")
x = input()
#print(type_breakdown[max_type_factor])
#print(sorted(type_breakdown.values()))