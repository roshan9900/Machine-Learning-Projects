# Project: Game Recommendation System 
[Demo](https://www.linkedin.com/posts/roshan-salunke-865425263_recommendersystems-flask-machinelearning-activity-7098677033156624384-LDHd?utm_source=share&utm_medium=member_desktop)

<img width="960" alt="image" src="https://github.com/roshan9900/Machine-Learning-Projects/assets/115538447/91c198cc-8447-4103-a50c-ebb7c5efd4b1">


## **Overview:**
The Game Recommendation System with User Validation is a dynamic web application designed to provide users with personalized game recommendations based on their preferences. Developed using Flask, pandas, and scikit-learn's cosine similarity function, the system not only offers tailored game suggestions but also validates user input for a seamless experience.

## **Technologies Used:**
- **Flask:** Employs Flask to build the web application, handle user interactions, and display recommendations.
- **pandas:** Utilizes pandas for data manipulation, preprocessing, and pivoting user-game rating data.
- **scikit-learn:** Utilizes scikit-learn to calculate cosine similarity between games, forming the foundation for recommendations.
- **Google Cloud Platform (GCP):** The project is deployed on GCP, providing online accessibility.

## **Key Components:**
1. **Data Transformation:** Transforms user-game rating data into a matrix representation using pandas. This matrix captures users, games, and their respective ratings.

2. **Cosine Similarity Calculation:** Utilizes scikit-learn's cosine_similarity function to calculate game similarity based on user ratings. The similarity matrix serves as the foundation for generating recommendations.

3. **Recommendation Function:** The core `recommend_games` function takes a user ID as input. It calculates the similarity between the user's rated games and all other games, generating a list of recommended games ranked by similarity.

4. **User Validation:** The system validates user input for a valid user ID before proceeding with recommendations. This ensures accurate results and a better user experience.
<img width="960" alt="Screenshot 2023-08-19 192649" src="https://github.com/roshan9900/Machine-Learning-Projects/assets/115538447/5c054193-a531-4571-8c1b-37fc150d4ecb">


6. **Flask Web Application:** Flask powers the user interface, manages interactions, and handles the display of recommendations.

## **User Interaction:**
Users engage with the recommendation system via a user-friendly web interface. Upon entering their user ID, the system validates the input and, upon successful validation, proceeds to analyze their game ratings and propose relevant recommendations.
<img width="960" alt="Screenshot 2023-08-19 192713" src="https://github.com/roshan9900/Machine-Learning-Projects/assets/115538447/17443738-2fce-4ff3-b0b2-9e198a0834ce">


## **Deployment:**
The project is hosted on Google Cloud Platform (GCP), providing users with convenient online access to the recommendation system. Users can effortlessly explore personalized game recommendations from any location with an internet connection.

## **Impact and Future Scope:**
The Game Recommendation System with User Validation aims to enhance user engagement by facilitating the discovery of games that match individual preferences. As a future step, enhancements might include refining recommendation accuracy, incorporating user feedback for continuous improvement, and exploring advanced machine-learning techniques for even more accurate predictions.

## **Learning and Growth:**
The project not only allowed for the development of skills in data preprocessing, similarity calculations, and web application development using Flask, but it also showcased the importance of input validation for delivering reliable and user-centric solutions.

## **Conclusion:**
The Game Recommendation System with User Validation project merges data analysis, machine learning, and web development skills to create an intuitive tool for gamers seeking customized game suggestions. By incorporating user validation, the system ensures accurate results, contributing to a seamless and satisfying user experience. The fusion of user interaction, recommendation algorithms, and validation techniques makes this project a valuable addition to the world of personalized game discovery.
