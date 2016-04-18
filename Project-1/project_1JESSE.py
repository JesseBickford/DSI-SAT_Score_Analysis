
# coding: utf-8

# # Project 1
# 
# ## Step 1: Open the `sat_scores.csv` file. Investigate the data, and answer the questions below.
# 

# ##### 1. What does the data describe?

# #The data set pertains to SAT scores and participation rates from all 50 states and DC. 

# ##### 2. Does the data look complete? Are there any obvious issues with the observations?

# #The data looks complete as a summary of scores across states. 

# ##### 3. Create a data dictionary for the dataset.

# #**State**    The State in America     Type = String
# #**Rate**     The participation rate of students take the SAT     Type = String
# #**Verbal**   The verbal SAT score for the state     Type = String
# #**Math**     The math SAT score for that state     Type = String
# #**Ratesint** The integer conversion of Rate Type = Integer
# #**Verbalint** The integer conversion of Verbal Score Type = Integer
# #**Mathint** The integer conversion if Math Score Type = Integer

# ## Step 2: Load the data.

# ##### 4. Load the data into a list of lists

# In[4]:

import numpy as np
import csv
#create a list of scores from the csv
with open('sat_scores.csv', 'rb') as f:
    reader = csv.reader(f)
    X = list(reader)


# ##### 5. Print the data

# In[3]:

X


# ##### 6. Extract a list of the labels from the data, and remove them from the data.

# In[5]:

#setup a function that removes the first row from the data set

labels = [X[0]]

def removelabels(X):
    X.remove(X[0])
    
removelabels(X)
print labels
print X


# ##### 7. Create a list of State names extracted from the data. (Hint: use the list of labels to index on the State column)

# In[6]:

#selects the first column and stores in a new list called states
states = [row[0] for row in X]
rates = [row[1] for row in X]
verbal = [row[2] for row in X]
math = [row[3] for row in X]


# ##### 8. Print the types of each column

# In[7]:

print type(states[0])
print type(rates[0])
print type(verbal[0])
print type(math[0])


# ##### 9. Do any types need to be reassigned? If so, go ahead and do it.

# In[8]:

#Yes, created new integer lists for rates, verbal, and math

ratesint = []
for i in rates:
    i = int(i)
    ratesint.append(i)

verbalint = []
for i in verbal:
    i = int(i)
    verbalint.append(i)
    
mathint = []
for i in math:
    i = int(i)
    mathint.append(i)


# ##### 10. Create a dictionary for each column mapping the State to its respective value for that column. 

# In[9]:

#create three different dictionaries zipping state with respective column
ratedict = dict(zip(states, rates))
verbaldict = dict(zip(states, verbal))
mathdict = dict(zip(states, math))


# ## Step 3: Describe the data

# ##### 12. Print the min and max of each column

# In[10]:

print 'The max rate is %d ' % max(ratesint)
print 'The max verbal score is %d' % max(verbalint)
print 'The max math score is %d' % max(mathint)


# ##### 13. Write a function using only list comprehensions, no loops, to compute Standard Deviation. Print the Standard Deviation of each numeric column.

# In[11]:

def stddev(X):
    numel = len(X)
    avgval = float(sum(X))/numel
    return (sum((i-avgval)**2 for i in X)/(numel-1))**0.5

print 'The standard deviation of the rate is %s ' % stddev(ratesint)
print 'The standard deviation of the verbal scores is %s ' %stddev(verbalint)
print 'The standard deviation of the math scores is %s ' %stddev(mathint)


# ## Step 4: Visualize the data

# ##### 14. Using MatPlotLib and PyPlot, plot the distribution of the Rate using histograms.

# In[12]:

get_ipython().magic(u'matplotlib inline')
import matplotlib
import matplotlib.pyplot as plt

plt.hist(ratesint, 15)
plt.title("Rates Histogram")
plt.xlabel("Rate")
plt.ylabel("Frequency")
plt.show()


# ##### 15. Plot the Math distribution

# In[13]:

import matplotlib
import matplotlib.pyplot as plt

plt.hist(mathint, 15)
plt.title("Rates Histogram")
plt.xlabel("Math Score")
plt.ylabel("Frequency")
plt.show()


# ##### 16. Plot the Verbal distribution

# In[14]:

get_ipython().magic(u'matplotlib inline')
import matplotlib
import matplotlib.pyplot as plt

plt.hist(verbalint, 15)
plt.title("Verbal Histogram")
plt.xlabel("Verbal Score")
plt.ylabel("Frequency")
plt.show()


# ##### 17. What is the typical assumption for data distribution?

# In[ ]:

#That the data is normally distributed


# ##### 18. Does that distribution hold true for our data?

# In[19]:

print "The math score mean: %d" % np.mean(mathint)
print "The math score median: %d" % np.median(mathint)
print "Seeing that the math score mean is greater than the median, we know the data is skewed to the right, so not for math."

print("\n")

print "The verbal score mean: %d" % np.mean(verbalint)
print "The verbal score median: %d" % np.median(verbalint)
print "Seeing that the verbal score mean is greater than the median, we know the data is skewed to the right"
print "so not for verbal either"


# ##### 19. Plot some scatterplots. **BONUS**: Use a PyPlot `figure` to present multiple plots at once.

# In[36]:

plt.scatter(verbalint, mathint)
plt.title("Math and Verbal Scores")
plt.show()

plt.scatter(mathint, ratesint, color = 'red')
plt.title("Math vs Participation Rate")
plt.show()

plt.scatter(verbalint, ratesint, color = 'green')
plt.title("Verbal vs Participation Rate")
plt.show()



# ##### 20. Are there any interesting relationships to note?

# In[37]:

#Math and verbal scores seem to be positively correlated. Higher math and verbal scores paired together while lower of 
#each also paired together. Additionally, the lower the participation rate, the better the score for both math and 
#verbal. One possible explanation is that test takers who participated in otherwise low particpation rated states had 
#intentionally studied for the exam versus those who were required to take it. 


# ##### 21. Create box plots for each variable. 

# In[43]:

plt.boxplot(verbalint)
plt.title("Verbal Distribution")
plt.show()

plt.boxplot(mathint)
plt.title("Math Distribution")
plt.show()

plt.boxplot(ratesint)
plt.title("Participation Rate Distribution")
plt.show()


# ##### BONUS: Using Tableau, create a heat map for each variable using a map of the US. 
