# Purpose: Calculates the toy with the highest and lowest votes with inputs of toy name and votes
# Author:  Michael Lee
# Date: 25 January 2023

# Calculates most and least popular toys
def mostPopToyCalc(toyNames, toyVotes):
     totalVotes = sum(toyVotes)
     
     votesPopularToy = toyVotes.index(max(toyVotes))
     namePopularToy = toyNames[votesPopularToy]
     popularPercentage = toyVotes[votesPopularToy] / totalVotes * 100 

     votesLeastToy = toyVotes.index(min(toyVotes))
     nameLeastToy = toyNames[votesLeastToy]
     leastPercentage = toyVotes[votesLeastToy] / totalVotes * 100 
     return (totalVotes, votesPopularToy, namePopularToy, popularPercentage, votesLeastToy, nameLeastToy, leastPercentage)

# Lists of toy names and votes
print("Most popular toy of the year")
numToys = int(input("How many toys are in this year's list: "))

toyNames = []
for i in range(numToys): 
        inputToyNames = input("Enter the name of toy #{}: ".format(i+1))
        toyNames.append(inputToyNames)

toyVotes = []
for inputToyNames in toyNames:
        inputToyVotes = int(input("Enter total votes for {}: ".format(inputToyNames)))
        toyVotes.append(inputToyVotes)

totalVotes, votesPopularToy, namePopularToy, popularPercentage, votesLeastToy, nameLeastToy, leastPercentage = mostPopToyCalc(toyNames, toyVotes)    

# Output
print("Total votes received: {} votes." .format(sum(toyVotes)))
print("{} has been selected as the most popular toy with a total of {} votes." .format(namePopularToy, max(toyVotes)))
print("That is {:.2f}% of the votes." .format(popularPercentage))
print("{} received the least number of votes with a total of {} votes." .format(nameLeastToy, min(toyVotes)))
print("That is {:.2f}% of the votes." .format(leastPercentage))
