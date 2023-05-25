# import matplotlib.pyplot as plt
# import numpy as np
# import seaborn as sns
#
# def getdata():
#     basecond = [[18, 20, 19, 18, 13, 4, 1],
#                 [20, 17, 12, 9, 3, 0, 0],
#                 [20, 20, 20, 12, 5, 3, 0]]
#
#     cond1 = [[18, 19, 18, 19, 20, 15, 14],
#              [19, 20, 18, 16, 20, 15, 9],
#              [19, 20, 20, 20, 17, 10, 0],
#              [20, 20, 20, 20, 7, 9, 1]]
#
#     cond2 = [[20, 20, 20, 20, 19, 17, 4],
#              [20, 20, 20, 20, 20, 19, 7],
#              [19, 20, 20, 19, 19, 15, 2]]
#
#     cond3 = [[20, 20, 20, 20, 19, 17, 12],
#              [18, 20, 19, 18, 13, 4, 1],
#              [20, 19, 18, 17, 13, 2, 0],
#              [19, 18, 20, 20, 15, 6, 0]]
#
#     return basecond, cond1, cond2, cond3
#
# data = getdata()
# fig = plt.figure()
# xdata = np.array([0, 1, 2, 3, 4, 5, 6])/5
# linestyle = ['-', '--', ':', '-.']
# color = ['r', 'g', 'b', 'k']
# label = ['algo1', 'algo2', 'algo3', 'algo4']
#
# for i in range(4):
#     # sns.plot
#     sns.tsplot(time=xdata, data=data[i], color=color[i], linestyle=linestyle[i], condition=label[i])
#
# plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

plt.style.use('ggplot')
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


def smooth(read_path, save_path, weight=0.75):

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
    base_dir = '/data/baiqing/PycharmProjects/Reinvent-master-3.2/result/LINK_invent/BRD9/'
    read_path = os.path.join(base_dir, 'custom_product_docking_weight1.csv')
    save_path = os.path.join(base_dir, 'smooth_custom_product_docking_weight1.csv')
    smooth(read_path, save_path, weight=0.75)

# smooth()




