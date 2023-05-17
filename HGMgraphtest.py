import matplotlib.pyplot as plt

left = ["The Hunger Games", "Catching Fire", "Mockingjay Part 1", "Mockingjay Part 2"]

height = [30499, 61822, 138535, 145869]

plt.bar(left, height, width=0.5)

plt.xlabel('The Hunger Games Series')

plt.ylabel('Likes vs. Dislikes')

plt.title('Hunger Games Bar Chart')

plt.show()
