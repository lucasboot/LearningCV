import sys
ros_path = '/opt/ros/kinetic/lib/python2.7/dist-packages'

if ros_path in sys.path:
    sys.path.remove(ros_path)
import cv2 as cv
sys.path.append('/opt/ros/kinetic/lib/python2.7/dist-packages')
if __name__ ==  '__main__':
	img = cv.imread('/home/lucas/Downloads/laser.png', cv.IMREAD_COLOR)

	main_win = 'Imagem'
	cv.namedWindow(main_win, cv.WINDOW_KEEPRATIO)
	cv.imshow(main_win, img)
	cv.waitKey(0)
	cv.destroyAllWindows()
