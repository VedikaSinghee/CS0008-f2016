#ask the user which system they use 
system = raw_input('What system would you like to use? (USC/Metric): ')

isUSC = False
isMetric = False
distanceUnit = ''
gasolineUnit = ''

#convert according to both the systems 
if (system == 'USC'):
    isUSC = True
    distanceUnit = 'miles'
    gasolineUnit = 'gallons'
elif (system == 'Metric'):
    isMetric = True
    distanceUnit = 'kilometers'
    gasolineUnit = 'liters'

#ask question in the particular system 
distance = input('How many ' + distanceUnit + ' did you drive? : ')
gasoline = input('How many ' + gasolineUnit + ' of gasoline did you use? : ')

#making sure all values are equal to 0, so it is easy to convert
distanceUSC = 0.0
gasolineUSC = 0.0
distanceMetric = 0.0
gasolineMetric = 0.0

#coverting to the other system given the formula provided
if (isUSC):
    distanceUSC = distance
    gasolineUSC = gasoline
    distanceMetric = distanceUSC * 1.60934
    gasolineMetric = gasolineUSC * 3.78541
elif (isMetric):
    distanceMetric = distance
    gasolineMetric = gasoline
    distanceUSC = distanceMetric * 0.621371
    gasolineUSC = gasolineMetric * 0.264172 

#calculating the consumption rate
consumptionUSC = distanceUSC / gasolineUSC
consumptionMetric = (gasolineMetric * 100) / distanceMetric

#checking if the consumption rate is good or not according to the metric system
consumptionCategory = ''

if (consumptionMetric <= 8):
    consumptionCategory = 'Excellent'
elif (consumptionMetric > 8 and consumptionMetric <= 10):
    consumptionCategory = 'Good'
elif (consumptionMetric > 10 and consumptionMetric <= 15):
    consumptionCategory = 'Average'
elif (consumptionMetric > 15 and consumptionMetric <= 20):
    consumptionCategory = 'Poor'
elif (consumptionMetric > 20):
    consumptionCategory = 'Extremely Poor'

#printing according to the format given
print ''
print '{:31} {:18} {}'.format('', 'USC', 'Metric')
print 'Distance ______________:', '{:10.3f} {:10} {:10.3f} {}'.format(distanceUSC, 'miles', distanceMetric, 'Km')
print 'Gas ___________________:', '{:10.3f} {:10} {:10.3f} {}'.format(gasolineUSC, 'gallons', gasolineMetric, 'Liters')
print 'Consumption ___________:', '{:10.3f} {:10} {:10.3f} {}'.format(consumptionUSC, 'mpg', consumptionMetric, 'l/100Km');
print ''
print 'Gas Consumption Rating : ', consumptionCategory
