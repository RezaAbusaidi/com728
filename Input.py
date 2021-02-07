
#Daily mood calculator by Reza Abusaidi

get_name = input("Please enter your name ")



yourmode_Score = ("Your moood score is: ")

#User enters how many hours slept
sleepdata_hr = input("please enter time slept last night ")

#heart rate is fecthed through data_feed
heart_rate = 73

#Program calculates data based on heart rate at that moment / Time slept
getmood = (heart_rate/int(sleepdata_hr))



print(f"hello {get_name} {yourmode_Score} ", getmood)

