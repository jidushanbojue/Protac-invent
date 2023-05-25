import os
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import argparse



def plot_item_line(item_file, item_name):

    filepath, file_name = os.path.split(item_file)
    df = pd.read_csv(item_file)


    # plt.rcParams['font.family'] = 'Time New Roman'
    plt.rcParams['font.size'] = 15
    plt.rcParams['axes.unicode_minus'] = False
    # plt.rcParams['font.weight'] = 'bold'


    fig = plt.figure(dpi=300)

    fig, axes = plt.subplots(2, 2, sharex=False, sharey=True, figsize=(20, 12))
    fig.subplots_adjust(wspace=0.2, hspace=0.5)

    sns.lineplot(df['Steps'], df['custom_product_docking_weight1'], color='r', ax=axes[0, 0], linewidth=3, label='custom_product')
    sns.lineplot(df['Steps'], df['custom_sum_docking_weight1'], color='b', ax=axes[0, 0], linewidth=3, label='custom_sum')
    axes[0, 0].set_ylabel(item_name)
    axes[0, 0].set_title('Docking Weight: 1')

    sns.lineplot(df['Steps'], df['custom_product_docking_weight2'], color='r', ax=axes[0, 1], linewidth=3)
    sns.lineplot(df['Steps'], df['custom_sum_docking_weight2'], color='b', ax=axes[0, 1], linewidth=3)
    axes[0, 1].set_ylabel(item_name)
    axes[0, 1].set_title('Docking Weight: 2')

    sns.lineplot(df['Steps'], df['custom_product_docking_weight3'], color='r', ax=axes[1, 0], linewidth=3)
    sns.lineplot(df['Steps'], df['custom_sum_docking_weight3'], color='b', ax=axes[1, 0], linewidth=3)
    axes[1, 0].set_ylabel(item_name)
    axes[1, 0].set_title('Docking Weight: 3')

    sns.lineplot(df['Steps'], df['custom_product_docking_weight4'], color='r', ax=axes[1, 1], linewidth=3)
    sns.lineplot(df['Steps'], df['custom_sum_docking_weight4'], color='b', ax=axes[1, 1], linewidth=3)
    axes[1, 1].set_ylabel(item_name)
    axes[1, 1].set_title('Docking Weight: 4')

    lines, labels = fig.axes[0].get_legend_handles_labels()
    # print(lines, labels)
    fig.legend(lines, labels, loc='center')

    axes[0, 0].get_legend().remove()


    # plt.title('Training log of Average Score')

    result_picture = os.path.join(filepath, file_name.split('.')[0]+'.png')
    plt.savefig(result_picture)

    # plt.show()

    print('Done')


if __name__ == '__main__':
    # base_dir = '/data/baiqing/PycharmProjects/Reinvent-master-3.2/result/LINK_invent/BRD9/picture_log'
    # average_score_file = os.path.join(base_dir, 'average_score_merged.csv')

    parser = argparse.ArgumentParser(description='Generate training log picture')
    parser.add_argument('-i', '--input', type=str, default=None, help='Specify the smooth absolute path')
    parser.add_argument('-n', '--item_name', type=str, default=None, help='Specify the item name of Log')
    # parser.add_argument('-o', '--out', type=str, default=None, help='Specify the result log dir')
    # parser.add_argument('-f', '--file', type=str, help='Specify the filename for the output_file')

    args = parser.parse_args()

    # if os.path.exists(args.out):
    #     pass
    # else:
    #     os.mkdir(args.out)



    plot_item_line(item_file=args.input, item_name=args.item_name)

