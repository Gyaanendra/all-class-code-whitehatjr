import csv
import statistics as st
import pandas as pd 

 
data = pd.read_csv("c109/height-weight.csv")
height = data["height"].to_list()
weight = data["weight"].to_list()

heightmean = st.mean(height)
weightmean = st.mean(weight)

heightmedian = st.median(height)
weightmedian = st.median(weight)

heightstd = st.stdev(height)
weightstd = st.stdev(weight)

# to find the three parts of stdev for height
heightsd1start, heightsd1end = heightmean -heightstd , heightmean +heightstd 
heightsd2start, heightsd2end = heightmean -(2 *heightstd) , heightmean +(2 *heightstd)
heightsd3start, heightsd3end = heightmean -(3 *heightstd) , heightmean +(3 *heightstd)

# to find the three parts of stdev for weight
weightsd1start, weightsd1end = weightmean -weightstd , weightmean +weightstd 
weightsd2start, weightsd2end = weightmean -(2 *weightstd) , weightmean +(2 *weightstd)
weightsd3start, weightsd3end = weightmean -(3 *weightstd) , weightmean +(3 *weightstd)

# to find the percentage of data with in stds for height
heightsd1 = [i for i in height if i>heightsd1start and i< heightsd1end]
heightsd2 = [i for i in height if i>heightsd2start and i< heightsd2end]
heightsd3 = [i for i in height if i>heightsd3start and i< heightsd3end]

# to find the percentage of data with in stds for weight
weightsd1 = [i for i in weight if i>weightsd1start and i< weightsd1end]
weightsd2 = [i for i in weight if i>weightsd2start and i< weightsd2end]
weightsd3 = [i for i in weight if i>weightsd3start and i< weightsd3end]

print("\033[1;31;40m Bright Red {}% of heightdata lies within sd1".format(len(heightsd1)*100.0/len(height)))
print("\033[1;32;40m Bright Green  {}% of heightdata lies within sd2".format(len(heightsd2)*100.0/len(height)))
print("\033[1;34;40m Bright Blue  {}% of heightdata lies within sd3".format(len(heightsd3)*100.0/len(height)))

print("\033[1;36;40m Bright Cyan  {}% of weightdata lies within sd1".format(len(weightsd1)*100.0/len(weight)))
print("\033[1;37;40m White  {}% of weightdata lies within sd2".format(len(weightsd2)*100.0/len(weight)))
print("\033[1;35;40m Bright Magenta {}% of weightdata lies within sd3".format(len(weightsd3)*100.0/len(weight)))