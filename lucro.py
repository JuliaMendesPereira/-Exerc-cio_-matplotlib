import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

dados = {
    "Mês": ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"],
    "Lucro": [12000, 15000, 17000, 14000, 16000, 18000, 22000, 21000, 19000, 23000, 25000, 24000]
}

df = pd.DataFrame(dados)

sns.lineplot(data=df, x="Mês", y="Lucro", marker='o', color='blue')
plt.title("Evolução do Lucro Mensal")
plt.show()