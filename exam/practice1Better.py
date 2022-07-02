user_integers = list()

user_input = input("Give me a number: ")

while(len(user_input) != 0 and not user_input.isspace()):

	user_integers.append(int(user_input))

	user_input = input("Give me a number: ")

# calculate the sum

alternating_sum = user_integers[0]
display_string  = str(user_integers[0])

for i in range(1,len(user_integers)):

	if i % 2 == 1: # sub on odd index
		alternating_sum -= user_integers[i]
		display_string  += f" + {user_integers[i]}"

	else: # add on even index
		alternating_sum += user_integers[i]
		display_string  += f" - {user_integers[i]}"

display_string += f" = {alternating_sum}"
print(display_string)
