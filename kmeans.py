import torch 
import numpy as np
import matplotlib.pyplot as plt
from kmeans_pytorch import kmeans, kmeans_predict

np.random.seed(123)
data_size=1000
dim=2
classes=3
x=np.random.randn(data_size,dim)/6
x=torch.from_numpy(x)

device=torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')

cluster_idx, cluster_center= kmeans(X=x, num_clusters=classes,distance='euclidean', device=device)

print(cluster_center)
print(cluster_idx)

plt.figure(figsize=(4,3),dpi=80)
plt.scatter(x[:, 0], x[:, 1], c=cluster_idx, cmap='cool')
plt.scatter(cluster_center[:,0],cluster_center[:,1],color='white',edgecolors='black',linewidths=2)
plt.axis([-1,1,-1,1])
plt.tight_layout(pad=33)
plt.show()





