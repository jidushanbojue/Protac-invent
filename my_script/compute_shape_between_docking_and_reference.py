from openeye import oechem, oeomega, oeshape, oequacpac
import pandas as pd
import os



def shape_scoring(ref_sdf, warheads_sdf):

    reffs = oechem.oemolistream(ref_sdf)
    fitfs = oechem.oemolistream(warheads_sdf)

    refmol = oechem.OEGraphMol()
    oechem.OEReadMolecule(reffs, refmol)

    prep = oeshape.OEOverlapPrep()
    prep.Prep(refmol)

    shapeFunc = oeshape.OEExactShapeFunc()
    shapeFunc.SetupRef(refmol)

    res = oeshape.OEOverlapResults()

    # shape_score_list = []
    for idx, fitmol in enumerate(fitfs.GetOEGraphMols()):
        if idx != 0:
            continue
        prep.Prep((fitmol))
        shapeFunc.Overlap(fitmol, res)

        shape_score = res.GetTanimoto()
        # shape_score_list.append(shape_score)
        print(shape_score)
        return shape_score



    # return shape_score_list

if __name__ == '__main__':
    reinvent_base_dir = '/data/baiqing/PycharmProjects/Reinvent-master-3.2'
    dockstream_base_dir = '/data/baiqing/PycharmProjects/DockStream-master'


    name_list = ['5T35',
                 '6BN7',
                 '6BOY',
                 '6HAY',
                 '6HR2',
                 '6W7O',
                 '6ZHC',
                 '7JTO',
                 '7JTP',
                 '7KHH',
                 '7Q2J',
                 'BRD9',
                 'BTK',
                 'BAF']

    # ref_sdf = os.path.join(reinvent_base_dir, 'data', 'protac', '5T35', '5t35_ligand.sdf')
    #
    # docking_sdf = os.path.join(dockstream_base_dir, 'result', '5T35', 'docked_result_docking_weight1_custom_product_scoring', 'e0000_ADV_ligands_docked.sdf')


    protac_invent_shape_score_list = []
    glide_shape_score_list = []
    vina_shape_score_list = []

    for name in name_list:
        ref_sdf = os.path.join(reinvent_base_dir, 'data', 'protac', name, name.lower()+'_ligand.sdf')

        protac_invent_docking_sdf = os.path.join(dockstream_base_dir, 'result', name, 'docked_result_docking_weight1_custom_product_scoring', 'e0000_ADV_ligands_docked.sdf')
        glide_docking_sdf = os.path.join(dockstream_base_dir, 'result', name, '0000_glide.sdf')
        vina_docking_sdf = os.path.join(dockstream_base_dir, 'result', name, '0000_ADV_out.sdf')

        protac_invent_shape_score = shape_scoring(ref_sdf, protac_invent_docking_sdf)
        protac_invent_shape_score_list.append(protac_invent_shape_score)

        glide_shape_score = shape_scoring(ref_sdf, glide_docking_sdf)
        glide_shape_score_list.append(glide_shape_score)

        vina_shape_score = shape_scoring(ref_sdf, vina_docking_sdf)
        vina_shape_score_list.append(vina_shape_score)




    df = pd.DataFrame()
    df['name'] = name_list
    df['Glide-SP'] = glide_shape_score_list
    df['Autodock-Vina'] = vina_shape_score_list
    df['Protac-INVENT'] = protac_invent_shape_score_list


    df.to_csv(reinvent_base_dir+'/result/three_docking_shape.csv')


