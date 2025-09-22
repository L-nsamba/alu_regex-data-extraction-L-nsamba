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
            print("Sample data loaded successfully!")
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
            #This for loop creates a list of items that meet the criteria
            for i, email in enumerate(emails, 1):
                print(f"{i}. {email}")
        else:
            print("No emails found!")

        print("")

    def phone_number_extractor(self):

        """
        This function extracts valid phone numbers
        from the sample text data
        """

        phone_pattern = r'\+\d{1,3}[-.\s]\d{3}[-.\s]\d{3}[-.\s]\d{3,4}'

        r"""
        Explanation of phone pattern

        1. \+\d{3} - This represents that the code must have between
                     1,3 numbers

        2. [-.\s]\d{3} - This represents that each field after the country
                         code must be followed by either a -, . or space then
                         three digits and the maximum digits after country code
                         is nine
        """

        phones = re.findall(phone_pattern, self.sample_text)

        print("")
        print("===== PHONE NUMBERS FOUND =====")
        if phones:
            #This for loop creates a list of items that meet the criteria
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

        url_pattern = r'https?://(?:[a-zA-Z-]+\.)*[a-zA-Z-]+\.[a-zA-Z]{2,4}\b'

        r"""
        Explanation of the url pattern

        1. https?:// -         This represents that the url pattern must start with
                               https://

        2. (?:[a-zA-Z-]+\.)* - This represents the subdomain and makes it optional
                               to include but if present it must contain only letters

        3. [a-zA-Z-]+\. -     This represents the second section of the subdomain
                              and indicates that it must include only letters and
                              followed by a literal dot

        4. [a-zA-Z]{2,4}  -    This represents the domain name and indicates that it
                               must include a minimum of two letters and maximum four

        5. \b              -  This represents the word boundary and indicates that
                              the url must meet all those conditions to be extracted


        """

        urls = re.findall(url_pattern, self.sample_text)

        print("")
        print("===== URL LINKS FOUND =====")

        if urls:
            #This for loop creates a list of items that meet the criteria
            for i, url in enumerate(urls, 1):
                print(f"{i}. {url}")
        else:
            print("No URL links found!")

        print("")


    def credit_card_extractor(self):

        """
        This function extracts valid credit card numbers
        from the sample data file
        """

        credit_card_pattern = r'[0-9]{4}[-\s][0-9]{4}[-\s][0-9]{4}(?:[-\s][0-9]{4})?'


        r"""
        Explanation of the credit card pattern

        1. [0-9]{4}[-\s]  - This represents that each of the fields
                            of the credit card number must contain four digits
                            followed by either a dash or space

        2. (?:[-\s][0-9]{4})? - This represents that the credit card can
                                have either three or four fields each only
                                consisting of four numbers
        """


        cards = re.findall(credit_card_pattern, self.sample_text)

        print("")
        print("===== CREDIT CARDS FOUND =====")

        if cards:
            #This for loop creates a list of items that meet the criteria
            for i, card in enumerate(cards, 1):
                print(f"{i}. {card}")
        else:
            print("No credit cards found!")

        print("")


    def hashtag_extractor(self):

        """
        This function extracts hashtaged text from the
        sample data file
        """

        hashtag_pattern = r'#[a-zA-Z0-9_]+'

        """
        Explanation of the hashtag pattern

        1. #[a-zA-Z0-9_] -  This represents that all texts that start
                            with the hashtag symbol followed by any letter
                            or number without any space but can be accompanied
                            by an underscore will be extracted
        """

        hashtags = re.findall(hashtag_pattern, self.sample_text)

        print("")
        print("===== HASHTAGS FOUND =====")

        if hashtags:
            #This for loop creates a list of items that meet the criteria
            for i, hashtag in enumerate(hashtags, 1):
                print(f"{i}. {hashtag}")
        else:
            print("No hashtags found!")

        print("")

    def currency_extractor(self):

        """
        This function extracts valid currencies from the
        sample data file
        """

        currency_pattern = r'UGX\s\d{1,3}(?:,\d{3})+|\$\d+(?:\.\d{2})?'

        r"""
        Explanation of the currency pattern

        1. UGX\s\d{1,3}  - This represents a possible currency format that
                           starts with UGX (Uganda shillings) followed by
                           a space and between 1-3 digits

        2. (?:,\d{3})+   - This represents the optional characters after the
                           first three digits that the user can add but specifies
                           that if the user adds they must be 3 digits only

        3. \$\d+(?:\.\d{2})? -  This represents the alternative currency (dollars)
                                and indicates that the user must enter minimum
                                of two characters if they add anything after the dot
                                separator
        """

        currencies = re.findall(currency_pattern, self.sample_text)

        print("")
        print("===== CURRENCIES FOUND =====")

        if currencies:
            #This for loop creates a list of items that meet the criteria
            for i, currency in enumerate(currencies, 1):
                print(f"{i}. {currency}")
        else:
            print("No currencies found!")

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
            print("Extracting valid email addresses...")
            time.sleep(0.5)
            extractor.email_extractor()

        elif choice == '2':
            print("")
            print("Extracting valid phone numbers...")
            time.sleep(0.5)
            extractor.phone_number_extractor()

        elif choice == '3':
            print("")
            print("Extracting valid URL links...")
            time.sleep(0.5)
            extractor.url_extractor()

        elif choice == '4':
            print("")
            print("Extracting valid credit cards...")
            time.sleep(0.5)
            extractor.credit_card_extractor()

        elif choice == '5':
            print("")
            print("Extracting valid hashtags...")
            time.sleep(0.5)
            extractor.hashtag_extractor()

        elif choice == '6':
            print("")
            print("Extracting valid currencies...")
            time.sleep(0.5)
            extractor.currency_extractor()


        elif choice == '7':
            print("Exiting program....")
            time.sleep(0.5)
            break

        else:
            time.sleep(0.5)
            print("Please enter a valid number.")
            print("")

if __name__ == "__main__":
    main()