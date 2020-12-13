from googletrans import Translator
import keyboard
import sys


def Translate(s):
    translator = Translator()
    if translator.detect(s).lang == "en":
        result = translator.translate(s, dest="ru")
    else:
        result = translator.translate(s)
    print(f"\n{result.origin} --> {result.text}\n")

WIDTH = 80

print("TRANSLATOR".center(WIDTH, '-'))
s = input("Введите фразу для перевода:")
Translate(s)
print("Для выхода нажмите клавишу Enter...")
while True:
    if keyboard.is_pressed("enter"):
        sys.exit(0)
