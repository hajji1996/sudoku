from tkinter import *

def chiffres_ligne(L,i):
    A=[]
    for j in L[i]:
        if j != 0:
            A.append(j)
    return A

def chiffres_colonne(L,i):
    A=[]
    for j in range(9):
        if 0 != L[j][i]:
            A.append(L[j][i])
    return A

def chiffres_bloc(L,i,j):
    i1=3*(i//3)
    j1 = 3*(j//3)
    A=[]
    for k in range(i1,i1+3):
        for l in range(j1,j1+3):
            if L[k][l] != 0 :
                A.append(L[k][l])
    return A

def chiffres_conflit(L,i,j):
    return chiffres_ligne(L,i)+chiffres_colonne(L,j)+chiffres_bloc(L,i,j)

def case_suivante(i,j):
    if j==8:
            return i+1,0
    else:
        return i,j+1

def chiffres_possible(L,i,j):
    A= chiffres_conflit(L,i,j)
    B=[]
    for k in range(1,10):
        if k not in A:
            B.append(k)
    return B

def solution_sudoku(L):
    def aux(i,j):
        if i==9 and j==0:
            return True
        if L[i][j] != 0:
            i,j=case_suivante(i,j)
            return aux(i,j)
        for k in chiffres_possible(L,i,j) :
                    L[i][j] = k
                    i1,j1 = case_suivante(i,j)
                    if aux(i1,j1):
                        return True
        L[i][j]=0
        return False
    return aux(0,0)

def test():
    L=[]
    for i in range(1,12):
        M=[]
        for j in range(1,12):
            if (i % 4 == 0 ) or (j % 4 == 0 ):
                pass
            else:
                if cases[i-1][j-1].get() =='':
                    M.append(0)
                else:
                    M.append( int(cases[i-1][j-1].get()))
        if M != []:
            L.append(M)
    if solution_sudoku(L):
        i1=0
        for i in range(1,12):
            j1=0
            if i % 4 == 0 :
                pass
            else :
                for j in range(1,12):
                    if j % 4 == 0 :
                        pass
                    else:
                        cases[i-1][j-1].delete(0,END)
                        cases[i-1][j-1].insert(0,str(L[i1][j1]))
                        j1+=1
                i1+=1



cases = [ [],[],[],[],[],[],[],[],[],[],[] ]
f=Tk()

dx, dy = 35,20
X0, Y0 = 100, 30
f.geometry("600x500+64+0")
text =Label(f,text="Sudoku",fg="red")
text.pack()
for u in range(1, 12):
    for v in range(1, 12):
        k=StringVar()
        cases[u-1].append(Entry( f , textvariable = k , width =5))
        if (v % 4 == 0 and v != 0) or (u % 4 == 0 and u != 0):
            pass
        else :
            cases[u-1][v-1].place(x=v*dx + X0, y=u*dy + Y0)
    text1 =Label(f,text='               ')
    text.pack()

bouton = Button(f,text="Resoudre",command=test)
bouton.pack(side=BOTTOM,padx=100,pady=30)
f.mainloop()
