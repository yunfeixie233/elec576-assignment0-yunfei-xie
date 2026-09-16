a = rect.copy()
Q, R = linalg.qr(a)
print(Q)
print(R)
Q, R = linalg.qr(a, mode="economic")
print(Q)
print(R)

