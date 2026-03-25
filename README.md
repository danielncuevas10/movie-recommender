# Film Recommender
This is a machine learning project built to help users discover films in a faster, smarter and more personal way. You aren't going to get random suggestions, because this web app gives you films based on the similarity in story, cast, directors and content.


## Process
I started by combining, cleaning and merging multiple movie datasets in Python to create a stronger, more complete dataset.

Then, I used Natural Language Processing (NLP) techniques to prepare the text data. This included tokenizing movie overviews and normalizing names so the model could better understand important patterns.

Next, I used CountVectorizer to transform the text into numerical vectors and then applied Cosine Similarity to compare movies mathematically and find the closest matches, where we seek for a number close to 1.

Finally, I saved the model with Pickle, built the interface with Streamlit, using the movie database and an API Key to retrieve the data poster and deployed the app so it could be used online.

## Tech Stack

- **Python** — Data processing and machine learning.

- **Pandas** — Data cleaning and manipulation.

- **Scikit-Learn** — Vectorization and similarity modeling.

- **Streamlit** — Interactive app interface.

- **Pickle** — Saving the trained model.

- **GitHub** — Version control and project hosting.

- **TMDB API** — Film poster retrieval

## What This Project Shows
Building an end-to-end recommendation system.

Applying NLP to real-world text data.

Using vectorization and cosine similarity for matching.

Turning a machine learning model into a live web app.

Connecting data science work with a user-friendly interface.

## Live Demo

https://ai-film-recommender.streamlit.app/
