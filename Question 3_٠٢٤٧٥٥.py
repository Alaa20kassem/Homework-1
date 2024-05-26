
import json

# Load quiz questions from the JSON file
with open('quiz_questions.json', 'r') as file:
    quiz_data = json.load(file)

# Initialize variables
total_questions = len(quiz_data)
score = 0

# Ask user's name
user_name = input("Enter your name: ")

# Ask quiz questions and calculate score
for question in quiz_data:
    print(question['question'])
    user_answer = input("Your answer: ")
    if user_answer.lower() == question['answer'].lower():
        score += 1

# Calculate user's percentage score
percentage_score = (score / total_questions) * 100

# Display user's results
print(f"\n{user_name}'s Quiz Results:")
print(f"Total Questions: {total_questions}")
print(f"Correct Answers: {score}")
print(f"Percentage Score: {percentage_score}%")

# Store user's name and result in a JSON file
user_results = {
    "name": user_name,
    "total_questions": total_questions,
    "correct_answers": score,
    "percentage_score": percentage_score
}

with open('user_results.json', 'w') as file:
    json.dump(user_results, file, indent=4)

print("User results have been saved in user_results.json file.")
