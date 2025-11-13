import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Dados
dados = {
    "Aplicativo": ["Instagram", "TikTok", "WhatsApp", "YouTube", "X (Twitter)"],
    "Minutos por dia": [95, 110, 80, 120, 60]
}

df = pd.DataFrame(dados)

# Gráfico simples de barras
sns.barplot(data=df, x="Aplicativo", y="Minutos por dia", color="skyblue")

# Título
plt.title("Tempo Médio Diário por Aplicativo")

# Mostra o gráfico
plt.show()
