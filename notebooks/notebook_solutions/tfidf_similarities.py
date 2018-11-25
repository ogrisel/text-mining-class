%matplotlib inline
import pandas as pd
import matplotlib.pyplot as plt


sorted_similarities = pd.DataFrame({
    "doc_id": np.arange(len(similarities)) + 1,
    "similarity": similarities,
    "category": categories[1:],
}).sort_values("similarity", ascending=False)

print(sorted_similarities.head(15))
plt.plot(sorted_similarities["similarity"].values);

closest_doc_id = int(sorted_similarities['doc_id'].iloc[0])

print("Query document:")
print(text_filepaths[0].read_text(encoding="utf-8"), end="\n\n")

print("First result document document:")
print(text_filepaths[closest_doc_id].read_text(encoding="utf-8"), end="\n\n")
