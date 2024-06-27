import matplotlib.pyplot as plt
import numpy as np

from matplotlib import cm
from matplotlib import axes

def main():
    plt.style.use('_mpl-gallery')

    # make data

    X = np.arange(1, 5, 1)
    Y = np.arange(1, 5, 1)
    X, Y = np.meshgrid(X, Y)
    Z = np.sin(np.sqrt(X**2 + Y**2))

    # plot

    fig, ax = plt.subplots(subplot_kw={'projection': '3d'})
    ax.set_zlim([0, 0.1])

    # ax.scatter(X, Y, Z)
    ax.plot_surface(X, Y, Z, vmin=Z.min() * 2, cmap=cm.rainbow)
    # ax.plot_wireframe(X, Y, Z, rstride=1, cstride=1)

    # ax.set(xticklabels=[], yticklabels=[], zticklabels=[])
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')

    plt.show()

# def make_z(X, Y):
#     arr = 

def hyperop(a, o, b):
    match o:
        case 1:
            return a + b
        case 2:
            return a * b
        case 3:
            return a ** b
        case 4:
            ret = a
            for i in range(0, b - 1):
                ret **= a
        case 5:
            ret = a
            for i in range(0, b - 1):
                ret = hyperop(ret, 4, a)

if __name__ == "__main__":
    main()
