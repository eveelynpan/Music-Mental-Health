#Evelyn Pan
#Bear ID: 892641836
#DSC 4320 Spring 2024: Homework 2

#DATASET 1: call the music mental health survey.csv.py file
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
file_path = pd.read_csv('/Users/evelynpan/Desktop/mxmh_survey_results.csv')

#number x word relationship
x = file_path['Frequency [Classical]'] #number
y = file_path['Music effects'] #words

# PLOT 1: Violin Plot
print('Source: Kaggle dataset website (https://www.kaggle.com/datasets), mxmh_survey_results.csv')
plt.figure(figsize=(10, 8))  # Adjust the figure size as needed
sns.violinplot(x='Frequency [Classical]', y='Music effects', data=file_path)
plt.xlabel('Frequency of listening to Classical Music')
plt.ylabel('Music effects (Anxiety, Depression, Insomnia, OCD)')
plt.title('Frequency of listening to Classical Music and its Effects: Violin Plot')  # Plot title
plt.show()

print("This first graph plot is a violin plot of the Frequency of listening to Classical Music and its Effects.\n"
      "When rarely listening to classical music, there is the least improvement in mental health (anxiety, depression,\n"
      "insomnia, and OCD, seen in the graph's trends. When sometimes listening to classical music, there is major \n"
      "improvement in mental health. The line drawn from the center of the violin plot to the no effect is more\n"
      "prominent, which suggests that in order to notice a more consistent trend, one should either rarely or \n"
      "frequently [do the action] for a more prominent result. When never listening to classical music, the graph \n"
      "shape is similar to rarely listening to classical music and there is very little improvement in mental health.\n"
      "Lastly, very frequently listening to classical music had the narrowest shaped graph, which means it had the \n"
      "most prominent improvement effect. Furthermore, the line drawn from the center to the worsen bottom of the\n"
      "chart is the slimmest, which suggests that listening to more classical music has more improvements in mental\n"
      "health than worsening factors. In conclusion from this violin plot, classical music is a great genre to listen\n"
"to to improve mental health. ")