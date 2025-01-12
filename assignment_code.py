import cv2
import numpy as np

image = cv2.imread("assignment-001-given.jpg")

overlay = image.copy()

text_position = (880, 162)
text_size = cv2.getTextSize("RAH972U", cv2.FONT_HERSHEY_SIMPLEX, 2, 5)[0]
background_coords = (
    text_position[0] - 25,
    text_position[1] - text_size[1] - 25,
    text_position[0] + text_size[0] + 15,
    text_position[1] + 15
)
cv2.rectangle(overlay, 
    (background_coords[0], background_coords[1]),
    (background_coords[2], background_coords[3]),
    (0, 0, 0),
    -1)

alpha = 0.6
image = cv2.addWeighted(overlay, alpha, image, 1 - alpha, 0)

cv2.rectangle(image, (260, 185), (990, 920), (0, 255, 0), 12)
cv2.putText(image, "RAH972U", (880, 150), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 5)

cv2.imshow("Assignment Image", image)

cv2.waitKey(0)

cv2.imwrite("assigment_code_result.jpg", image)

cv2.destroyAllWindows()