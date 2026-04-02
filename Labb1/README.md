# Movie recommender

This is a simple movie recommender system built in Python using scikit-learn.

The model is content-based and uses movie genres to find similar movies. Each movie is converted into a vector based on its genres, and then cosine similarity is used to calculate how similar movies are.

I used the MovieLens dataset and focused on the movies and genres. The ratings file is included but not used in this basic version.

## How to run

Run the program from the terminal like this:

python main.py "Movie Name"

Example:

python main.py "Cinderella"

## Requirements

pip install pandas scikit-learn

## Files

main.py – main script  
movies.csv – movie data  
ratings.csv – not used in this version  

## Notes

This is a simple version made for the assignment. It can be improved by using ratings or more advanced methods.