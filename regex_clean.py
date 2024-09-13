import re

# Load the text file
with open('bing_base_1.txt', 'r', encoding='UTF-8') as file:
    text = file.read()

# Define the regular expressions and replacements
regex_replacements = [
    (re.compile(r'Answer choices\tCorrect\tYour choice\tUsers statistics\r?\nTRUE\s+\d+%\r?\nFALSE\s+\d+%\r?\nThis question was answered \d+ times'), ''),  # Remove answer statistics
    (re.compile(r'Question Feedback:\r?\n\s*Correct'), 'Question Feedback: Correct'),
    (re.compile(r'(QUESTION \d+)(?=\S)', re.MULTILINE), r'\1'),  # Group question and content lines
    (re.compile(r'(\r?\n){3,}'), '\r\n\r\n'),
    (re.compile(r'Question Feedback:\r?\n\s+'), 'Question Feedback: '),
    (re.compile(r'•\s+(\S.*)\s+\n'), r'• \1 '),  # Replace "-" with bullet points
    (re.compile(r'•\s+(\S.*)\s+\n'), r'• \1 '),  # Remove line breaks in bullet point questions
    (re.compile(r'(QUESTION \d+)'), r'\1')  # Group question and content lines
]

# Apply the regular expressions in order
for regex, replacement in regex_replacements:
    text = regex.sub(replacement, text)

# Save the cleaned text to a new file with the correct encoding
with open('bing_clean_1.txt', 'w', encoding='UTF-8') as file:
    file.write(text)

print(text)