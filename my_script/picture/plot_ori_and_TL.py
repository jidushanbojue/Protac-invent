import os
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import argparse


def plot_item_line(item_file):

    filepath, file_name = os.path.split(item_file)
    df = pd.read_csv(item_file)


    # plt.rcParams['font.family'] = 'Time New Roman'
    plt.rcParams['font.size'] = 15
    plt.rcParams['axes.unicode_minus'] = False
    # plt.rcParams['font.weight'] = 'bold'


    fig = plt.figure(dpi=300)

    fig, axes = plt.subplots(1, 3, sharex=False, sharey=False, figsize=(30, 8))
    fig.subplots_adjust(wspace=0.3, hspace=0.5)

    sns.lineplot(df['Steps'], df['Average_score'], color='r', ax=axes[0], linewidth=3, label='ori')
    sns.lineplot(df['Steps'], df['Average_score_TL'], color='b', ax=axes[0], linewidth=3, label='TL')
    axes[0].set_ylabel('Average_Score')

    sns.lineplot(df['Steps'], df['ADV'], color='r', ax=axes[1], linewidth=3, label='ori')
    sns.lineplot(df['Steps'], df['ADV_TL'], color='b', ax=axes[1], linewidth=3, label='TL')
    axes[1].set_ylabel('Sigmoid of Docking Score')

    sns.lineplot(df['Steps'], df['Valid_SMILES'], color='r', ax=axes[2], linewidth=3, label='ori')
    sns.lineplot(df['Steps'], df['Valid_SMILES_TL'], color='b', ax=axes[2], linewidth=3, label='TL')
    axes[2].set_ylabel('Valid SMILES')

    # lines, labels = fig.axes[0].get_legend_handles_labels()
    # # print(lines, labels)
    # fig.legend(lines, labels, loc='upper center')
    #
    # axes[0].get_legend().remove()

    result_picture = os.path.join(filepath, file_name.split('.')[0]+'.png')
    plt.savefig(result_picture)

    plt.show()

    # axes[0, 0].set_title('Average')




if __name__ == '__main__':
    base_dir = '/data/baiqing/PycharmProjects/Reinvent-master-3.2/result/LINK_invent/BAF/picture_log'
    average_score_file = os.path.join(base_dir, 'ori_and_TL_merged.csv')

    # parser = argparse.ArgumentParser(description='Generate training log picture')
    # parser.add_argument('-i', '--input', type=str, default=None, help='Specify the smooth absolute path')
    # # parser.add_argument('-n', '--item_name', type=str, default=None, help='Specify the item name of Log')
    # # parser.add_argument('-o', '--out', type=str, default=None, help='Specify the result log dir')
    # # parser.add_argument('-f', '--file', type=str, help='Specify the filename for the output_file')
    #
    # args = parser.parse_args()

    # if os.path.exists(args.out):
    #     pass
    # else:
    #     os.mkdir(args.out)



    # plot_item_line(item_file=args.input)
    plot_item_line(average_score_file)