import numpy as np
import numpy.ma as ma
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans,  MiniBatchKMeans, AffinityPropagation


def run_code(prices_list, reviews_list, num_of_beds_list, num_of_clusters=9, clustering_algorithm=1):

    # Scaling Features
    sc = StandardScaler()
    avg_price = sc.fit_transform(np.array(prices_list).reshape(-1, 1))
    med_review = sc.fit_transform(np.array(reviews_list).reshape(-1, 1))
    med_beds = sc.fit_transform(np.array(num_of_beds_list).reshape(-1, 1))

    # Combine Scaled feature
    X_comb = np.column_stack([avg_price, med_review, med_beds])

    # Handling null value with masked array
    X = np.where(np.isnan(X_comb), ma.array(
        X_comb, mask=np.isnan(X_comb)).mean(axis=0), X_comb)

    # Modeling
    result = []
    if clustering_algorithm == 1:
        kmeans = KMeans(n_clusters=num_of_clusters, random_state=99)
        result = kmeans.fit_predict(X).tolist()
    elif clustering_algorithm == 2:
        minib = MiniBatchKMeans(n_clusters=num_of_clusters, random_state=99)
        result = minib.fit_predict(X).tolist()
    else:
        aff = AffinityPropagation().fit(X)
        result = aff.predict(X).tolist()

    return result
