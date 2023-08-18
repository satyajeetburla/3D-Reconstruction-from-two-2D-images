import numpy as np

def pose_candidates_from_E(E):
  transform_candidates = []
  ##Note: each candidate in the above list should be a dictionary with keys "T", "R"
  """ YOUR CODE HERE
  """
  u,s,vt = np.linalg.svd(E)
  R_pos = np.array([[0,-1,0],[1,0,0],[0,0,1]])
  R_neg = np.array([[0, 1, 0], [-1, 0, 0], [0, 0, 1]])

  R1 = np.dot(np.dot(u, R_pos.T),vt)
  R2 = np.dot(np.dot(u, R_neg.T), vt)
  T1 = u[:,2]
  T2 = -u[:,2]
  transform_candidates = [{"T":T1,"R":R1},{"T":T1,"R":R2},{"T":T2,"R":R1},{"T":T2,"R":R2}]

  """ END YOUR CODE
  """
  return transform_candidates