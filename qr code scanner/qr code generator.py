import tkinter as tk
from tkinter import messagebox
import qrcode
import os
from PIL import Image, ImageTk

# Function to generate and save the QR code
def generate_qr():
    data = entry.get()
    if not data:
        messagebox.showwarning("Input Error", "Please enter some data to generate the QR code.")
        return

    # Generate the QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')
    
    # Save the QR code to the Downloads folder
    download_path = os.path.join(os.path.expanduser('~'), 'Downloads')
    file_path = os.path.join(download_path, 'qrcode.png')
    img.save(file_path)
    
    messagebox.showinfo("Success", f"QR code has been generated and saved to {file_path}")

# Create the main application window
root = tk.Tk()
root.title("QR Code Generator")

# Load the background image
bg_image_path = "C:/Users/2002a/Downloads/qr code scanner/bg.jpg"  # Path to your background image

if not os.path.isfile(bg_image_path):
    messagebox.showerror("File Error", f"Background image not found: {bg_image_path}")
    root.destroy()
else:
    bg_image = Image.open(bg_image_path)
    bg_image = ImageTk.PhotoImage(bg_image)

    # Create a canvas to place the background image
    canvas = tk.Canvas(root, width=500, height=400)
    canvas.pack(fill="both", expand=True)

    # Display the background image on the canvas
    canvas.create_image(0, 0, image=bg_image, anchor="nw")

    # Create a frame to hold the widgets and place it on the canvas
    frame = tk.Frame(canvas, bg='white')  # Adjust the background color to white
    frame.place(relx=0.5, rely=0.5, anchor='center')

    # Create the input field for the data
    label = tk.Label(frame, text="Enter data to generate QR code:", bg='white')  # Match the background color
    label.pack(pady=10)

    entry = tk.Entry(frame, width=40, bg='#f0f0f0', fg='black', font=("Arial", 12))  # Set background to light grey, text color to black, and increase font size
    entry.pack(pady=10)

    # Create the button to generate the QR code
    generate_button = tk.Button(frame, text="Generate QR Code", command=generate_qr, bg="#007bff", fg="white", font=("Arial", 10), relief="flat", activebackground="#0056b3", activeforeground="white")
    generate_button.pack(pady=20)

    # Styling the button on hover
    def on_enter(e):
        generate_button.config(bg="#0056b3")

    def on_leave(e):
        generate_button.config(bg="#007bff")

    generate_button.bind("<Enter>", on_enter)
    generate_button.bind("<Leave>", on_leave)

    # Start the Tkinter event loop
    root.mainloop()
