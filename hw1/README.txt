Instructions for running the Python codes for homework 1


To run integrate.py:
	The tests for the file reside in the if __name__ == '__main__' block
	and calculates the error of a integrateing the equation of a circle of
	raduis 1  for the default step size. In addition, the test calcualte and
	plot the erroe for the integration of the line y=x on the interval (0, 1)
	for 1000 step sizes in the range of 1e-6 to 0.1. The plotting function,
	located in the testing block, does plot backward in that the x axis
	show the steps from left to right such that the error increases as the
	step size increases rather than showing the error decrease a 1/(step size)
	
	The inputs and outputs of the function are:
	
	 Inputs:
        f: a lambda function to be inetgrated (must be LambdaType)
        a: the lower bound of the variables
        b: the upper bound of the variables
        step: the step size or delta used for the integration

    Outputs:
        value: the value resulting from the definite integration
		
To run area.py
	The tests for the file reside in the if __name__ == '__main__' block where
	the area of a circle is calculated using Monte Carlo sampling. The area is
	calculated for 100 different sets of points ranging from 100 points to
	1e4 points to calcualte the area. The error is then calcualted and plotted
	int the test block.
	
	The inputs and outputs of the function are:
	
	 Inputs:
        f: the function for which the area is calculated (must be LambdaType)
        p1: defines the forst corner of the bounding box around the area
        p2: defines the second corner of the bounding box around the area
        samples: sets how many samples to use for the integration

    Outputs:
        area: the area of the arbitrary shape input to the function