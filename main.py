from datetime import datetime
import time

import pyscreenshot as GetImage
import schedule
from paddleocr import PaddleOCR, draw_ocr
from PIL import Image

def triggerScreenshot():
    name = f"image"
    screenshot = GetImage.grab()
    w, h = screenshot.size
    dimensions = (w-325, h-600, w-35, h-100)
    cropped = screenshot.crop(dimensions)
    path = f"./screenshots/{name}.png"
    cropped.save(path)
    
    

    ocr = PaddleOCR(lang="en")
    scraped = ocr.ocr(".\\screenshots\\image.png")
    for line in scraped[0]:
        parsedText = line[1][0]
        splitText = parsedText.split(":")
        textToTranslate = ""
        if(len(splitText) == 1):
            textToTranslate = splitText[0]
        else:
            textToTranslate = splitText[1]


    return path


def main():
    
    schedule.every(5).seconds.do(triggerScreenshot)

    while True:
        schedule.run_pending()
        time.sleep(1)



if __name__ == "__main__":
    main()