
letter_to_adjacent_letters_dict = {'a': 'qwsxz', 'b': 'vghn', 'c': 'xdfv', 'd': 'sfrexc', 'e': 'wsdfr', 'f': 'drtgcv', 'g': 'bvftyh', 'h': 'gyujnb', 'i': 'ujklo', 'j': 'nhuikm', 'k': ',mjiol', 'l': 'kop;.,', 'm': 'njk,', 'n': 'mjhb', 'o': 'ikl;p', 'p': "ol;'[", 'q': 'wsa', 'r': 'edfgt', 's': 'awedxz', 't': 'ryhfg', 'u': 'yhjki', 'v': 'cbfg', 'w': 'qasde', 'x': 'zsdc', 'y': 'tghju', 'z': 'asx'}
common_mistype_letters_dict = {'a': 'sqw', 'b': 'vnfc', 'c': 'vfbx', 'd': 'sfe', 'e': 'rdw', 'f': 'gd', 'g': 'hfj', 'h': 'gjy', 'i': 'ouk', 'j': 'hk', 'k': 'lji', 'l': 'k;', 'm': 'n,j', 'n': 'mjb', 'o': 'ipl', 'p': ';[o', 'q': 'wa', 'r': 'tfe', 's': 'ad', 't': 'rfy', 'u': 'yj', 'v': 'bcf', 'w': 'sqe', 'x': 'zsc', 'y': 'ujt', 'z': 'xa'}

#dictionary_file = 'dictionary_spell_check_algorithm.txt'
#dictionary_file = '10000_word_dict.txt'
#dictionary_file = '58110_word_dict.txt'
dictionary_file = '178385_word_dict.txt'

# reads dictionary into list ("words_dictionary_list")
with open(dictionary_file) as file:
	words_dictionary_list = [line.rstrip() for line in file]


"""-----------------------------------------------------------------------------------------------------------------------------------"""


"""
def autosize_user_input(_word, user_input_word, word_to_matched_letters_positions_dict, word_to_unmatched_positions_dict):
	# when user entry is the same length as _word
	if len(_word) == len(user_input_word):
		...
	elif len(_word) > len(user_input_word):
		...
	elif len(_word) < len(user_input_word):
		...
"""

def get_word_to_anylocation_matching_letters_dict(user_input_word, words_dictionary_list):
	word_to_anylocation_matching_letters_dict = {}
	# iterate list of all words
	for _word in words_dictionary_list:
		number_of_matching_letters = 0
		# checks how many letters match for that _word
		for c in _word:
			if c in user_input_word:
				number_of_matching_letters+=1
		# appends number of matching letters to word_to_anylocation_matching_letters_dict with _word as key
		word_to_anylocation_matching_letters_dict[_word] = number_of_matching_letters

	return word_to_anylocation_matching_letters_dict
	# END

def get_word_to_exactlocation_matching_letters_dict(user_input_word, words_dictionary_list):
	word_to_exactlocation_matching_letters_dict = {}
	# iterate list of all words
	for _word in words_dictionary_list:
		number_of_matching_letters = 0
		# iterates through each letter in word
		for c in _word:
			# condition to prevent out of range error
			if _word.index(c) < len(user_input_word):
				# checks if at that "position" the letters of "_word" and "user_input_word" match
				if c == user_input_word[_word.index(c)] :
					number_of_matching_letters += 1
		# 
		word_to_exactlocation_matching_letters_dict[_word] = number_of_matching_letters
	
	return word_to_exactlocation_matching_letters_dict
	# END

def get_word_to_matched_letters_positions_dict(user_input_word, words_dictionary_list):	
	word_to_matched_letters_positions_dict = {}
	# iterates list of all words
	for _word in words_dictionary_list:
		# individual dictionary that correlates each matched letter with the position it is in
		matched_letters_positions_dict = {}
		# iterates through each letter in word
		for c in _word:
			# condition to prevent out of range error
			if _word.index(c) < len(user_input_word):
				if c == user_input_word[_word.index(c)] :
					# adds "letter" to matched_letters_positions_dict with its "index" as the key
					matched_letters_positions_dict[_word.index(c)] = c
		# for each _word adds corresponding matched_letters_positions_dict
		word_to_matched_letters_positions_dict[_word] = matched_letters_positions_dict

	return word_to_matched_letters_positions_dict
	# END

def get_word_to_unmatched_positions_dict(word_to_matched_letters_positions_dict, words_dictionary_list):
	word_to_unmatched_positions_dict = {}
	# iterates list of all words
	for _word in words_dictionary_list:		
		unmatched_positions_list = [] # list of all "index positions" without a "letter match" for each _word
		
		# iterates through each index position in _word
		for _index_position in range(len(_word)):
			not_matched = True
			# checks if _index_position is in "index position" keys in matched_letters_positions; thereby seeing if _index_position holds a "matched letter" for the "_word"
			if _index_position in word_to_matched_letters_positions_dict[_word]:
				# note: word_to_matched_letters_positions_dict[_word] = matched_letters_positions_dict
				not_matched = False
			# assuming _index_position "holds" no matched letter, will add _index_position to the unmatched_postions_list
			if not_matched:
				unmatched_positions_list.append(_index_position)

		# adds "every" unmatched_positions_list to broad word_to_unmatched_positions_dict for each "_word"
		word_to_unmatched_positions_dict[_word] = unmatched_positions_list

	return word_to_unmatched_positions_dict
	# END

def get_ALL_groups_of_x_letters(x_letters, user_input_word, words_dictionary_list):
	x = x_letters
	word_to_all_groups_of_x_dict = {}
	groups_of_x_list = [] # holds the list of "x letter" strings that'll be added to word_to_all_groups_of_x_dict

	# gets all groups of "x letters" for "user_input_word" by iterating through each "_letter" in "_word" *note: stop at "x" to last letter
	for _letter in user_input_word:

		_index_position = user_input_word.index(_letter) # index position of each _letter
		_group_of_x_string = user_input_word[_index_position:_index_position+x] # the "x letter" string for each letter
		# add each "x letter" string to the "groups_of_x_list" for that word
		groups_of_x_list.append(_group_of_x_string)

		# break condition for "x" to last letter, prevents out of range error
		if _index_position == len(user_input_word)-x :
			break
	# finally update "word_to_all_groups_of_x_dict" for that "word"
	word_to_all_groups_of_x_dict[user_input_word] = groups_of_x_list

	# NOW get groups_of_x for each word in "words_dictionary_list"
	for _word in words_dictionary_list:
		# condition to prevent "out of range" errors
		if len(_word) >= x_letters:
			# resets "groups_of_x_list" for each "_word"
			groups_of_x_list = []
			
			# gets all groups of "x letters" for each "_word"
			for _letter in _word:
				_index_position = _word.index(_letter) # index position of each _letter
				_group_of_x_string = _word[_index_position:_index_position+x] # the "x letter" string for each letter
				# add each "x letter" string to the "groups_of_x_list" for that "_word"
				groups_of_x_list.append(_group_of_x_string)

				# break condition for "x" to last letter, prevents out of range error
				if _index_position == len(_word)-x :
					break
			# finally update "word_to_all_groups_of_x_dict" for that "_word"
			word_to_all_groups_of_x_dict[_word] = groups_of_x_list
		# condition appends empty list to prevent 'KeyError:'
		else:
			word_to_all_groups_of_x_dict[_word] = []

	# return a dictionary with "list" of all "x letter" strings for each "_word" including "user_input_word"
	return word_to_all_groups_of_x_dict
	# END

"""-----------------------------------------------------------------------------------------------------------------------------------"""


# First algorithm to "GUESS" word from dicitonary
def get_top_3_simple_same(user_input_word, words_dictionary_list, word_to_exactlocation_matching_letters_dict):
	same_length_words_list = []
	for _word in words_dictionary_list:
		if len(_word) == len(user_input_word):
			same_length_words_list.append(_word)

	top_3_simple_same = [] # ranked with the best as "first" in the list

	for _word in same_length_words_list:
		if not top_3_simple_same:
			top_3_simple_same.append(_word)
		else:
			for w in top_3_simple_same:
				# checks if new "_word" has more "anylocation_matching_letters" than current word "w"
				if word_to_exactlocation_matching_letters_dict[_word] > word_to_exactlocation_matching_letters_dict[w]:
					# add _word to top_3 in front of lesser word
					top_3_simple_same.insert(top_3_simple_same.index(w),_word)
					break

			# if there are still less than 3 elements appends to end of list
			if len(top_3_simple_same) < 3:
				# prevents repeat "_word"
				if _word not in top_3_simple_same:
					top_3_simple_same.append(_word)
			# if there are now more than 3 elements remove the last element (i.e. worst ranked)
			if len(top_3_simple_same) > 3:
				top_3_simple_same.remove(top_3_simple_same[len(top_3_simple_same)-1])

	return top_3_simple_same
	# END

def get_top_3_same_length(user_input_word, words_dictionary_list, word_to_anylocation_matching_letters_dict, word_to_exactlocation_matching_letters_dict, word_to_matched_letters_positions_dict, word_to_unmatched_positions_dict):
	top_3_same_length = [] # ranked with the best as "first" in the list
	"""
	Algorithm (right now just do it for top_3_same_length)
	same_length	x/100:
		overall_score = (30*first_letter_match + 50*anylocation_score + 20*exactlocation_score)

		anylocation score = number_matched / length of _word
		exact_location score = number_matched / length of user_input_word
	"""
	same_length_words_list = []
	for _word in words_dictionary_list:
		if len(_word) == len(user_input_word):
			same_length_words_list.append(_word)

	word_anylocation_score_dict = {}
	word_exactlocation_score_dict = {}
	# get anylocation and exactlocation scores for each word and append to dict
	for _word in same_length_words_list:
		anylocation_score = word_to_anylocation_matching_letters_dict[_word] / len(_word)
		exactlocation_score = word_to_exactlocation_matching_letters_dict[_word] / len(user_input_word)

		word_anylocation_score_dict[_word] = anylocation_score
		word_exactlocation_score_dict[_word] = exactlocation_score

	# finds top 3 highest ranked within same_length_words_list[]
	for _word in same_length_words_list:
		first_letter_match = 0
		if _word[0] == user_input_word[0]:
			first_letter_match = 1
		overall_score = (30*first_letter_match + 50*word_anylocation_score_dict[_word] + 20*word_exactlocation_score_dict[_word])
		if not top_3_same_length:
			top_3_same_length.append(_word)
		else:
			for w in top_3_same_length:
				first_letter_match = 0
				if _word[0] == user_input_word[0]:
					first_letter_match = 1
				score_of_w = (30*first_letter_match + 50*word_anylocation_score_dict[w] + 20*word_exactlocation_score_dict[w])
				if overall_score > score_of_w:
					# add _word to top_3 in front of lesser word
					top_3_same_length.insert(top_3_same_length.index(w),_word)
					break

			# if there are still less than 3 elements appends to end of list
			if len(top_3_same_length) < 3:
				# prevents repeat "_word"
				if _word not in top_3_same_length:
					top_3_same_length.append(_word)
			# if there are now more than 3 elements remove the last element (i.e. worst ranked)
			if len(top_3_same_length) > 3:
				top_3_same_length.remove(top_3_same_length[len(top_3_same_length)-1])

	return top_3_same_length
	# END

def get_top_3_most_anylocation(user_input_word, words_dictionary_list, word_to_anylocation_matching_letters_dict):
	"""
	Algorithm: simply returns the "3 words" with the most "anylocation_matched_letters"
	"""		
	top_3_most_anylocation = [] # ranked with the best as "first" in the list

	for _word in word_to_anylocation_matching_letters_dict:
		if not top_3_most_anylocation:
			top_3_most_anylocation.append(_word)
		else:
			for w in top_3_most_anylocation:
				# checks if new "_word" has more "anylocation_matching_letters" than current word "w"
				if word_to_anylocation_matching_letters_dict[_word] > word_to_anylocation_matching_letters_dict[w]:
					# add _word to top_3 in front of lesser word
					top_3_most_anylocation.insert(top_3_most_anylocation.index(w),_word)
					break

			# if there are still less than 3 elements appends to end of list
			if len(top_3_most_anylocation) < 3:
				# prevents repeat "_word"
				if _word not in top_3_most_anylocation:
					top_3_most_anylocation.append(_word)
			# if there are now more than 3 elements remove the last element (i.e. worst ranked)
			if len(top_3_most_anylocation) > 3:
				top_3_most_anylocation.remove(top_3_most_anylocation[len(top_3_most_anylocation)-1])

	return top_3_most_anylocation
	# END

def get_top_3_exact_location(user_input_word, words_dictionary_list, word_to_exactlocation_matching_letters_dict):
	"""
	Algorithm: simply returns the "3 words" with the most "exactlocation_matched_letters"
	"""		
	top_3_exact_location = [] # ranked with the best as "first" in the list

	for _word in word_to_exactlocation_matching_letters_dict:
		if not top_3_exact_location:
			top_3_exact_location.append(_word)
		else:
			for w in top_3_exact_location:
				# checks if new "_word" has more "anylocation_matching_letters" than current word "w"
				if word_to_exactlocation_matching_letters_dict[_word] > word_to_exactlocation_matching_letters_dict[w]:
					# add _word to top_3 in front of lesser word
					top_3_exact_location.insert(top_3_exact_location.index(w),_word)
					break

			# if there are still less than 3 elements appends to end of list
			if len(top_3_exact_location) < 3:
				# prevents repeat "_word"
				if _word not in top_3_exact_location:
					top_3_exact_location.append(_word)
			# if there are now more than 3 elements remove the last element (i.e. worst ranked)
			if len(top_3_exact_location) > 3:
				top_3_exact_location.remove(top_3_exact_location[len(top_3_exact_location)-1])

	return top_3_exact_location
	# END

def get_top_3_groups_of_x(x_letters, user_input_word, words_dictionary_list):
	word_to_all_groups_of_x_dict = get_ALL_groups_of_x_letters(x_letters, user_input_word, words_dictionary_list)

	top_3_groups_of_x = [] # ranked with the best as "first" in the list

	"""
	Algorithm:
	score = "_num_of_matched_pairs" / "number of pairs in that _word"
		score = word_to_num_of_matched_pairs_dict[_word] / len(word_to_all_groups_of_x_dict[_word])
		score = word_to_score_for_matched_pairs_dict[_word]
	
	* score = x/1
	rank by greatest score
	"""

	word_to_score_for_matched_pairs_dict = {} # variable for matched pair score
	word_to_num_of_matched_pairs_dict = {} # variable for number of matched pairs

	# for each "_word" assign "_score" based on number of matched pairs with "user_input_word"
	for _word in words_dictionary_list:
		# give each word a number of matched pairs score, starting at '0'
		_num_of_matched_pairs = 0

		# access "word_to_all_groups_of_x_dict" for that "_word"
		groups_of_x_list = word_to_all_groups_of_x_dict[_word]
		# iterate through each "string" in list of "groups of x_letters"
		for _group in groups_of_x_list:
			# for each string check if it is in "groups of x_letters" for "user_input_word"
			if _group in word_to_all_groups_of_x_dict[user_input_word]:
				# if yes, then update matched pairs score
				_num_of_matched_pairs += 1

		word_to_num_of_matched_pairs_dict[_word] = _num_of_matched_pairs

		# calculate "_score" for each "_word"	
		if len(word_to_all_groups_of_x_dict[_word]) != 0: # prevents 'x/0' error
			_score = word_to_num_of_matched_pairs_dict[_word] / len(word_to_all_groups_of_x_dict[_word])
		else:
			_score = 0
		# update "word_to_score_for_matched_pairs_dict"
		word_to_score_for_matched_pairs_dict[_word] = _score

	# find top 3 "_word"s with the best "_score"
	for _word in words_dictionary_list:
		if not top_3_groups_of_x:
			top_3_groups_of_x.append(_word)
		else:
			for w in top_3_groups_of_x:
				# checks if new "_word" has better "_score" than current word "w"
				if word_to_score_for_matched_pairs_dict[_word] > word_to_score_for_matched_pairs_dict[w]:
					# add "_word" to "top_3" in front of lesser word "w"
					top_3_groups_of_x.insert(top_3_groups_of_x.index(w),_word)
					break
			# if there are still less than 3 elements appends to end of list
			if len(top_3_groups_of_x) < 3:
				# prevents repeat "_word"
				if _word not in top_3_groups_of_x:
					top_3_groups_of_x.append(_word)
			# if there are now more than 3 elements remove the last element (i.e. worst ranked)
			if len(top_3_groups_of_x) > 3:
				top_3_groups_of_x.remove(top_3_groups_of_x[len(top_3_groups_of_x)-1])

	return top_3_groups_of_x
	# END			

def get_most_groups_of_2(x_letters, user_input_word, words_dictionary_list):
	word_to_all_groups_of_x_dict = get_ALL_groups_of_x_letters(x_letters, user_input_word, words_dictionary_list)
	most_groups_of_2 = [] # ranked with the best as "first" in the list
	"""
	Algorithm:
	score = "_num_of_matched_pairs"
	* only looks at words < len(user_input_word) + 2

	rank by greatest score
	"""
	list_available_words = []
	for _word in words_dictionary_list:
		if len(_word) < len(user_input_word) + 2 and _word[0] == user_input_word[0]:
			list_available_words.append(_word)

	word_to_num_of_matched_pairs_dict = {} # variable for number of matched pairs
	for _word in list_available_words:
		# give each word a number of matched pairs score, starting at '0'
		_num_of_matched_pairs = 0
		groups_of_x_list = word_to_all_groups_of_x_dict[_word]
		# iterate through each "string" in list of "groups of x_letters"
		for _group in groups_of_x_list:
			if _group in word_to_all_groups_of_x_dict[user_input_word]:
				# if yes, then update matched pairs score
				_num_of_matched_pairs += 1
		word_to_num_of_matched_pairs_dict[_word] = _num_of_matched_pairs

	#print(f"\n\nword_to_num_of_matched_pairs_dict['bicycle'] = {word_to_num_of_matched_pairs_dict['bicycle']}\n\n")

	# find top 5 "_word"s with the most "_num_of_matched_pairs"
	for _word in list_available_words:
		if not most_groups_of_2:
			most_groups_of_2.append(_word)
		else:
			for w in most_groups_of_2:
				if word_to_num_of_matched_pairs_dict[_word] > word_to_num_of_matched_pairs_dict[w]:
					most_groups_of_2.insert(most_groups_of_2.index(w),_word)
					break
			if len(most_groups_of_2) < 5:
				if _word not in most_groups_of_2:
					most_groups_of_2.append(_word)
			# if there are now more than 5 elements remove the last element (i.e. worst ranked)
			if len(most_groups_of_2) > 5:
				most_groups_of_2.remove(most_groups_of_2[len(most_groups_of_2)-1])

	return most_groups_of_2
	# END


def get_overall_pick(list_all_grouping_alg_suggestions, top_3_same_length, top_3_most_anylocation, top_3_exact_location):
	"""
	Algorithm:
	* right now very simple, could make it more impressive
	
	overall_pick is "_word" with most appearances in list_all_grouping_alg_suggestions
	"""

	overall_pick = list_all_grouping_alg_suggestions[0]
	_number_of_appearances = 0
	for _word in list_all_grouping_alg_suggestions:
		_number_of_appearances = list_all_grouping_alg_suggestions.count(_word)
		# checks if "_word" appears more than old "overall_pick"
		if _number_of_appearances > list_all_grouping_alg_suggestions.count(overall_pick):
			# updates overall_pick
			overall_pick = _word

	return overall_pick
	# END

"""-----------------------------------------------------------------------------------------------------------------------------------"""


# Parent function for all the thinking (no internal logic)
	# calls "get" functions for all statistic variables that are used in algorithms
	# runs each algorithm method
	# compiles results into suggested_words_dict with the "algorithm type" as reference key
	# returns suggested_words_dict
def find_suggestion(user_input_word, words_dictionary_list):
	 # holds all suggested words, with the algorithm type as the reference key
	suggested_words_dict = {}

	 # shows the number of letters each _word has that are in user_input word at any location, with _word as reference key to number of matched letters as values
	word_to_anylocation_matching_letters_dict = get_word_to_anylocation_matching_letters_dict(user_input_word, words_dictionary_list)
	
	 # shows the number of of letters each _word has that are in exact same position as user_input word, with _word as reference key to number of matched letters as values
	word_to_exactlocation_matching_letters_dict = get_word_to_exactlocation_matching_letters_dict(user_input_word, words_dictionary_list)
	
	 # double tiered dictionary, uses _word to reference sub-dictionary with the index position for each matched letter
	word_to_matched_letters_positions_dict = get_word_to_matched_letters_positions_dict(user_input_word, words_dictionary_list)

	# dictionary, _word is key to a list of each unmatched index position for that word
	word_to_unmatched_positions_dict = get_word_to_unmatched_positions_dict(word_to_matched_letters_positions_dict, words_dictionary_list)

	top_3_simple_same = get_top_3_simple_same(user_input_word, words_dictionary_list, word_to_exactlocation_matching_letters_dict)
	top_3_same_length = get_top_3_same_length(user_input_word, words_dictionary_list, word_to_anylocation_matching_letters_dict, word_to_exactlocation_matching_letters_dict, word_to_matched_letters_positions_dict, word_to_unmatched_positions_dict)
	top_3_exact_location = get_top_3_exact_location(user_input_word, words_dictionary_list, word_to_exactlocation_matching_letters_dict)
	top_3_most_anylocation = get_top_3_most_anylocation(user_input_word, words_dictionary_list, word_to_anylocation_matching_letters_dict)
	# Compiles results into suggested_words_dict with the "algorithm type" as reference key 
	suggested_words_dict['top_3_simple_same'] = top_3_simple_same
	suggested_words_dict['top_3_same_length'] = top_3_same_length
	suggested_words_dict['top_3_exact_location'] = top_3_exact_location
	suggested_words_dict['top_3_most_anylocation'] = top_3_most_anylocation

	# Grouping algorithms...
	list_all_grouping_alg_suggestions = []

	if len(user_input_word) > 1:
		for x_letters in range(2,len(user_input_word)+1):
			top_3_groups_of_x = get_top_3_groups_of_x(x_letters, user_input_word, words_dictionary_list)
			# appends all "_suggestion"s to list_all_grouping_alg_suggestions
			for _suggestion in top_3_groups_of_x:
				list_all_grouping_alg_suggestions.append(_suggestion)
			name = 'top_3_groups_of_' + str(x_letters)
			suggested_words_dict[name] = top_3_groups_of_x
	# Just groups of 2
	suggested_words_dict['most_groups_of_2'] = get_most_groups_of_2(2, user_input_word, words_dictionary_list)

	# Overall Pick alg
	overall_pick = get_overall_pick(list_all_grouping_alg_suggestions, top_3_same_length, top_3_most_anylocation, top_3_exact_location)
	suggested_words_dict['overall_pick'] = overall_pick

	return suggested_words_dict
	# END

"""-----------------------------------------------------------------------------------------------------------------------------------"""


def begin_check_word(dictionary_file):
	# takes in user word
	user_input_word = input("\n\n\nPlease enter a word: ")
	user_input_word = user_input_word.lower()

	if user_input_word in words_dictionary_list:
		# user_input_word "is" in dictionary
		print("Good shit! "+user_input_word+" is spelled correctly\n")
		want_to_continue = input("Would you like to check another word? (yes/no) : ")
		if want_to_continue == 'yes':
			begin_check_word(dictionary_file)
		else:
			print("\nOkay. Goodbye :)")
			return 0	
	# user_input_word "not" in dictionary, commence spell check
	else:
		print("We could NOT find "+user_input_word+" in words_dictionary_list\n")
		suggested_words_dict = find_suggestion(user_input_word, words_dictionary_list)

		print(f"Did you mean one of the following ?\n")
		# prints suggestions for each algorithm type
		for _alg_type in suggested_words_dict:
			# condition for "spacer" for "overall_pick"
			if _alg_type == 'overall_pick':
				print("\n")
			print(f"{_alg_type}:\t{suggested_words_dict[_alg_type]}")
		# checks with user if the algorithm worked
		algorithm_successful = input("(yes/no) : ")

		if algorithm_successful == 'yes':
			print("\nBet. Glad I could help.")
			want_to_continue = input("Would you like to check another word? (yes/no) : ")
			if want_to_continue == 'yes':
				begin_check_word(dictionary_file)
			else:
				print("\nOkay. Goodbye :)")
				return 0
		else:
			print("Sorry I couldn't help.\n\n")
			want_to_continue = input("Would you like to check another word? (yes/no) : ")
			if want_to_continue == 'yes':
				begin_check_word(dictionary_file)
			else:
				print("\nOkay. Goodbye :)")
				return 0

# main() function, simply calls begin_check_word() which has all the code to ask for user input and then run algorithm
begin_check_word(dictionary_file)


"""-----------------------------------------------------------------------------------------------------------------------------------"""


""" Next Steps:

	DONE - modulate find_suggestions() into more subfunctions, so it's less messy
	DONE - write additional function that runs ranking algorithm, so it's done in the main function
	DONE - fix word_to_matched_letters_positions dict so that it uses "index value" as keys rather than the "letter"	
	DONE - decide simple algorithm for top_3_most_anylocation and top_3_exact_location
	DONE - code algorithm function for top_3_most_anylocation and top_3_exact_location
	DONE - decide logic for grouping function
	DONE - write grouping algorithm, that looks at groups of letters, separate from index positions
	DONE - rewrite so it takes an value "x_letters" for the size of the groups
	DONE - implement grouping algorithm into find_suggestions
	DONE - decide if I want to use multiple group sizes
	DONE - implement multiple group sizes
	DONE - expand to bigger dictionary
	DONE - add overall pick function
	DONE - sew overall pick into output

	- have overall pick look at all top_3 lists
	- create auto input vowel or letter algorithm
	- make overall pick alg more complex i.e. takes into account more factors(gonna be intensive)
	- add advanced "user search options"
"""


















