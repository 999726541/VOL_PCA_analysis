import numpy as np
from sklearn.decomposition import PCA
import pandas as pd

ipca = PCA()
data = pd.read_csv('/home/leo-gwise/PycharmProjects/vix_termstructure_PCA_analysis/vix_term_strcuture.csv')
matrix = data.filter(regex='_VOL').as_matrix()
matrix = np.square(matrix)
ipca.fit(matrix)


print(ipca.explained_variance_ratio_)
for i in ipca.components_:
    for z in i:
        print(z)


