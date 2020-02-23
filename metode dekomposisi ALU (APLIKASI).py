from numpy import*

 #~~~~~~inisialisasi matrik augment~~~~~#
A = array([[1.,4/10.,16/10.,64/1000.],\
           [1.,7/10.,49/10.,343/1000.],\
           [1.,1.,1.,1.],\
           [1.,13/10.,169/100.,2197/1000.]])
print('Matriks A')
print (A)

b = array([[516/100.],\
           [3347/1000.],\
           [3.],\
           [3228/1000]])
print('')
print('Matriks B')
print(b)
n=len(A)

#========== matrik L dari sini ===================#
L=zeros((n,n))
for i in range(0,n):
    L[i][i]=1

#~~~~~~proses triangularisasi~~~~~~#
for k in range(0,n-1):                  #-----proses pivot dari sini-------#
    if A[k][k]==0:
        for s in range(0,n):
            v=A[k][s]
            u=A[k+1][s]
            A[k][s]=u
            A[k+1][s]=v
#-----proses pivot sampai sini-----#
    for j in range(k+1,n):
        m=A[j][k]/A[k][k]
        L[j][k]=m # nilai m disimpan di matrik L
        for i in range(0,n):
            A[j][i]=A[j][i]-m*A[k][i]
print()
print('Matriks L')
print(L)
 #========== matrik L sampai sini =================#

 #========== matrik U dari sini ===================#
print()
print('Matriks U')
print(A)      
 #========== matrik U sampai sini =================#

#------proses substitusi maju------#
y=zeros((n,1))
y[0][0]=b[0][0]/L[0][0]
for j in range(1,n):
    S=0
    for i in range(0,j):
        S=S+y[i][0]*L[j][i]
    y[j][0]=b[j][0]-S

#------proses substitusi mundur----#
x=zeros((n,1))
x[n-1][0]=y[n-1][0]/A[n-1][n-1]
for j in range(n-2,-1,-1):
    S=0
    for i in range(j+1,n):
        S=S+A[j][i]*x[i][0]
    x[j][0]=(y[j][0]-S)/A[j][j]
print()
print('Solusinya:')
print(x)
