import tkinter as tk
from PIL import Image, ImageTk

# Open the image file
image = Image.open(r"C:\Users\Uzer\Desktop\python\logBook\views\Images\icon.png") 


# Define the desired width and height for the image
width = 300
height = 200

# Resize the image
image = image.resize((width, height), Image.Resampling.LANCZOS)

# Create a Tkinter window
window = tk.Tk()
window.title("Rounded Image Borders")

# Create a style object
style = tk.ttk.Style()

# Configure the style to add rounded borders
style.configure("RoundedImage.TLabel", borderwidth=5, relief="solid", bordercolor="black")

# Convert the image to Tkinter-compatible format
image_tk = ImageTk.PhotoImage(image)

# Create a Tkinter label with rounded borders and display the image
label = tk.ttk.Label(window, image=image_tk, style="RoundedImage.TLabel")
label.pack()

# Run the Tkinter event loop
window.mainloop()