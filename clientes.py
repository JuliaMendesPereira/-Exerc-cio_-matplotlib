import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

dados = {
    "Cliente": ["Ana", "Bruno", "Carla", "Daniel", "Eduarda", "Felipe", "Gabriela", "Heitor"],
    "Satisfação": [8.5, 6.0, 9.0, 7.5, 8.0, 5.5, 9.5, 7.0],
    "Categoria": ["Premium", "Básico", "Premium", "Básico", "Premium", "Básico", "Premium", "Básico"]
}

df = pd.DataFrame(dados)

sns.boxplot(data=df, x="Categoria", y="Satisfação")
plt.title("Satisfação dos Clientes por Categoria")
plt.show()