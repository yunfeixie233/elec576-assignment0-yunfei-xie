a = small.copy()
print(a.max())
print(np.nanmax(a))
a[0, 0] = np.nan
print(a.max())
print(np.nanmax(a))

