# 1. Training Dataset (8 Happy, 7 Sad)
train_data = [
    ("I got full marks in the test today!", "Happy"),
    ("We won the college cricket match", "Happy"),
    ("My friends planned a surprise party for me", "Happy"),
    ("The food in the canteen was really tasty", "Happy"),
    ("I am so excited for the weekend trip", "Happy"),
    ("Our project got selected for the exhibition", "Happy"),
    ("I finally learned how to ride a bicycle", "Happy"),
    ("Mom made my favourite sweets today", "Happy"),
    ("I lost my phone on the bus", "Sad"),
    ("I failed in the mathematics exam", "Sad"),
    ("My best friend is moving to another city", "Sad"),
    ("It rained and our picnic was cancelled", "Sad"),
    ("I missed the last bus and felt very upset", "Sad"),
    ("My laptop stopped working before the submission", "Sad"),
    ("I felt lonely during the long holidays", "Sad"),
]

# 2. Level 1: Count the moods
def count_moods(data):
    happy_count = 0
    sad_count = 0
    for sentence, mood in data:
        if mood == "Happy":
            happy_count += 1
        elif mood == "Sad":
            sad_count += 1
    return happy_count, sad_count

print("Level 1 Output:", count_moods(train_data))
print("-" * 40)

# 3. Level 2: Guess the mood (N = 10 words each, since roll number ends in 0)
happy_words = [
    "full", "won", "surprise", "party", "tasty",
    "excited", "selected", "learned", "favourite", "sweets"
]

sad_words = [
    "lost", "failed", "moving", "rained", "cancelled",
    "missed", "upset", "stopped", "lonely", "holidays"
]

def guess_mood(sentence):
    clean_text = sentence.lower()
    for ch in ".,!?\"'":
        clean_text = clean_text.replace(ch, "")
    
    words = clean_text.split()
    happy_score = 0
    sad_score = 0
    
    for w in words:
        if w in happy_words:
            happy_score += 1
        if w in sad_words:
            sad_score += 1
            
    if happy_score > sad_score:
        return "Happy"
    elif sad_score > happy_score:
        return "Sad"
    else:
        # Tie-breaker: Defaulting to Happy because neutral everyday sentences tend to be positive unless sad words appear.
        return "Happy"

# 4. Level 3: Test on practice_data
practice_data = [
    ("I won a medal in the sports meet", "Happy"),
    ("I lost my notebook before the exam", "Sad"),
    ("My friends gave me a lovely surprise", "Happy"),
    ("The train was late and I felt upset", "Sad"),
    ("Today was a great day", "Happy"),
]

print("Level 3 Practice Results:")
correct = 0
for sentence, actual in practice_data:
    guess = guess_mood(sentence)
    print(f"Sentence: '{sentence}' -> Predicted: {guess} | Actual: {actual}")
    if guess == actual:
        correct += 1

accuracy = (correct / len(practice_data)) * 100
print(f"Level 2/3 Accuracy: {accuracy}%")
print("-" * 40)

# 5. Bonus (Optional +6 Marks): Automatic Score Learning
def learn_scores(data):
    scores = {}
    for sentence, mood in data:
        clean_text = sentence.lower()
        for ch in ".,!?\"'":
            clean_text = clean_text.replace(ch, "")
        for word in clean_text.split():
            if word not in scores:
                scores[word] = 0
            if mood == "Happy":
                scores[word] += 1
            else:
                scores[word] -= 1
    return scores

def guess_mood_learned(sentence, scores):
    clean_text = sentence.lower()
    for ch in ".,!?\"'":
        clean_text = clean_text.replace(ch, "")
    total = sum(scores.get(word, 0) for word in clean_text.split())
    return "Happy" if total > 0 else "Sad"

learned = learn_scores(train_data)
bonus_correct = sum(1 for s, m in practice_data if guess_mood_learned(s, learned) == m)
print(f"Bonus Learned Model Accuracy: {(bonus_correct / len(practice_data)) * 100}%")
