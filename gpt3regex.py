## METHOD 1 ##
# import re

# # Load the text file
# with open('bing_base_1.txt', 'r', encoding='UTF-8') as file:
#     text = file.read()

# # Define the regular expressions and replacements
# regex_replacements = [
#     (re.compile(r'Answer choices[\s\S]*?This question was answered \d+ times\n'), ''),  # Remove answer statistics
#     (re.compile(r'Question Feedback:\r?\n\s*Correct'), 'Question Feedback: Correct'),
#     (re.compile(r'(\r?\n){3,}'), '\r\n\r\n'),
#     (re.compile(r'•\s+(\S.*)\s+\n'), r'• \1 '),  # Replace "-" with bullet points
#     (re.compile(r'(QUESTION \d+)'), r'\1'),  # Group question and content lines
#     (re.compile(r'Your choice[\s\S]*?(TRUE\s+\d+%\s+FALSE\s+\d+%)'), ''),  # Remove "Your choice" and "Users statistics"
# ]

# # Apply the regular expressions in order
# for regex, replacement in regex_replacements:
#     text = regex.sub(replacement, text)

# # Remove any remaining lines with "Your choice"
# text = re.sub(r'Your choice.*', '', text)

# # Save the cleaned text to a new file with the correct encoding
# with open('bing_clean_1.txt', 'w', encoding='UTF-8') as file:
#     file.write(text)

# print(text)

## METHOD 2 ##
import re

# Load the text file
with open('bing_base_1.txt', 'r', encoding='UTF-8') as file:
    text = file.read()

# Define the regular expressions and replacements
regex_replacements = [
    (re.compile(r'Answer choices[\s\S]*?This question was answered \d+ times\n'), ''),  # Remove answer statistics
    (re.compile(r'Question Feedback:\r?\n\s*Correct'), 'Question Feedback: Correct'),
    (re.compile(r'Question Feedback:\r?\n\s*'), 'Question Feedback: '),  # Remove newline after 'Question Feedback:'
    (re.compile(r'(\r?\n){3,}'), '\r\n\r\n'),
    (re.compile(r'•\s+(\S.*)\s+\n'), r'• \1 '),  # Replace "-" with bullet points
    (re.compile(r'(QUESTION \d+)'), r'\1'),  # Group question and content lines
    (re.compile(r'Your choice[\s\S]*?(TRUE\s+\d+%\s+FALSE\s+\d+%)'), ''),  # Remove "Your choice" and "Users statistics"
]

# Apply the regular expressions in order
for regex, replacement in regex_replacements:
    text = regex.sub(replacement, text)

# Remove any remaining lines with "Your choice"
text = re.sub(r'Your choice.*', '', text)

# Save the cleaned text to a new file with the correct encoding
with open('bing_clean_1.txt', 'w', encoding='UTF-8') as file:
    file.write(text)

print(text)
