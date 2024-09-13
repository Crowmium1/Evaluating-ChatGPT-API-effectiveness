## SINGLE FILE CREATION ##
import re
import csv

# Define a list to store the extracted data
data = []

# The name of the single text file you want to read
file_name = "bing_clean_1.txt"

try:
    with open(file_name, 'r') as file:
        text = file.read()

        # Use regular expressions to find all question sections
        question_matches = re.finditer(r'QUESTION (\d+)\n(.*?)\n\nYour score: (\d+)(?:\nQuestion Feedback: (.*?)(?=\nQUESTION \d|\Z))?', text, re.DOTALL)

        for match in question_matches:
            question_number = match.group(1)
            question_text = match.group(2)
            score = match.group(3)
            feedback = match.group(4) if match.group(4) else "No feedback provided."

            data.append([question_number, question_text, score, feedback.strip()])  # Remove leading/trailing whitespace

    # Write the extracted data to a CSV file
    with open('bing.csv', 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)

        # Write header row
        csv_writer.writerow(['Question Number', 'Question Text', 'Score', 'Feedback'])

        # Write data rows
        csv_writer.writerows(data)

    print("Questions from the file have been saved to 'bing.csv'")

except FileNotFoundError:
    print(f"File {file_name} not found.")
except Exception as e:
    print(f"An error occurred: {e}")


## JOINING MULTIPLE FILES ##

# import re
# import csv

# # Define a list to store the extracted data
# data = []

# # Loop through each of the text files
# file_names = ["me_clean_1.txt", "me_clean_2.txt", "me_clean_3.txt", "gpt4_clean_1.txt"]

# for file_name in file_names:
#     with open(file_name, 'r') as file:
#         text = file.read()

#         # Use regular expressions to find all question sections
#         question_matches = re.finditer(r'QUESTION (\d+)\n(.*?)\n\nYour score: (\d+)(?:\nQuestion Feedback: (.*?)(?=\nQUESTION \d|\Z))?', text, re.DOTALL)

#         for match in question_matches:
#             question_number = match.group(1)
#             question_text = match.group(2)
#             score = match.group(3)
#             feedback = match.group(4) if match.group(4) else "No feedback provided."

#             # Get the file name without the extension
#             file_label = file_name.split('.')[0]

#             data.append([question_number, question_text, score, feedback.strip(), file_label])  # Remove leading/trailing whitespace

# # Write the extracted data to a CSV file
# with open('combined_questions2.csv', 'w', newline='') as csv_file:
#     csv_writer = csv.writer(csv_file)

#     # Write header row
#     csv_writer.writerow(['Question Number', 'Question Text', 'Score', 'Feedback', 'File Label'])

#     # Write data rows
#     csv_writer.writerows(data)

# print("Combined questions from all files have been saved to 'combined_questions.csv'")
