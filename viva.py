import numpy as np
import matplotlib.pyplot as plt

# IMAGES: 2x2 matrices
A = np.array([[100, 200], [50, 150]])
B = np.array([[0, 100], [200, 50]])

print("Blend 0.5A + 0.5B:")
print(0.5*A + 0.5*B)

print("Brighter 1.2A:")
print(1.2*A)

D = 2*A
print("2A (has 400, over 255):")
print(D)

print("After clipping:")
print(np.clip(D, 0, 255))

# AUDIO: two pure tones as vectors
t = np.linspace(0, 1, 8000)
x = np.sin(2*np.pi*440*t)   # 440 Hz
y = np.sin(2*np.pi*660*t)   # 660 Hz
z = 0.5*x + 0.5*y           # mix

plt.plot(t[:200], x[:200], label="x (440 Hz)")
plt.plot(t[:200], y[:200], label="y (660 Hz)")
plt.plot(t[:200], z[:200], label="0.5x + 0.5y")
plt.legend()
plt.title("Audio mixing as a linear combination")
plt.show()

# import numpy as np
# import matplotlib.pyplot as plt
# from PIL import Image

# A = Image.open("a.jpg").convert("L")        # L = grayscale
# B = Image.open("b.jpg").convert("L").resize(A.size)   # same size as A

# A = np.array(A, dtype=float)
# B = np.array(B, dtype=float)

# C = 0.5*A + 0.5*B                # blend
# D = np.clip(2*A, 0, 255)         # brighter, clipped

# fig, ax = plt.subplots(1, 4, figsize=(14, 4))
# for a, img, title in zip(ax, [A, B, C, D],
#                          ["Image A", "Image B", "0.5A + 0.5B", "2A (clipped)"]):
#     a.imshow(img, cmap="gray", vmin=0, vmax=255)
#     a.set_title(title)
#     a.axis("off")
# plt.show()