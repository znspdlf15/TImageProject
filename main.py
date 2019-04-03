import matplotlib.pyplot as plt
import cv2
from PIL import Image
import pytesseract

if __name__ == "__main__":
    image_path = r"./test_image/sudoku.png"
    image = cv2.imread(image_path)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cropped_image = gray_image[10:45, 60:80]
    retval, final_image = cv2.threshold(cropped_image, 100, 255, cv2.THRESH_BINARY)
    closing = cv2.morphologyEx(cropped_image, cv2.MORPH_CLOSE, (5, 5))
    aa = cv2.erode(closing, (5, 5), iterations=1)

    cv2.imshow('image', cropped_image)
    print(pytesseract.image_to_string(cropped_image, config='--psm 6'))
    cv2.waitKey(0)
    cv2.destroyAllWindows()
