from datetime import datetime
import time

import pyscreenshot as GetImage
import schedule
from paddleocr import PaddleOCR, draw_ocr
from PIL import Image
import deepl



OCR = 0
TRANSLATOR = 0

def triggerScreenshot():
    name = f"image"
    screenshot = GetImage.grab()
    w, h = screenshot.size
    dimensions = (w-325, h-600, w-15, h-150)
    cropped = screenshot.crop(dimensions)
    path = f"./screenshots/{name}.png"
    cropped.save(path)
    
    
    scraped = OCR.ocr(".\\screenshots\\image.png")
    for line in scraped[0]:
        parsedText = line[1][0]
        splitText = parsedText.split(":")
        user = ""
        textToTranslate = ""
        if(len(splitText) == 1):
            textToTranslate = splitText[0]
        else:
            textToTranslate = splitText[1]
        print(textToTranslate)
        if textToTranslate != "":
            translatedText = TRANSLATOR.translate_text(textToTranslate, target_lang="EN-US")
        print(translatedText)
        print("------")
    return path


    

def main():
    

    global OCR
    global TRANSLATOR

    OCR = PaddleOCR(lang="korean")
    auth=""
    TRANSLATOR = deepl.Translator(auth)
    schedule.every(5).seconds.do(triggerScreenshot)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
