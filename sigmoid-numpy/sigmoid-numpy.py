import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    # Write code here
    x = np.array(x)
    ans = np.divide(1,(np.exp(-x)+1))
    return ans