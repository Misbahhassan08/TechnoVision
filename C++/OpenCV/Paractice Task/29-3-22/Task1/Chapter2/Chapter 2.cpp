#include <opencv2/imgcodecs.hpp>
#include<opencv2/highgui.hpp>
#include<opencv2/imgproc.hpp>
#include<iostream>

using namespace cv;
using namespace std;
/////////// Basic Function///////////
void main() {
	string path = "Resources/Profile.jpg";
	Mat img = imread(path);
	Mat imgGray, imgBlur,imgCanny,imgDil,imgErode;//Decalring objects
	Mat kernel = getStructuringElement(MORPH_RECT, Size(5, 5));

	cvtColor(img,imgGray, COLOR_BGR2GRAY);//Functioon to convert image into gray scale
	GaussianBlur(img, imgBlur, Size(5, 5), 5, 0);//Convert into Blur Image 
	Canny(imgBlur, imgCanny, 50, 100);//Edge detection
	dilate(imgCanny, imgDil, kernel);//To dilate the image 
	erode(imgDil, imgErode, kernel);
	imshow ("Image", img);
	imshow("ImageGray", imgGray);
	imshow("ImageBlur", imgBlur);
	imshow("ImageCanny", imgCanny);
	imshow("ImageErode", imgErode);
	imshow("ImageDil", imgDil);
	waitKey(0);




}
