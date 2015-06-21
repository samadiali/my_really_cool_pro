
#remove_val
state_list = ['california', 'oklahama' 'a good', 'boy']

vawol_sound = list ('aeoui')

output = []

for state in state_list:
	state_list = list (state.lower())
	print state_list

	for vawol in vawol_sound:
		while True :
	
			try:
	 			state_list.remove(vawol)
	 		except:
	 			break
	output.append(' '.join(state_list).capitalize())
print (output)
		




