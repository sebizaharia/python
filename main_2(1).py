import pandas as pd
import matplotlib.pyplot as plt

x = 15
y = 7

data = pd.read_csv("data.csv")

plt.figure()
plt.plot(data["Durata"], label="Durata", color="red")
plt.plot(data["Puls"], label="Puls", color="blue")
plt.title(f"Primele {x} valori")
plt.title("Toate valorile")
plt.xlabel("Index")
plt.ylabel("Valoare")
plt.legend()
plt.show()

plt.figure()
plt.plot(data["Durata"].head(x), label=f"Durata (primele {x})")
plt.plot(data["Puls"].head(x), label=f"Puls (primele {x})")
plt.title(f"Primele {x} valori")
plt.xlabel("Index")
plt.ylabel("Valoare")
plt.legend()
plt.show()

plt.figure()
plt.plot(data["Durata"].tail(y), label="Durata (ultimele Y)")
plt.plot(data["Puls"].tail(y), label="Puls (ultimele Y)")
plt.title(f"Ultimele {y} valori")
plt.xlabel("Index")
plt.ylabel("Valoare")
plt.legend()
plt.show()
