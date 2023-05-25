import os
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import argparse


def plot_log(training_log_file, item_name):
    df = pd.read_csv(training_log_file)
    df.rename(columns={'step': 'Step'}, inplace=True)

    df = df[df.index % 2 == 0]

    # sns.set_palette('Blues_d')

    plt.rcParams['font.size'] = 15
    plt.rcParams['axes.unicode_minus'] = False


    path, name = os.path.split(training_log_file)

    if 'sum' in name:
        result_name = item_name+'_custom_sum'
    else:
        result_name = item_name+'_custom_product'



    fig = plt.figure(dpi=300, figsize=(20, 15))

    # palette = sns.xkcd_palette(["dusty purple", "red", "black", "cyan"])

    palette = sns.xkcd_palette(["windows blue", "amber", "greyish", "faded green"])

    # sns.relplot(x='Step', y=item_name, data=df, hue='model', kind='line', linewidth=2.0, palette=palette)
    # sns.relplot(x='Step', y=item_name, data=df, hue='model', kind='scatter', linewidth=2.2, palette=palette)
    sns.lineplot(x='Step', y=item_name, data=df, hue='model', linewidth=3.0, palette=palette, markers=True)

    plt.xlabel('Step', fontsize=30)
    plt.ylabel(item_name, fontsize=30)

    fig_path = os.path.join(path, result_name+'.png')
    plt.savefig(fig_path)


    # plt.show()




if __name__ == '__main__':

    base_dir = '/data/baiqing/PycharmProjects/Reinvent-master-3.2/my_script/picture'

    file = os.path.join(base_dir, 'four_model_compare', 'four_model_7_15_sum.csv')

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

    for item_name in item_list:
        plot_log(args.input, item_name)





