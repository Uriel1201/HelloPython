# %%
# !! {"metadata":{
# !!   "id": "jywBdimLt9Vj"
# !! }}
"""
# Band Matrices
Band Matrices are matrices whose non zero entries are restricted to a diagonal band. They arise in numerical linear algebra.
"""

# %%
# !! {"metadata":{
# !!   "id": "QN12nFSxt367",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1706825816199,
# !!     "user_tz": 360,
# !!     "elapsed": 316,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   }
# !! }}
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

# %%
# !! {"metadata":{
# !!   "id": "gq9IKS47uW5v"
# !! }}
"""
A zero (0) for each element whose distance from the main diagonal is strictly more than width (w), and an asterisk (*) for each entry that is not.
"""

# %%
# !! {"metadata":{
# !!   "id": "eGSEX1D2lRO5",
# !!   "colab": {
# !!     "base_uri": "https://localhost:8080/"
# !!   },
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1706825825236,
# !!     "user_tz": 360,
# !!     "elapsed": 5596,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   },
# !!   "outputId": "172df0ce-2d67-44fb-b07f-b24fefd8817e"
# !! }}
if __name__ == '__main__':
    main()

# %%
# !! {"main_metadata":{
# !!   "colab": {
# !!     "provenance": [],
# !!     "authorship_tag": "ABX9TyOpisRQz+JjZSgf55B8B65Y"
# !!   },
# !!   "kernelspec": {
# !!     "name": "python3",
# !!     "display_name": "Python 3"
# !!   },
# !!   "language_info": {
# !!     "name": "python"
# !!   }
# !! }}
