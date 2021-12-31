#Helpful algorithms
#NewWidth and height = sqrt((int(width/2)-0)**2 + (int(height/2)-0)**2)
#sin(alpha) = abs(height/2 - x_1)/sqrt((int(width/2 - x)**2+(int(height/2 - y))**2))
import math
def Rotate(orig_img, angle, direction)
	width = len(orig_img[0])
	height = len(orig_img)
	NewWidthHeight = int(sqrt((int(width/2)-0)**2 + (int(height/2)-0)**2))
	new_img = [[""] * NewWidthHeight] * NewWidthHeight
