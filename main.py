nric = input('Enter an NRIC number: ')

# Type your code below
prefix = nric[0].upper()
list_prefix = ['S', 'T', 'F', 'G']
if len(prefix) != 1:
  print('invalid_nric')
elif prefix.isalpha() == list_prefix:
  print('valid_nric')
else:
  print('invalid_nric')

digits = nric[1:8]
list_digits = ['1', '2', '3', '4', '5', '6', '7']
valid = ('len(7)')
if len(digits) != 7:
  print('invalid_nric')
elif digits.isdigit() == list_prefix:
  print('valid_nric')
else:
  print('invalid_nric')

suffix = nric[8:].upper()
list_suffixvalid1 = ('J', 'Z', 'I','H', 'G', 'F', 'E', 'D', 'C', 'B', 'A')
list_suffixvalid2 = ('X', 'W', 'U', 'T', 'R', 'Q', 'P', 'N','M', 'L', 'K')
if len(suffix) != 1:
  print('invalid_nric')
elif suffix.isalpha() == list_suffixvalid1 or list_suffixvalid2:
  print ('valid_nric')
else:
  print ('invalid_nric')

invalid_nric = "NRIC is invalid."
valid_nric = "NRIC is valid."