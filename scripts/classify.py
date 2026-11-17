from google import genai
import csv
import os
import time

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(SCRIPT_DIR)
DATA_DIR = os.path.join(PROJECT_DIR, "data")
LLM_PATH = os.path.join(DATA_DIR, "llm.csv")
TAXONOMY_PATH = os.path.join(PROJECT_DIR, "taxonomy_guide.md")

completed = set()

if os.path.exists(LLM_PATH):
    with open(LLM_PATH, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            completed.add(row["Name"])

client = genai.Client() # initializes the client

with open(TAXONOMY_PATH) as f:
    categories = f.read() # reads entire taxonomy guide into one string and stores it in categories

posts = []

for filename in [os.path.join(DATA_DIR, "final_labeled_dataset_mcgill.tsv"), os.path.join(DATA_DIR, "final_labeled_dataset_concordia.tsv")]:

    with open(filename) as f:
        reader = csv.DictReader(f, delimiter='\t')
        for row in reader:
            posts.append(row)

file_exists = os.path.exists(LLM_PATH)

with open(LLM_PATH, "a", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["Name", "Prediction"])
    if not file_exists:
        writer.writeheader()

    for post in posts:
        if post["Name"] not in completed:
            title = post["title"]
            name = post["Name"]
            interaction = client.interactions.create(model="gemini-3.5-flash-lite", input=f"Here's a Reddit post title. Which of the categories fits it best? {categories}? (Return only one category abbreviation, and no other text) Title: {title}")
            prediction = interaction.output_text
    
            writer.writerow({"Name": name, "Prediction": prediction})
            time.sleep(5)



