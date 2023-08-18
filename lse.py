import numpy as np

def least_squares_estimation(X1, X2):
  """ YOUR CODE HERE
  """
  m = X1.shape[0]
  A = np.zeros((m, 9))
  for i in range(X1.shape[0]):
    A[i,:] = np.reshape(np.matmul(X2[i,:].reshape(1,3).T,X1[i,:].reshape(1,3)).T,(1,9))


  u,s,vt = np.linalg.svd(A, full_matrices=True)
  E = vt[8,:].reshape(3,3)
  E = E.T

  un , sn , vtn = np.linalg.svd(E,  full_matrices=True)
  snew = np.array([[1,0,0],[0,1,0],[0,0,0]])
  E = un @ snew @ vtn

  """ END YOUR CODE
  """
  return E

