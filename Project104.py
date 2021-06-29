import plotly.figure_factory as px
import csv
import pandas as pd
import random
import statistics

df = pd.read_csv("class109.csv")
Hlist = df["Height(Inches)"].to_list()
Wlist = df["Weight(Pounds)"].to_list()


mean = sum(Hlist)/len(Hlist)
print ("mean", mean)

median = statistics.median(Hlist)
print("median", median)

mode = statistics.mode(Hlist)
print("mode", mode)

SD = statistics.stdev(Hlist)
print("standard deviation", SD)

#wegth
mean = sum(Wlist)/len(Wlist)
print ("mean", mean)

median = statistics.median(Wlist)
print("median", median)

mode = statistics.mode(Wlist)
print("mode", mode)

SD = statistics.stdev(Wlist)
print("standard deviation", SD)

# firstSD_start,firstSD_end = mean - SD , mean + SD
# print("{} % of data lies betw first SD", len(dice_result)*100/)

    