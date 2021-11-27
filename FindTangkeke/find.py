import numpy as np
import cv2.cv2 as cv2



def findtangkeke(imagepath,modelpath):
    img = cv2.imread(imagepath)
    img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    model = cv2.imread(modelpath,0)
    res = cv2.matchTemplate(img_gray,model,method=cv2.TM_CCORR_NORMED)

    w,h = model.shape[::-1]
    loc = np.where(res >=0.99)

    for l in zip(*loc[::-1]):
        cv2.rectangle(img,l,(l[0]+w,l[1]+h),[0,0,255],2)
    # print(loc)
    

    imgname = imagepath.split('/')[-1].split('.')[0]
    cv2.imwrite('res_'+imgname+'.jpg',img)

    cv2.imshow('result',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    findtangkeke('findkeke(10x10).jpg','samples/keke.jpeg')