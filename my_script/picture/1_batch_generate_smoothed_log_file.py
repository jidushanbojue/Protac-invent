import os

if __name__ == '__main__':
    base_dir = '/data/baiqing/PycharmProjects/Reinvent-master-3.2/result/LINK_invent/BTK'

    generate_log_file_script = '/data/baiqing/PycharmProjects/Reinvent-master-3.2/my_script/picture/1_generate_smoothed_log_file.py'


    # idx_list = [9, 11, 13, 15]
    #
    # for idx in idx_list:
    #     # log_dir = os.path.join(base_dir, 'progress_docking_weight1_custom_sum_contain_oxygen_bond_distance_aromatic_linkinvent_7_' + str(idx) + '_3.log')
    #     log_dir = os.path.join(base_dir, 'progress_docking_weight1_custom_product_contain_oxygen_bond_distance_aromatic_linkinvent_no_constraint_3.log')
    #     cmd = 'python ' + generate_log_file_script + ' -e ' + log_dir + ' -o ' + log_dir + ' -f training_log.csv'
    #     os.system(cmd)



    idx_list = range(2, 6)
    for idx in idx_list:
        print(idx)

        log_dir = os.path.join(base_dir, 'progress_docking_weight' + str(idx) + '_custom_sum_contain_oxygen_bond_distance_aromatic_linkinvent_7_15_3.log')

        cmd = 'python ' + generate_log_file_script + ' -e ' + log_dir + ' -o ' + log_dir + ' -f training_log.csv'
        os.system(cmd)
    # print(log_dir)



    # idx_list = range(8, 16)
    #
    # for idx in idx_list:
    #     print(idx)
    #
    #
    #     # log_dir = os.path.join(base_dir, 'progress_docking_weight1_custom_product_contain_oxygen_bond_distance_aromatic_linkinvent_7_'+str(idx)+'.log')
    #     # log_dir = os.path.join(base_dir, 'progress_docking_weight1_custom_sum_contain_oxygen_bond_distance_aromatic_linkinvent_7_'+str(idx)+'.log')
    #
    #     # log_dir = os.path.join(base_dir, 'progress_docking_weight1_custom_product_contain_oxygen_bond_distance_aromatic_linkinvent_TL_protacDB_7_'+str(idx)+'.log')
    #     # log_dir = os.path.join(base_dir, 'progress_docking_weight1_custom_sum_contain_oxygen_bond_distance_aromatic_linkinvent_TL_protacDB_7_'+str(idx)+'.log')
    #
    #     # log_dir = os.path.join(base_dir, 'progress_docking_weight1_custom_sum_contain_oxygen_bond_distance_aromatic_piperidine_7_' + str(idx)+'_linkinvent_TL_piperidine.log')
    #     # log_dir = os.path.join(base_dir, 'progress_docking_weight1_custom_product_contain_oxygen_bond_distance_aromatic_piperidine_7_' + str(idx)+'_linkinvent_TL_piperidine.log')
    #
    #     # log_dir = os.path.join(base_dir, 'progress_docking_weight1_custom_product_contain_oxygen_bond_distance_aromatic_piperidine_7_'+str(idx)+'_true.log')
    #     log_dir = os.path.join(base_dir, 'progress_docking_weight1_custom_sum_contain_oxygen_bond_distance_aromatic_piperidine_7_'+str(idx)+'_true.log')
    #
    #
    #
    #     cmd = 'python ' + generate_log_file_script + ' -e ' + log_dir + ' -o ' + log_dir + ' -f training_log.csv'
    #     os.system(cmd)

    # idx_list = range(1, 6)
    #
    # for idx in idx_list:
    #     print(idx)
    #
    #     # log_dir = os.path.join(base_dir, 'progress_docking_weight' + str(idx) + '_custom_sum_contain_oxygen_bond_distance_aromatic_linkinvent_7_15.log')
    #
    #     # log_dir = os.path.join(base_dir, 'progress_docking_weight' + str(idx) + '_custom_sum_contain_oxygen_bond_distance_aromatic_linkinvent_TL_protacDB_7_15.log')
    #
    #     # log_dir = os.path.join(base_dir, 'progress_docking_weight' + str(idx) + '_custom_sum_contain_oxygen_bond_distance_aromatic_piperidine_7_15_linkinvent_TL_piperidine.log')
    #
    #     log_dir = os.path.join(base_dir, 'progress_docking_weight' + str(idx) + '_custom_sum_contain_oxygen_bond_distance_aromatic_piperidine_7_15_true.log')
    #
    #     cmd = 'python ' + generate_log_file_script + ' -e ' + log_dir + ' -o ' + log_dir + ' -f training_log.csv'
    #     os.system(cmd)
    #     # print(log_dir)








