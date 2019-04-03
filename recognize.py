import cv2
import pytesseract


def tesseract_recognize(image, config='--psm 6'):
    str = pytesseract.image_to_string(image, config=config)
    print("tesseract recognize: {}".format(str))

    return str


if __name__ == "__main__":
    image_path = r"./test_image/sudoku.png"
    image = cv2.imread(image_path)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cropped_image = gray_image[10:45, 60:80]
    retval, final_image = cv2.threshold(cropped_image, 100, 255, cv2.THRESH_BINARY)
    closing = cv2.morphologyEx(cropped_image, cv2.MORPH_CLOSE, (5, 5))
    aa = cv2.erode(closing, (5, 5), iterations=1)

    cv2.imshow('image', cropped_image)

    tesseract_recognize(cropped_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
