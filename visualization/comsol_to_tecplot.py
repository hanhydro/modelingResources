# -*- coding: utf-8 -*-
"""
Convert COMSOL dl.u and dl.v model output to TecPlot360-compatible format
Kyungdoe "Doe" Han (khan99@wisc.edu)
"""
import pandas as pd
import numpy as np

dlu_file = 'Your file path 1'
dlv_file = 'Your file path 1'
tecplot_filename = "flux_vector_tecplot.dat"

skip_lines = 0
with open(dlu_file, "r") as file:
    for line in file:
        if line.startswith(('%', 'velocity', 'X')):  # Identifying header lines
            skip_lines += 1
        else:
            break

dlu_df = pd.read_csv(dlu_file, skiprows=skip_lines, delim_whitespace=True, names=["X", "Y", "dl.u"])
dlv_df = pd.read_csv(dlv_file, skiprows=skip_lines, delim_whitespace=True, names=["X", "Y", "dl.v"])
merged_flux_df = pd.merge(dlu_df, dlv_df, on=["X", "Y"], how="inner").sort_values(["Y", "X"], kind='mergesort')

unique_x = np.sort(merged_flux_df["X"].unique())
unique_y = np.sort(merged_flux_df["Y"].unique())
num_x, num_y = len(unique_x), len(unique_y)

structured_data = pd.DataFrame([(x, y) for y in unique_y for x in unique_x], columns=["X", "Y"])
merged_flux_df = structured_data.merge(merged_flux_df, on=["X", "Y"], how="left").fillna(0)

with open(tecplot_filename, "w") as f:
    f.write('TITLE="Flux Vectors"\n')
    f.write('VARIABLES="X", "Y", "dl.u", "dl.v"\n')
    f.write(f'ZONE T="Time=7.5168E7", I={num_x}, J={num_y}, F=POINT\n')
    merged_flux_df.to_csv(f, sep=" ", index=False, header=False, mode='a', float_format="%.6e")

