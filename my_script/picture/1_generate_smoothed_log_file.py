import matplotlib.pyplot as plt
import os

from tensorboard.backend.event_processing import event_accumulator
import pandas as pd
import seaborn as sns
import argparse


"""
This scripts process the training origin event data, extract every score-components data and  smooth it (user can change the smooth weight, default: 0.75)
"""


def generate_log_table(event_path, result_folder, result_name):
    ea = event_accumulator.EventAccumulator(event_path)
    ea.Reload()

    k = ea.scalars.Keys()
    print(k)


    result_df = pd.DataFrame()
    for item_name in k:
        # item_name = '_'.join(item.split(' '))
        item = ea.scalars.Items(item_name)
        # result_list.append(item)
        temp_df = pd.DataFrame(item)
        temp_df.rename(columns={'value': '_'.join(item_name.split(' '))}, inplace=True)
        result_df = pd.concat([result_df, temp_df], axis=1)

    result_df = result_df.loc[:, ~result_df.columns.duplicated()]
    del result_df['wall_time']

    result_file = os.path.join(result_folder, result_name)
    result_df.to_csv(result_file)

def plot_log(result_file):
    fig = plt.figure()
    df = pd.read_csv(result_file)
    sns.tsplot(time=df['step'], data=df['ADV'], color='r', condition='ADV')
    plt.show()

def smooth(file_path, file_name, weight=0.75):

    # file_path, file_name = os.path.split(read_path)
    read_path = os.path.join(file_path, file_name)
    save_path = os.path.join(file_path, 'smooth_'+file_name)

    data = pd.read_csv(read_path)

    result_dict = {}
    result_dict['step'] = data['step']
    for column in data.columns:

        if column != 'step' and column != 'Unnamed: 0':
            print(column)
            scalar = data[column].values
            last = scalar[0]
            smoothed = []
            for point in scalar:
                smoothed_val = last * weight + (1 - weight) * point
                smoothed.append(smoothed_val)
                last = smoothed_val
            result_dict[column] = smoothed
    save = pd.DataFrame(result_dict)
    save.to_csv(save_path)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate training log result and smoothed result')
    parser.add_argument('-e', '--event', type=str, default=None, help='Specify the event absolute path')
    parser.add_argument('-o', '--out', type=str, default=None, help='Specify the result log dir')
    parser.add_argument('-f', '--file', type=str, help='Specify the filename for the output_file')

    # args = parser.parse_args(['-e', '/data/baiqing/PycharmProjects/Reinvent-master-3.2/result/LINK_invent/BTK/progress_docking_weight1_custom_product_contain_oxygen_bond_distance_aromatic_linkinvent_7_8.log/events.out.tfevents.1676630338.localhost.localdomain.211554.0',
    #                           '-o', '/data/baiqing/PycharmProjects/Reinvent-master-3.2/result/LINK_invent/BTK/progress_docking_weight1_custom_product_contain_oxygen_bond_distance_aromatic_linkinvent_7_8.log',
    #                           '-f', 'training_log.csv'])

    # args = parser.parse_args(['-e', '/data/baiqing/PycharmProjects/Reinvent-master-3.2/result/LINK_invent/BTK/progress_docking_weight1_custom_product_contain_oxygen_bond_distance_aromatic_linkinvent_7_9.log',
    #                           '-o', '/data/baiqing/PycharmProjects/Reinvent-master-3.2/result/LINK_invent/BTK/progress_docking_weight1_custom_product_contain_oxygen_bond_distance_aromatic_linkinvent_7_9.log',
    #                           '-f', 'training_log.csv'])

    # args = parser.parse_args(['-e', '/data/baiqing/PycharmProjects/Reinvent-master-3.2/result/LINK_invent/BTK/progress_docking_weight1_custom_sum_contain_oxygen_bond_distance_aromatic_linkinvent_none_bond_distance.log',
    #                           '-o', '/data/baiqing/PycharmProjects/Reinvent-master-3.2/result/LINK_invent/BTK/progress_docking_weight1_custom_sum_contain_oxygen_bond_distance_aromatic_linkinvent_none_bond_distance.log',
    #                           '-f', 'training_log.csv'])

    args = parser.parse_args()


    if os.path.exists(args.out):
        pass
    else:
        os.mkdir(args.out)




    # base_dir = '/data/baiqing/PycharmProjects/Reinvent-master-3.2/result/LINK_invent/BRD9'
    # progress_path = os.path.join(base_dir, 'progress_1.log')
    # event_path = os.path.join(progress_path, 'events.out.tfevents.1669688752.localhost.localdomain.261196.0')
    #
    # result_file = os.path.join(base_dir, 'picture_log', 'custom_product_docking_weight1.csv')
    # generate_log_table(event_path, result_file)
    # smooth(result_file)

    generate_log_table(args.event, args.out, args.file)
    smooth(args.out, args.file)

    # smooth()






