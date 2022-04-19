#include <iostream>
using namespace std;

class Cube {//Class of Cube name 
public:
	int x;
	int y;
	int z;


};
int main() {
	Cube cube1;
	Cube cube2;
	double vol = 0;
	//cube1 dimensions
	cube1.x = 1;
	cube1.y = 2;
	cube1.z = 3;
	//cube 2 dimensions
	cube2.x = 1;
	cube2.y = 2;
	cube2.z = 3;
	vol = cube1.x * cube1.y * cube1.z;
	cout << "Volume of cube 1 " << vol<<endl;
	vol = cube2.x * cube2.y * cube2.z;
	cout << "Volume of cube 2 " << vol<<endl;

}