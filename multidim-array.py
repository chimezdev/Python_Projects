# # A device records the air temperature on an hourly basis and does it throughout the month. This gives you a total of 24 × 31 = 744 values.
# # the thermometer measures to 0.1C accuracy so we adopt a float.
# # Let each row of the matrix represent the hourly reading therefore will have 24 elements and we need 31 rows
# # To determine the monthly average noon temperature. Add up all 31 readings recorded at noon and divide the sum by 31. 
# # You can assume that the midnight temperature is stored first. Here's the relevant code:

# temps = [[0.0 for h in range(24)] for d in range(31)]
# #print(temps)

# # monthly average temperature at noon
# # count the days when the temp at noon was at least 20C
# total = 0.0
# count = 0
# for day in temps:
#     total += day[11]
#     if day[11] >= 20.0:
#         count += 1

# print("%d days were hot" % count)
# average = total / 31
# print("Average temp at noon:", average)

# # highest temperature during the whole months
# highest_temp = -100
# for day in temps:
#     for i in day:
#         if i >= highest_temp:
#             continue
#         else:
#             highest_temp = i
# print(" %d is the highest monthly temp recorded" % highest_temp)

# #Three-dimensional array
# # rooms = [[[False for r in range(20)] for f in range(15)] for t in range(3)]

try:
    value = input("Enter a value: ")
    print(value/value)
except ValueError:
    print("Bad input...")
except ZeroDivisionError:
    print("Very bad input...")
except TypeError:
    print("Very very bad input...")
except:
    print("Booo!")
