# function for removing common characters
# with their respective occurrences


def remove_match_char(list1, list2):

	for i in range(len(list1)):
		for j in range(len(list2)):

			# if common character is found
			# then remove that character
			# and return list of concatenated
			# list with True Flag
			if list1[i] == list2[j]:
				c = list1[i]

				# remove character from the list/trouver l'élement en commun et on le supprime directement
				list1.remove(c)
				list2.remove(c)

				# concatenation of two list elements with *
				# * is act as border mark here
				list3 = list1 + ["*"] + list2

				# return the concatenated list with True flag / retourner la liste 3 avec l'élement TRUE
				return [list3, True]

	# If no common characters is found
	# return the concatenated list with False flag
	list3 = list1 + ["*"] + list2
	return [list3, False]

print(remove_match_char(['S','A','R','A','H'],['L','O','U','I','Z','A']))

# Driver code


	# take first name
player1 = input("Player 1 name : ")

	# converted all letters into lower case
player1 = player1.lower()

	# replace any space with empty string
player1.replace(" ", "")

	# make a list of letters or characters
player1_list = list(player1)

	# take 2nd name
player2 = input("Player 2 name : ")
player2 = player2.lower()
player2.replace(" ", "")
player2_list = list(player2)

	# taking a flag as True initially
proceed = True

	# keep calling remove_match_char function
	# until common characters is found or
	# keep looping until proceed flag is True
while proceed:

		# function calling and store return value
	ret_list = remove_match_char(player1_list, player2_list)

		# take out concatenated list from return list
	con_list = ret_list[0]

		# take out flag value from return list
	proceed = ret_list[1]

		# find the index of "*" / border mark
	star_index = con_list.index("*")

		# list slicing perform

		# all characters before * store in player1_list
	player1_list = con_list[: star_index]

		# all characters after * store in player2_list
	player2_list = con_list[star_index + 1:]

	# count total remaining characters
count = len(player1_list) + len(player2_list)
print(count)

	# list of FLAMES acronym
result = ["Friends", "Love", "Affection", "Marriage", "Enemy", "Siblings"]

	# keep looping until only one item
	# is not remaining in the result list
while len(result) > 1:

		# store that index value from
		# where we have to perform slicing.
	split_index = (count % len(result) - 1)
	print (split_index)

		# this steps is done for performing
		# anticlock-wise circular fashion counting.
	if split_index >= 0:

			# list slicing
		right = result[split_index + 1:]
		print(right)
		left = result[: split_index]
		print(left)

			# list concatenation
		result = right + left

	else:
		result = result[: len(result) - 1]
		print(result)

	# print final result
print("Relationship Status :", result[0])

