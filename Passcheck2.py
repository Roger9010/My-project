def passw_check() :
	passin = raw_input('Enter the password')

	if len(passin) == 8:
		if sum(map(str.isupper, passin)) == 2:
			if sum(map(str.islower, passin)) == 2:
				if sum (map(str.isdigit, passin)) == 4:
					print('Password Okay')
				else: 
					print('Not Okay!')

passw_check()

