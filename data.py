import pandas as pd
import plotly.figure_factory as ff
import statistics
import plotly.graph_objects as go

df=pd.read_csv("sp.csv")
list=df["reading score"].tolist()

mean=statistics.mean(list)
median=statistics.median(list)
mode=statistics.mode(list)
std_dev=statistics.stdev(list)
first_stdev_start,first_stdev_end=mean-std_dev,mean+std_dev
second_stdev_start,second_stdev_end=mean-(2*std_dev),mean+(2*std_dev)
third_stdev_start,third_stdev_end=mean-(3*std_dev),mean+(3*std_dev)
list_of_data_onestdev=[result for result in list if result>first_stdev_start and result<first_stdev_end]
list_of_data_secondstdev=[result for result in list if result>second_stdev_start and result<second_stdev_end]
list_of_data_thirdstdev=[result for result in list if result>third_stdev_start and result<third_stdev_end]

print("Mean ,Median and Mode of reading score is {} , {} and {} respectively".format(mean,median,mode))
print("Std_Dev of reading score is ",str(std_dev))
print("{}% of data lies with in one StdDev".format(len(list_of_data_onestdev)*100.0/len(list)))
print("{}% of data lies with in second StdDev".format(len(list_of_data_secondstdev)*100.0/len(list)))
print("{}% of data lies with in second StdDev".format(len(list_of_data_thirdstdev)*100.0/len(list)))

fig= ff.create_distplot([list], ["Reading Scores"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean], y=[0,0.17], mode="lines", name="Mean"))
fig.add_trace(go.Scatter(x=[first_stdev_start,first_stdev_start], y=[0,0.17], mode="lines", name="Standard Deviation 1"))
fig.add_trace(go.Scatter(x=[first_stdev_end,first_stdev_end], y=[0,0.17], mode="lines", name="Standard Deviation 1"))
fig.add_trace(go.Scatter(x=[second_stdev_start,second_stdev_start], y=[0,0.17], mode="lines", name="Standard Deviation 2"))
fig.add_trace(go.Scatter(x=[second_stdev_end,second_stdev_end], y=[0,0.17], mode="lines", name="Standard Deviation 2"))
fig.show()