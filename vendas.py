import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


dados = {
    "Região": ["Sul", "Sudeste", "Centro-Oeste", "Nordeste", "Norte"],
    "Vendas": [35000, 52000, 27000, 31000, 18000]
}

df = pd.DataFrame(dados)

sns.barplot(data=df, x="Região",y="Vendas")

plt.title("vendas por região do paí")
plt.show()