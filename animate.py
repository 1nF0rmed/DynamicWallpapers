import ctypes
import os
import time

count = -1

try:
    while 1:
        count = 0 if count==1200 else count+1
        image_path = "Absolute Path to img\\frame%d.jpg" % count
        try:
            SPI_SETDESKWALLPAPER = 20
            SPIF_UPDATEINIFILE = 1
            ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image_path , SPIF_UPDATEINIFILE)

        except Exception as e:
            print("Not possible")
            print(e)

        time.sleep(0.09)

        print("Complete")

except KeyboardInterrupt:
    print("Exiting..")
    quit()
