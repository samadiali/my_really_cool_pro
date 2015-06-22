def sillycap (s):
	cap_list = []
	lastpart_list= []
	list_s = list (s)
	mid = (len(list_s))/2  
	first_part = list_s [:mid]
	second_part = list_s[mid:]
	for letter in second_part:
		let1=letter.capitalize()
		cap_list.append(let1)
	lastpart_list= first_part + cap_list 
	s = ''.join(lastpart_list)
	return (s)

