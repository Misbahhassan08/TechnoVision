#include <opencv2/imgcodecs.hpp>
#include<opencv2/highgui.hpp>
#include<opencv2/imgproc.hpp>
#include<iostream>

using namespace cv;
using namespace std;
/////////// Resizing Image ///////////
void main() {
	string path = "Resources/Profile.jpg";
	Mat img = imread(path);
	Mat imgResize,imgCrop;
	resize(img, imgResize, Size(100, 100));
	Rect roi(100, 100, 300, 250);
	imgCrop = img(roi);
	imshow("Image", img);
	imshow("Image Resize", imgResize);
	imshow("Image Crop", imgCrop);
	waitKey(0);




}
