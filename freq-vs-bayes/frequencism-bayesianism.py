# coding:utf-8
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from matplotlib import animation
import os

rand_nums = np.random.rand(400)
pred_array = np.array([])
fig = plt.figure(figsize=(4, 4))


def makeAnim(fig, imgArray):

    anim = animation.ArtistAnimation(fig, imgArray, interval=10)
    anim.save(
        os.path.dirname(__file__) + '/anim.gif', writer='imagemagick', fps=30)


def plot(sample_nums, pred_nums):

    sample_num = len(sample_nums)
    plt.plot(range(sample_num), sample_nums)
    plt.plot(range(1, sample_num + 1), pred_nums)


def frequence():
    sample_nums = np.array([])
    averaged_nums = np.array([])

    for i in range(200):
        sample_nums = np.append(sample_nums, rand_nums[i])
        averaged_nums = np.append(averaged_nums, np.average(sample_nums[0:i]))

        plot(sample_nums, averaged_nums)

    plt.show()


def bayes():

    sample_nums = np.array([])
    averaged_nums = np.array([])
    pred_array = np.array([0])

    # fig = plt.figure(figsize=(4, 4))
    imgArray = []
    for i in range(200):
        sample_nums = np.append(sample_nums, rand_nums[i])
        averaged_nums = np.append(averaged_nums,
                                  np.average(sample_nums[0:i + 1]))
        sample_num = len(sample_nums)

        if (sample_num >= 2):

            pred_num = np.random.normal(
                loc=averaged_nums[i], scale=np.var(sample_nums)**0.5)
            pred_array = np.append(pred_array, pred_num)
            #plot(sample_nums, pred_array)
            plt.ylim(ymin=0, ymax=2)
            x = np.arange(-1, 2, 0.1)

            img = plt.plot(
                x,
                norm.pdf(x,
                         loc=averaged_nums[i],
                         scale=np.var(sample_nums)**0.5),
                "b",
                averaged_nums[i],
                0,
                "ro")

            imgArray.append(img)
            #plt.pause(0.04)

            # plt.show()
        # plt.show()

        #plt.plot(averaged_nums)
        #plt.plot(pred_array)
        #plt.show()

    makeAnim(fig, imgArray)


if __name__ == '__main__':
    #frequence()
    bayes()
    print "finish"
