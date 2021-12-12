#import self as self
# de tai: nhan dien bien so xe
# HUYNV
# LINHNH
# NAMDP


from recognition import E2E
import cv2
from pathlib import Path
import argparse
import time

def get_arguments():
    arg = argparse.ArgumentParser()
    arg.add_argument('-i', '--image_path', help='link to image', default='./images/21.jpg')

    return arg.parse_args()


args = get_arguments()
img_path = Path(args.image_path)

# read image
img = cv2.imread(str(img_path))

# start time
start = time.time()

# load model
model = E2E()

# recognize license plate
image = model.predict(img)

# end time
end = time.time()
print('Timer: %.2f s' % (end - start))
# show image
cv2.imshow('License Plate', image)
if cv2.waitKey(0) & 0xFF == ord('q'):
    exit(0)

cv2.destroyAllWindows()

#python example.py --image_path=C:\Users\huy\PycharmProjects\LicensePlateRecognition\images\.jpg
