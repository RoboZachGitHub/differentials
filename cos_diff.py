# differentiation of cosine using various numerical differentiation methods
import math

def cos_x(x):
	return math.cos(float(x)) 

def differentials(x, step_size):
	h = float(step_size)
	fwd_diff = (cos_x(x + h) - cos_x(x))/h
	centr_diff = (cos_x(x + (h/2.0)) - cos_x(x - (h/2.0)))/h
	extrap_diff = (8*(cos_x(x + h/4.0) - cos_x(x - h/4.0)) - (cos_x(x + h/2.0) - cos_x(x - h/2.0)))/(3*h)

	print "fwd diff: %f" % fwd_diff
	print "center diff: %f" % centr_diff
	print "extrapolation diff: %f" % extrap_diff

	return 0




def scnd_differential(x, step_size):
	h = float(step_size)
	centr_2nd_diff = (cos_x(x + h) + cos_x(x - h) - 2*cos_x(x))/(h*h)
	print "second differntial is: %f" % centr_2nd_diff

	return 0



differentials(1.0, 0.00005)
scnd_differential(1.0, 0.00005)






