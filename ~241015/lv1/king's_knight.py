direction=[[-2,1],[-2,-1],[2,1],[2,-1],[1,-2],[-1,-2],[1,2],[-1,2]]
alphabet={'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8}
count=0
N = input()
def convert_to_coordinates(s):

    col = alphabet[s[0].lower()]
    row = int(s[1])
    return [col, row]

coordinates = convert_to_coordinates(N)

for i in range(len(direction)):
    if 0<coordinates[0]+direction[i][0]<9 and 0<coordinates[1]+direction[i][1]<9 :
        count+=1

print(count)
