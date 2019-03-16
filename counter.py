import tkinter as tk
counter = 0
def hamza(label):
  def count():
    global counter
    counter += 1
    label.config(text=str(counter))
    label.after(1000, count) 
  return count()
root = tk.Tk()
root.title('counting seconds')
label = tk.Label(root,fg = "green")
label.pack()
hamza(label)
button = tk.Button(root,text="stop",width = "30",command = root.destroy)
button.pack()
root.mainloop()