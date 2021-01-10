# DATA CULMINATING

# Install Needed Packages
!pip3 install gender
!pip3 install gender-guesser

# Python Libraries Used
import numpy as np
import pandas as pd
from gender import GenderDetector
import gender_guesser.detector as gender2

# Create Gender Detectors
gd = GenderDetector()
d = gender2.Detector()

# Test Detectors with Generic Names
names = ["Bob", "Anna", "John", "Smith", "Lucy", "David", "Mike", "Sally"]
genders1 = []
genders2 = []

for name in names:
    genders1.append(gd.gender(name))
    genders2.append(d.get_gender(name))

print(genders1)
print(genders2)

# Can conclude that both gender detectors are accurate
# Can conclude that gender detector from package "gender" is more consistant
# gd.gender() will be used

%%timeit -n 1 -r 1

# Add a SEX column in each of the excel sheets (2014-2018)
for i in range(2014,2019):
    file = pd.ExcelFile(f"SunshineList{i}.xlsx")
    data = pd.read_excel(file)
    data["SEX"] = data["First Name"].apply(lambda x: gd.gender(x))
    data.to_excel(f"ModifiedSunshineList{i}.xlsx")
    print(data.SEX.value_counts())
    print(f"Year: {i}'s excel file is completed! ")
print("")
print("DONE EVERYTHING! ")
print("")
