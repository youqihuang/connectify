from sklearn import metrics
from sklearn.cluster import KMeans
from sklearn.datasets import load_digits
from sklearn.decomposition import PCA
from sklearn.preprocessing import scale

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('features.csv', sep="\"\,\"")
data = pd.concat([df.iloc[:,0].str.split(',', expand=True).rename(columns=dict(zip([0,1], df.columns[0].split(',')))), df.iloc[:,1:]], axis=1)

# Drop first row using drop()
data.drop(index=data.index[0], axis=0, inplace=True)
data.drop(index=data.index[0], axis=0, inplace=True)

print(data.shape)
print(data.head(60))

# finding out the proper number of clusters
df_val = data.iloc[:, [4,5,6,7,8,9,10,11]].values
# wcss = []
# for i in range(1,11):
#   kmeans = KMeans(n_clusters = i, init = 'k-means++', max_iter = 300, n_init = 10, random_state = 0)
#   kmeans.fit(df_val)
#   wcss.append(kmeans.inertia_)
# plt.plot(range(1,11), wcss)
# plt.title('Elbow Method')
# plt.xlabel('Number of Clusters')
# plt.ylabel('WCSS')
# plt.savefig('Elbow_Method.png')
# plt.show()
     
# data preprocessing
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
scaled = scaler.fit_transform(df_val)

# instantiating model
kmeans = KMeans(n_clusters = 5, init = 'k-means++', max_iter = 300, n_init = 10, random_state = 0)
y_kmeans = kmeans.fit_predict(scaled)
# print(y_kmeans)

# from mpl_toolkits.mplot3d import Axes3D
# # visualizing clusters
# fig, ax = plt.subplots(figsize=(13,11))
# ax = fig.add_subplot(111, projection='3d')
# plt.scatter(scaled[y_kmeans == 0,0],scaled[y_kmeans == 0,1], s= 50, c= 'red',label= 'Cluster 1')
# plt.scatter(scaled[y_kmeans == 1,0], scaled[y_kmeans == 1,1], s= 50, c= 'blue', label= 'Cluster 2')
# plt.scatter(scaled[y_kmeans == 2,0], scaled[y_kmeans == 2,1], s= 50, c= 'green', label= 'Cluster 3')
# plt.scatter(scaled[y_kmeans == 3,0], scaled[y_kmeans == 3,1], s= 50, c= 'cyan', label= 'Cluster 4')
# plt.scatter(scaled[y_kmeans == 4,0], scaled[y_kmeans == 4,1], s= 50, c= 'magenta', label= 'Cluster 5')
# # centroids
# plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:,1], s= 300, c= 'yellow', label= 'Centroids')
# plt.title('Clusters')
# plt.legend()
# plt.savefig('clusters.png')
# plt.show()


# converting predictions into a df
kmeans = pd.DataFrame(data=y_kmeans, dtype=int)
kmeans.columns = ['k_cluster']

# predictions as a df
# print(kmeans.shape)
# print(kmeans.head())

df_cluster = pd.concat([data, kmeans], axis=1)
df_cluster = df_cluster[:-2]
df_cluster.at[50,'k_cluster'] = 0.0
df_cluster.at[51,'k_cluster'] = 1.0
with pd.option_context('display.max_rows', None,
                       'display.max_columns', None,
                       'display.precision', 3,
                       ):
    print(df_cluster)
df_cluster.to_csv('df_cluster.csv', mode = 'w')
# checking for null
# print()
# print((df_cluster.isnull().sum()/ df_cluster.shape[0]).sort_values(ascending=False))

# print(df_cluster['k_cluster'].value_counts())

# print(df_cluster.loc[df_cluster['k_cluster'] == 0][:10])
# print(df_cluster.loc[df_cluster['k_cluster'] == 1][:10])
# print(df_cluster.loc[df_cluster['k_cluster'] == 2][:10])
# print(df_cluster.loc[df_cluster['k_cluster'] == 3][:10])
# print(df_cluster.loc[df_cluster['k_cluster'] == 4][:10])
