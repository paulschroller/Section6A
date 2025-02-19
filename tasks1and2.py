import numpy as np

#Task 1) Average number of stars in a spherical volume of radius R: n*(4/3)*np.pi*R**3
#if the nearest star is at distance R, that means 0 stars are in that volume
#according to poisson distribution, the probability of 0 stars occuring in this radius would be np.exp(-n*(4/3)*np.pi*R**3)


#Task 2) Revisit hamiltonian on a ring Markov Chain
#Question 1)
def hamconstruct(N):
    matrix = []
    for i in range(2**N):
        istate = bin(i).replace("0b","")
        iarray = []
        for m in range(N):
            if m > len(istate)-1:
                iarray.insert(0,0)
            else:
                iarray.append(int(istate[m]))
        matrixrow = []
        for j in range(2**N):
            jstate = bin(j).replace("0b", "")
            jarray = []
            for l in range(N):
                if l > len(jstate)-1:
                    jarray.insert(0, 0)
                else:
                    jarray.append(int(jstate[l]))

            elementsum = 0
            for k in range(N):
                index1 = k
                index2 = (index1+1)%N
                modifiedstate1 = []
                modifiedstate2 = []
                modifiedstate3 = []
                for p in range(N):
                    modifiedstate1.append(jarray[p])
                    modifiedstate2.append(jarray[p])
                    modifiedstate3.append(jarray[p])
                if modifiedstate1[index2] == 1:
                    modifiedstate1[index2] = 0
                else:
                    modifiedstate1[index2] = 2
                if modifiedstate1[index1] == 0:
                    modifiedstate1[index1] = 1
                else:
                    modifiedstate1[index1] = 2

                if modifiedstate2[index2] == 0:
                    modifiedstate2[index2] = 1
                else:
                    modifiedstate2[index2] = 2
                if modifiedstate2[index1] == 1:
                    modifiedstate2[index1] = 0
                else:
                    modifiedstate2[index1] = 2

                term1 = 1/2
                term2 = 1/2
                term3 = 1/4
                for p in range(N):
                    if modifiedstate1[p] != iarray[p]:
                        term1 = 0
                    if modifiedstate2[p] != iarray[p]:
                        term2 = 0
                    if modifiedstate3[p] != iarray[p]:
                        term3 = 0
                if term3 != 0 and modifiedstate3[index2] != modifiedstate3[index1]:
                    term3 = term3*-1
                elementsum = elementsum + term1 + term2 + term3
            term4 = N/4
            for p in range(N):
                if iarray[p] != jarray[p]:
                    term4 = 0
            elementsum = elementsum + term4
            matrixrow.append(elementsum)
        matrix.append(matrixrow)
    return matrix

def normalizerows(matrix):
    for i in range(len(matrix)):
        rowsum = 0
        for j in range(len(matrix[i])):
            rowsum = rowsum + matrix[i][j]
        for j in range(len(matrix[i])):
            matrix[i][j] = matrix[i][j]/rowsum
    return matrix


matrix3N = hamconstruct(3)
print(normalizerows(matrix3N))

#Question 2:
pi = [1,0,0,0,0,0,0,0]
# this will be stationary