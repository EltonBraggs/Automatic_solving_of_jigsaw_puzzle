%paste the 'puzzle pieces' folder in desired directory
%copy the directory path below
folder_path='C:\Users\Kapil Singh\Documents\MATLAB\kukaCP\Step 8\Puzzle';
%angle='0';
%slide=1;
%file_path1 = [folder_path,'\puzzle pieces\angle_0\Slide1.PNG']
%file_path2 = [folder_path,'\puzzle pieces\angle_',sprintf('%s',angle),'\Slide',sprintf('%d',(slide)),'.PNG']

%code to make a image library of 12 pieces with 4 orientation each
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
%image library with 4 different orientations
%angle 0    %1  2   3   4   5   6   7   8   9   10  11  12
%angle +90  %1  2   3   4   5   6   7   8   9   10  11  12
%angle -90  %1  2   3   4   5   6   7   8   9   10  11  12
%angle 180  %1  2   3   4   5   6   7   8   9   10  11  12

%Saving that image library data as .mat file
save('image_library.mat', 'image_library') 

%Selecting a random image at random column and random row
R= randi([1 4])
C= randi([1 12])
random_image=image_library{R,C}
random_image_path={random_image}

%Saving that image path data as .mat file
save('random_image_path.mat', 'random_image_path') 

%code to make entries 0 after each selection
%image_library_2=image_library;% dublicate image library
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

% code to generate a unsorted matrix 
image_library_2=image_library;% dublicate image library
i=1;
j=1;
k=1;
columns={1 2 3 4 5 6 7 8 9 10 11 12};
while i<=12 %till 12 random values are picked
    R= randi([1 4]);
    while true
        C= randi([1 12]);
        if columns{C}~=0; %ensure the orientation is not picked already 
            C=C;
            columns{C}=0; %make the position void
            break;
        else
        end
    end
    
    if image_library_2{R,C}~=0 %ensure the cell was not picked already
        random_image=image_library_2{R,C};
        unsorted_mat{j,k}= random_image;
        image_library_2{R,C}=0; %make the position void
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

%correct matrix with right piece orientation and position
%1  5   9
%2  6   10
%3  7   11
%4  8   12

%code to generate correct_mat
i=1;
for k=1:3
    for j=1:4
        correct_mat{j,k}=image_library{1,i};
        i=i+1;
    end
end
correct_mat

%Saving that image path data as .mat file
save('correct_mat.mat', 'correct_mat') 

%code to find the right position of each piece in the unsorted matrix
k1=1;
k2=1;

while k2<4
    i=1;
    e1=1;
    e2=1;
    %     for j=1:12
    %         if strcmp(unsorted_mat{k1,k2},image_library{i,j})==1
    %             disp(sprintf('piece %d, %d',e1,e2)); % C-like fprintf-function
    %         elseif strcmp(unsorted_mat{k1,k2},image_library{i+1,j})==1
    %             disp(sprintf('piece %d, %d',e1,e2)); % C-like fprintf-function
    %         elseif strcmp(unsorted_mat{k1,k2},image_library{i+2,j})==1
    %             disp(sprintf('piece %d, %d',e1,e2)); % C-like fprintf-function
    %         elseif strcmp(unsorted_mat{k1,k2},image_library{i+3,j})==1
    %             disp(sprintf('piece %d, %d',e1,e2)); % C-like fprintf-function
    %         else
    %         end
    for j=1:12
        if strcmp(unsorted_mat{k1,k2},image_library{i,j})==1 || ...
                strcmp(unsorted_mat{k1,k2},image_library{i+1,j})==1 || ...
                strcmp(unsorted_mat{k1,k2},image_library{i+2,j})==1 || ...
                strcmp(unsorted_mat{k1,k2},image_library{i+3,j})==1
            disp(sprintf('piece location on matrix 4x3 is %d, %d',e1,e2)); % C-like fprintf-function
        else
        end
        
        e1=e1+1;
        if e1==5
            e1=1;
            e2=e2+1;
        end
        
    end
    
    k1=k1+1;
    if k1==5
        k1=1;
        k2=k2+1;
    end
end