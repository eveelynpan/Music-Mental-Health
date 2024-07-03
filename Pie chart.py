#Evelyn Pan
#Bear ID: 892641836
#DSC 4320 Spring 2024: Homework 2

#DATASET 1: call the music mental health survey.csv.py file
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
file_path = pd.read_csv('/Users/evelynpan/Desktop/mxmh_survey_results.csv')

# Aggregate Data
agg_df = file_path.groupby('Fav genre')['Age'].sum()

# PLOT 2: Plot the Pie Chart
print('Source: Kaggle dataset website (https://www.kaggle.com/datasets), mxmh_survey_results.csv')
plt.figure(figsize=(8, 8))
plt.pie(agg_df, labels=agg_df.index, autopct='%1.1f%%', startangle=140)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('Music and Mental Health Survey Results: Ages (12-73) and '
          'Favorite Genre, Pie Chart')
plt.show()

print("The second graph plot is a pie chart: Music and Mental Health Survey Results: Ages (12-73) and Favorite Genre.\n"
      "The lowest age in the .csv file was 12, while the eldest was 73. Among this age range, I took various genres\n"
      "of music to compare the percentages of how frequent each genre was listened to. The most popular genre of \n"
      "music is Rock, while the least popular genre is Latin. I think rock is the most popular genre because a this \n"
      "genre includes subgenres such as psychedelic rock, blues rock, jazz rock, alternative rock,\n"
      "punk rock, and more. (Wikipedia).\n Pop came in as the second ranked most listened to genre and I think \n"
      "it's because of the same reason as having subgenres. According to byjusfutureschool, there are at least 16 \n"
      "types of pop genres under the pop category. These include folk pop, country pop, indie pop, dance pop, \n"
      "and more.Metal is ranked third, and then Classical is fourth. I think the constrast among these 2 genres are \n"
      "very bipolar because metal has strong vocals, sometimes even screaming, with heavy electric guitar and bass \n"
      "and drums. Contrarily, classical music is very calming with musical stringed and brass instruments and piano. \n"
      "I think that being about to enjoyt these opposing genres of music is what makes a person have complexities. \n"
      "In conclusion, genres with heavier rhythm and stronger vocals are more popular, with the top three genres \n"
      "being Rock, Pop, and Metal.")
