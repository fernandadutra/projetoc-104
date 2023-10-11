import cv2 

image=cv2.imread("solar-system.jpg")



cv2.putText(image, "Sol", (100,80), cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,255))
cv2.putText(image, "Mercurio", (120,180), cv2.FONT_HERSHEY_COMPLEX,0.4,(0,0,255))
cv2.putText(image, "Venus", (190,260), cv2.FONT_HERSHEY_COMPLEX,0.4,(0,0,255))
cv2.putText(image, "Terra!", (280,170), cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,255))
cv2.putText(image, "Marte", (370,250), cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,255))
cv2.putText(image, "Jupiter", (580,60), cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,255))
cv2.putText(image, "Saturno", (740,300), cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,255))
cv2.putText(image, "Urano", (970,140), cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,255))
cv2.putText(image, "Netuno", (1120,300), cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,255))

cv2.imshow("resultado",image)
cv2.waitKey(0)
cv2.imwrite("Solar_systemwithname.jpg",image)
