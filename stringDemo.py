import string
'''Course Week 5: Object Oriented Programming Problem Set 5'''
def build_shift_dict(shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        shift_dict_lower, shift_dict_upper = {}, {}
        alpha_string, upper_alpha= string.ascii_lowercase, string.ascii_uppercase
        first_letters, other_letters = alpha_string[:shift], alpha_string[shift:]
        first_upper, other_upper = upper_alpha[:shift], upper_alpha[shift:]
        shifted_letters = other_letters + first_letters
        shifted_upper = other_upper + first_upper
        for i, j in zip(alpha_string, shifted_letters):
                shift_dict_lower[i] = j
        for i, j in zip(upper_alpha, shifted_upper):
                shift_dict_upper[i] = j
        shifted = shift_dict_lower.copy()
        shifted.update(shift_dict_upper)
        return shifted

def apply_shift(message, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        shift_dict = build_shift_dict(shift)
        shifted_message = ''    
        for letter in message:
                try:
                        letter = shift_dict[letter]
                except KeyError:
                        pass
                shifted_message += letter
        return shifted_message
         
print(apply_shift('abcdef', 3))

