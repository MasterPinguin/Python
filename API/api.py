import requests

posto = input("Inserisci la città: ")
posto = posto.replace(' ', '%20')
link = f"https://api.openweathermap.org/data/2.5/weather?q={posto}&appid=d7d80b56700431c8027827cc9932af78&units=metric"

response = requests.get(link)

if response.status_code == 200:
    result = response.json()
    temp = result['main']['temp']
    print(f"Oggi a {posto} ci sono {temp}˚C")
else:
    print("La città che stai cercando è inesistente")
