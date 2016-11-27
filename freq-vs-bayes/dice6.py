import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from matplotlib import animation
import os


def makeAnim(fig, imgArray):

    anim = animation.ArtistAnimation(fig, imgArray, interval=20)
    anim.save(
        os.path.dirname(__file__) + '/anim.gif', writer='imagemagick', fps=10)


def dice6(trial_num):
    samples = np.array([])
    for i in range(trial_num):
        samples = np.append(samples, np.random.randint(1, 7))
    return samples


if __name__ == "__main__":
    fig = plt.figure(figsize=(4, 4))
    imgArray = []

    trial_num = 200
    all_samples = dice6(trial_num)
    roll = range(1, 7)
    sum_of_rolls = np.zeros([7])

    for step in range(1, trial_num):
        samples = all_samples[:step]
        for i in roll:
            sum_of_rolls[i] = len(samples[samples == i])

        sum_of_rolls = sum_of_rolls / step

        print step, ":", sum_of_rolls
        imgArray.append(plt.bar(roll, sum_of_rolls[1:7]))
    # plt.show()
    makeAnim(fig, imgArray)
