import os
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import argparse



def plot_log(training_log_file):
    df = pd.read_csv(training_log_file)

    # df = df[df.index % 2 == 0]

    df.rename(columns={'step': 'Step'}, inplace=True)
    # sns.set_palette('Blues_d')

    plt.rcParams['font.size'] = 20
    plt.rcParams['font.weight'] = 'bold'
    plt.rcParams['axes.unicode_minus'] = False


    path, name = os.path.split(training_log_file)

    # if 'sum' in name:
    #     result_name = item_name+'_custom_sum'
    # else:
    #     result_name = item_name+'_custom_product'


    fig = plt.figure(dpi=300, figsize=(20, 15))

    # palette = sns.xkcd_palette(["dusty purple", "red", "black", "cyan", "magenta])

    palette = sns.xkcd_palette(["amber", "greyish", "faded green", "cyan", "magenta"])

    sns.violinplot(x='Link Length', y='raw_Linker_Effective_Length', data=df[:])

    plt.xlabel('Link Length', fontdict={'fontsize': 30, 'fontweight': 'bold'})
    plt.ylabel('raw_Linker_Effective_Length', fontdict={'fontsize': 30, 'fontweight': 'bold'})

    ax = plt.gca()
    ax.spines['bottom'].set_linewidth(2)
    ax.spines['top'].set_linewidth(2)
    ax.spines['left'].set_linewidth(2)
    ax.spines['right'].set_linewidth(2)

    fig_path = os.path.join(path, 'bond_distance_violinplot_custom_sum_3_1.png')
    plt.savefig(fig_path)

    # plt.show()




if __name__ == '__main__':

    base_dir = '/data/baiqing/PycharmProjects/Reinvent-master-3.2/my_script/picture'

    # file = os.path.join(base_dir, 'linkinvent', 'BTK', 'training_log_sum_3.csv')
    file = os.path.join(base_dir, 'linkinvent', 'BTK', 'link_length_distribution.csv')

    parser = argparse.ArgumentParser(description='Generate training log picture')
    parser.add_argument('-i', '--input', type=str, default=None, help='Specify the smooth absolute path')
    # parser.add_argument('-n', '--item_name', type=str, default=None, help='Specify the item name of Log')


    args = parser.parse_args(['-i', file])

    plot_log(args.input)


