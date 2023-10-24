# 3D Reconstruction from two 2D-images

## Overview

This project exploces the classical computer vision technique (non-deep learning) of converting 2D images into 3D Reconstruction. By harnessing the power of computer vision methodologies and utilities, I converted two images depicting a castle into a three-dimensional representation. A pivotal aspect of this effort was ascertaining the camera's positions when the photographs were captured, followed by the creation of the 3D visual.
<p float="center">
  <img src="https://github.com/satyajeetburla/3D-Reconstruction-from-two-2D-images/blob/main/img/img1.png" width="400" />
  <img src="https://github.com/satyajeetburla/3D-Reconstruction-from-two-2D-images/blob/main/img/img2.png" width="400" /> 
</p>
Highlighted milestones of this endeavor are:

1. **Retrieving 3D Transformations**: 
   - The objective here was to uncover the 3D transformation (R, T) between dual viewpoints. For two points \(P1, P2 in R^3\) that represent the same scene in the first and second frames, the relationship is given by \(P2 = RP1 + T\).

2. **Deriving the Essential Matrix**:
   - **Method of Least Squares**: 
     - I utilized the 8-point technique to deduce the essential matrix \(E\) by way of the SVD decomposition approach.
   - **RANSAC Technique**: 
     - To improve the resilience of the \(E\) derivation, I incorporated the elementary RANSAC method, ensuring protection against inconsistencies from incorrect matches.
     ![Description of Image](https://github.com/satyajeetburla/3D-Reconstruction-from-two-2D-images/blob/main/img/img3.png)
   - **Depicting Epipolar Lines**: 
     - With the help of the essential matrix, I illustrated the epipolar lines on both snapshots, providing insight into the correlation between corresponding points.

3. **Deciphering Pose & Constructing 3D**:
   - **Resolving Twisted Pair Ambiguity**: 
     - Investigated the solutions concerning twisted pair ambiguity associated with \(E\), which gave rise to four potential solutions for the transformation (R, T).
   - **Point Triangulation**: 
     - Points were triangulated to pinpoint the confluence of rays from the two cameras. From the four potential transformations, I refined the 3D construction by opting for the transformation where the majority of the 3D points appeared in the foreground for both cameras.

4. **Reprojection Verification**: 
   - As an essential verification step, I juxtaposed points from one camera's original snapshot against the reprojected points from the alternate camera. This process called for the application of the camera's projection blueprint and a deep dive into the transformation's articulation across the two viewpoints.
<p float="left">
  <img src="https://github.com/satyajeetburla/3D-Reconstruction-from-two-2D-images/blob/main/img/img4.png" width="400" />
  <img src="https://github.com/satyajeetburla/3D-Reconstruction-from-two-2D-images/blob/main/img/img5.png" width="800" /> 
</p>     
