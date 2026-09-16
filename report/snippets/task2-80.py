t = np.arange(12.) / 12
x = np.sin(2 * np.pi * t)
q = 3
try:
    signal.resample(x, np.ceil(len(x)/q))
except TypeError as error:
    print(type(error).__name__ + ": " + str(error))
print(signal.resample(x, int(np.ceil(len(x)/q))))

