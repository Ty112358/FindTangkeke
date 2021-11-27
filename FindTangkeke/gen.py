import numpy as np
import random
import cv2.cv2 as cv2




def gen(rows,cols,num):

    keke = cv2.imread('samples/keke.jpeg')
    w,h = keke.shape[:2]

    kotori = cv2.imread('samples/kotori.jpeg')
    you = cv2.imread('samples/you.jpeg')
    lovelives = [kotori,you]

    assert keke.shape == kotori.shape == you.shape
    gen_map = np.zeros(rows*cols)
    

    for i in random.sample(range(rows*cols),num):
        gen_map[i] = 1
    
    gen_map = gen_map.reshape((rows,cols))

    init_pic = np.zeros((h * rows,w * cols,3))


    for x in range(rows):
        for y in range(cols):
            if gen_map[x,y] == 1:
                init_pic[x*h:(x+1)*h,y*w:(y+1)*w] = keke
            else:
                init_pic[x*h:(x+1)*h,y*w:(y+1)*w] = random.choice(lovelives)

    cv2.imwrite('findkeke({}x{}).jpg'.format(rows,cols),init_pic)
 



if __name__ == '__main__':
    gen(10,10,3)