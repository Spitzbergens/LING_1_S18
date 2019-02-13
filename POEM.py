# This line imports the square root function
# Use it with sqrt()
# Example: square root of 9 is:  sqrt(9)
from math import sqrt


# N-Grams
unigrams = ['i', 'have', 'been', 'one', 'acquainted', 'with', 'the', 'night', 'i', 'have', 'walked', 'out', 'in', 'rain', 'and', 'back', 'in', 'rain', 'i', 'have', 'outwalked', 'the', 'furthest', 'city', 'light', 'i', 'have', 'looked', 'down', 'the', 'saddest', 'city', 'lane', 'i', 'have', 'passed', 'by', 'the', 'watchman', 'on', 'his', 'beat', 'and', 'dropped', 'my', 'eyes', 'unwilling', 'to', 'explain', 'i', 'have', 'stood', 'still', 'and', 'stopped', 'the', 'sound', 'of', 'feet', 'when', 'far', 'away', 'an', 'interrupted', 'cry', 'came', 'over', 'houses', 'from', 'another', 'street', 'but', 'not', 'to', 'call', 'me', 'back', 'or', 'say', 'good-bye', 'and', 'further', 'still', 'at', 'an', 'unearthly', 'height', 'one', 'luminary', 'clock', 'against', 'the', 'sky', 'proclaimed', 'the', 'time', 'was', 'neither', 'wrong', 'nor', 'right', 'i', 'have', 'been', 'one', 'acquainted', 'with', 'the', 'night']
bigrams = ['i have', 'have been', 'been one', 'one acquainted', 'acquainted with', 'with the', 'the night', 'night i', 'i have', 'have walked', 'walked out', 'out in', 'in rain', 'rain and', 'and back', 'back in', 'in rain', 'rain i', 'i have', 'have outwalked', 'outwalked the', 'the furthest', 'furthest city', 'city light', 'light i', 'i have', 'have looked', 'looked down', 'down the', 'the saddest', 'saddest city', 'city lane', 'lane i', 'i have', 'have passed', 'passed by', 'by the', 'the watchman', 'watchman on', 'on his', 'his beat', 'beat and', 'and dropped', 'dropped my', 'my eyes', 'eyes unwilling', 'unwilling to', 'to explain', 'explain i', 'i have', 'have stood', 'stood still', 'still and', 'and stopped', 'stopped the', 'the sound', 'sound of', 'of feet', 'feet when', 'when far', 'far away', 'away an', 'an interrupted', 'interrupted cry', 'cry came', 'came over', 'over houses', 'houses from', 'from another', 'another street', 'street but', 'but not', 'not to', 'to call', 'call me', 'me back', 'back or', 'or say', 'say good', 'good bye', 'bye and', 'and further', 'further still', 'still at', 'at an', 'an unearthly', 'unearthly height', 'height one', 'one luminary', 'luminary clock', 'clock against', 'against the', 'the sky', 'sky proclaimed', 'proclaimed the', 'the time', 'time was', 'was neither', 'neither wrong', 'wrong nor', 'nor right', 'right i', 'i have', 'have been', 'been one', 'one acquainted', 'acquainted with', 'with the', 'the night']

token_1 = "have"
token_2 = "been"

# Length of  token_1
f1 = unigrams.count(token_1)
# Length of token_2
f2 = unigrams.count(token_2)
# Length of corpus
Nc = len(unigrams)

# Expected frequency
Fe = (float(f1) / float(Nc)) * float(f2)
# Observed Bigram frequency
F = bigrams.count(token_1 + " " + token_2)
# t-score
tScore = (F - Fe) / sqrt(F)

print("The t-score of the bigram 'have been': " + str(tScore))

print("f1: " + str(f1))
print("f2: " + str(f2))
print("Nc: " + str(Nc))
print("Fe: " + str(Fe))
print ("F: " + str(F))
print("t-score: " + str(tScore))
