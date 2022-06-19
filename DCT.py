import numpy as np

a = np.matrix([[0,255,0,255,0,255,0,255],
          [255,0,255,0,255,0,255,0],
          [0,255,0,255,0,255,0,255],
          [255,0,255,0,255,0,255,0],
          [0,255,0,255,0,255,0,255],
          [255,0,255,0,255,0,255,0],
          [0,255,0,255,0,255,0,255],
          [255,0,255,0,255,0,255,0]])




#a=np.matrix([[61,19,50,20],
#          [82,26,61,45],
#          [89,90,82,43],
#          [93,59,53,97]])

A = np.zeros((8, 8))
shape = a.shape[1]
for i in range(8):
    for j in range(8):
        if i == 0:
            x = np.sqrt(1/shape)
        else:
            x = np.sqrt(2/shape)
        A[i][j] = x * np.cos(np.pi * (j + 0.5) * i / shape)  # 与维数相关

A_T = A.transpose()
Y1 = np.matmul(A, a)
Y= np.matmul(Y1, A_T)
print(Y)

a_dct = np.matmul(A_T, Y)
a_dct = np.matmul(a_dct, A)
print('a_dct',a_dct )


'''
想要近似值可以尝试这样输出
for i in range(shape):
    for j in range(shape):
        print('{:^8.4f}'.format(Y[i][j]),end='\n')
print()
'''

git config --global user.name "lianliu1"
git config --global user.email ge32mur@mytum.de