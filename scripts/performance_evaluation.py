import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Load the updated results CSV file with true labels
updated_results = pd.read_csv('labeled_results.csv')

# Drop rows with missing values (NaN) if any
updated_results.dropna(inplace=True)

# Extract true labels from the updated DataFrame
true_labels = updated_results['True_Label'].astype(int).tolist()

# Extract predicted labels from the updated DataFrame
predicted_labels = updated_results['Predicted_Label'].astype(int).tolist()

# Calculate performance metrics
accuracy = accuracy_score(true_labels, predicted_labels)
precision = precision_score(true_labels, predicted_labels)
recall = recall_score(true_labels, predicted_labels)
f1 = f1_score(true_labels, predicted_labels)

print(f'Accuracy: {accuracy}')
print(f'Precision: {precision}')
print(f'Recall: {recall}')
print(f'F1-score: {f1}')
