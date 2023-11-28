import numpy as np
import cv2 


def compute_homography(src, dst):
  '''Computes the homography from src to dst.
   Input:
    src: source points, shape (N, 2), where N >= 4
    dst: destination points, shape (N, 2)
   Output:
    H: homography from source points to destination points, shape (3, 3)'''

  #making matrix A from src and dst points

  a = np.zeros([2*len(src),9])
  for i in range(len(src)):
    a[2*i,:]=[src[i,0],src[i,1],1,0,0,0,-src[i,0]*dst[i,0],-src[i,1]*dst[i,0],-dst[i,0]]
    a[2*i+1,:]=[0,0,0,src[i,0],src[i,1],1,-src[i,0]*dst[i,1],-src[i,1]*dst[i,1],-dst[i,1]]
  # print("A: ",a)

  #finding out eigenvalues and eigenvectors of AtA

  c,d = np.linalg.eigh(np.dot(np.transpose(a),a))
  d=d[:,0]
  d=d/d[-1]
  # print(d)
  H = np.reshape(d,[3,3])
  # print("H: ",H)
  return H

##############################
# TO DO: Implement the apply_homography function

def apply_homography(src, H):
  '''Applies a homography H to the source points.
   Input:
      src: source points, shape (N, 2)
      H: homography from source points to destination points, shape (3, 3)
   Output:
     dst: destination points, shape (N, 2)
  '''

  dst= np.zeros([len(src),2])
  for i in range(len(src)):
    temp = np.dot(H,np.array([src[i,0],src[i,1],1]))
    dst[i]=[temp[0]/temp[2],temp[1]/temp[2]]
  # print("dst: ",dst)
  return dst


def warp_img(src_img, H, dst_img_size):
  '''Warping of a source image using a homography.
   Input:
      src_img: source image with shape (m, n, 3)
      H: homography, with shape (3, 3), from source image to destination image
      dst_img_size: height and width of destination image; shape (2,)
   Output:
      dst_img: destination image; height and width specified by dst_img_size parameter
  '''

  dst_img = np.zeros((dst_img_size[0],dst_img_size[1],3))
  m,n = dst_img_size[0],dst_img_size[1]
  p,q = src_img.shape[0],src_img.shape[1]

  H = np.mat(H)
  H_inv = np.linalg.inv(H)



  for i in range(m):
    for j in range(n):

      temp = np.dot(H_inv,np.array([i,j,1]))
      temp1 = temp[0,0]/temp[0,2]
      temp2 = temp[0,1]/temp[0,2]

      if 0<=int(temp1)<p and 0<=int(temp2)<q:
        dst_img[i,j]=src_img[int(temp1),int(temp2)]

  return dst_img

trapezoid_pts = np.array([[490 ,2690], [1660,2690], [2030,3350], [70,3350]], dtype='float32') # for portrait mode in 4K (3840x2160)

#rectangle points
rectangle_pts = np.array([[0,0],[1920,0],[1920,1080],[0,1080]],dtype='float32')

custom_H = compute_homography(trapezoid_pts,rectangle_pts)
perspective_matrix = cv2.getPerspectiveTransform(trapezoid_pts, rectangle_pts)

print(custom_H)
print(perspective_matrix)


image=cv2.imread("test_13_11/cards_nouser.jpg")


# Apply the perspective transformation to the image

# custom_image = warp_img(image,custom_H,(1080, 1920))
custom_image = cv2.warpPerspective(image,custom_H,(1920,1080))
td_image = cv2.warpPerspective(image, perspective_matrix, (1920, 1080)) 
td_image = cv2.rotate(td_image,cv2.ROTATE_180)
cv2.imshow('cv',td_image)
cv2.imshow('custom',custom_image)

cv2.waitKey()