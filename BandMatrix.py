#-----------------------------------------------------------------
"""
# Band Matrices
Band Matrices are matrices whose non zero entries are restricted to a diagonal band. They arise in numerical linear algebra.
"""
#-----------------------------------------------------------------
def main():
    n = int(input("n-by-n pattern: "))
    w = int(input("width between main diagonal: "))
    print(f'\n')
    if n < 0 or w < 0:
        print(f'n and w must be no negative')
    else:
        for i in range(1, n + 1):
            for j in range(1, n+1):
                k = j - i
                if k < 0:
                    k = -1 * k
                if k > w:
                    print(f'0  ', end = '')
                else:
                    print(f'*  ', end = '')
            print()


#-----------------------------------------------------------------
"""
A zero (0) for each element whose distance from the main diagonal 
is strictly more than width (w), and an asterisk (*) 
for each entry that is not.
"""
if __name__ == '__main__':
    main()
