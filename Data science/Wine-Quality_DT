import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
import seaborn as sns
# Load the wine quality dataset
# Adjust the file path according to the location of your dataset
file_path = "WineQuality.csv"
wine_data = pd.read_csv(file_path)

print(wine_data.isnull().sum())
wine_data=wine_data.dropna()

# Display the first few rows of the dataset
print("Original Wine Quality Dataset:")
print(wine_data.head())
plt.figure(figsize=(10, 6))
sns.histplot(data=wine_data, x='alcohol', bins=30, kde=True, color='skyblue')
plt.title('Distribution of Alcohol Content in Wines')
plt.xlabel('Alcohol Content')
plt.ylabel('Frequency')
plt.show()
# Encode the 'type' column (red: 0, white: 1)
label_encoder = LabelEncoder()
wine_data['type'] = label_encoder.fit_transform(wine_data['type'])

# Specify features and target variable
features = ['type', 'fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar',
            'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density', 'pH',
            'sulphates', 'alcohol']
target = 'quality'

X = wine_data[features]
y = wine_data[target]

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a decision tree classifier
decision_tree = DecisionTreeClassifier(random_state=42)

# Train the model
decision_tree.fit(X_train, y_train)

# Make predictions on the test set
y_pred = decision_tree.predict(X_test)

# Evaluate the performance of the model
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
classification_rep = classification_report(y_test, y_pred)

print("\nModel Evaluation:")
print(f"Accuracy: {accuracy:.2f}")
print("\nConfusion Matrix:")
print(conf_matrix)
print("\nClassification Report:")
print(classification_rep)
