// you can use includes, for example:
// #include <algorithm>
#include <math.h>

// you can write to stdout for debugging purposes, e.g.
// cout << "this is a debug message" << endl;

int solution(int X, int Y, int D) {
	//Need a double, float not precise enough.
	double jumps = (double)(Y - X) / D;
	return ceil(jumps);
}