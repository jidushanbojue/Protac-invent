# PROTAC-invent
Source code for our paper "3D Based Generative PROTAC Linker Design with Reinforcement Learning".
The code was built based on Reinvent (https://github.com/MolecularAI/Reinvent), DockStream (https://github.com/MolecularAI/DockStream).
Thanks a lot for their sharing.


### **Figure 1. Illustration of PROTAC-invent model</center>**
![Figure1](https://github.com/jidushanbojue/Protac-invent/blob/master/my_script/picture/image/figure1.png "Figure1")

### **Figure 2. The general workflow of PROTAC-invent</center>**
![Figure1](https://github.com/jidushanbojue/Protac-invent/blob/master/my_script/picture/image/figure2.png "Figure2")

### **Figure 3. The workflow of generating and scoring 3D binding conformation of PROTAC</center>**
![Figure1](https://github.com/jidushanbojue/Protac-invent/blob/master/my_script/picture/image/figure3.png "Figure3")


## Quick start

Installation
-------------

1. Install [Conda](https://conda.io/projects/conda/en/latest/index.html)
2. Clone this Git repository
3. Open a shell, and go to the repository and create the Conda environment:
   
        $ conda env create -f reinvent.yml

4. Activate the environment:

        $ conda activate reinvent.v3.2

5. Install in-house reinvent_scoring

        $ cd reinvent_scoring

        $ pip install reinvent_scoring-0.0.73_bq-py3-none-any.whl

6. Open another shell, and clone in-house [DockStream](https://github.com/jidushanbojue/DockStream-master) repository

   This is the docking component special for Protac-invent.

        $ conda env create -f environment.yml



## Usage
1. Edit template Json file (for example in result/LINK_invent/BTK/template.json).

   Templates can be manually edited before using. The only thing that needs modification for a standard run are the file and folder paths. Most running modes produce logs that can be monitored by tensorboard
2. python input.py template.json

## Analyse the results

1. tensorboard --logdir "progress.log"

    progress.log is the "logging_path" in template.json

### We selected top200 solutions for some specific Ternary Complex, such as BTK(PDB code: 6W8I), BAF(PDB code: 6HAX), BRD4(PDB code: 5T35), the result as follow:

1. For BTK Ternary Complex:

   BTK_poses_top200.sdf: (https://github.com/jidushanbojue/Protac-invent/tree/master/result/LINK_invent/BTK/BTK_poses_top200.sdf)

   BTK_scored_smiles_top200.xlsx (https://github.com/jidushanbojue/Protac-invent/tree/master/result/LINK_invent/BTK/BTK_scored_smiles_top200.xlsx)

2. For BAF Ternary Complex

   BAF_poses_top200.sdf: (https://github.com/jidushanbojue/Protac-invent/tree/master/result/LINK_invent/BAF/BAF_poses_top200.sdf)

   BAF_scored_smiles_top200.xlsx (https://github.com/jidushanbojue/Protac-invent/tree/master/result/LINK_invent/BAF/BAF_scored_smiles_top200.xlsx)

3. For BRD4 Ternary Complex

   BRD4_poses_top200.sdf: (https://github.com/jidushanbojue/Protac-invent/tree/master/result/LINK_invent/BRD4/BRD4_poses_top200.sdf)

   BTK_scored_smiles_top200.xlsx (https://github.com/jidushanbojue/Protac-invent/tree/master/result/LINK_invent/BRD4/BRD4_scored_smiles_top200.xlsx)

### We manually selected 25 solutions for BTK, perform MD simulation and MM-GBSA calculation, the result as follow

   26_PROTAC_MM-GBSA_value.xlsx (https://github.com/jidushanbojue/Protac-invent/tree/master/result/LINK_invent/BTK/26_PROTAC_MM-GBSA_value.xlsx)


