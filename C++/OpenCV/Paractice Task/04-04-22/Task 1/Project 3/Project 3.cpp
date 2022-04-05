#include <opencv2/imgcodecs.hpp>
#include<opencv2/highgui.hpp>
#include<opencv2/imgproc.hpp>
#include<opencv2/objdetect.hpp>
#include<iostream>

using namespace cv;
using namespace std;
/////////// Project 3///////////

void main() {
	string path = "Resources/Stylish Car and bike Number plate designs - best number plate font - Born Creator.mp4";
	VideoCapture cap(path);
	Mat img;

	CascadeClassifier plateCascade;
	plateCascade.load("Resources/haarcascade_russian_plate_number.xml");
	if (plateCascade.empty()) { cout << "XML file not loaded" << endl; }
	vector<Rect> plates;
	while (true) {

		cap.read(img);
		plateCascade.detectMultiScale(img, plates, 1.1, 10);
		for (int i = 0; i < plates.size(); i++) {
			rectangle(img, plates[i].tl(), plates[i].br(), Scalar(255, 255, 255), 2);
		}
		imshow("Image", img);
		waitKey(200);


	}
	}
