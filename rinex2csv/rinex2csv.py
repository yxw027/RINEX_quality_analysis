##############################################################################
# This script transform the RINEX file 3.03 into a pandas dataframe and save  
# it as csv
# 
# The script is tested with Geo++ and RINEX ON produced by Xiaomi Mi8
##############################################################################

from readObs import readObs

(df_1, head_1) = readObs("data/RINEXON.20o")
df_1.to_csv("data/RINEXON.csv")

file = open("data/RINEXON_header.txt","w")
file.write(head_1)
file.close()