from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import streamlit as st
from model import *
import seaborn as sns

st.markdown("# ANALYSE 📈")
st.sidebar.markdown("Analyse📈")
#----------------------------elbow methods-----------------------

st.markdown(f"<h5>Avec le Elbows Methods, on constate qu'on peut classer 5 types de clients dans un centre commercial</h5>", unsafe_allow_html=True)


wcss = []

for i in range(1, 11):
    kmeans2 = KMeans(n_clusters = i, init = 'k-means++', random_state = 42, n_init="auto")
    kmeans2.fit(X)
    wcss.append(kmeans2.inertia_) #inertia_ = wcss


fig, ax = plt.subplots()
ax.plot(range(1, 11), wcss)
ax.set_xlabel("Number of clusters")
ax.set_ylabel("WCSS") 
st.pyplot(fig)

#------------seaborn--------------------
st.markdown(f"<h3 style='color:yellow;'>GRAPHIQUE DU DATASET:</h3>", unsafe_allow_html=True)

splot = sns.pairplot(dataset)
st.pyplot(splot.fig)



#--------------------cluster customer--------------------------------
st.markdown(f"<h3 style='color:green;'>GRAPHIQUE DU CLASSEMENT:</h3>", unsafe_allow_html=True)

fig2, ax2 = plt.subplots()

ax2.scatter(X[y_kmeans == 0, 0], X[y_kmeans == 0, 1], s = 50, c = 'red', label = 'Cluster 1')

ax2.scatter(X[y_kmeans == 1, 0], X[y_kmeans == 1, 1], s = 50, c = 'blue', label = 'Cluster 2')

ax2.scatter(X[y_kmeans == 2, 0], X[y_kmeans == 2, 1], s = 50, c = 'green', label = 'Cluster 3')

ax2.scatter(X[y_kmeans == 3, 0], X[y_kmeans == 3, 1], s = 50, c = 'cyan', label = 'Cluster 4')

ax2.scatter(X[y_kmeans == 4, 0], X[y_kmeans == 4, 1], s = 50, c = 'magenta', label = 'Cluster 5')

ax2.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s = 300, c = 'black', label = 'Centroids', marker='x')

ax2.set_xlabel('Annual Income (k$)')

ax2.set_ylabel('Spending Score (1-100)')

ax2.legend()

st.pyplot(fig2)



st.markdown(f"<h5 style='color: red;'>Classe 1 : </h5><h5>Client qui a un revenu moyen et qui fait une dépense moyenne</h5>", unsafe_allow_html=True)
st.markdown(f"<h5 style='color: blue;'>Classe 2 : </h5><h5>Client qui a un revenu élevé et qui fait une dépense élevée</h5>", unsafe_allow_html=True)
st.markdown(f"<h5 style='color: green;'>Classe 3 : </h5><h5>Client qui a un revenu faible mais qui fait une dépense élvée</h5>", unsafe_allow_html=True)
st.markdown(f"<h5 style='color: cyan;'>Classe 4 : </h5><h5>Client qui a un revenu élevé mais qui fait une dépense faible</h5>", unsafe_allow_html=True)
st.markdown(f"<h5 style='color: purple;'>Classe 5 : </h5><h5>Client qui a un revenu faible et qui fait une dépense faible</h5>", unsafe_allow_html=True)
