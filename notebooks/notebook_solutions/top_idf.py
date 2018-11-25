import pandas as pd

weighted_terms = pd.DataFrame({"term": vectorizer.get_feature_names(), "idf": tfidf_transformer.idf_})

print("Most 'informative' terms:")
print(weighted_terms.nlargest(10, "idf"), end="\n\n")

print("Least informative terms:")
print(weighted_terms.nsmallest(10, "idf"), end="\n\n")