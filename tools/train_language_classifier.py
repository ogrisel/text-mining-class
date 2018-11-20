import pandas as pd
import sys
import shutil
from time import time
from gzip import GzipFile
import pickle
from sklearn.model_selection import cross_val_score, GroupKFold
from tmclass_exercises import MODEL_FOLDER_PATH as MODEL_FOLDER_EXERCISES_PATH
from tmclass_solutions import MODEL_FOLDER_PATH as MODEL_FOLDER_SOLUTIONS_PATH
from tmclass_solutions import DATA_FOLDER_PATH
from tmclass_solutions.language_detector import build_language_classifier
from tmclass_solutions.data_download import download_wikipedia_language_dataset


verbose = "--verbose" in sys.argv
skip_cross_validation = "--skip-cross-validation" in sys.argv

download_wikipedia_language_dataset(verbose=verbose)

data_path = DATA_FOLDER_PATH / "wikipedia_language.parquet"

print(f"Loading dataset from {data_path} ...")
t0 = time()
df = pd.read_parquet(data_path)
print(f"done in {time() - t0:.3f}s")

print(f"Training classifier ...")
t0 = time()
model = build_language_classifier(df["text"], df["language"], verbose=verbose)
print(f"done in {time() - t0:.3f}s")

model_path_so = MODEL_FOLDER_SOLUTIONS_PATH / "language_classifier.pkl.gz"
model_path_ex = MODEL_FOLDER_EXERCISES_PATH / "language_classifier.pkl.gz"

print(f"Saving model to {model_path_so}")
with GzipFile(model_path_so, mode="wb") as f:
    pickle.dump(model, f, protocol=4)

print(f"Copying model to {model_path_so}")
shutil.copyfile(model_path_so, model_path_ex)

if not skip_cross_validation:
    t0 = time()
    print("Performing 5-fold cross-validation across wikipedia articles...")
    cv = GroupKFold(n_splits=5).split(df, groups=df["article_name"])
    cv_scores = cross_val_score(model, df["text"], df["language"], cv=cv,
                                verbose=verbose)
    print(f"done in {time() - t0:.3f}s")
    print(f"Cross-valided accuracy: "
          f"{cv_scores.mean():.3f} (+/- {cv_scores.std():.3f})")
