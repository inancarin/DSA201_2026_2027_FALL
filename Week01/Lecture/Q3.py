mat = [[1,2,3],
       [4,5,6],
       [9,8,9]]

r1 = 0 # left to rigth diagonal
r2 = 0 # right to left diagonal
for i in range(len(mat)):
    r1 += mat[i][i]
    r2 += mat[i][len(mat)-1-i]

diff = abs(r1 - r2)
print(diff)