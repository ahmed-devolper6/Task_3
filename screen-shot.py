# Program to take screenshot
import schedule   
import pyscreenshot
def screenshots():
    image = pyscreenshot.grab()
    image.show()
    image.save("Task.png")

schedule.every(10).minutes.do(screenshots)
s = screenshots()