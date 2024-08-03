import tkinter as tk 
from tkinter import filedialog, messagebox   
from PIL import Image
def load_image(path): 
    img = Image.open(path) 
    return img 

def encrypt_image(img): 
    encrypted_img = img.copy() 
    pixels = encrypted_img.load() 

    for i in range(encrypted_img.size[0]): 
        for j in range(encrypted_img.size[1]): 
            r, g, b = pixels[i, j] 
            pixels[i, j] = (g, b , r )  # Swap colour channels

    return encrypted_img

def decrypt_image(encrypted_img): 
    decrypted_img = encrypted_img.copy()       
    pixels = decrypted_img.load()        

    for i in range(decrypted_img.size[0]):         
        for j in range(decrypted_img.size[1]):             
            g, r, b = pixels[i, j]             
            pixels[i, j] = (r, g, b)  # Swap colour channels back                  
    return decrypted_img 

def save_image(img, path):     
    img.save(path) 

def open_file():     
    file_path = filedialog.askopenfilename(filetypes=[("Image files", ".jpg;.jpeg;*.png")])     
    if file_path:         
        img = load_image(file_path)         
        img.show()         
        return img 

def encrypt_and_show():     
    global img, encrypted_img     
    img = open_file()    
    if img: 9          
    encrypted_img = encrypt_image(img)         
    encrypted_img.show() 
    print("Image Encrypted Successfully")

def decrypt_and_show():    
     if encrypted_img:        
         decrypted_img = decrypt_image(encrypted_img)         
         decrypted_img.show()       
         print("Image Decrypted Successfully")
         return decrypted_img     
     else:         
         messagebox.showerror("Error", "No encrypted image to decrypt") 

def save_encrypted_image():    
    if encrypted_img:        
        file_path = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("JPEG files", ".jpg"), ("All files", ".*")])         
        if file_path:            
            save_image(encrypted_img, file_path)     
        else:        
            messagebox.showerror("Error", "No encrypted image to save") 

def save_decrypted_image():     
    decrypted_img = decrypt_and_show()     
    if decrypted_img: file_path = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("JPEG files", ".jpg"), ("All files", ".*")]) 
    if file_path: 
        save_image(decrypted_img, file_path) 
    else: 
        messagebox.showerror("Error", "No decrypted image to save") 

root = tk.Tk() 
root.title("Image Encrypter and Decrypter") 
root.configure(bg="lightblue")

frame = tk.Frame(root) 
frame.configure(bg="lightblue")
frame.pack(padx=100, pady=100) 

open_button = tk.Button(frame, text="Image to Encrypt ", command=encrypt_and_show, bg="yellow",fg="red") 
open_button.pack(pady=6)  

save_encrypted_button = tk.Button(frame, text="Save Encrypted Image", command=save_encrypted_image, bg="yellow",fg="red") 
save_encrypted_button.pack(pady=6) 

decrypt_button = tk.Button(frame, text="Decrypt the Image", command=decrypt_and_show, bg="yellow",fg="red") 
decrypt_button.pack(pady=6) 

save_decrypted_button = tk.Button(frame, text="Save Decrypted Image", command=save_decrypted_image, bg="yellow",fg="red")
save_decrypted_button.pack(pady=6)

root.mainloop()