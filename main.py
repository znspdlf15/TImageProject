import matplotlib.pyplot as plt
import cv2
from PIL import Image
import pytesseract

if __name__ == "__main__":
    image_path = r"./test_image/sudoku.png"
    # image = cv2.imread(image_path)
    # gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = Image.open(image_path)
    print(pytesseract.image_to_string(image))
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
