import numpy as np

points = np.array([[0., 0.], [3., 4.], [0., 4.]])
differences = points[:, None, :] - points[None, :, :]
distances = np.sqrt(np.sum(differences**2, axis=2))
print("Pairwise distances:")
print(distances)
print("Column means:")
print(points.mean(axis=0))
print("Rows whose distance from the origin is at least four:")
print(points[np.linalg.norm(points, axis=1) >= 4])
original = np.arange(6).reshape(2, 3)
view = original[:, 1:]
copy = view.copy()
view[0, 0] = 99
print("Array after changing a slice:")
print(original)
print("Independent copy:")
print(copy)
