# Heart-Disease-Research-Part-II
Heart Disease Research Part II
In this project, you’ll investigate some data from a sample patients who were evaluated for heart disease at the Cleveland Clinic Foundation. The data was downloaded from the UCI Machine Learning Repository and then cleaned for analysis. The principal investigators responsible for data collection were:

Hungarian Institute of Cardiology. Budapest: Andras Janosi, M.D.
University Hospital, Zurich, Switzerland: William Steinbrunn, M.D.
University Hospital, Basel, Switzerland: Matthias Pfisterer, M.D.
V.A. Medical Center, Long Beach and Cleveland Clinic Foundation: Robert Detrano, M.D., Ph.D.
Note that a solution.py file is loaded for you in the workspace, which contains solution code for this project. We highly recommend that you complete the project on your own without checking the solution, but feel free to take a look if you get stuck or want to check your answers when you’re done!

Finally, we ask you to both print results and graph results in this project. Sometimes the printouts are formatted in a way that is difficult to read — feel free to expand the middle segment to make your printouts more readable.

Tasks
14/14 Complete
Mark the tasks as complete by checking them off
Inspect the Data
1.
The data has been saved as a dataframe named heart in script.py. It contains the following variables:

age: age in years
sex: sex assigned at birth; 'male' or 'female'
trestbps: resting blood pressure in mm Hg
chol: serum cholesterol in mg/dl
cp: chest pain type ('typical angina', 'atypical angina', 'non-anginal pain', or 'asymptomatic')
exang: whether the patient experiences exercise-induced angina (1: yes; 0: no)
fbs: whether the patient’s fasting blood sugar is >120 mg/dl (1: yes; 0: no)
thalach: maximum heart rate achieved in exercise test
heart_disease: whether the patient is found to have heart disease ('presence': diagnosed with heart disease; 'absence': no heart disease)
Inspect the first few rows of data using the .head() method.


Stuck? Get a hint
Predictors of Heart Disease
2.
Each of the patients in this dataset underwent an exercise test, during which their heart rate was monitored. For each patient, thalach gives us the highest heart rate that the patient achieved during this test.

Is thalach associated with whether or not a patient will ultimately be diagnosed with heart disease? Use sns.boxplot() to plot side by side box plots of thalach for patients who were and were not diagnosed with heart disease (indicated by the heart_disease variable). Do you think there is a relationship between these variables?


Stuck? Get a hint
3.
In order to investigate this question further, save the values for thalach among patients who were diagnosed with heart disease as a variable named thalach_hd. Then save the values of thalach among patients who were not diagnosed with heart disease as thalach_no_hd.


Stuck? Get a hint
4.
Calculate and print the difference in mean thalach for patients diagnosed with heart disease compared to patients without heart disease. Then do the same for the median difference.


Stuck? Get a hint
5.
We’d like to find out if the average thalach of a heart disease patient is significantly different from the average thalach for a person without heart disease.

Import the statistical test from scipy.stats that we would use to test the following null and alternative hypotheses:

Null: The average thalach for a person with heart disease is equal to the average thalach for a person without heart disease.
Alternative: The average thalach for a person with heart disease is NOT equal to the average thalach for a person without heart disease.

Stuck? Get a hint
6.
Run the hypothesis test from task 5 and print out the p-value. Using a significance threshold of 0.05, is there a significant difference in average thalach for people with heart disease compared to people with no heart disease?


Stuck? Get a hint
7.
Using the same process, investigate at least one other quantitative variable. Options include age, trestbps (resting blood pressure), and chol (cholesterol). Are any of these variables also significantly associated with heart disease?

Note: before every new plot that you make, be sure to use plt.clf() to clear the previous plot first, so that plots don’t get layered on top of each other. For example:

# first box plot:
sns.boxplot(x=heart.heart_disease, y=heart.thalach)
plt.show()
 
# second box plot:
plt.clf()
sns.boxplot(x=heart.heart_disease, y=heart.age)
plt.show()

Stuck? Get a hint
Chest Pain and Max Heart Rate
8.
Next, let’s investigate the relationship between thalach (maximum heart rate achieved during exercise) and the type of heart pain a person experiences. Create a set of side-by-side box plots of thalach for each chest pain type in the data. Make sure to use plt.clf() to clear the previous plots first!

Are there any chest pain types for which average thalach is significantly higher or lower (compared to other chest pain types)?


Stuck? Get a hint
9.
To investigate this further, save the values of thalach for patients who experienced each type of chest pain as thalach_typical, thalach_asymptom, thalach_nonangin, and thalach_atypical, respectively.


Stuck? Get a hint
10.
Run a single hypothesis test to address the following null and alternative hypotheses:

Null: People with typical angina, non-anginal pain, atypical angina, and asymptomatic people all have the same average thalach.
Alternative: People with typical angina, non-anginal pain, atypical angina, and asymptomatic people do not all have the same average thalach.
Save the resulting p-value as pval and print it out. Using a significance threshold of 0.05, is there at least one pair of chest pain categories for which people in those categories have significantly different thalach?


Stuck? Get a hint
11.
If you completed the previous step correctly, you should have concluded that there is at least one pair of chest pain types (cp) for which people with those pain types have significantly different average max heart rates during exercise (thalach).

Run another hypothesis test to determine which of those pairs are significantly different. Use an overall type I error rate of 0.05 for all six comparisons.


Stuck? Get a hint
Heart Disease and Chest Pain
12.
Finally, let’s investigate the relationship between the kind of chest pain a person experiences and whether or not they have heart disease. Create a contingency table of cp and heart_disease and save it as Xtab, then print it out.


Stuck? Get a hint
13.
Run a hypothesis test for the following null and alternative hypotheses:

Null: There is NOT an association between chest pain type and whether or not someone is diagnosed with heart disease.
Alternative: There is an association between chest pain type and whether or not someone is diagnosed with heart disease.
Save the p-value as pval and print it out. Using a significance threshold of 0.05, is there a significant association between chest pain type and whether or not someone is diagnosed with heart disease?


Stuck? Get a hint
Further Exploration
14.
Congratulations! You’ve used a sample of data to understand how health related outcomes are associated with heart disease. Now that you’ve gotten your feet wet, there are a number of additional variables in this dataset that we haven’t looked at yet! If you want additional practice, use this space to continue your investigation. What other variables might be predictive of heart disease? Can you identify which hypothesis test to use for each variable?

As a reminder, the variables in this data are:

age: age in years
sex: sex assigned at birth; 'male' or 'female'
trestbps: resting blood pressure in mm Hg
chol: serum cholesterol in mg/dl
cp: chest pain type ('typical angina', 'atypical angina', 'non-anginal pain', or 'asymptomatic')
exang: whether the patient experiences exercise-induced angina (1: yes; 0: no)
fbs: whether the patient’s fasting blood sugar is >120 mg/dl (1: yes; 0: no)
thalach: maximum heart rate achieved in exercise test
heart_disease: whether the patient is found to have heart disease ('presence': diagnosed with heart disease; 'absence': no heart disease)
