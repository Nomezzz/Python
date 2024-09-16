from hashlib import sha1
from requests import get
import logging


class PasswordManager:
    #
    def get_password(self):
        """
        Prompts the user to input a password and returns the SHA-1 hashed version of it.
        """
        password = input("Enter Password for checking: ")  # Ask the user for a password
        hashed_password = sha1(password.encode('utf-8'))  # Hash the password using SHA-1
        return hashed_password.hexdigest()  # Return the hashed password as a hexadecimal string
        
    def save_password(self):
        """
        Saves the hashed password to a file named 'passwords.txt'.
        """
        password_to_save = self.get_password()  # Get the hashed password
        with open('passwords.txt', 'w') as file:  # Open 'passwords.txt' in write mode
            file.write(password_to_save + '\n')  # Write the hashed password to the file
        
    def compare(self):
        """
        Compares the saved hashed password with the Pwned Passwords API to check if it has been compromised.
        """
        with open('passwords.txt', 'r') as file:  # Open the file containing the hashed password
            prefix = file.read(5).strip().upper()  # Read the first 5 characters of the hash (prefix)
            logging.debug(prefix)  # Log the prefix for debugging
            last_35_cars = file.readline().strip().upper()  # Read the rest of the file
            suffix = last_35_cars[-35:]  # Extract the last 35 characters (suffix)
            logging.debug(suffix)  # Log the suffix for debugging

            # Send the prefix to the Pwned Passwords API to get all hashes with the same first 5 characters
            response = get(f'https://api.pwnedpasswords.com/range/{prefix.upper()}')

        # Iterate over each line in the response from the API
        for line in response.text.splitlines():
            api_suffix, counter = line.split(':')  # Split the hash suffix and count of breaches
            # Compare the saved suffix with the one from the API
            if suffix.upper() == api_suffix:
                print(f'Your password has been leaked {counter} times')  # Print breach count if the password was found
                return
        print('The password was not leaked')  # If no match, print that the password was not found in breaches


# Instantiate the PasswordManager class and run the save and compare functions
pwd = PasswordManager()
pwd.save_password()  # Save the user's hashed password to a file
pwd.compare()  # Check if the password has been leaked
