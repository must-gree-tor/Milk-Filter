#please know that this is not any better than the normal code
#it's just my version of the code
from PIL import Image, ImageFile
import numpy as np
import time

import random

def decision(
        probability:float
    ) -> bool:

    return np.random.rand() < probability

def apply_milk_inside_filter(
        imag:ImageFile.ImageFile, pointillism_Decimal:float = 1.0, copy:bool = False
    ) -> ImageFile.ImageFile:

    def image_change(
            xy: tuple[int, int], probality: float, 
            ColorIfTrue: tuple[int, int, int], ColorIfFalse: tuple[int, int, int]
        ) -> None:
        if decision(probality):
            imag.putpixel(xy, ColorIfTrue)
            return
        imag.putpixel(xy, ColorIfFalse)
    if copy:
        imag = imag.copy()
    width, height = imag.size
    for x in range(width):
        for y in range(height):
            pixelRGB = imag.getpixel((x,y))
            R,G,B = pixelRGB

            brightness = (R+G+B)//3 #range from 0-255
            
            if brightness < 25:
                imag.putpixel((x,y), (0, 0, 0))
            elif brightness < 70:
                image_change((x,y), pointillism_Decimal, (0,0,0), (102,0,31))
            elif brightness < 120:
                image_change((x,y), pointillism_Decimal, (102,0,31), (0,0,0))
            elif brightness < 200:
                imag.putpixel((x,y),(102,0,31))
            elif brightness < 230:
                image_change((x,y), pointillism_Decimal, (137,0,146), (102,0,31))
            else:
                imag.putpixel((x,y),(137,0,146))
    
    return imag

def apply_milk_outside_filter(
        imag:ImageFile.ImageFile, pointillism_Decimal:float = 1.0, copy:bool = False
    ) -> ImageFile.ImageFile:

    def image_change(
            xy: tuple[int, int], probality: float, 
            ColorIfTrue: tuple[int, int, int], ColorIfFalse: tuple[int, int, int]
        ) -> None:
        if decision(probality):
            imag.putpixel(xy, ColorIfTrue)
            return
        imag.putpixel(xy, ColorIfFalse)
    if copy:
        imag = imag.copy()
    width, height = imag.size
    for x in range(width):
        for y in range(height):
            pixelRGB = imag.getpixel((x,y))
            R,G,B = pixelRGB

            brightness = (R+G+B)//3 #range from 0-255
            
            if brightness < 25: 
                imag.putpixel((x,y), (0, 0, 0))
            elif brightness < 70:
                image_change((x,y), pointillism_Decimal, (0,0,0), (92,36,60))
            elif brightness < 90:
                image_change((x,y), pointillism_Decimal, (92,36,60), (0,0,0))
            elif brightness < 150:
                imag.putpixel((x,y),(92,36,60))
            elif brightness < 200:
                image_change((x,y), pointillism_Decimal, (203,43,43), (92,36,60))
            else:
                imag.putpixel((x,y),(203,43,43))

    return imag

if __name__ == "__main__":
    data = Image.open('temp.jpg')
    inside_filter = apply_milk_inside_filter(data)
    outside_filter = apply_milk_outside_filter(data)

    inside_filter.show()
    outside_filter.show()