import os
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import argparse

# def plot_log(training_log_file, item_name):
#
#     path, name = os.path.split(training_log_file)
#
#
#
#     if 'sum' in name:
#         result_name = item_name+'_custom_sum_1'
#     else:
#         result_name = item_name+'_custom_product_1'
#
#     df = pd.read_csv(training_log_file)
#     df.rename(columns={'step': 'Step'}, inplace=True)
#     # sns.set_palette('Blues_d')
#
#     plt.rcParams['font.size'] = 15
#     plt.rcParams['axes.unicode_minus'] = False
#
#
#     #
#
#     # sns.lineplot(x='step', y='Average_score', data=df[:400])
#     # sns.lineplot()
#     # sns.scatterplot()
#
#     # action_set = df['class'].unique().tolist()
#
#     # pallette = sns.color_palette('bright', 4)
#     # palette = sns.xkcd_palette(["windows blue", "amber", "greyish", "faded green"])
#
#
#     ### effective code-----------
#     # f, axes = plt.subplots(nrows=2, ncols=1, figsize=(20, 15))
#     # palette1 = sns.xkcd_palette(["windows blue", "amber", "greyish", "faded green"])
#     # sns.lineplot(x='step', y=item_name, data=df[:800], hue='class', palette=palette1, linewidth=2.2, ax=axes[0]) ###style='class'
#     # axes[0].set_xlabel('', size=20)
#     # axes[0].set_ylabel(item_name, size=20)
#     #
#     # palette2 = sns.xkcd_palette(["dusty purple", "red", "black", "cyan"])
#     # sns.lineplot(x='step', y=item_name, data=df[800:], hue='class', palette=palette2, linewidth=2.2, ax=axes[1])  ### style='class'
#     # axes[1].set_xlabel('Step', size=20)
#     # axes[1].set_ylabel(item_name, size=20)
#     ###------------------------------
#
#
#     # sns.set()
#     # sns.set_style('ticks')
#
#     ### only for custom_sum, because for custom_sum, we do the bond-distance: no constraint,
#     fig = plt.figure(dpi=300, figsize=(20, 5))
#     palette1 = sns.xkcd_palette(["cyan", "windows blue", "amber", "greyish", "faded green"])
#     sns.relplot(x='Step', y=item_name, data=df[200:1000], col='Link Length', kind='line', linewidth=2.2, palette=palette1)
#     fig1 = os.path.join(path, '8_11_'+result_name+'.png')
#     # plt.xlabel('Step', fontsize=30)
#     plt.ylabel(item_name, fontsize=30)
#     plt.savefig(fig1)
#
#     fig = plt.figure(dpi=300, figsize=(20, 5))
#     palette2 = sns.xkcd_palette(["windows blue", "amber", "greyish", "faded green"])
#     sns.relplot(x='Step', y=item_name, data=df[1000:], col='Link Length', kind='line', linewidth=2.2, palette=palette2)
#     # plt.xlabel('Step', fontsize=30)
#     plt.ylabel(item_name, fontsize=30)
#     fig2 = os.path.join(path, '12_15_'+result_name+'.png')
#     plt.savefig(fig2)
#     # sns.relplot(x='step', y='Average_score', data=df[800:], col='class', kind='line', ax=plt.subplot(2, 1, 2))
#     # plt.show()



def plot_log(training_log_file, item_name):

    path, name = os.path.split(training_log_file)



    if 'sum' in name:
        result_name = item_name+'_custom_sum_3'
    else:
        result_name = item_name+'_custom_product_3'

    df = pd.read_csv(training_log_file)
    df.rename(columns={'step': 'Step'}, inplace=True)

    df = df[df.index % 2 == 0]
    # sns.set_palette('Blues_d')

    plt.rcParams['font.size'] = 20
    plt.rcParams['font.weight'] = 'bold'
    plt.rcParams['axes.unicode_minus'] = False

    # sns.set()
    # sns.set_style('ticks')

    ### only for custom_sum, because for custom_sum, we do the bond-distance: no constraint,
    fig = plt.figure(dpi=300, figsize=(20, 15))
    # palette1 = sns.xkcd_palette(["cyan", "windows blue", "amber", "greyish", "faded green"])
    palette1 = sns.xkcd_palette(["cyan", "maroon", "orange", "medium blue", "magenta"])
    # sns.relplot(x='Step', y=item_name, data=df, col='Link Length', kind='line', linewidth=2.2, palette=palette1)
    sns.lineplot(x='Step', y=item_name, data=df, hue='Link Length', linewidth=3.0, palette=palette1)
    # sns.lineplot(x='Step', y=item_name, data=df, hue='Link Length', linewidth=2.2)
    fig1 = os.path.join(path, '8_15_'+result_name+'.png')
    plt.xlabel('Step', fontdict={'fontsize': 30, 'fontweight': 'bold'})
    plt.ylabel(item_name, fontdict={'fontsize': 30, 'fontweight': 'bold'})

    ax = plt.gca()
    ax.spines['bottom'].set_linewidth(2)
    ax.spines['top'].set_linewidth(2)
    ax.spines['left'].set_linewidth(2)
    ax.spines['right'].set_linewidth(2)

    # plt.show()

    plt.savefig(fig1)



if __name__ == '__main__':

    base_dir = '/data/baiqing/PycharmProjects/Reinvent-master-3.2/my_script/picture'

    # linkinvent_product_dir = os.path.join(base_dir, 'linkinvent', 'BTK', 'training_log_product.csv')
    # linkinvent_sum_dir = os.path.join(base_dir, 'linkinvent', 'BTK', 'training_log_sum.csv')

    parser = argparse.ArgumentParser(description='Generate training log picture')
    parser.add_argument('-i', '--input', type=str, default=None, help='Specify the smooth absolute path')
    # parser.add_argument('-n', '--item_name', type=str, default=None, help='Specify the item name of Log')


    args = parser.parse_args(['-i', '/data/baiqing/PycharmProjects/Reinvent-master-3.2/my_script/picture/linkinvent/BTK/training_log_sum_3.csv'])

    item_list = ['Custom_alerts',
                 'Linker_Num_Aromatic_Rings',
                 'Linker_Effective_Length',
                 'ADV',
                 'PostDock_Tanimoto_ROCS_sim',
                 'raw_Linker_Num_Aromatic_Rings',
                 'raw_Linker_Effective_Length',
                 'raw_ADV',
                 'Valid_SMILES',
                 'Number_of_SMILES_found',
                 'Average_score']

    for item_name in item_list:
        plot_log(args.input, item_name)

    # plot_log(linkinvent_sum_dir, item_name='raw_Linker_Effective_Length')


    # plot_log(args.input, args.item_name)


