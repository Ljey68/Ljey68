import tkinter as tk
import requests


root = tk.Tk()
root.title("Weather App")
root.geometry("400x500")
root.configure(bg="lightblue")


label_temp = tk.Label(root, text="-- °C", fg="black", bg="lightblue", font=("Arial", 25))
label_temp.place(x=80, y=330)

label_humidity = tk.Label(root, text="-- %RH", fg="black", bg="lightblue", font=("Arial", 25))
label_humidity.place(x=230, y=330)

label2=tk.Label(root,text="welcome back!!",fg="black", bg="blue", font=("Arial", 25))
label2.place(x=0,y=10)

def update_weather():
    try:
       
        response = requests.get("https://cdn.ituring.ir/weather/today")
        data = response.json()

      
        temperature = data["temperature"]
        humidity = data["humidity"]
        status = data["status"]

       
        label_temp.config(text=f"{temperature} °C")
        label_humidity.config(text=f"{humidity} %RH")

       
        weather_image = tk.PhotoImage(file=f"./images/{status}.png")
        label_image.config(image=weather_image)
        label_image.image = weather_image

    except Exception as e:
        label_temp.config(text="Error!")
        label_humidity.config(text="Error!")
        print(f"we got some error!!: {e}")


button_update = tk.Button(root, text="Update Weather", command=update_weather, width=20, bg="blue", fg="white", font=("Arial", 12))
button_update.place(x=90, y=400)


def Runbutt():
    
    label1.config(text="today is -- of dec")

butt=tk.Button(root,command=Runbutt,width=30,text="click for date")

butt.place(x=80,y=260)
label1=tk.Label(root,width=30,bg="pink")
label1.place(x=80,y=450)


default_image = tk.PhotoImage(file="./images/clear.png")
label_image = tk.Label(root, image=default_image, bg="lightblue")
label_image.place(x=70, y=30)

root.mainloop()
