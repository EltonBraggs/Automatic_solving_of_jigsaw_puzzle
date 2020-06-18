from scipy.io import loadmat
importLib=loadmat('ImageLibrary.mat')
a1=importLib['I']
print(a1[0,0])