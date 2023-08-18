from lse import least_squares_estimation
import numpy as np

def ransac_estimator(X1, X2, num_iterations=60000):
    sample_size = 8

    eps = 10**-4

    best_num_inliers = -1
    best_inliers = None
    best_E = None
    m = X1.shape[0]
    for i in range(num_iterations):
        # permuted_indices = np.random.permutation(np.arange(X1.shape[0]))
        permuted_indices = np.random.RandomState(seed=(i*10)).permutation(np.arange(X1.shape[0]))
        sample_indices = permuted_indices[:sample_size]
        test_indices = permuted_indices[sample_size:]
        """ YOUR CODE HERE
        """

        x1 = X1[sample_indices]
        x2 = X2[sample_indices]

        E = least_squares_estimation(x1, x2)
        #curr_inliers = 0
        inliers = sample_indices
        for j in test_indices:
            #print("j",j)
            y1 = X1[j].reshape(3,1)
            y2 = X2[j].reshape(3,1)

            dis1 = epidis1(y2,y1,E)
            #print(dis1)
            dis2 = epidis2(y2,y1,E)
            #print(dis2)
            dis = dis1 + dis2
            if dis <eps:
                #curr_inliers += 1
                inliers = np.append(inliers, j)
        # if curr_inliers > best_num_inliers:
        #     best_E = E
        #     print("bestE",best_E)
        #     best_num_inliers = curr_inliers
        #     print("best_num_inliers",best_num_inliers)
        #     best_inliers = inliers

        """ END YOUR CODE
        """
        if inliers.shape[0] > best_num_inliers:
            best_num_inliers = inliers.shape[0]
            best_E = E
            best_inliers = inliers

    return best_E, best_inliers



def epidis1(a2,a1,f):
    # distance between a2 and epi a1
    #e3 = np.array([0, 0, 1]).T
    # e3_hat = np.array([[0, -e3[2], e3[1]],
    #                    [e3[2], 0, -e3[0]],
    #                    [-e3[1], e3[0], 0]])
    e3_hat = np.array([[0,-1,0],[1,0,0],[0,0,0]])
    n = e3_hat@f@a1
    norm = np.linalg.norm(n, axis=0)
    dist = np.square(a2.T@f@a1) / np.square(norm)
    return dist
def epidis2(a2,a1,f):
    # distance between a1 and epi a2
    # e3 = np.array([0, 0, 1]).T
    # e3_hat = np.array([[0, -e3[2], e3[1]],
    #                    [e3[2], 0, -e3[0]],
    #                    [-e3[1], e3[0], 0]])
    e3_hat = np.array([[0, -1, 0], [1, 0, 0], [0, 0, 0]])
    # n = e3_hat@f.T@a2
    n = e3_hat @ ((a2.T@f).T)

    norm = np.linalg.norm(n, axis=0)
    dist = np.square(a2.T@f@a1) / np.square(norm)
    return dist




#
# X2 = np.array([0,2,3])
# X1 = np.array([1,4,3])
# E = np.eye(3)
# print(X2.shape,X1.shape,E.shape)
# epidis(X2,X1,E)