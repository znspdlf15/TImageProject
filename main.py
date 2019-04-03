import cv2
import recognize
import matplotlib.pyplot as plt

if __name__ == "__main__":
    image_path = r"./test_image/sudoku2.jpg"
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

    exact_contours = [[]]
    index = 0
    for i, cnt in enumerate(contours):
        x, y, w, h = cv2.boundingRect(cnt)
        if h < len(final_image)/10 or w < len(final_image[0])/10:
            continue
        if h > len(final_image)/8 or w > len(final_image[0])/8:
            continue

        exact_contours[index].insert(0, cnt)

        if len(exact_contours[index]) == 9:
            exact_contours[index] = sorted(exact_contours[index], key=lambda temp: cv2.boundingRect(temp)[0])
            if len(exact_contours) == 9:
                break
            exact_contours.append([])
            index += 1

    exact_contours.reverse()

    answer = [[] for i in range(9)]
    # recognize numbers
    for r, row in enumerate(exact_contours):
        for cnt in row:
            x, y, w, h = cv2.boundingRect(cnt)
            cropped_image = final_image[y+2:y+h-2, x+2:x+w-2]
            data = recognize.tesseract_recognize(cropped_image)

            if len(data) == 0 or not ('1' <= data[0] <= '9'):
                answer[r].append(0)
                continue

            if 1 <= int(data) <= 9:
                answer[r].append(int(data))
            else:
                answer[r].append(0)

    # for debug, print image
    # for i, cnt in enumerate(contours):
    #     x, y, w, h = cv2.boundingRect(cnt)
    #     if h < len(final_image)/10 or w < len(final_image[0])/10:
    #         continue
    #     if h > len(final_image)/8 or w > len(final_image[0])/8:
    #         continue
    #     if i % 4 == 0:
    #         cv2.rectangle(final_image, (x, y), (x + w, y + h), (255, 0, 0), 2)
    #     elif i % 4 == 1:
    #         cv2.rectangle(final_image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    #     elif i % 4 == 2:
    #         cv2.rectangle(final_image, (x, y), (x + w, y + h), (0, 0, 255), 2)
    #     else:
    #         cv2.rectangle(final_image, (x, y), (x + w, y + h), (255, 255, 0), 2)
    # plt.imshow()
    # plt.show()

