import csv

CATEGORIES = ["AAC", "APP", "CFS", "HT", "CESB", "PSI", "SWB", "SLA"]

##### creating confusion matrix ############
confusion = {} # will be a nested dictionary
               # outer key = actual category
               # inner key = predicted category
               # value = how many have this combination


for actual in CATEGORIES:
    confusion[actual] = {}

    for predicted in CATEGORIES:
        confusion[actual][predicted] = 0


gold = {} # key = name, value = actual category
predictions = {} # key = name, value = predicted category


with open("../data/final_labeled_dataset.csv", 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        gold[row["Name"]] = row["Coding"]


with open("../data/llm.csv", 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        predictions[row["Name"]] = row["Prediction"]


for name in gold:
    actual = gold[name]
    predicted = predictions[name]

    confusion[actual][predicted] += 1

with open("../data/confusion.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerow(["Actual / Predicted"] + CATEGORIES)

    for actual in CATEGORIES:
        row = [actual]

        for predicted in CATEGORIES:
            row.append(confusion[actual][predicted])

        writer.writerow(row)

###### creating recall/precision ########
results = {} # key = category
             # value - dictionary with precision and recall as keys

for actual  in CATEGORIES:

    correct  = confusion[actual][actual] # diagnoal value
    
    row_total = 0
    for predicted in CATEGORIES:
        row_total += confusion[actual][predicted] # predicted (vertical value) is changing


    if row_total > 0:
        recall = round(correct / row_total, 2)
    else:
        recall = None

    column_total = 0

    for category in CATEGORIES:
        column_total += confusion[category][actual] # actual (horizontal value) is changing

    if column_total > 0:
        precision = round(correct / column_total, 2)
    else:
        precision = None

    results[actual] = {
        "Precision": precision,
        "Recall": recall
        }


# saving results to a CSV file
with open("../data/precision_recall.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerow(["Label", "Precision", "Recall"])

    for category in CATEGORIES:
        writer.writerow([
            category,
            results[category]["Precision"],
            results[category]["Recall"]
        ])


