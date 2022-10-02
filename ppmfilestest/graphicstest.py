'''

Writing PPM Files (Raw image files): P6 File Format

'''

from typing import List


# Dimensions 
WIDTH, HEIGHT = 800, 600

# Colors
COLOR_BLUE = 0x0000FFFF 
COLOR_RED = 0xFF0000FF
COLOR_GREEN = 0x00FF00FF
COLOR_BLACK = 0x000000FF 
COLOR_WHITE = 0xFFFFFFFF
COLOR_BG = 0x75797dFF


# wrong array init, there's some memory reference issue in this , so this wont work
'''
    Problem with initializing 2d arrays like this: img = [[0]*WIDTH]*HEIGHT
    here, [0]*WIDTH makes shallow copy of 0, call this A1, 
    which becomes: A1 = [0, 0, ...., 0]

    so, initializing a 1D array this way is fine, but for 2d array

    Now A1*HEIGHT gives: img = [A1, A1, A1, ...., A1] 

    doing img[0][0] = 10
    with turn all the first element in A2 to 0

'''
img = [[0]*WIDTH]*HEIGHT 


img = [[COLOR_BG]* WIDTH for _ in range(HEIGHT)] # initial image

'''
    Fill circle
    color: RRGGBBAA
'''
def fill_circle(cx, cy, radius, color = 0x00FFFFFF):
    global img
    x0 = cx - radius
    y0 = cy - radius
    if((cx-radius)<0 or (cy-radius)<0):
        # print("Invalid radius for the given centre")
        exit("Invalid radius for the given centre")

    for x in range(x0, cx+radius):
        if(x>=0 and x<WIDTH):
            for y in range(y0, cy+radius):
                if(y>=0 and y<HEIGHT):
                    dx = cx - x
                    dy = cy - y
                    # write_config([x, y])
                    if(dx*dx + dy*dy <= radius**2):
                        img[y][x] = color 

    # print(img)
    
'''

    Write image to a file

'''    

def write_config(data:List):
    with open("data/config_color_sample.txt","a+") as f: 
        f.write(str(data)+"\n")


'''

Test ppm write out

'''
def quadrant_test():
    global img
    ct = [0]*4
    print("DIMENSIONS", len(img), len(img[0]))
    print(img[0])

    for y in range(0, HEIGHT):
        for x in range(0, WIDTH):
            if((y<HEIGHT//2) and (x<WIDTH//2)):
                ct[0]+=1
                img[y][x] = COLOR_BLACK
            elif(y<HEIGHT//2 and x>=WIDTH//2):
                ct[1]+=1
                img[y][x] = COLOR_BLUE
            elif(y>=HEIGHT//2 and x<WIDTH//2):
                ct[2]+=1
                img[y][x] = COLOR_GREEN
            elif(y>=HEIGHT//2 and x>=WIDTH//2):
                ct[3]+=1
                img[y][x] = COLOR_RED
    
    print("Count:", ct)
    # print(img)

        
'''
    Write image array to ppm file(P6 header)
'''
def write_to_file(file_path):
    with open(file_path, "wb") as f:
        f.write(f"P6\n{WIDTH} {HEIGHT} 255\n".encode('utf-8'))

        # write pixel to file sequentially 
        for pixelset in img:
            write_config(pixelset)
            for pixel in pixelset:
                # pull out RGB from the pixel value (RRGGBBAA)
                pixelArr = [
                    (pixel & 0xFF000000)>>8*3,
                    (pixel & 0x00FF0000)>>8*2, 
                    (pixel & 0x0000FF00)>>8*1,
                ]
                # print(pixelArr)
                # write_config(pixelArr)
                # break
                f.write(bytes(pixelArr))
                

# write_to_file("data/sampleimg1.ppm")
with open("data/config_color_sample.txt","w") as f: 
    f.write(str("Data:")+"\n")

# quadrant_test()

fill_circle(200, 200, 150)

write_to_file("data/sampleimg1.ppm")