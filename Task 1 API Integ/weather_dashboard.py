import requests
import matplotlib.pyplot as plt
import seaborn as sns

API_KEY = "0f6601632718ccfd3f34d839bcf7af0c"  
CITY = "Delhi"

URL = f"https://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"

response = requests.get(URL)
data = response.json()

# Checking if API is working 
if data.get("cod") != "200":
    print("❌ API Error:", data)
    exit()

dates = []
temperatures = []

for item in data['list'][:10]:
    dates.append(item['dt_txt'])
    temperatures.append(item['main']['temp'])

plt.figure(figsize=(10,5))
sns.lineplot(x=dates, y=temperatures, marker='o')

plt.title(f"Temperature Forecast for {CITY}")
plt.xlabel("Date & Time")
plt.ylabel("Temperature (°C)")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("weather_visualization.png")
plt.show()
