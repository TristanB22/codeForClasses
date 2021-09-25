import pytesseract as py
import cv2 as cv
import numpy as np
import pandas as pd

#this is a simple project for getting the data from screenshots that I took from the advanced physics lab
pt1_1=400
pt2_1=620
pt3_1=1230
pt4_1=1310

pt1_2=1190
pt2_2=1400
pt3_2=1230
pt4_2=1310

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

V1frame = np.zeros(22)
V2frame = np.zeros(22)
T1frame = np.zeros(22)
T2frame = np.zeros(22)
T3frame = np.zeros(22)
T4frame = np.zeros(22)



for i in range(23):
    name = str(i)
    try: 
        img = cv.cvtColor(cv.imread("/Users/tristanbrigham/Desktop/AdvPhysData/CarGravityData/" + name + ".png"), cv.COLOR_RGB2GRAY)
        print(name)
        # cv.rectangle(img, (pt1, pt3), (pt2, pt4), (0, 255, 0), thickness=5)
        cv.imshow("img", img)
        data = np.zeros(6)
        V1 = py.image_to_string(img[pt3_1:pt4_1, pt1_1:pt2_1]).strip().replace("@", "0").replace("/", "7")
        V2 = py.image_to_string(img[pt3_2:pt4_2, pt1_2:pt2_2]).strip().replace("@", "0").replace("/", "7")
        T1 = py.image_to_string(img[pt3_ti1:pt4_ti1, pt1_ti1:pt2_ti1]).strip().replace("@", "0").replace("/", "7")
        T2 = py.image_to_string(img[pt3_ti2:pt4_ti2, pt1_ti2:pt2_ti2]).strip().replace("@", "0").replace("/", "7")
        T3 = py.image_to_string(img[pt3_ti3:pt4_ti3, pt1_ti3:pt2_ti3]).strip().replace("@", "0").replace("/", "7")
        T4 = py.image_to_string(img[pt3_ti4:pt4_ti4, pt1_ti4:pt2_ti4]).strip().replace("@", "0").replace("/", "7")
        print("V1: " +  V1)
        print("V2: " +  V2)
        print("TI1: " + T1)
        print("TI2: " + T2)
        print("TI3: " + T3)
        print("TI4: " + T4)
        cv.imshow(V1, img[pt3_1:pt4_1, pt1_1:pt2_1]) #560, 580, 700, 630
        cv.imshow(V2, img[pt3_2:pt4_2, pt1_2:pt2_2]) #560, 580, 700, 630
        cv.imshow(T1, img[pt3_ti1:pt4_ti1, pt1_ti1:pt2_ti1]) #560, 580, 700, 630
        cv.imshow(T2, img[pt3_ti2:pt4_ti2, pt1_ti2:pt2_ti2]) #560, 580, 700, 630
        cv.imshow(T3, img[pt3_ti3:pt4_ti3, pt1_ti3:pt2_ti3]) #560, 580, 700, 630
        cv.imshow(T4, img[pt3_ti4:pt4_ti4, pt1_ti4:pt2_ti4]) #560, 580, 700, 630
        V1frame[i-1] = float(V1)
        V2frame[i-1] = float(V2)
        T1frame[i-1] = float(T1)
        T2frame[i-1] = float(T2)
        T3frame[i-1] = float(T3)
        T4frame[i-1] = float(T4)

        # if cv.waitKey(0) & 0xFF  == ord('q'):
            # exit(0)
        # cv.destroyAllWindows()
        print("")
    except:
        print("ERROR")
df = pd.DataFrame({
    "V1": V1frame,
    "V2": V2frame,
    "T1": T1frame,
    "T2": T2frame,
    "T3": T3frame,
    "T4": T4frame })
writer = pd.ExcelWriter("/Users/tristanbrigham/Desktop/AccelerationCars.xlsx")
df.to_excel(writer, sheet_name="CarData")
writer.save()

print(V1frame)
print(V2frame)
print(T1frame)
print(T2frame)
print(T3frame)
print(T4frame)