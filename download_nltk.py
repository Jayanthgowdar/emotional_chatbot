import nltk

# Download necessary NLTK data files to the specified directory
nltk.download('punkt', download_dir='./nltk_data')
nltk.download('averaged_perceptron_tagger', download_dir='./nltk_data')
nltk.download('wordnet', download_dir='./nltk_data')
nltk.download('omw-1.4', download_dir='./nltk_data')

print("Downloads completed successfully!")
