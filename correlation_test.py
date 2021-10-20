import matplotlib.pyplot as plot
import csv
import datetime
from dateutil import parser

fig=plot.figure(figsize=(12,6), facecolor='#DEDEDE')
ax=plot.subplot(121)
ax.set_facecolor('#DEDEDE')

accumulated_data_x=[]
accumulated_data_y=[]
var="update me"

with open("./eBay_ML_Challenge_Dataset_2021/train.tsv") as tsvfile:
    reader=csv.reader(tsvfile, delimiter="\t", quotechar='"')
    next(reader)
    try:
        for num, row in enumerate(reader):
            time1=parser.parse(row[3]).replace(tzinfo=None)
            time2=parser.parse(row[14]).replace(tzinfo=None)
            input()
            print(str(num)+"___"+str(time1)+"___"+str(time2))
            ship_time=(time2-time1).total_seconds()
            accumulated_data_x.append(row[4])
            accumulated_data_y.append(ship_time)
    except:
        pass
ax.cla()
ax.plot(accumulated_data_x,accumulated_data_y,'bo',label="shipment method")
#plot.draw()
plot.show()

