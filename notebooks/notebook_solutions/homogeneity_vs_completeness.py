from sklearn.metrics import homogeneity_score
from sklearn.metrics import completeness_score

true_classes = ["a", "b", "b", "a"]
clustering = [0, 1, 2, 0]

print(true_classes, clustering)
print(f"Homogeneity: {homogeneity_score(true_classes, clustering):.3f}, "
      f"Completeness: {completeness_score(true_classes, clustering):.3f}",
      end="\n\n")


true_classes = ["a", "b", "b", "a"]
clustering = [1, 1, 1, 1]

print(true_classes, clustering)
print(f"Homogeneity: {homogeneity_score(true_classes, clustering):.3f}, "
      f"Completeness: {completeness_score(true_classes, clustering):.3f}")