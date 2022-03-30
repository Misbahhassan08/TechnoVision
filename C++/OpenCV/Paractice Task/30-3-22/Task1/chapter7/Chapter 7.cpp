#include <opencv2/imgcodecs.hpp>
#include<opencv2/highgui.hpp>
#include<opencv2/imgproc.hpp>
#include<iostream>

using namespace cv;
using namespace std;
Mat imgGray, imgBlur, imgCanny, imgDil, imgErode;
void getContours(Mat imgDil, Mat img) {

	vector<vector<Point>>contours;
	vector < Vec4i >hierarchy;
	findContours(imgDil, contours, hierarchy, RETR_EXTERNAL, CHAIN_APPROX_SIMPLE);
	drawContours(img, contours, -1, Scalar(255, 0, 255), 2);
	for (int i = 0; i < contours.size(); i++)//find the area of shapes 
	{
		int area = contourArea(contours[i]);
		cout << area << endl;
		vector<vector<Point>>conPoly(contours.size());
		vector<Rect>boundRect(contours.size());
		string objectType;
		if (area > 1000) {

			float peri = arcLength(contours[i], true);
			approxPolyDP(contours[i], conPoly[i], 0.02 * peri, true);//Count the edges 

			cout << conPoly[i].size() << endl;
			boundRect[i] = boundingRect(conPoly[i]);


			int objCon = (int)conPoly[i].size();//Tell which shape is which
			if (objCon == 3) { objectType = "Triangle"; }
			if (objCon == 4) {
				float aspRatio = (float)boundRect[i].width / (float)boundRect[i].height;
				if (aspRatio > 0.95 && 1.05) { objectType = "Square"; }
				else {
					objectType = "Rectangle";
				}
			}
			if (objCon > 4) { objectType = "Circle"; }

			putText(img, objectType, { boundRect[i].x,boundRect[i].y - 5 }, FONT_HERSHEY_PLAIN, 1, Scalar(0, 0, 255), 2);
			drawContours(img, contours, i, Scalar(255, 0, 255), 1);
			rectangle(img, boundRect[i].tl(), boundRect[i].br(), Scalar(0, 255, 0), 5);//It draw the rectangle around the shape}


		}
	}
}

/////////// shape detection///////////
	void main() {
		string path = "Resources/shapes.png";
		Mat img = imread(path);



		cvtColor(img, imgGray, COLOR_BGR2GRAY);//Functioon to convert image into gray scale
		GaussianBlur(imgGray, imgBlur, Size(3, 3), 5, 0);//Convert into Blur Image 
		Canny(imgBlur, imgCanny, 50, 100);//Edge detection
		Mat kernel = getStructuringElement(MORPH_RECT, Size(3, 3));
		dilate(imgCanny, imgDil, kernel);
		getContours(imgDil, img);
		imshow("Image", img);
		/*imshow("Image Gray", imgGray);
		imshow("Image Blur", imgBlur);
		imshow("Image Canny", imgCanny);
		imshow("Image Dilate", imgDil);*/

		waitKey(0);
	}