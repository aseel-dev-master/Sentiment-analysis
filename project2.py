import google.generativeai as genai
import re

# 🔹 Configure Gemini API
genai.configure(api_key="AIzaSyCu9ixQz1NuT3QzwETbnN5DEMx6udH8tbs")

# Create model
model = genai.GenerativeModel("gemini-1.5-flash")


def get_words_and_examples():
    """Ask Gemini for 10 English words and example sentences."""
    prompt = """
    You are an English teacher.
    1. Give me 10 useful English words for learning.
    2. For each word, write one simple example sentence.
    Format your answer as:
    word - example
    """
    response = model.generate_content(prompt)
    return response.text


def make_quiz(words_examples):
    """Ask Gemini to create a quiz about the given words."""
    prompt = f"""
    You are an English teacher.
    I have these words with examples:
    {words_examples}

    Make a 10-question quiz for me.
    Use multiple choice (A/B/C/D).
    After listing the questions, write the correct answers as:
    Answers: 1-A, 2-C, 3-B ...
    """
    response = model.generate_content(prompt)
    return response.text


def run_interactive_quiz(quiz_text):
    """Run an interactive quiz from Gemini's response."""
    print("\n📝 QUIZ START:\n")

    # Split questions and answers
    parts = quiz_text.split("Answers:")
    questions = parts[0].strip()
    answers_text = parts[1].strip() if len(parts) > 1 else ""

    # Extract answer key
    answer_key = {}
    matches = re.findall(r"(\d+)\s*[-:]?\s*([A-D])", answers_text)
    for num, ans in matches:
        answer_key[int(num)] = ans.upper()

    # Print and ask user
    print(questions)
    print("\nType your answers (A/B/C/D):\n")

    score = 0
    for i in range(1, len(answer_key) + 1):
        user_ans = input(f"Q{i}: ").strip().upper()
        correct_ans = answer_key.get(i, "?")

        if user_ans == correct_ans:
            print("🌟 ✅ Correct! 🎉😃\n")
            score += 1
        else:
            print(f"❌ Wrong 😢👎 | Correct answer: {correct_ans}\n")

    print(f"\n🎯 Your final score: {score}/{len(answer_key)}")
    if score == len(answer_key):
        print("🏆🌟 PERFECT SCORE! 🎉🥳")
    elif score >= len(answer_key) // 2:
        print("👏 Good job! Keep practicing 💪")
    else:
        print("📘 Don’t give up, study again and retry! 🚀")


# Main program
if __name__ == "__main__":
    print("📚 Welcome! Your English lesson starts now...\n")

    # Step 1: Get words + examples
    words_examples = get_words_and_examples()
    print("✨ Here are your 10 words and examples:\n")
    print(words_examples)

    # Step 2: Generate quiz
    print("\n📝 Now let's test you with a quiz!\n")
    quiz = make_quiz(words_examples)

    # Step 3: Run interactive quiz
    run_interactive_quiz(quiz)
