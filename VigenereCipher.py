def vigenereEncrypt():
	# A list that includes all possible character entries in the plaintext
	alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ']
	
	# Message prompt
	print("Welcome to the Vigenere Encryption Program!\n")

	# Promt the user to enter the filename 
	fileName = input("Enter filename: ")
	inFile = open(fileName, 'r')
	# Create the output file name that includes the original file name
	outFileName = fileName[:7] + '-cipher.txt'
	outFile = open(outFileName, 'w')

	# Transferring contents of file into plaintext variable
	plainText = inFile.read()

	# Prompt the user to enter the key
	key = input("\nEnter the key: ")
	keyLength = len(key)
	# Create newKey list that will hold repeated key
	newKey = []

	# List to hold value of ciphertext that equals that of alphabet
	cipherText = []

	# While loop to repeat the key for length of the plaintext and include spaces
	i = 0
	j = 0
	while (len(newKey) < len(plainText)):
		if ord(plainText[j]) == 32:
			newKey.append(chr(32))
		else:
			newKey.append(key[i % keyLength])
			i += 1
		j += 1

	# For loop to iterate through plaintext and repeated key
	for p,k in zip(plainText, newKey):
		temp1 = alphabet.index(p)
		temp2 = alphabet.index(k)
		newChar = temp1 + temp2
		
		# if both values are space
		if ((temp1 == 52) & (temp2 == 52)):
			newChar -= 52
		# If plaintext character is uppercase
		elif temp1 < 26:
			newChar -= 52
		# If statement to guarantee that all lowercase letters remain that way
		elif newChar > 78:
			newChar -= 52
		# Else value is lowercase
		else:
			newChar -= 26
		cipherText.append(alphabet[newChar])			

	# Print the ciphertext to a file	
	print (''.join(cipherText), end=' ', file = outFile)
	
	# Close the files
	inFile.close()
	outFile.close()
				
vigenereEncrypt()
