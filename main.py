import matplotlib.pyplot as plt
import cv2

if __name__ == "__main__":
    image_path = r"./test_image/sudoku.png"
    origin_image = cv2.imread(image_path)
    gray_image = cv2.cvtColor(origin_image, cv2.COLOR_BGR2GRAY)
    retval, thresholding_image = cv2.threshold(gray_image, 120, 230, cv2.ADAPTIVE_THRESH_MEAN_C)
    closing_image = cv2.morphologyEx(thresholding_image, cv2.MORPH_OPEN, (3, 3))
    # closing_image = cv2.morphologyEx(thresholding_image, cv2.MORPH_OPEN, (3, 3))
    # closing_image = cv2.erode(closing_image, (3, 3), iterations=1)
    # edges = cv2.Canny(thresholding_image, 100, 200)

    image, contours, hierachy = cv2.findContours(closing_image.copy(),
                                                 cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    rects = [cv2.boundingRect(each) for each in contours]

    final_image = origin_image.copy()
    # final_image = cv2.drawContours(origin_image, contours, -1, (0, 255, 0), 1)
    for i, cnt in enumerate(contours):
        x, y, w, h = cv2.boundingRect(cnt)
        if h < len(final_image)/10 or w < len(final_image[0])/10:
            continue
        if h > len(final_image)/8 or w > len(final_image[0])/8:
            continue
        if i % 4 == 0:
            cv2.rectangle(final_image, (x, y), (x + w, y + h), (255, 0, 0), 2)
        elif i % 4 == 1:
            cv2.rectangle(final_image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        elif i % 4 == 2:
            cv2.rectangle(final_image, (x, y), (x + w, y + h), (0, 0, 255), 2)
        else:
            cv2.rectangle(final_image, (x, y), (x + w, y + h), (255, 255, 0), 2)

    # print image
    cv2.imshow('image', final_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
