import pytesseract as py
import cv2 as cv

#this is a simple project for getting the data from screenshots that I took from the advanced physics lab
pt1_1=400
pt2_1=620
pt3_1=1150
pt4_1=1250

pt1_2=1190
pt2_2=1400
pt3_2=1150
pt4_2=1250

pt1_ti1=110
pt2_ti1=250
pt3_ti1=308
pt4_ti1=335

pt1_ti2=110
pt2_ti2=250
pt3_ti2=340
pt4_ti2=375

pt1_ti3=110
pt2_ti3=250
pt3_ti3=370
pt4_ti3=405

pt1_ti4=110
pt2_ti4=250
pt3_ti4=410
pt4_ti4=445

pt1=pt1_ti3
pt2=pt2_ti3
pt3=pt3_ti3
pt4=pt4_ti3

for i in range(1, 7):
    for q in range(1, 4):
        name = "T" + str(i) + "-" + str(q)
        try: 
            img = cv.cvtColor(cv.imread("/Users/tristanbrigham/Desktop/AdvPhysData/AccLab/" + name + ".png"), cv.COLOR_RGB2GRAY)
            print(name)
            # cv.rectangle(img, (pt1, pt3), (pt2, pt4), (0, 255, 0), thickness=5)
            cv.imshow("img", img)
            print("V1: " + py.image_to_string(img[pt3_1:pt4_1, pt1_1:pt2_1]).strip().replace("@", "0"))
            print("V2: " + py.image_to_string(img[pt3_2:pt4_2, pt1_2:pt2_2]).strip().replace("@", "0"))
            print("TI1: " + py.image_to_string(img[pt3_ti1:pt4_ti1, pt1_ti1:pt2_ti1]).strip().replace("@", "0"))
            print("TI2: " + py.image_to_string(img[pt3_ti2:pt4_ti2, pt1_ti2:pt2_ti2]).strip().replace("@", "0"))
            print("TI3: " + py.image_to_string(img[pt3_ti3:pt4_ti3, pt1_ti3:pt2_ti3]).strip().replace("@", "0"))
            print("TI4: " + py.image_to_string(img[pt3_ti4:pt4_ti4, pt1_ti4:pt2_ti4]).strip().replace("@", "0"))
            # cv.imshow("TI1", img[pt3:pt4, pt1:pt2]) #560, 580, 700, 630
            # if cv.waitKey(0) & 0xFF  == ord('q'):
            #     exit(0)
            print("")
        except:
            continue
