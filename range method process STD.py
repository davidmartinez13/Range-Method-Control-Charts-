import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
# Mean = 0, SD = 1.
mu=0
sigma=1
samples= 100000
dist1=np.random.normal(mu, sigma, samples)
dist2=np.random.normal(mu, sigma, samples)
dist3=np.random.normal(mu, sigma, samples)
dist4=np.random.normal(mu, sigma, samples)
dist5=np.random.normal(mu, sigma, samples)
n5=np.array([dist1,dist2,dist3,dist4,dist5])

rangeStat1= abs(dist1-dist2)#range n=2 calculation
d2_n2=float(sum(rangeStat1)/samples)/sigma#find d2 as the average of ranges/ sigma


rangeStat2= abs(np.amax(n5, axis=0)-np.amin(n5, axis=0))#range n=5 calculation
print(rangeStat2)
d2_n5=float(sum(rangeStat2)/samples)/sigma#find d2 as the average of ranges/ sigma


plt.subplot(1,2,1)
plt.title("Range Histogram with n=2")
plt.xlabel("Ranges")
plt.ylabel("Frequency")
plt.hist(rangeStat1,bins='auto',color = "skyblue",alpha=0.3)
plt.scatter(d2_n2,0.0)
plt.annotate("  d2 ~="+str(d2_n2),[d2_n2,0.0])

plt.subplot(1,2,2)
plt.title("Range Histogram with n=5")
plt.xlabel("Ranges")
plt.ylabel("Frequency")
plt.hist(rangeStat1,bins='auto',color = "r",alpha=0.3)
plt.scatter(d2_n5,0.0)
plt.annotate("  d2 ~="+str(d2_n5),[d2_n5,0.0])
plt.show()
