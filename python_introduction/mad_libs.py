# mad_libs.py
# A simple Mad Libs generator with conditional touches (if / else).

# 1) Collect words from the user
adj_day = input("Enter an adjective to describe the day (e.g., beautiful): ")
adj_monkey = input("Enter an adjective for the monkey (e.g., funny): ")
adj_lion = input("Enter an adjective for the lion (e.g., majestic): ")
adj_experience = input("Enter an adjective to describe the experience (e.g., wild): ")
noun = input("Enter a noun (optional, press Enter to skip): ")
verb = input("Enter a verb (optional, press Enter to skip): ")

# 2) Conditional touches to vary sentences
if adj_day.strip().lower() in ["beautiful", "sunny", "lovely", "gorgeous"]:
    day_sentence = f"On a {adj_day} day, I went to the zoo with a big smile."
else:
    day_sentence = f"On a {adj_day} day, I went to the zoo."

if "funny" in adj_monkey.strip().lower() or len(adj_monkey.strip()) > 7:
    monkey_sentence = f"I saw a funny {adj_monkey} monkey swinging from the trees, and it made everyone laugh."
else:
    monkey_sentence = f"I saw a {adj_monkey} monkey swinging from the trees."

if adj_lion.strip().lower() == "majestic":
    lion_sentence = f"Then, I spotted a majestic {adj_lion} lion lounging in the sun — truly regal."
else:
    lion_sentence = f"Then, I spotted a {adj_lion} lion lounging in the sun."

experience_sentence = f"What a wild and {adj_experience} experience!"

# 3) Optional extras (only added if the user provided them)
extra = ""
if noun.strip():
    extra += f" I even bought a little {noun.strip()} as a souvenir."
if verb.strip():
    extra += f" It made me want to {verb.strip()} all evening."

# 4) Build and show the final story
story = " ".join([day_sentence, monkey_sentence, lion_sentence, experience_sentence]) + extra
print("\nHere is your Mad Libs story:\n")
print(story)
