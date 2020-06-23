%paste the 'puzzle pieces' folder in desired directory
%copy the directory path below
folder_path='C:\Users\Kapil Singh\Documents\MATLAB\kukaCP\Step 8\Puzzle';
%angle='0';
%slide=1;
%file_path1 = [folder_path,'\puzzle pieces\angle_0\Slide1.PNG']
%file_path2 = [folder_path,'\puzzle pieces\angle_',sprintf('%s',angle),'\Slide',sprintf('%d',(slide)),'.PNG']
for i=1:4;
    if i==1
        angle='0';
    elseif i==2
        angle='plus90';
    elseif i==3
        angle='minus90';
    else
        angle='180';
    end
    for slide=1:12;
        file_path = [folder_path,'\puzzle pieces\angle_',sprintf('%s',angle),'\Slide',sprintf('%d',(slide)),'.PNG'];
        image_library{i,slide}= file_path; %matrix of 12 pieces with 4 orientations of each piece
        size(image_library);
    end
    
end
image_library

%Saving that image library data as .mat file
save('image_library.mat', 'image_library') 

%Selecting a random image at random column and random row
R= randi([1 4])
C= randi([1 12])
random_image=image_library{R,C}
random_image_path={random_image}

%Saving that image path data as .mat file
save('random_image_path.mat', 'random_image_path') 

%make entries 0 after each selection
% i=0;
% while i<=12
%     R= randi([1 4]);
%     C= randi([1 12]);
%     if image_library_2{R,C}~=0
%         random_image=image_library_2{R,C};
%         image_library_2{R,C}=0;
%         i=i+1;
%     else
%     end
% 
% end
% image_library_2

image_library_2=image_library;% dublicate image library
i=1;
j=1;
k=1;
while i<=12 %till 12 random values are picked
    R= randi([1 4]);
    C= randi([1 12]);
    if image_library_2{R,C}~=0
        random_image=image_library_2{R,C};
        unsorted_mat{j,k}= random_image;
        image_library_2{R,C}=0;
        i=i+1;
        j=j+1;
        if j==5
            j=1;
            k=k+1;
        end
    else
    end
    
    
end
image_library_2
unsorted_mat

%Saving that image path data as .mat file
save('unsorted_mat.mat', 'unsorted_mat') 
