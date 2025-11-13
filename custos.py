import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

dados = {
    "Produto": ["Notebook", "Celular", "Tablet", "Fone", "Monitor"],
    "Custo": [2500, 1800, 1200, 200, 900],
    "Receita": [3200, 2300, 1700, 350, 1200]
}
df = pd.DataFrame(dados)

fig, ax = plt.subplots(1, 2, figsize=(9, 4))
sns.barplot(data=df, x="Produto", y="Custo", color="salmon", ax=ax[0])
sns.barplot(data=df, x="Produto", y="Receita", color="lightgreen", ax=ax[1])
ax[0].set_title("Custos"); ax[1].set_title("Receita")
plt.tight_layout()
plt.show()
