import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# Membaca data dari Excel
df = pd.read_excel('midfielderstop5leagues.xlsx')

# Statistik Casemiro
stat_casemiro_2022_2023 = {
    'Player': 'Casemiro',
    'Passes Attempted': 1447,
    'Pass Completion %': 77.5,
    'Progressive Passes': 152,
    'Tackles': 88,
    'Blocks': 49,
    'Clearances': 64,
    'Interceptions': 34,
    'Aerial Duels Won': 56
}

# Menambahkan baris Casemiro ke DataFrame
df.loc[len(df)] = stat_casemiro_2022_2023

# Kolom fitur untuk analisis
features = ['Passes Attempted', 'Progressive Passes', 'Tackles', 'Blocks', 'Clearances', 'Interceptions', 'Aerial Duels Won', 'Pass Completion %']

# Normalisasi data
scaler = StandardScaler()
df_normalized = scaler.fit_transform(df[features])

# K-Means clustering
kmeans = KMeans(n_clusters=10, random_state=42)
df['Cluster'] = kmeans.fit_predict(df_normalized)

# Menemukan cluster Casemiro
casemiro_cluster = df[df['Player'] == 'Casemiro']['Cluster'].values[0]

# Filter pemain yang berada di cluster yang sama dengan Casemiro
similar_players = df[df['Cluster'] == casemiro_cluster]

# Streamlit interface
st.title("Pemain yang Mirip dengan Casemiro")

# Pilih pemain untuk dibandingkan
selected_player = st.selectbox("Pilih pemain untuk dibandingkan dengan Casemiro:", similar_players['Player'].unique(), index=0)

# Mendapatkan data untuk radar chart
def get_normalized_data(player_name):
    player_index = df[df['Player'] == player_name].index[0]
    return df_normalized[player_index]

# Membuat radar chart
fig = go.Figure()

# Menambahkan Casemiro
casemiro_data = get_normalized_data('Casemiro')
fig.add_trace(go.Scatterpolar(
      r=casemiro_data,
      theta=features,
      fill='toself',
      name='Casemiro',
      line=dict(color='blue')
))

# Menambahkan pemain yang dipilih
selected_data = get_normalized_data(selected_player)
fig.add_trace(go.Scatterpolar(
      r=selected_data,
      theta=features,
      fill='toself',
      name=selected_player,
      line=dict(color='red')
))

# Menentukan rentang sumbu radial secara dinamis
max_val = max(casemiro_data.max(), selected_data.max())
min_val = min(casemiro_data.min(), selected_data.min())

# Setel layout dan rentang axis
fig.update_layout(
  polar=dict(
    radialaxis=dict(
      visible=True,
      range=[min_val - 0.5, max_val + 0.5],  # Rentang disesuaikan secara dinamis
    ),
    angularaxis=dict(
      visible=True,
      tickvals=list(range(len(features))),
      ticktext=features
    )
  ),
  showlegend=True
)

st.plotly_chart(fig)