This project is a Movie Recommender System built using Python and Pycharm. I also tried using Heroku for deployment purposes, but could not complete it since it was asking for credit card credentials, and I do not own one.

The method used to recommend movies is content based filtering. However, I could not calculate any of the accuracy scores since the dataset I used did not consist of user-defined ratings (I have attached the files in the repository)

The first step in the project was to clean and preprocess the data, which was done by removing null values, editing out unwanted columns and merging some of them to create a better dataframe.
![image](https://github.com/user-attachments/assets/144e841d-f597-42b5-99f6-ee3b74d87bad)
Then, I created a multi-dimensional vector space to represent the movies and keywords used in their description (In accordance with the datatframe), which helped in the movie recommendation prcess using deep learning.
![image](https://github.com/user-attachments/assets/1eece92e-a382-4cb8-83ae-163dd369a4c6)

Next, I imported the code to pycharm using the pickle library (In pkl format), which was used to create the frontend for the local project.
![image](https://github.com/user-attachments/assets/9e0082e9-32be-4d53-ab69-2d36d62867f1)


To run the project, the user would first have to download the dataframe files and replace the path of the files. Then, in pycharm, the user would have to write the command:

                                                        streamlit run ProjectApplication.py

in the pycharm terminal. This will give the address to the localhost of the recommendation system, where the user can search for a movie, then press 'Recommend', and five movies will bbe recommended based on the input.
![image](https://github.com/user-attachments/assets/3c97565a-acc4-481b-97bc-6a617b3b0ee6)
![image](https://github.com/user-attachments/assets/6d56fa1c-0a90-46f2-aeb5-5afdaf2a0361)
