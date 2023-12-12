from sklearn.preprocessing import LabelEncoder

# Example data
education_levels = ['High School', 'Bachelor', 'Master', 'PhD']

# Initialize the encoder
encoder = LabelEncoder()

# Fit and transform the data
encoded_education = encoder.fit_transform(education_levels)

print(encoded_education)
