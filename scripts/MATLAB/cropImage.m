function cropped = cropImage(img, left, right, top, bottom)
% cropImage  Crops pixels from all four sides of an image
%
%   cropped = cropImage(img, left, right, top, bottom)
%
%   img    : input image
%   left   : pixels to remove from left
%   right  : pixels to remove from right
%   top    : pixels to remove from top
%   bottom : pixels to remove from bottom
%
%   Returns the cropped image
%
% Example usage:
% * Have the figure you want to save open, and it will
% be caught using gcf
%
% saveas(gcf, 'test.png')
% img = imread('test.png');
% result = cropSides(img, 100);
% imwrite(result, 'test_new.png');

    if any([left right top bottom] < 0)
        error('Crop values must be non-negative');
    end

    [rows, cols, ch] = size(img);

    newWidth  = cols - left - right;
    newHeight = rows - top - bottom;

    if newWidth <= 0 || newHeight <= 0
        error('Cropping too large — image would disappear 🫥');
    end

    cropped = img(top+1 : rows-bottom, left+1 : cols-right, :);
end
