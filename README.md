[![CC BY 4.0][cc-by-shield]][cc-by]

# Electronic Notebook: Thermodynamics of Urea's Effects on the Solubility of Polyethylene Glycol 

This is supporting information for the scientific manuscript by _Hervø-Hansen et al._ (_Journal_, 2024, doi: [xx.xxxxxx/xxxxxxxxxx](https://hervoe.dk)) on the solvation free energy of PEG in urea solutions using the energy-representation theory of solvation in combination with all-atom simulations. All figures within the analysis are publication ready and can be reproduced by running the provided Jupyter notebooks (`.ipynb`). 

### Layout
- `PDB_files` PDB files for various chemical species utilized.
- `Simulations` Directory containing raw ermod results and processed results. The directory is also used for location of trajectories and corresponding analysis upon reproduction.
- `Force_fields` Directory containing force parameters files (in OpenMM format) for the various chemical species utilized.
- `Figures` Directory containing publication ready figures and images imported in the Juypter notebooks.
- `Data` Directory containing pre-processed data.
- `Simulations.ipynb` Jupyter notebook for running molecular dynamics simulations using OpenMM.
- `Analysis.ipynb` Jupyter notebook for analysis of simulations and free energy computations and production of publication ready figures.
- `ERmod.ipynb` Jupyter notebook for running free energy calculations using energy-representation theory.
- `environment.yml` Conda environment file to recreate the simulation environment. The environment most importantly contains Numpy, Scipy, OpenMM, parmed, mdtraj, and Packmol.

### Usage
To open the notebook, install Python via [Miniconda](https://conda.io/miniconda.html) and make sure all required packages are loaded by issuing the following terminal commands
```bash
   conda env create -f environment.yml
   conda activate PEO
   jupyter-notebook
```

### License
This work is licensed under a
[Creative Commons Attribution 4.0 International License][cc-by].

[![CC BY 4.0][cc-by-image]][cc-by]

[cc-by]: http://creativecommons.org/licenses/by/4.0/
[cc-by-image]: https://i.creativecommons.org/l/by/4.0/88x31.png
[cc-by-shield]: https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg
