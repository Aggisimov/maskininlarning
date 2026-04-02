# Movie Recommender Report

## Introduction

In this assignment, I built a simple movie recommender system using Python and scikit-learn. The goal was to create a system that can suggest similar movies based on a given input.

## Method

I implemented a content-based filtering approach. The model uses movie genres to represent each movie as a vector. Since each movie can have multiple genres, I used MultiLabelBinarizer to convert the genres into a numerical format.

To measure similarity between movies, I used cosine similarity. This makes it possible to find movies that have similar genre combinations.

## Implementation

The data comes from the MovieLens dataset. I used the movies.csv file and extracted the genres column. Each genre string was split into a list before being transformed into a binary matrix.

The system is implemented as a Python script (main.py), which takes a movie title as input from the command line and returns similar movies.

## Results

The model is able to recommend movies that have similar genres. For example, if the input is an animation movie, the recommendations are also mainly animation and family movies.

## Discussion

The model works well for basic recommendations but has some limitations. It only uses genres and does not take into account user ratings or preferences. This means the recommendations can sometimes be too similar or not personalized.

## Conclusion

I successfully built a working movie recommender system using a content-based approach. The system meets the requirements of the assignment and can be extended with more advanced techniques in the future.
