# Converting COMSOL Flux Output to TecPlot360-Compatible Format
This Python script converts model output files containing horizontal (`dl.u`) and vertical (`dl.v`) flux data into a TecPlot360-compatible format for visualization.
## Workflow

| **Step**                | **Description** |
|-------------------------|----------------|
| **Loading Data Files**  | Reads `dl.u` (horizontal flux) and `dl.v` (vertical flux) from separate text files. <br> Skips header lines that contain metadata (e.g., comments, labels). |
| **Processing & Restructuring** | Merges the two datasets based on common `X` and `Y` coordinates. <br> Sorts data for structured grid arrangement (by `Y` first, then `X`). <br> Ensures a complete structured grid by filling missing values with zeros. |
| **Preparation**         | Extracts unique `X` and `Y` values to determine grid dimensions (`I, J`). <br> Formats the data in **TecPlot360's POINT format**, which explicitly lists values for each grid point. |
| **Output**             | Outputs structured flux data in **TecPlot format** with a header specifying the **title, variables, zone info, and time**. <br> Saves numerical values in **scientific notation** (`%.6e`) for precision. |

---

