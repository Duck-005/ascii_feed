from PIL import Image
from numpy import asarray
import cv2 as cv
import time, sys, math

ASCII_map = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"

def average(r, g, b):
        return (r + g + b)/3

def lightness(r, g, b):
    return (max(r, g, b) + min(r, g, b))/2

# weighted average accounting for human perception
def luminosity(r, g, b):
    return 0.21*r + 0.72*g + 0.07*b

def ascii_art(data, width, height):
    image = Image.fromarray(cv.cvtColor(data, cv.COLOR_BGR2RGB)).resize((width, height))    

    pixels = asarray(image)
    
    ascii_image = []

    for row in pixels:
        for pixel in row:
            r, g, b = pixel
            pixelAverage = luminosity(r, g, b)
        
            if pixelAverage % 4 == 0 and pixelAverage > 4:
                index = math.floor(pixelAverage/4)
            else: index = math.floor(pixelAverage/4) + 1
        
            ascii_image.append(ASCII_map[index])
        ascii_image.append("\n")
        
    return ''.join(ascii_image)

def main():
    cap = cv.VideoCapture(0)
    # cap = cv.VideoCapture("<VIDEO FILE>")  # use a video file to convert to ascii art

    while True:
        ret, frame = cap.read()
    
        aspect_ratio = 2  
        terminal_height = 80
        terminal_width = int(terminal_height * aspect_ratio)

        reduced = cv.resize(frame, (terminal_width, terminal_height))
    
        # ANSI escape character to clear terminal in an efficient way
        sys.stdout.write("\033[H") 
        print(ascii_art(reduced, terminal_width, terminal_height))
        time.sleep(0.04) 
    
        cv.imshow('title', frame) # shows the live cam feed
    
        if cv.waitKey(1) == ord('q'): 
            break
    
    cap.release()
    cv.destroyAllWindows()    

if __name__ == "__main__":
    main()
        