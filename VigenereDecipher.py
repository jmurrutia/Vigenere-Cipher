def vigenereDecrypt():
	# A list that includes all possible character entries in the plaintext
	alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ']

	# Message prompt
	print("Welcome to the Vigenere Decryption Program!\n")

	# Promt the user to enter the filename
	fileName = input("Enter filename: ")
	inFile = open(fileName, 'r')
	# Create the output file name that includes the original file name
	outFileName = fileName[:14] + '-clear.txt'
	outFile = open(outFileName, 'w')

	# Transferring contents of file into ciphertext variable
	cipherText = inFile.read()
	
	# Prompt the user to enter the key
	key = input("\nEnter the key: ")
	keyLength = len(key)
	# Create newKey list that will hold repeated key
	newKey = []

	# List to hold value of decipherText that equals that of alphabet
	decipherText = []

	# While loop to repeat the key for length of the ciphertext and include spaces
	i = 0
	j = 0
	while (len(newKey) < len(cipherText)):
		if ord(cipherText[j]) == 32:
			newKey.append(chr(32))
		else:
			newKey.append(key[i % keyLength])
			i += 1
		j += 1

	# For loop to iterate through ciphertext and repeated key
	for p,k in zip(cipherText, newKey):
		temp1 = alphabet.index(p)
		temp2 = alphabet.index(k)
		newChar = temp1 - temp2
		
		# if both values are space
		if ((temp1 == 52) & (temp2 == 52)):
			newChar += 52
		# If plaintext character is uppercase
		elif temp1 < 26:
			newChar += 52
		# If plaintext values are out of bounds from alphabet list
		elif temp1 < temp2:
			newChar += 52
		# Else value is lowercase
		else:
			newChar += 26
		decipherText.append(alphabet[newChar])			

	# Print the ciphertext to a file	
	print (''.join(decipherText), end=' ', file = outFile)
	
	# Close the files
	inFile.close()
	outFile.close()

vigenereDecrypt()