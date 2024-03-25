from picamera2 import Picamera2, Preview
import tkinter as tk
import time
from datetime import datetime
from PIL import ImageTk, Image

photo = None

def loop():
    while (True):
        cam.configure(cam_pre_config)
        cam.start_preview(Preview.QTGL)
        cam.start()
        time.sleep(60)
        start = datetime.now()
        date_time = start.strftime("%Y_%m_%d %H_%M_%S")
        format_str = date_time + ".jpg"
        filename_ent.delete(0, tk.END)
        filename_ent.insert(tk.END, date_time)
        #cam.switch_mode_and_capture(cam_cap_config, format_str)
        # putting images in
        image = Image.open("cat.jpg").resize((1640, 1232)) # replace with cam pic
        photo = ImageTk.PhotoImage(image)
        main.update()

###### tkinter window stuff
main = tk.Tk()
main.rowconfigure(0,weight=1, minsize=40)
main.rowconfigure(1, weight=1, minsize=100)
main.columnconfigure(0, weight=1, minsize=100)
main.columnconfigure(1, weight=1, minsize=100)
main.title("Methanol level cameras")

# Buttons
start_btn = tk.Button(main, text="Start captures", command=loop)
start_btn.grid(row=2, column=3, padx=5, pady=5)
exit_btn = tk.Button(main, text="Exit", command=main.quit)
exit_btn.grid(row=3, column=3, padx=5, pady=5)

# Labels + adding the image in the grid
test = tk.Label(main, text="Current displayed photo is from: ")
test.grid(row=1, column=2, padx=5, pady=5)
label = tk.Label(main, text="P", image=photo)
label.image = photo
label.grid(row=1, padx=5, pady=5)

# Entries
filename_ent = tk.Entry(main, width=10)
filename_ent.grid(row=1, column=3, padx=20, pady=5)
###### picamera stuff
#cam = Picamera2()
#cam_cap_config = cam.create_still_configuration()
#cam_pre_config = cam.create_preview_configuration()

main.mainloop()
