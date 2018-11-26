import pandas as pd
feature_names = tfidf_vectorizer.get_feature_names()

for i, center in enumerate(kmeans.cluster_centers_):
    print(f"Cluster #{i}:")
    df = pd.DataFrame({"word": feature_names, "weight": center})
    print(df.nlargest(10, "weight"))
    print()
