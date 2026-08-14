import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # Write code here
    form = []
    ans = []
    for row in range(len(A[0])):
        for col in range(len(A)):
            form.append(A[col][row])
        ans.append(form[:])
        form.clear() 
    return np.array(ans)
