# -*- coding: utf-8 -*-
"""
Convert COMSOL dl.u and dl.v model output to TecPlot360-compatible format
Kyungdoe "Doe" Han (khan99@wisc.edu)
"""
import pandas as pd
dlu_file = 'Your file path 1'
dlv_file = 'Your file path 2'

dlu_df = pd.read_csv(
    dlu_file, skiprows=6, delim_whitespace=True, names=["X", "Y", "dl.u"]
)
dlv_df = pd.read_csv(
    dlv_file, skiprows=6, delim_whitespace=True, names=["X", "Y", "dl.v"]
)

merged_flux_df = pd.merge(dlu_df, dlv_df, on=["X", "Y"], how="inner")
merged_flux_df = merged_flux_df.sort_values(by=["Y", "X"])

tecplot_filename = "flux_vector_tecplot.dat"
with open(tecplot_filename, "w") as f:
    f.write('TITLE = "Flux Vector Field"\n')
    f.write('VARIABLES = "X", "Y", "dl.u", "dl.v"\n')
    f.write(f'ZONE T="Timestep 20881", I={len(merged_flux_df["X"].unique())}, J={len(merged_flux_df["Y"].unique())}, F=POINT\n')
    for _, row in merged_flux_df.iterrows():
        f.write(f'{row["X"]} {row["Y"]} {row["dl.u"]} {row["dl.v"]}\n')
