<h1 align="center"> ALU REGEX ONBOARDING HACKHATHON 🤖</h1>

 ### 🎯  Project Description
<p>A Python-menu based regex data extraction tool that processes text files and
extracts various types of structured data using regular expressions (Regex).
This application demonstrates the power of regular expressions for data extraction
from unstructured text, simulating real-world scenarios where developers need to
extract specific information from large datasets.
</p>

### ✨ Features
<p>The application can extract the following data types:
<li>📧Email Addresses: Validates and extracts email addresses in standard formats</li>
<li>📱Phone Numbers: Extracts international phone numbers with country codes</li>
<li>🌐URLS: Finds HTTP/HTTPS website links</li>
<li>💳Credit Card Numbers: Identifies credit card numbers in various formats</li>
<li>#️⃣Hashtags: Extracts social media style hashtags</li>
<li>💰Currency: Regonizes US Dollars ($) and Uganda Shillings (UGX) currency ammounts</li>
</p>


### 📂 Project Structure
```plaintext
📁 alu_regex-data-extraction-L-nsamba/
├── 📄main.py               #Main application file
├── 📄sample_data.txt       #Sample text data for extraction
├── 📄README.md             #Project documentation
```

 ### 🛠️ Setup & Installation
 i. Clone the project repository locally using your desired terminal
 ```sh
      git clone https://github.com/L-nsamba/alu_regex-data-extraction-L-nsamba.git
      cd alu_regex-data-extraction-L-nsamba
```
ii. Run the application
```sh
     python3 main.py
```

### 📖 Usage
1. Lauch the application: Run ``` python3 main.py ```
2. Load the sample data: The application automatically loads ``` sample_data.txt ```
3. Select extraction type: Choose from the menu options [1-7]
4. View results: Extracted data is displayed in a numbered list
5. Repeat or exit: Continue with other extractions or exit program

### 🔧 Regex Patterns Used:
1. Email address extractor: ```[a-zA-Z0-9._-]+@[a-zA-Z0-9._]+\.[a-zA-Z]{2,}``` <br>
2. Phone number extractor: ```\+\d{1,3}[-.\s]\d{3}[-.\s]\d{3}[-.\s]\d{3,4}```<br>
3. URL link extractor: ```https?://(?:[a-zA-Z-]+\.)*[a-zA-Z-]+\.[a-zA-Z]{2,4}\b```<br>
4. Credit card extractor: ```[0-9]{4}[-\s][0-9]{4}[-\s][0-9]{4}(?:[-\s][0-9]{4})?```<br>
5. Hashtag extractor: ```#[a-zA-Z0-9_]+```<br>
6. Currency extractor: ```UGX\s\d{1,3}(?:,\d{3})+|\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?```<br>

### 🏗️ Project Development Notes
This project demonstrates:
<li>Regular expression pattern matching</li>
<li>Object-oriented programming basics</li>
<li>Menu-driven user interface</li>
<li>Error handling and validation</li>

### 👤 Author
👨🏽‍💻**Leon Nsamba**<br>
📧 **Email: l.nsamba@alustudent.com**<br>
💻 **GitHub: [L-nsamba](https://github.com/L-nsamba)**
