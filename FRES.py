TEXT1 = ["The politician who holds the authority of all EU countries has just completely condemned a chunk of the British cabinet wondering aloud",
"What that special place in hell looks like for those who promoted Brexit without even a sketch of a plan how to carry it out safely",
"Sure for a long time the EU has been frustrated with how the UK has approached all of this",
"And sure plenty of voters in the UK are annoyed too at how politicians have been handling these negotiations",
"But it is quite something for Donald Tusk to have gone in like this studs up even though he sometimes reminisces about his time as a football hooligan in his youth"]

TEXT2 = ["An outbreak of the flu in Alabama has closed an elementary and middle school with school officials struggling to find enough healthy teachers to teach",
"The schools will be closed for the rest of the week because of the number of cases of flu among students and employees",
"Lawrence County Schools Superintendent Jon Bret Smith told news outlets that Moulton Elementary School and Moulton Middle School are closed Wednesday through Friday"]

# Code for TEXT1
# Length of TEXT1
text_one_sentences = len(TEXT1)
# Declaring array to store splitted words from TEXT1
text_one_words_arr = []

# Looping over every sentence in TEXT1
for sentence in TEXT1:  # Looping every word in each sentence, splitted at space.
    for words in sentence.split(" "):  # Appends each word to the new array "text_one_words_arr" in lower-case
        text_one_words_arr.append(words)  # Stores the length of "text_one_words_arr" and prints it
word_count_text_one = len(text_one_words_arr)


# Code for TEXT2
# Length of  TEXT2
text_two_sentences = len(TEXT2)
text_two_words_arr = []  # New array to store words of TEXT2


for sentence in TEXT2:  # Same as for TEXT1. Loops over every sentence -
    for words in sentence.split(" "):  # - and then every word and stores it in the array above
        text_two_words_arr.append(words)
word_count_text_Two = len(text_two_words_arr)


# Takes in a word as param.
# @PARAM: the word
def count_vowels(word):
    count = 0
    vowels = "AEIOUaeiou"  # Variable vowels is only in lower-case because the words are stored in array in lower-case
    for letter in word:  # Loops each letter in the word
        if letter in vowels:   # checks if the letter is in the variable vowels
            count += 1  # Counts the vowels 
    return count  # Returns the vowel count


# Takes in a list of words and returns the total amount of vowels in the list.
# @PARAM: List of words
def count_vowels_list(word_list):
    total_vowels = 0   # Counter for vowels
    vowel_list = []  # An empty array to store vowels
    for word in word_list:  # Loops over every word in the list
        word = count_vowels(word)  # Calls the count_vowels() method for each word
        vowel_list.append(word)  # Appends each vowel to the list
    for num in vowel_list:  # Loops over each vowel number in the list
        total_vowels += num  # Adds the numbers
    return total_vowels  # Returns the numbers


# Stores the sum of vowels for the lists
vowels_list_one = count_vowels_list(text_one_words_arr)
vowels_list_two = count_vowels_list(text_two_words_arr)


# Calculates the FRES-score.
# @PARAM: wordcount: sum of words. sentence: sum of sentences. vowels_list: sum of vowels for each TEXT
def fres(word_count, sentences, vowels_list):
    val1 = 206.835  # Stores each constant value as a variable.
    val2 = 1.015
    val3 = 84.6
    # Uses the fresch Reading Ease formula to calculate the fres score
    result = val1 - val2 * word_count/sentences - val3 * vowels_list/word_count
    return result   # Returns the result


print("No sentences in TEXT1: " + str(text_one_sentences))  # Prints 5
print("No sentences in TEXT2: " + str(text_two_sentences))  # Prints 3
print("Word count for TEXT1: " + str(word_count_text_one))  # Prints 117
print("Word count for TEXT2: " + str(word_count_text_Two))  # Prints 71
print("TEXT1 syllables: " + str(count_vowels_list(text_one_words_arr)))  # Prints 206 vowels
print("TEXT2 syllables: " + str(count_vowels_list(text_two_words_arr)))  # Prints 133 vowels
# Prints the fres-score 34.1301 for TEXT1
print("FRES-score for TEXT1: " + str(fres(word_count_text_one, text_one_sentences, vowels_list_one)))
# Print the fres-score 24.3372 for TEXT2
print("FRES-score for TEXT2: " + str(fres(word_count_text_Two, text_two_sentences, vowels_list_two)))
