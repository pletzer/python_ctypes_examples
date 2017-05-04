/**
 * Example of a C API that is callable from Python
 * A. Pletzer NeSI/NIWA
 */
#include <stdio.h>
#include <math.h>
#include <stdlib.h>

/**
 * Say hello
 * @param name name of the person to greet
 * @return error code (0 = ok)
 */
 int sayHello(const char* name) {
   	printf("hello %s\n", name);
   	return 0;
 }

/**
 * Compute sum of array elements
 * @param n number of elements
 * @param arr input array
 * @return result
 */
 int getSum(int n, const double arr[], double* sum) {
 	int i;
 	*sum = 0;
 	for (i = 0; i < n; ++i) {
 		*sum += arr[i];
 	}
 	return 0;
 }

 struct Position {
 	double x;
 	double y;
 };

/**
 * Get the distance between two points
 * @param pos1 first position
 * @param pos2 second position
 * @return distance
 */
double getDistance(const struct Position* pos1,
	               const struct Position* pos2) {
	double dx, dy;
	dx = pos2->x - pos1->x;
	dy = pos2->y - pos1->y;
	return sqrt(dx*dx + dy*dy);
}

/**
 * Object oriented C API. it contains a constructor, a setter, 
 * a print object method and a destructor
 */
void createPosition(struct Position** self) {
	*self = malloc(sizeof(struct Position));
}

void setPosition(struct Position** self, double x, double y) {
	(*self)->x = x;
	(*self)->y = y;
}

void printPosition(struct Position** self) {
	printf("Position: x = %lf y = %lf\n", (*self)->x, (*self)->y);
}

void destroyPosition(struct Position** self) {
	free(*self);
	*self = NULL;
}