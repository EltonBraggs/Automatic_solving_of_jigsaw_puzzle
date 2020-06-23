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
image_library;

%Selecting a random image at random column and random row
R= randi([1 4])
C= randi([1 12])
random_image=image_library{R,C}
random_image_path={random_image}

% %Saving that image path data as .mat file
save('mat_file.mat', 'random_image_path') 