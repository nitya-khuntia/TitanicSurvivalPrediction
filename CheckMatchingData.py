import pandas as pd

# load the two CSV files
submission = pd.read_csv('gender_submission.csv')
predictions = pd.read_csv('predictions.csv')

# merge the two dataframes on the 'PassengerId' column
# merged = submission.merge(predictions, on='PassengerId')

# calculate the percentage of matching data
matching_data = predictions['Survived'] == submission['Survived']
percent_matching = (matching_data.sum() / len(matching_data)) * 100
print(f"Percentage of matching data: {percent_matching:.2f}%")

# find the passenger IDs where the predictions do not match
mismatching_passenger_ids = predictions.loc[~matching_data, 'PassengerId']
print(f"Passenger IDs with mismatched predictions: {list(mismatching_passenger_ids)}")

# # check if the values of the 'Survived_x' and 'Survived_y' columns match
# if all(merged['Survived_x'] == merged['Survived_y']):
#     print("The predictions match the submission file.")
# else:
#     print("The predictions do not match the submission file.")