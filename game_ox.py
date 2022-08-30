#list = [['-', '-', '-'],['-', '-', '-']]
#print(list)
list = [['-'] * 3 for i in range(3)]
class game_1:
    def __init__(self, tate, yoko, s) -> None:
        self.__tate = tate
        self.__yoko = yoko
        self.__s = s

    def set(self, yoko, tate, list, s):
        for i in range(yoko):
            for j in range(tate):
                list[i][j] = s

    def show(self, yoko, tate, list):
        print(" ")
        for i in range(yoko):
            print(" " + str(i), end="")
        print("")
        for i in range(yoko):
            print(i, end="")
            for j in range(tate):
                print(list[i][j], end=" ")
            print("")

    def turn(self, yoko, tate, list, s):
        print(str(s)+"の番です")
        #b, c = int(input("入力してください"))
        b, c = (int(x) for x in input().split())
        if list[b][c] != '-':
            print("入力されています")
            return 1
        list[b][c] = s
        return 0

    def judge(self, yoko, tate, list, s):
        for j in range(tate):
            for i in range(yoko):
                if list[i][j] != s:
                    break
                if i == yoko-1:
                    return 1
        for i in range(yoko):
            for j in range(tate):
                if list[i][j] != s:
                    break
                if j==tate-1:
                    return 1
        for i in range(yoko):
            if list[i][i] != s:
                break
            if i == yoko-1:
                return 1
        for i in range(yoko):
            if list[i][yoko-1-i] != s:
                break
            if i == yoko-1:
                return 1
        for i in range(yoko):
            for j in range(tate):
                if list[i][j] == '-':
                    return 0
        return 2

game = game_1(3, 3, 'o')
yoko = 3
tate = 3
game.set(yoko, tate, list, '-')
game.show(yoko, tate, list)

while(True):
    if game.turn(yoko,tate,list,'o')!=0 and game.turn(yoko,tate,list,'o')!=1:
        game.show(yoko,tate,list)
    else: game.show(yoko,tate,list)
    if game.judge(yoko,tate,list,'o')!=0:
        break
    if game.turn(yoko,tate,list,'x')!=0 and game.turn(yoko,tate,list,'x')!=1:
        game.show(yoko,tate,list)
    else: game.show(yoko,tate,list)
    if game.judge(yoko,tate,list,'x')!=0:
        break
if game.judge(yoko,tate,list,'o')==1:
    print("oの勝ち")
if game.judge(yoko,tate,list,'x')==1:
    print("xの勝ち")
if game.judge(yoko,tate,list,'o')==2:
    print("引き分け")