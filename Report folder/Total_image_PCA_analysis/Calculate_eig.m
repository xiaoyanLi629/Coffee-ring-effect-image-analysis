clc;
clear;
close all;

X = [];
for ite = 1:60
    filename = strcat(num2str(ite), '.jpg');
    %read data
    RGB = imread(filename);
    %convert colorful image to black and white
    grey = rgb2gray(RGB);
    grey = reshape(grey', [1, 490*490]);
    X = [X; grey];
end

X = double(X);

S = X'*X;
