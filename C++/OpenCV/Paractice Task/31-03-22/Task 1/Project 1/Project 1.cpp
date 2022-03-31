#include <opencv2/imgcodecs.hpp>
#include<opencv2/highgui.hpp>
#include<opencv2/imgproc.hpp>
#include<iostream>

using namespace cv;
using namespace std;
vector < vector<int>>myColors{ {0,19,110,240,163,255}/////Orange 
	,{62,72,156,102,126,255},////Green 
	{0,62,0,35,255,255 } };////orange
vector < Scalar>myColorValues{
	{0,255,255},///Orange
	{0,255,0},//green
	{51,153,255}
};//Orange ///Which color to show when these are detected 
Mat img;
vector<vector<int>>newPoints;
 Point getContours(Mat imgDil) {

	vector<vector<Point>>contours;
	vector < Vec4i >hierarchy;
	findContours(imgDil, contours, hierarchy, RETR_EXTERNAL, CHAIN_APPROX_SIMPLE);
	drawContours(img, contours, -1, Scalar(255, 0, 255), 2);
	vector<vector<Point>>conPoly(contours.size());
	vector<Rect>boundRect(contours.size());
	string objectType;
	Point myPoint(0, 0);
	for (int i = 0; i < contours.size(); i++)//find the area of shapes 
	{
		int area = contourArea(contours[i]);
		cout << area << endl;
		
		if (area > 1000) {

			float peri = arcLength(contours[i], true);
			approxPolyDP(contours[i], conPoly[i], 0.02 * peri, true);//Count the edges 

			cout << conPoly[i].size() << endl;
			boundRect[i] = boundingRect(conPoly[i]);
			myPoint.x = boundRect[i].x + boundRect[i].width / 2;
			myPoint.y = boundRect[i].y;

			
			putText(img, objectType, { boundRect[i].x,boundRect[i].y - 5 }, FONT_HERSHEY_PLAIN, 1, Scalar(0, 0, 255), 2);
			rectangle(img, boundRect[i].tl(), boundRect[i].br(), Scalar(0, 255, 0), 5);//It draw the rectangle around the shape}
			drawContours(img, contours, i, Scalar(255, 0, 255), 1);
		}
	}
 return myPoint;
}
 vector < vector<int>> findColor(Mat img) {
	 Mat imgHSV;
	 cvtColor(img, imgHSV, COLOR_BGR2HSV);
	 Point myPoint(0, 0);
	 for (int i = 0; i < myColors.size(); i++) {
		 Scalar lower(myColors[i][0], myColors[i][1], myColors[i][2]);
		 Scalar Upper(myColors[i][3], myColors[i][4], myColors[i][5]);
		 Mat mask;

		 inRange(imgHSV, lower, Upper, mask);

		 //imshow(to_string(i), mask);

		 Point myPoint = getContours(mask);
		 if (myPoint.x != 0 && myPoint.y != 0) {
			 newPoints.push_back({ myPoint.x,myPoint.y,i });
		 }

	 }return newPoints;
 }

void drawOnCanvas(vector<vector<int>>newPoints, vector < Scalar>myColorValues) {
	for (int i = 0; i < newPoints.size(); i++) {
		circle(img, (Point(newPoints[i][0],newPoints[i][1])), 10, myColorValues[newPoints[i][2]
		], FILLED);
	}
}

void main() {
			string path = "Resources/test_video.mp4";
			VideoCapture cap(path);
			
	
			while (true) {
				
				cap.read(img);
				newPoints=findColor(img);
				drawOnCanvas(newPoints, myColorValues);
				imshow("Image", img);
				waitKey(20);
			}
			
			
			
			}