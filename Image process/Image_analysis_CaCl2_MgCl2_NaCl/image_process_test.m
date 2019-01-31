clc;
clear;
close all;

final_result = [];
% for BWthreshold = 0.85:0.02:0.95
for BWthreshold = 0.95
    for noise_threshold = 6 %5:1:15
    
total_perimeter = 0;
%1 column: total particle numbers for BW_2
%2 column: particle average perimeter for BW_2
%3 column: particle average ara for BW_2

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%4 column: largest particle perimeter
%5 column: largest particle area
%6 column: small particles average perimeter
%7 column: small particles average area
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%4 column: total particle numbers for BW_3
%5 column: particle average perimeter for BW_3
%6 column: particle average area for BW_3

warning('off','all')

properties_data = [];
histogram_RGB_total = [];

mkdir T_temp;
mkdir T_1;
mkdir BW_1;
mkdir T_2;
mkdir BW_2;
mkdir BW_3;
mkdir BW_2_BW_3;
mkdir largest_object;
mkdir smallest_object;
mkdir middle_object;
mkdir new_images_joint;
mkdir histogram_per;
mkdir histogram_area;
mkdir histogram_RGB;

for ite = 1:15
    filename = strcat(num2str(ite), '.jpg');
    %read data
    RGB = imread(filename);
    %histogram equalization
    RGB = histeq(RGB);
    %convert colorful image to black and white
    T = im2bw(RGB, BWthreshold);

    %figure;
    %imshow(T);
    %title("T");

    T_1=0;

%make the frame all 0
    for m = 1:490
        T_1(1, m) = 0;
        T_1(490, m) = 0;
    end


    for n = 1:490
        T_1(n, 1) = 0;
        T_1(n, 490) = 0;
    end

    %T_temp is used as reference
    T_temp = T;

    T_2 = T_1;

%T_temp is the BW version of original image

    filename_write = ['/T_temp/', filename];
    %mkdir T_temp;
    imwrite(T_temp,[pwd, filename_write]);

%T_1 is to enlarge objects
    for m = 2:489
        for n = 2:489
            if T_temp(n,m) == 1
                T_1(n-1,m-1) = 1;
                T_1(n-1,m) = 1;
                T_1(n-1,m+1) = 1;
                T_1(n,m-1) = 1;
                T_1(n,m) = 1;
                T_1(n,m+1) = 1;
                T_1(n+1,m-1) = 1;
                T_1(n+1,m) = 1;
                T_1(n+1,m+1) = 1;
            end
        end
    end

    %figure;
    %imshow(T_1);
    %title("T_1");
    
    filename_write = ['/T_1/', filename];
    %mkdir T_1;
    imwrite(T_1,[pwd, filename_write]);
    
    %BW_1 is to find edge of T_1
    BW_1 = edge(T_1, 'canny');
    
    %calculate total particles number
    %calculate average particle perimeter
    per_1 = regionprops(BW_1, 'Perimeter');
    
    particle_number = size(per_1);
    
    %particle number
    %properties_data(ite, 1) = particle_number(1);
    
    per_1 = struct2cell(per_1);
    per_1 = cell2mat(per_1);
    
    particle_average_perimeter = sum(per_1)/particle_number(1);
    
    %particle average perimeter
    %properties_data(ite, 2) = particle_average_perimeter;

    %calculate average particle area
    area_1 = regionprops(BW_1, 'Area');
    area_1 = struct2cell(area_1);
    area_1 = cell2mat(area_1);
    particle_average_area = sum(area_1)/particle_number(1);
    
    %particle average area
    %properties_data(ite, 3) = particle_average_area(1);
    
    
    
    filename_write = ['/BW_1/', filename];
    %mkdir BW_1;
    imwrite(BW_1,[pwd, filename_write]);
    
    
    %per_1 = struct2cell(per_1);
    %per_1 = cell2mat(per_1);
    %perimeter_1 = sum(per_1);

    
    %T_2 is to shrink the object
    for m = 2:489
        for n = 2:489
            if T_1(n-1,m-1) == 1 && T_1(n-1,m) == 1 && T_1(n-1,m+1) == 1 && T_1(n,m-1) == 1 && T_1(n,m) == 1 && T_1(n,m+1) == 1 && T_1(n+1,m-1) == 1 && T_1(n+1,m) == 1 && T_1(n+1,m+1) == 1
                T_2(n,m) = 1;
            else
                T_2(n,m) = 0;
            end
        end
    end

    %figure;
    %imshow(T_2);
    %title("T_2");
    
    %BW_2 is to find the edge of T_2, BW_2 is more reasonale
    BW_2 = edge(T_2, 'canny');
    
    per_2 = regionprops(BW_2, 'Perimeter');
    
    per_2 = struct2cell(per_2);
    per_2 = cell2mat(per_2);
    
    perimeter_2 = sum(per_2);

    particle_number_BW_2 = size(per_2);
    properties_data(ite, 1) = particle_number_BW_2(2);
    
    
    particle_average_perimeter_BW_2 = sum(per_2)/particle_number_BW_2(2);
    
    %particle average perimeter for BW_2
    properties_data(ite, 2) = particle_average_perimeter_BW_2;

    %calculate average particle area
    area_2 = regionprops(BW_1, 'Area');
    area_2 = struct2cell(area_2);
    area_2 = cell2mat(area_2);
    particle_average_area_BW_2 = sum(area_1)/particle_number_BW_2(2);
    
    %particle average area
    properties_data(ite, 3) = particle_average_area_BW_2(1);
    
    
    
    
    filename_write = ['/T_2/', filename];
    %mkdir T_2;
    imwrite(T_2,[pwd, filename_write]);
    
    filename_write = ['/BW_2/', filename];
    %mkdir BW_2;
    imwrite(BW_2,[pwd, filename_write]);
    
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    %remove noise dots
    %BW_3 is the noise remove version of BW_2
    
    T_2_median = medfilt2(T_2, [noise_threshold, noise_threshold]);
    %T_2_median = medfilt2(T_2_median, [10, 10]);

    BW_3 = edge(T_2_median, 'canny');
    %figure;
    %imshowpair(BW_2,BW_3,'montage');
    per_3 = regionprops(BW_3, 'Perimeter');
    per_3 = struct2cell(per_3);
    per_3 = cell2mat(per_3);
    perimeter_3 = sum(per_3);

    %calculate BW_3 average particle area
    area_3 = regionprops(BW_3, 'Area');
    area_3 = struct2cell(area_3);
    area_3 = cell2mat(area_3);
    
    particle_number_BW_3 = size(per_3);
    particle_average_per_BW_3 = sum(per_3)/particle_number_BW_3(2);

    particle_average_area_BW_3 = sum(area_3)/particle_number_BW_3(2);
    
    %BW_3 particle average area
    
    properties_data(ite, 4) = particle_number_BW_3(2);

    properties_data(ite, 5) = particle_average_per_BW_3(1);

    properties_data(ite, 6) = particle_average_area_BW_3(1);
    
    
    total_perimeter(ite) = perimeter_3;

    filename_write = ['/BW_3/', filename];
    %mkdir BW_3;
    imwrite(BW_3,[pwd, filename_write]);
    
    joint_image_BW_2_BW_3 = cat(2, BW_2, BW_3);
    filename_write_joint_BW_2_BW_3 = ['/BW_2_BW_3/', filename];
    %mkdir BW_2_BW_3;
    imwrite(joint_image_BW_2_BW_3,[pwd, filename_write_joint_BW_2_BW_3]);
    
    %calculate largest 1 object perimeter and area
    largest_object = bwareafilt(BW_3,1);
    
    largest_object_perimeter = regionprops(largest_object, 'Perimeter');
    largest_object_perimeter = struct2cell(largest_object_perimeter);
    largest_object_perimeter = cell2mat(largest_object_perimeter);
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    %properties_data(ite, 4) = largest_object_perimeter;

    largest_object_area = regionprops(largest_object, 'Area');
    largest_object_area = struct2cell(largest_object_area);
    largest_object_area = cell2mat(largest_object_area);
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    %properties_data(ite, 5) = largest_object_area;
    
    filename_write_largest_object = ['/largest_object/', filename];
    %mkdir largest_object;
    imwrite(largest_object,[pwd, filename_write_largest_object]);

    %calculate smallest 10% object average perimeter and area
    smallest_object = bwareafilt(BW_3, round(particle_number(1)/3), 'smallest');
    
    smallest_object_perimeter = regionprops(smallest_object, 'Perimeter');
    smallest_object_perimeter = struct2cell(smallest_object_perimeter);
    smallest_object_perimeter = cell2mat(smallest_object_perimeter);
    smallest_object_average_perimeter = sum(smallest_object_perimeter)/max(size(smallest_object_perimeter));
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    %properties_data(ite, 6) = smallest_object_average_perimeter;
    
    smallest_object_area = regionprops(smallest_object, 'Area');
    smallest_object_area = struct2cell(smallest_object_area);
    smallest_object_area = cell2mat(smallest_object_area);
    smallest_object_average_area = sum(smallest_object_area)/max(size(smallest_object_area));
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    %properties_data(ite, 7) = smallest_object_average_area;
  
    
    filename_write_smallest_object = ['/smallest_object/', filename];
    %mkdir smallest_object;
    imwrite(smallest_object,[pwd, filename_write_smallest_object]);
    
    
    
    
    %calculate middle objet perimeter and area
    middle_object = bwareafilt(BW_3, [20, 100]);
    filename_write_middle_object = ['/middle_object/', filename];
    %mkdir middle_object;
    imwrite(middle_object,[pwd, filename_write_middle_object]);
    
    joint_image = cat(2,BW_3,largest_object);
    filename_write_joint = ['/new_images_joint/', filename];
    %mkdir new_images_joint;
    imwrite(joint_image,[pwd, filename_write_joint]);

    per_without_0 = per_3(per_3 >0);
    figure('visible', 'off');
    per_3_histogram = histogram(per_without_0, 50);
    ylim([0, 10]);
    %mkdir histogram_per;
    saveas(per_3_histogram, [pwd, '/histogram_per/', num2str(ite), '.jpg'], 'jpg');
    close;
    
    area_without_0 = area_3(area_3 >0);
    figure('visible', 'off');
    area_3_histogram = histogram(area_without_0, 50);
    ylim([0, 10]);
    %mkdir histogram_area;
    saveas(area_3_histogram, [pwd, '/histogram_area/', num2str(ite), '.jpg'], 'jpg');
    close;
    
    residue = mod(ite, 10);
    if residue == 0
        disp([num2str(ite), ' images processed']);
    end
    
    %RGB_eq = histeq(RGB);
    
    Red = RGB(:, :, 1);
    Green = RGB(:, :, 2);
    Blue = RGB(:, :, 3);
    
    
    %%%%%This works in command line but not work in script
    %red_histogram = histogram(Red, 'Normalization', 'probability');
    %green_histogram = histogram(Green, 'Normalization', 'probability');
    %blue_histogram = histogram(Blue, 'Normalization', 'probability');
    
    filename_red = ['/histogram_RGB/R_', filename];
    filename_green = ['/histogram_RGB/G_', filename];
    filename_blue = ['/histogram_RGB/B_', filename];
    
    %mkdir histogram_RGB;
    
    fh_1 = figure('visible', 'off');
    histogram(Red, 256, 'Normalization', 'probability');
    ylim([0, 0.07]);
    title('Red Pixel Histogram');
    xlabel('Red Intensity');
    ylabel('Frequency');
    saveas(fh_1, [pwd, filename_red]);
    close(fh_1);
    
    fh_2 = figure('visible', 'off');
    histogram(Green, 256, 'Normalization', 'probability');
    ylim([0, 0.08]);
    title('Green Pixel Histogram');
    xlabel('Green Intensity');
    ylabel('Frequency');
    saveas(fh_2, [pwd, filename_green]);
    close(fh_2);
    
    fh_3 = figure('visible', 'off');
    histogram(Blue, 256, 'Normalization', 'probability');
    ylim([0, 0.14]);
    title('Blue Pixel Histogram');
    xlabel('Blue Intensity');
    ylabel('Frequency');
    saveas(fh_3, [pwd, filename_blue]);
    close(fh_3);

    R_histogram = imread([pwd, filename_red]);
    G_histogram = imread([pwd, filename_green]);
    B_histogram = imread([pwd, filename_blue]);
    
    %R,G,B images joint together
    histogram_RGB = cat(2, R_histogram, G_histogram, B_histogram);
    
    histogram_RGB_total = cat(1, histogram_RGB_total, histogram_RGB);
        
    total_area_3_cell(ite) = {area_without_0'};
    total_per_3_cell(ite) = {per_without_0'};
    

end

temp_fig = figure('visible', 'off');
plot(properties_data(:, 6))
fig_name = ['/Results/', num2str(BWthreshold), '_', num2str(noise_threshold) '.jpg'];
saveas(temp_fig, [pwd, fig_name]);
close;


histogram_total = figure('visible', 'off');
edges = [0:10:350];
hold on;
histogram(cell2mat(total_area_3_cell(1)), edges, 'FaceColor', 'red')
histogram(cell2mat(total_area_3_cell(2)), edges, 'FaceColor', 'red')
histogram(cell2mat(total_area_3_cell(3)), edges, 'FaceColor', 'red')
histogram(cell2mat(total_area_3_cell(4)), edges, 'FaceColor', 'red')
histogram(cell2mat(total_area_3_cell(5)), edges, 'FaceColor', 'red')

histogram(cell2mat(total_area_3_cell(6)), edges, 'FaceColor', 'blue')
histogram(cell2mat(total_area_3_cell(7)), edges, 'FaceColor', 'blue')
histogram(cell2mat(total_area_3_cell(8)), edges, 'FaceColor', 'blue')
histogram(cell2mat(total_area_3_cell(9)), edges, 'FaceColor', 'blue')
histogram(cell2mat(total_area_3_cell(10)), edges, 'FaceColor', 'blue')

histogram(cell2mat(total_area_3_cell(11)), edges, 'FaceColor', 'green')
histogram(cell2mat(total_area_3_cell(12)), edges, 'FaceColor', 'green')
histogram(cell2mat(total_area_3_cell(13)), edges, 'FaceColor', 'green')
histogram(cell2mat(total_area_3_cell(14)), edges, 'FaceColor', 'green')
histogram(cell2mat(total_area_3_cell(15)), edges, 'FaceColor', 'green')

ylim([0, 250]);
title('Histogram of particles area distribution');
xlabel('Area distribution');
ylabel('Frequency');
mkdir histogram_total;
filename_histogram_total = ['/histogram_total/', 'Histogram of particles area distribution.jpg'];

saveas(histogram_total, [pwd, filename_histogram_total]);
close(histogram_total);



   % histogram_area_total = histogram(total_area_3, 50);
    %ylim([0, 90]);
    %saveas(histogram_area_total, [pwd, 'histogram_area_total', num2str(ite), '.jpg'], 'jpg');
    %close;
    
    %histogram_per_total = histogram(total_per_3, 50);
    %ylim([0, 90]);
    %saveas(histogram_per_total, [pwd, 'histogram_per_total', num2str(ite), '.jpg'], 'jpg');
    %close;

%filename = 'properties_data.csv';

empty_line = zeros(1, 6); 

properties_data = [empty_line; properties_data];

properties_data = num2cell(properties_data);

properties_data(1,1) = {'total particle numbers for BW_2'};
properties_data(1,2) = {'particle average perimeter for BW_2'};
properties_data(1,3) = {'particle average area for BW_2'};
properties_data(1,4) = {'total particle numbers for BW_3'};
properties_data(1,5) = {'particle average perimeter for BW_3'};
properties_data(1,6) = {'particle average area for BW_3'};


csvname = ['total_properties_', num2str(BWthreshold), '_', num2str(noise_threshold) '.csv'];
fid = fopen(csvname, 'w') ;
fprintf(fid, '%s,', properties_data{1,1:end-1}) ;
fprintf(fid, '%s\n', properties_data{1,end}) ;
fclose(fid) ;
dlmwrite(csvname, properties_data(2:end,:), '-append') ;

%csvwrite(filename, properties_data);

clc;

    end

end

