%matplotlib inline
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path


sorted_similarities = pd.DataFrame({
    "filepath": text_filepaths[1:],
    "category": categories[1:],
    "similarity": similarities,
}).sort_values("similarity", ascending=False)

# Most related document
print(sorted_similarities.head(15))

# Distribution of all cosine similarities w.r.t. the first
# document.
plt.plot(sorted_similarities["similarity"].values);

# Most similar document:
closest_doc_path = Path(sorted_similarities['filepath'].iloc[0])

print("Query document:")
print(text_filepaths[0].read_text(encoding="utf-8"), end="\n\n")

print("First result document document:")
print(closest_doc_path.read_text(encoding="utf-8"), end="\n\n")