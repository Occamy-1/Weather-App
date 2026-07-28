import tkinter as tk
from tkinter import messagebox
import requests

# Enter your OpenWeatherMap API key here
API_KEY = "8687eaa89eaac04addb9c6abfb68d9c2"

# -------------------- Function --------------------
def get_weather():
    city = city_entry.get()

    if city == "":
        messagebox.showwarning("Warning", "Please enter a city name!")
        return

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        if data["cod"] != 200:
            messagebox.showerror("Error", "City not found!")
            return

        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        weather = data["weather"][0]["description"].title()
        wind = data["wind"]["speed"]
        country = data["sys"]["country"]

        result = f"""
📍 {city.title()}, {country}

🌡 Temperature : {temp} °C

☁ Weather : {weather}

💧 Humidity : {humidity}%

🌬 Wind : {wind} m/s
"""

        weather_label.config(text=result)

    except Exception:
        messagebox.showerror("Error", "Unable to fetch weather.")

# -------------------- Window --------------------
root = tk.Tk()
root.title("🌤 Modern Weather App")
root.geometry("500x600")
root.config(bg="#1E293B")

# -------------------- Title --------------------
title = tk.Label(
    root,
    text="🌤 Weather Forecast",
    font=("Helvetica", 24, "bold"),
    bg="#1E293B",
    fg="white"
)
title.pack(pady=20)

# -------------------- Entry --------------------
city_entry = tk.Entry(
    root,
    font=("Arial", 16),
    width=22,
    justify="center",
    bd=0
)
city_entry.pack(ipady=8)

# -------------------- Button --------------------
search_btn = tk.Button(
    root,
    text="🔍 Search",
    font=("Arial", 14, "bold"),
    bg="#38BDF8",
    fg="white",
    activebackground="#0EA5E9",
    activeforeground="white",
    padx=20,
    pady=8,
    bd=0,
    cursor="hand2",
    command=get_weather
)
search_btn.pack(pady=20)

# -------------------- Weather Card --------------------
card = tk.Frame(
    root,
    bg="#334155",
    bd=0
)
card.pack(padx=20, pady=20, fill="both", expand=True)

weather_label = tk.Label(
    card,
    text="Enter a city name above",
    font=("Arial", 15),
    bg="#334155",
    fg="white",
    justify="left"
)
weather_label.pack(pady=30)

# -------------------- Footer --------------------
footer = tk.Label(
    root,
    text="Made with ❤️ using Python & Tkinter",
    font=("Arial", 10),
    bg="#1E293B",
    fg="lightgray"
)
footer.pack(pady=10)

root.mainloop()



