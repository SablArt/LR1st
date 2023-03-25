import numpy as np

R1 = 10
R2 = 30
R3 = 15
R4 = 20
R5 = 25
R6 = 30

E1 = 80
E2 = 75
E3 = 15

din = {}

def Det(S): 
  Net = len(S)
  if Net == 2:
    Dsec = S[0][0] * S[1][1] - S[0][1] * S[1][0]
  else:
    Dsec = 0
    for n in range (Net):
      Z = np.copy(S)
      Z = np.delete(Z,0,0)
      Z = np.delete(Z,n,1)
      Y = Det(Z)
      Dsec += (-1) ** n * S[0][n] * Y
  return Dsec

# Создание матрицы

A = np.zeros((6,6))
A[0]  = np.array([0, 0, -1, 0, -1, 1])
A[1]  = np.array([1, 0, 1, 1, 0, 1])
A[2]  = np.array([0, -1, 0,-1, 1, 0])
A[3]  = np.array([0, 0, R3, -R6, -R5, 0])
A[4]  = np.array([-R2, 0, R3, 0, 0, R4])
A[5]  = np.array([-R2,-R1, 0, R6, 0, 0])


# Массив для подстановок
B = np.array([0, 0, 0,(-E3-E1), -E2, E1])

D = np.copy(A)
M = Det(D)


for i in range(6):
  D[0][i] = B[0]
  D[1][i] = B[1] 
  D[2][i] = B[2]
  D[3][i] = B[3] 
  D[4][i] = B[4] 
  D[5][i] = B[5]
  din["X" + str(i)] = Det(D)
  D = np.copy(A)

I1 = din["X0"]/M
I2 = din["X1"]/M
I3 = din["X2"]/M
I4 = din["X3"]/M
I5 = din["X4"]/M
I6 = din["X5"]/M

print("I1 =", I1, "А")
print("I2 =", I2, "А")
print("I3 =", I3, "А")
print("I4 =", I4, "А")
print("I5 =", I5, "А")
print("I6 =", I6, "А")

np.linalg.solve(A,B)
