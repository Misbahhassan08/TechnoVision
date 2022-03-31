#include <opencv2/imgcodecs.hpp>
#include<opencv2/highgui.hpp>
#include<opencv2/imgproc.hpp>
#include<iostream>

using namespace cv;
using namespace std;
Mat imgHSV, mask;
int hmin = 0, smin = 110, vmin = 153;
int hmax = 19, smax = 240, vmax = 255;

string path = "Resources/test_video.mp4";
VideoCapture cap(path);
Mat img;

/////////// Color Detector///////////
int main() {
	//cap.read(img);
	//cvtColor(img, imgHSV, COLOR_BGR2HSV);
	namedWindow("Trackbars", (640, 200));//create a track bar of 640x240
	createTrackbar("hue min", "Trackbars", &hmin, 179);//Creating traackbar
	createTrackbar("hue max", "Trackbars", &hmax, 179);//creating the trackbar to control the Hue,saturation and Value 
	createTrackbar("sat min", "Trackbars", &smin, 255);
	createTrackbar("sat max", "Trackbars", &smax, 255);
	createTrackbar("val min", "Trackbars", &vmin, 255);
	createTrackbar("val max", "Trackbars", &vmax, 255);
	while (true) {
		cap.read(img);
		cvtColor(img, imgHSV, COLOR_BGR2HSV);
		Scalar lower(hmin, smin, vmin);
		Scalar Upper(hmax, smax, vmax);

		inRange(imgHSV, lower, Upper, mask);
		imshow("Image", img);
		imshow("Image HSV", imgHSV);
		imshow("Image Mask", mask);
		waitKey(1);
	}




}