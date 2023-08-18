import numpy as np

def reconstruct3D(transform_candidates, calibrated_1, calibrated_2):
  """This functions selects (T,R) among the 4 candidates transform_candidates
  such that all triangulated points are in front of both cameras.
  """

  best_num_front = -1
  best_candidate = None
  best_lambdas = None
  for candidate in transform_candidates:
    R = candidate['R']
    T = candidate['T']

    lambdas = np.zeros((2, calibrated_1.shape[0]))
    """ YOUR CODE HERE
    """
    m = calibrated_1.shape[0]
    for i in range(m):
      x1 = calibrated_1[i,:].reshape(3,1)
      x2 = calibrated_2[i, :].reshape(3, 1)

      A = np.hstack((x2, -R@x1))
      ls = np.linalg.pinv(A) @ T
      lambdas[0, i] = ls[0]
      lambdas[1, i] = ls[1]
    """ END YOUR CODE
    """
    num_front = np.sum(np.logical_and(lambdas[0]>0, lambdas[1]>0))

    if num_front > best_num_front:
      best_num_front = num_front
      best_candidate = candidate
      best_lambdas = lambdas
      print("best", num_front, best_lambdas[0].shape)
    else:
      print("not best", num_front)


  P1 = best_lambdas[1].reshape(-1, 1) * calibrated_1
  P2 = best_lambdas[0].reshape(-1, 1) * calibrated_2
  T = best_candidate['T']
  R = best_candidate['R']
  return P1, P2, T, R