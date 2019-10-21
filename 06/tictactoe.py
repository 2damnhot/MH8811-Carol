#tictactoe Module

def tic(x):
    for v in x:
        for i in v:
            for i in range (len(v)):
                if v[i] == 0:
                    v[i] = 'O'
                if v[i] == 1:
                    v[i] = 'X'
                if v[i] == 2:
                    v[i] = ' '
    return x

if __name__ != "__main__":
    def TicTacDraw(board):
        a = tic(board)
        for i in range(len(a)-1):
            print("|".join(a[i]))
            print('-'*(len(a)+(len(a)-1)))
        print("|".join(a[len(a)-1]))





        
