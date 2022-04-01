#include <opencv2/imgcodecs.hpp>
#include<opencv2/highgui.hpp>
#include<opencv2/imgproc.hpp>
#include<iostream>

using namespace cv;
using namespace std;
/////////// Images///////////
Mat imgOrignal, imgGray, imgCanny,imgThre,imgBlur,imgDil,imgErode,imgWarp,imgCrop;
vector<Point>initialPoints,docPoints;
float w = 420, h = 596;
Mat preProcessing(Mat img) {
	Mat kernel = getStructuringElement(MORPH_RECT, Size(3, 3));
	cvtColor(img, imgGray, COLOR_BGR2GRAY);//Functioon to convert image into gray scale
	GaussianBlur(img, imgBlur, Size(5, 5), 5, 0);//Convert into Blur Image 
	Canny(imgBlur, imgCanny, 25, 75);//Edge detection
	dilate(imgCanny, imgDil, kernel);//To dilate the image 
	//erode(imgDil, imgErode, kernel);
	return imgDil;
	 }
vector<Point> getContours(Mat image) {

	vector<vector<Point>>contours;
	vector < Vec4i >hierarchy;
	findContours(image, contours, hierarchy, RETR_EXTERNAL, CHAIN_APPROX_SIMPLE);
	//drawContours(img, contours, -1, Scalar(255, 0, 255), 2);
	vector<vector<Point>>conPoly(contours.size());
	vector<Rect>boundRect(contours.size());
	string objectType;
	vector<Point> biggest;
	
	int maxArea=0;
	for (int i = 0; i < contours.size(); i++)//find the area of shapes 
	{
		int area = contourArea(contours[i]);
		cout << area << endl;

		if (area > 1000) {

			float peri = arcLength(contours[i], true);
			approxPolyDP(contours[i], conPoly[i], 0.02 * peri, true);//Count the edges 

			if (area > maxArea && conPoly[i].size() == 4) //if biggest area found its gonna replace with area 
			{
				//drawContours(imgOrignal, contours, i, Scalar(255, 0, 255), 5);
				biggest = { conPoly[i][0],conPoly[i][1] ,conPoly[i][2],conPoly[i][3] };
				maxArea = area;
			}

			//putText(img, objectType, { boundRect[i].x,boundRect[i].y - 5 }, FONT_HERSHEY_PLAIN, 1, Scalar(0, 0, 255), 2);
			//rectangle(img, boundRect[i].tl(), boundRect[i].br(), Scalar(0, 255, 0), 5);//It draw the rectangle around the shape}
			//drawContours(imgOrignal, contours, i, Scalar(255, 0, 255), 1);
		}
	}
	return biggest;
}

void drawPoints(vector<Point>points, Scalar color) {
	for (int i = 0; i < points.size(); i++) {
		circle(imgOrignal, points[i], 10, color, FILLED);//draw circle around the edges of paper
		putText(imgOrignal, to_string(i), points[i], FONT_HERSHEY_PLAIN, 4, color, 4);//put numbering at the edges

	}


}
vector<Point>reorder(vector<Point>points) {
	vector<Point>newPoints;
	vector<int>sumPoints, subPoints;
	for (int i = 0; i < 4; i++) {
		sumPoints.push_back(points[i].x + points[i].y);
		subPoints.push_back(points[i].x - points[i].y);
	}
	newPoints.push_back(points[min_element(sumPoints.begin(), sumPoints.end()) - sumPoints.begin()]);//0
	newPoints.push_back(points[max_element(subPoints.begin(), subPoints.end()) - subPoints.begin()]);///1
	newPoints.push_back(points[min_element(subPoints.begin(), subPoints.end()) - subPoints.begin()]);//2
	newPoints.push_back(points[max_element(sumPoints.begin(), sumPoints.end()) - sumPoints.begin()]);//3

	return newPoints;
}
Mat getWarp(Mat img, vector<Point>points, float w, float h) {
	Point2f src[4] = { points[0],points[1],points[2],points[3] };//point get by using paint
	Point2f dst[4] = { {0.0f,0.0f},{w,0.0f},{0.0f,h }, { w,h } };//w is the width and h is the height
	Mat matrix = getPerspectiveTransform(src, dst);
	warpPerspective(img, imgWarp, matrix, Point(w, h));
	return imgWarp;
}
void main() {
	string path = "Resources/paper.jpg";
	imgOrignal = imread(path);
	//resize(imgOrignal, imgOrignal, Size(), 0.5, 0.5);
	//Pre processing
	imgThre=preProcessing(imgOrignal);

	//get contours-Biggest 
	initialPoints =getContours(imgThre);
	//drawPoints(initialPoints,Scalar(0,0,255));//draw the points at edges 
	docPoints = reorder(initialPoints);
	//drawPoints(docPoints, Scalar(0,255, 0));
	//Warp
	imgWarp = getWarp(imgOrignal, docPoints, w, h);
	//crop
	int cropVal = 10;
	Rect roi(cropVal, cropVal, w - (2 * cropVal), h - (2 * cropVal));
	imgCrop = imgWarp(roi);
	Mat img = imread(path);
	imshow("Image Orignal", imgOrignal);
	imshow("Image Threshold", imgThre);
	imshow("Image Warp", imgWarp);
	imshow("Image Crop", imgCrop);
	waitKey(0);




}