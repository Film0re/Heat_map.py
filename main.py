import numpy as np
import matplotlib.pyplot as plt


def main():
    array = load_array()
    print_2d_array(array)

    X = np.array(array)

    X_flipped = np.flipud(X)  # Flip array so that the heatmap matches the array

    print(X)

    # fig = plt.figure(figsize=(8, 6))
    fig, ax = plt.subplots()

    for i in range(5):
        for j in range(5):
            text = ax.text(j, i, X_flipped[i, j],
                           ha="left", va="bottom", color="black")

    plt.pcolormesh(X_flipped, cmap="pink_r")
    plt.title("Plot 2D array")
    plt.colorbar()
    plt.savefig('fp.png')
    plt.show()


def print_2d_array(array):
    """
    Prints out a 2d array
    :param array: A 2d array
    :return: None
    """
    print('\n'.join([''.join(['{:4}'.format(item) for item in row])
                     for row in array]))


def load_array():
    """
    Loads a 2d array of ints and returns it
    :return: A 2d array containing ints
    """
    name = "p081_matrix.txt"
    name2 = "5x5.txt"

    file = open(name2)

    file_lines = file.readlines()
    # print(file_lines)

    array2D = []

    for line in file_lines:
        line = line.strip("\n")

        array2D.append(line.split(","))

    array2D = [list(map(int, i)) for i in array2D]

    return array2D


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
