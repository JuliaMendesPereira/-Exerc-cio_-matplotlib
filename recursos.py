import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

dados = {
    "Funcionário": ["Alice", "Bruno", "Carlos", "Diana", "Eduardo", "Fernanda", "Gustavo", "Helena"],
    "Produtividade": [82, 74, 90, 65, 77, 88, 93, 70],
    "Horas_Semanais": [40, 36, 42, 30, 38, 44, 45, 35]
}

df = pd.DataFrame(dados)

sns.scatterplot(data=df, x="Horas_Semanais", y="Produtividade")
plt.xlabel("Horas Semanais")
plt.ylabel("Produtividade")
plt.title("Relação entre Produtividade e Horas de Trabalho")
plt.show()