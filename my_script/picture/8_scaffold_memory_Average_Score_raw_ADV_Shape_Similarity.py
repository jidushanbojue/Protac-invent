import os
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import argparse


# def plot_log(file):
#     df = pd.read_csv(file)
#
#     plt.rcParams['font.size'] = 20
#     plt.rcParams['font.weight'] = 'bold'
#     plt.rcParams['axes.unicode_minus'] = False
#
#     fig = plt.figure(dpi=300, figsize=(20, 15))
#     sns.barplot(x='Link Length', y='Count', hue='Score Component', data=df)
#
#
#     plt.xlabel('Link Length', fontdict={'fontsize': 30, 'fontweight': 'bold'})
#     plt.ylabel('Number of SMILES', fontdict={'fontsize': 30, 'fontweight': 'bold'})
#
#     ax = plt.gca()
#     ax.spines['bottom'].set_linewidth(2)
#     ax.spines['top'].set_linewidth(2)
#     ax.spines['left'].set_linewidth(2)
#     ax.spines['right'].set_linewidth(2)
#
#     # plt.show()
#
#
#     path, name = os.path.split(file)
#
#     result_file_path = os.path.join(path, 'scaffold_memory_Average_Score_raw_ADV_PostDock.png')
#     plt.savefig(result_file_path)


def plot_log(file):
    df = pd.read_csv(file)

    plt.rcParams['font.size'] = 20
    plt.rcParams['font.weight'] = 'bold'
    plt.rcParams['axes.unicode_minus'] = False

    fig = plt.figure(dpi=300, figsize=(20, 15))
    sns.barplot(x='Link Length', y='Ratio', hue='Score Component', data=df)


    plt.xlabel('Link Length', fontdict={'fontsize': 30, 'fontweight': 'bold'})
    plt.ylabel('Ratio', fontdict={'fontsize': 30, 'fontweight': 'bold'})

    ax = plt.gca()
    ax.spines['bottom'].set_linewidth(2)
    ax.spines['top'].set_linewidth(2)
    ax.spines['left'].set_linewidth(2)
    ax.spines['right'].set_linewidth(2)

    # plt.show()


    path, name = os.path.split(file)

    result_file_path = os.path.join(path, 'scaffold_memory_Average_Score_raw_ADV_PostDock_1.png')
    plt.savefig(result_file_path)




if __name__ == '__main__':

    base_dir = '/data/baiqing/PycharmProjects/Reinvent-master-3.2/my_script/picture'

    file = os.path.join(base_dir, 'linkinvent', 'BTK', 'scaffold_memory_average_score_raw_ADV_PostDock.csv')

    parser = argparse.ArgumentParser(description='Generate training log picture')
    parser.add_argument('-i', '--input', type=str, default=None, help='Specify the smooth absolute path')
    # parser.add_argument('-n', '--item_name', type=str, default=None, help='Specify the item name of Log')


    args = parser.parse_args(['-i', file])

    plot_log(args.input)