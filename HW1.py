# Part. 1

#=======================================

# Import module

#  csv -- fileIO operation

import csv

#=======================================


# Part. 2

#=======================================

# Read cwb weather data

cwb_filename = '107060009.csv'

data = []

header = []

with open(cwb_filename) as csvfile:

   mycsv = csv.DictReader(csvfile)

   header = mycsv.fieldnames

   for row in mycsv:

      data.append(row)

answer = []

#--------------------------------------------------------------------------------- 1
target_data = list(filter(lambda item: item['station_id'] == 'C0A880', data))

length = len(target_data)

max = float(target_data[0]['TEMP'])

for i in range(length):
   
   if (float(target_data[i]['TEMP'])>max):
      max = float(target_data[i]['TEMP'])
   else:
      max = max

if((max == -99) or (max == -999)):
   max = 'None'

answer.append(['C0A880',max])

#--------------------------------------------------------------------------------- 1

#--------------------------------------------------------------------------------- 2
target_data = list(filter(lambda item: item['station_id'] == 'C0F9A0', data))

length = len(target_data)

max = float(target_data[0]['TEMP'])

for i in range(length):
   
   if (float(target_data[i]['TEMP'])>max):
      max = float(target_data[i]['TEMP'])
   else:
      max = max

if((max == -99) or (max == -999)):
   max = 'None'

answer.append(['C0F9A0',max])

#--------------------------------------------------------------------------------- 2



#--------------------------------------------------------------------------------- 3
target_data = list(filter(lambda item: item['station_id'] == 'C0G640', data))

length = len(target_data)

max = float(target_data[0]['TEMP'])

for i in range(length):
   
   if (float(target_data[i]['TEMP'])>max):
      max = float(target_data[i]['TEMP'])
   else:
      max = max

if((max == -99) or (max == -999)):
   max = 'None'

answer.append(['C0G640',max])

#--------------------------------------------------------------------------------- 3



#--------------------------------------------------------------------------------- 4
target_data = list(filter(lambda item: item['station_id'] == 'C0R190', data))

length = len(target_data)

max = float(target_data[0]['TEMP'])

for i in range(length):
   
   if (float(target_data[i]['TEMP'])>max):
      max = float(target_data[i]['TEMP'])
   else:
      max = max

if((max == -99) or (max == -999)):
   max = 'None'


answer.append(['C0R190',max])


#--------------------------------------------------------------------------------- 4



#--------------------------------------------------------------------------------- 5
target_data = list(filter(lambda item: item['station_id'] == 'C0X260', data))

length = len(target_data)

max = float(target_data[0]['TEMP'])

for i in range(length):
   
   if (float(target_data[i]['TEMP'])>max):
      max = float(target_data[i]['TEMP'])
   else:
      max = max

if((max == -99) or (max == -999)):
   max = 'None'


answer.append(['C0X260',max])
print(answer)

#--------------------------------------------------------------------------------- 5