from scipy.io import loadmat
importLib=loadmat('mat_file.mat')
a1=importLib['I']
print(a1[0,0])