import os
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import argparse


# def plot_log(training_log_file, item_name):
#     df = pd.read_csv(training_log_file)
#
#     df = df[df.index % 2 == 0]
#
#     df.rename(columns={'step': 'Step'}, inplace=True)
#     # sns.set_palette('Blues_d')
#
#     plt.rcParams['font.size'] = 30
#     plt.rcParams['axes.unicode_minus'] = False
#
#
#     path, name = os.path.split(training_log_file)
#
#     if 'sum' in name:
#         result_name = item_name+'_custom_sum'
#     else:
#         result_name = item_name+'_custom_product'
#
#
#
#     fig = plt.figure(dpi=300, figsize=(20, 15))
#
#     # palette = sns.xkcd_palette(["dusty purple", "red", "black", "cyan"])
#
#     palette = sns.xkcd_palette(["windows blue", "amber", "greyish", "faded green", "cyan"])
#
#     sns.lineplot(x='Step', y=item_name, data=df, hue='docking_weight', linewidth=3.0, palette=palette, markers=True, style='docking_weight')
#     plt.xlabel('Step', fontsize=40)
#     plt.ylabel(item_name, fontsize=40)
#
#     # plt.show()
#
#     fig_path = os.path.join(path, result_name+'_docking_weight1_5_1.png')
#     plt.savefig(fig_path)
#
#
#     # plt.show()


def plot_log(training_log_file, item_name):
    df = pd.read_csv(training_log_file)

    df = df[df.index % 2 == 0]

    df.rename(columns={'step': 'Step'}, inplace=True)
    # sns.set_palette('Blues_d')

    plt.rcParams['font.size'] = 20
    plt.rcParams['font.weight'] = 'bold'
    plt.rcParams['axes.unicode_minus'] = False


    path, name = os.path.split(training_log_file)

    if 'sum' in name:
        result_name = item_name+'_custom_sum'
    else:
        result_name = item_name+'_custom_product'



    fig = plt.figure(dpi=300, figsize=(20, 15))

    # palette = sns.xkcd_palette(["dusty purple", "red", "black", "cyan"])

    # palette = sns.xkcd_palette(["windows blue", "amber", "greyish", "faded green", "cyan"])
    palette = sns.xkcd_palette(["cyan", "maroon", "orange", "medium blue", "magenta"])

    sns.lineplot(x='Step', y=item_name, data=df, hue='docking_weight', linewidth=3.0, palette=palette)
    plt.xlabel('Step', fontdict={'fontsize': 30, 'fontweight': 'bold'})
    plt.ylabel(item_name, fontdict={'fontsize': 30, 'fontweight': 'bold'})

    ax = plt.gca()
    ax.spines['bottom'].set_linewidth(2)
    ax.spines['top'].set_linewidth(2)
    ax.spines['left'].set_linewidth(2)
    ax.spines['right'].set_linewidth(2)

    # plt.show()

    fig_path = os.path.join(path, result_name+'_docking_weight1_5_3.png')
    plt.savefig(fig_path)



if __name__ == '__main__':

    base_dir = '/data/baiqing/PycharmProjects/Reinvent-master-3.2/my_script/picture'

    file = os.path.join(base_dir, 'linkinvent', 'BTK', 'training_log_sum_docking_weight1_5_3.csv')

    parser = argparse.ArgumentParser(description='Generate training log picture')
    parser.add_argument('-i', '--input', type=str, default=None, help='Specify the smooth absolute path')
    # parser.add_argument('-n', '--item_name', type=str, default=None, help='Specify the item name of Log')


    args = parser.parse_args(['-i', file])

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

    # item_list = ['Average_score']

    for item_name in item_list:
        print(item_name)
        plot_log(args.input, item_name)





