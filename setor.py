import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

dados = {
    "Setor": ["Financeiro", "Comercial", "TI", "RH", "Marketing", "Comercial", "TI", "Financeiro", "Marketing", "RH"],
    "Idade": [34, 29, 25, 41, 28, 33, 26, 38, 31, 45]
}

df = pd.DataFrame(dados)

sns.violinplot(data=df, x="Setor", y="Idade")
plt.title("Distribuição de Idades por Setor")
plt.show()