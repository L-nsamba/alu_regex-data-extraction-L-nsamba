#usr/bin/env python3
import re
import time

"""
This class contains the function to open the sample
data file
"""

class DataExtractor:

    def __init__(self):
        self.sample_text = ""

    def sample_data_loader(self):

        """
        This function is responsible for opening, reading
        and displaying the sample text to the user
        """

        try:
            #Opening and reading the sample data file
            with open('sample_data.txt', 'r') as file:
                self.sample_text = file.read()
            print("Sample data loaded succesfully!")
            print("")
            return True

        except FileNotFoundError:
            print("Unable to locate 'sample_data.txt'")
            return False

        except Exception as e:
            print(f"Error reading file: {e}")
            return False

    def menu_display(self):

        """
        This function contains the menu
        """

        print("===== REGEX EXTRACTOR MENU =====")
        print("")
        print("1. Extract email addresses")
        print("2. Extract telephone numbers")
        print("3. Extract URL links")
        print("4. Extract credit card info")
        print("5. Extract hashtags")
        print("6. Extract currency ")
        print("7. Exit")

        user_input = input("Enter your choice [1-7]: ")
        return user_input

    def email_extractor(self):

        """
        This function contains the logic and regex pattern
        to extract emails from the sample data
        """

        email_pattern = r'[a-zA-Z0-9._-]+@[a-zA-Z0-9._]+\.[a-zA-Z]{2,}'

        r"""

        Explanation of the email pattern

        1. [a-zA-Z0-9._-] - This represents the username section of the
                            email. It allows there to be any lowercase letter,
                            uppercase letter, number, underscore or dash
                            in the username only

        2. +@ - This represents that the username must be followed
                by an @ symbol

        3. [a-zA-Z0-9] - This represents the domain name section of the
                         email. It allows there to be any lowercase letter,
                         uppercase letter, number or underscore only.

        4. +\. -        This represents that a literal dot must come after the
                        domain name

        5. [a-zA-Z]{2,} - This represents the top level domain and specifies
                          that it must contain only letters and the minimum
                          limit is only 2 characters
        """

        #Searching through sample text for emails matching required pattern
        emails = re.findall(email_pattern, self.sample_text)

        print("")
        print("===== EMAIL ADDRESSES FOUND =====")
        if emails:
            for i, email in enumerate(emails, 1):
                print(f"{i}. {email}")
        else:
            print("No emails found!")

        print("")

    def phone_number_extractor(self):

        """
        This function extracts valid phone numbers
        from the sampe text data
        """

        phone_pattern = r'\+?\d{1,3}[-.\s]?\d{3}[-.\s]?\d{3}[-.\s]?\d{3,4}'

        r"""
        Explanation of the phone pattern

        1. \+?\d{1,3} -  This represents the country code section and
                         indicates that the code must contain atleast
                         once character accompained either with a plus
                         sign or not

        2. [-.\s]?\d{3} - This represents that the country code is followed
                          by either a '-' or '.' or space then three digits

        3. [-.\s]?\d{3,4} - This represents the last digits of the number
                            must start with either a '-' or '.' or space
                            then followed by atmost four digits
        """

        phones = re.findall(phone_pattern, self.sample_text)

        print("")
        print("===== PHONE NUMBERS FOUND =====")
        if phones:
            for i, phone in enumerate(phones, 1):
                print(f"{i}. {phone}")
        else:
            print("No phone numbers found!")

        print("")

    def url_extractor(self):

        """
        This function extracts valid URL links from
        the sample text
        """

        url_pattern = r'https?://(?:[a-zA-Z-]+\.)?[a-zA-Z-]+\.[a-zA-Z]{2,}'

        r"""
        Explanation of the url pattern

        1. https?:// -         This represents that the url pattern must start with
                               https://

        2. (?:[a-zA-Z-]+\.) - This represents the subdomain and indicates that
                              it must only contain letters and followed by a
                              literal dot

        3. [a-zA-Z-]+\. -     This represents the second section of the subdomain
                              and indicates that it must include only letters and
                              followed by a literal dot

        4. [a-zA-Z]{2,} -     This represents the domain name and indicates that it
                              must include a minimum of two letters


        """

        urls = re.findall(url_pattern, self.sample_text)

        print("")
        print("===== URL LINKS FOUND =====")
        if urls:
            for i, url in enumerate(urls, 1):
                print(f"{i}. {url}")
        else:
            print("No phone numbers found!")

        print("")



def main():

    """
    This function links the logic and runs the program
    """
    print("")
    print("Welcome to the Regex Data Extractor!")
    time.sleep(1.0)
    print("")

    #Assigning the DataExtractor class a variable
    extractor = DataExtractor()

    #Printing the sample data
    if extractor.sample_data_loader():
        print(extractor.sample_text)
        print("")
        print("")
        time.sleep(1.0)
    else:
        print("Please ensure 'sample_data.txt' exists in the location this file is being run.")


    #Displaying the regex extraction menu
    while True:
        choice = extractor.menu_display()

        if choice == '1' :
            print("")
            print("Extracting valid email addressess...")
            time.sleep(1.0)
            extractor.email_extractor()

        elif choice == '2':
            print("")
            print("Extracting valid phone numbers...")
            time.sleep(1.0)
            extractor.phone_number_extractor()

        elif choice == '3':
            print("")
            print("Extracting valid URL links...")
            time.sleep(1.0)
            extractor.url_extractor()

        elif choice == '7':
            print("Exiting program....")
            time.sleep(1.0)
            break

if __name__ == "__main__":
    main()