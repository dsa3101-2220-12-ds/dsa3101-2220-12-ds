# File contents:
1. <b>Data Table/</b> : This folder contains the final graph analytics csv file from Gephi for both schools.
2. <b>gephi_formatting.ipynb</b> : Python script that transforms a pandas DataFrame into two CSV files in Gephi format, which can be used for network analysis and visualization. The main function in this script is transform_to_gephi_format(df), which takes a DataFrame as input and returns two DataFrames, one for nodes and one for edges. The script then exports the nodes and edges DataFrames to nodes and edges CSV files to be used in Gephi
3. <b> NTU/</b> : This folder contains the relevant files for the NTU pre-requisite graph. <br>
This includes:
a. The .gephi file for the interactive final NTU pre-requisite graph<br>
b. The .png file which shows the static graph. <br>
c. ntu_edges.csv the edges file generated from gephi_formatting.ipynb<br>
d. ntu_nodes.csv the nodes file generated from gephi_formatting.ipynb
4. <b> NUS/</b> : This folder contains the relevant files for the NUS pre-requisite graph.<br> 
This includes:<br>
a. The .gephi file for the interactive final NUS pre-requisite graph <br>
b. The .png file which shows the static graph. <br>
c. nus_edges.csv the edges file generated from gephi_formatting.ipynb <br>
d. nus_nodes.csv the nodes file generated from gephi_formatting.ipynb <br>


