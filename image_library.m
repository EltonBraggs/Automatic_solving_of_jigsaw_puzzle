%Image Path Library. Use custom path as per your convenient 
I11='C:\Users\HP\Desktop\Mechatronic\Scientific Project\Photo Library\1,1.png'
I12='C:\Users\HP\Desktop\Mechatronic\Scientific Project\Photo Library\1,2.png'
I13='C:\Users\HP\Desktop\Mechatronic\Scientific Project\Photo Library\1,3.png'
I14='C:\Users\HP\Desktop\Mechatronic\Scientific Project\Photo Library\1,4.png'
I15='C:\Users\HP\Desktop\Mechatronic\Scientific Project\Photo Library\1,5.png'
I16='C:\Users\HP\Desktop\Mechatronic\Scientific Project\Photo Library\1,6.png'
I17='C:\Users\HP\Desktop\Mechatronic\Scientific Project\Photo Library\1,7.png'
I18='C:\Users\HP\Desktop\Mechatronic\Scientific Project\Photo Library\1,8.png'
I19='C:\Users\HP\Desktop\Mechatronic\Scientific Project\Photo Library\1,9.png'
I20='C:\Users\HP\Desktop\Mechatronic\Scientific Project\Photo Library\2,0.png'
I21='C:\Users\HP\Desktop\Mechatronic\Scientific Project\Photo Library\2,1.png'
I22='C:\Users\HP\Desktop\Mechatronic\Scientific Project\Photo Library\2,2.png'
I23='C:\Users\HP\Desktop\Mechatronic\Scientific Project\Photo Library\2,3.png'
I24='C:\Users\HP\Desktop\Mechatronic\Scientific Project\Photo Library\2,4.png'
I25='C:\Users\HP\Desktop\Mechatronic\Scientific Project\Photo Library\2,5.png'
I26='C:\Users\HP\Desktop\Mechatronic\Scientific Project\Photo Library\2,6.png'
I27='C:\Users\HP\Desktop\Mechatronic\Scientific Project\Photo Library\2,7.png'
I28='C:\Users\HP\Desktop\Mechatronic\Scientific Project\Photo Library\2,8.png'
I29='C:\Users\HP\Desktop\Mechatronic\Scientific Project\Photo Library\2,9.png'
I30='C:\Users\HP\Desktop\Mechatronic\Scientific Project\Photo Library\3,0.png'

%Creating a library with image path Matrice
ImageLibrary = ({I11 I12 I13 I14 I15 I16 I17 I18 I19 I20; I21 I22 I23 I24 I25 I26 I27 I28 I29 I30})

%Selecting a random image at random column and random row
R= randi([1 2])
C= randi([1 10])
ImagePath=ImageLibrary{R,C}
I={ImagePath}

%Saving that image path data as .mat file
save('ImageLibrary.mat', 'I') 