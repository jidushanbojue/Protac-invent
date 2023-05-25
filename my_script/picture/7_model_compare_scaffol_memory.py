import os
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import argparse


def plot_log(file):
    df = pd.read_csv(file)
    plt.rcParams['font.size'] = 15
    plt.rcParams['axes.unicode_minus'] = False

    fig = plt.figure(dpi=300, figsize=(20, 15))
    sns.barplot(x='bond_distance', y='ratio', hue='model', data=df)

    plt.xlabel('Link Length', fontsize=30)
    plt.ylabel('Ratio of Average Score > 0.8', fontsize=30)

    path, name = os.path.split(file)

    result_file_path = os.path.join(path, 'scaffold_memory_ratio.png')
    plt.savefig(result_file_path)

    # plt.show()


if __name__ == '__main__':

    base_dir = '/data/baiqing/PycharmProjects/Reinvent-master-3.2/my_script/picture'

    file = os.path.join(base_dir, 'four_model_compare', 'four_model_sum_scaffold_memory.csv')

    parser = argparse.ArgumentParser(description='Generate training log picture')
    parser.add_argument('-i', '--input', type=str, default=None, help='Specify the smooth absolute path')
    # parser.add_argument('-n', '--item_name', type=str, default=None, help='Specify the item name of Log')


    args = parser.parse_args(['-i', file])

    plot_log(args.input)