/* 
https://app.codility.com/programmers/lessons/3-time_complexity/frog_jmp/

Fairly trivial maths with some casting thrown in

Time compelxity     O(1)
Space complexity    O(1)
 */
#include <math.h>

int solution(int X, int Y, int D) {
	//Need a double, float not precise enough.
	double jumps = (double)(Y - X) / D;
	return ceil(jumps);
}