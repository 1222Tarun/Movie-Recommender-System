
# Movie-Recommender-System

A **Content-Based Movie Recommender System** built using the **TMDB dataset** that provides personalized movie recommendations. This system analyzes various features such as **genres**, **keywords**, **cast**, and **crew** to suggest movies similar to the one selected by the user.

This project demonstrates end-to-end implementation, from **data analysis** and **preprocessing** to **recommendation generation**, and serves as a practical application of machine learning concepts.

---

## 📊 **Data Analysis and Transformation**

The system leverages data from the **TMDB 5000 Movies** and **TMDB 5000 Credits** datasets. Comprehensive data analysis and feature engineering were conducted to optimize recommendation accuracy.

### Key Steps:

1. **Data Cleaning:**
   - Removed duplicates and irrelevant columns.
   - Handled missing values in critical fields.

2. **Feature Engineering:**
   - Combined relevant features like **genres**, **keywords**, **cast**, and **crew** into a unified content vector.
   - Extracted director information separately for additional insights.

3. **Data Transformation:**
   - Utilized **TF-IDF Vectorization** to transform text features into numerical vectors.
   - Calculated **cosine similarity** between movies based on their vector representations.

---

## ⚙️ **Technologies Used**

- **Programming Language:** Python
- **Libraries:**  
  - `Pandas` for data manipulation  
  - `NumPy` for numerical operations  
  - `Scikit-Learn` for vectorization and similarity computation  
  - `Matplotlib` and `Seaborn` for optional data visualization

---

## 📁 **Project Structure**

```
Movie-Recommender-System/
│
├── data/                   
│   └── tmdb_5000_movies.csv      # Movies dataset
│   └── tmdb_5000_credits.csv     # Credits dataset
│
├── notebooks/                
│   └── data_analysis.ipynb       # Jupyter notebook for EDA and visualizations
│
├── src/                         
│   └── recommender.py            # Core recommendation engine
│   └── preprocessing.py          # Data preprocessing and transformation logic
│
├── app.py                        # Main script to run the system
│
├── README.md                     # Project documentation
│
└── requirements.txt              # Python dependencies
```

---

## 🚀 **Getting Started**

Follow these steps to set up and run the project:

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/Movie-Recommender-System.git
cd Movie-Recommender-System
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Application
```bash
python app.py
```

---

## 🖥️ **How to Use**

1. **Launch the application** by running `app.py`.
2. **Input the name** of a movie you like.
3. The system will display a list of **top similar movies** based on content features.
4. **Explore** and discover new movies similar to your favorite ones!

---

## 🔍 **Example**

**Input:**  
`Inception`  

**Output:**  
1. Interstellar  
2. The Matrix  
3. Shutter Island  
4. The Prestige  
5. Memento  

---

## 📚 **Core Concepts**

### 1. **Content-Based Filtering**
This approach recommends items (movies) based on their similarity to a user-provided input. The similarity is computed using a combination of features like:

- **Genres**
- **Cast**
- **Director**
- **Keywords**

### 2. **Vectorization & Similarity**
- **TF-IDF Vectorizer:** Converts text data into a vectorized format.
- - **Cosine Similarity:** Measures the similarity between two vectors and returns a score between 0 and 1.

---

## 📈 **Data Analysis Insights**

- **Top Genres:** Action, Drama, Comedy, Adventure.
- **Most Frequently Appearing Actors:** Robert Downey Jr., Leonardo DiCaprio, Scarlett Johansson.
- **Popular Keywords:** Hero, Revenge, Friendship, Space.

---

## 🛠️ **Customization**

You can enhance the recommender system by:

- **Adding more features** such as movie ratings, release dates, or user reviews.
- **Incorporating collaborative filtering** to combine user-based preferences with content-based recommendations.
- **Integrating a web interface** using frameworks like Flask or Django for a more interactive user experience.

---

## 📜 **License**

This project is licensed under the **MIT License**. See the `LICENSE` file for more details.

---

## ❤️ **Acknowledgments**

- **TMDB API** for providing the movie data.
- Open-source libraries and community resources that made this project possible.

---

## 🚧 **Future Improvements**

- **Hybrid Recommender System:** Combining content-based and collaborative filtering for better recommendations.
- **User Feedback Loop:** Allow users to rate recommendations and improve results over time.
- **Scalability:** Deploying the system on cloud platforms like AWS or Heroku.

---
