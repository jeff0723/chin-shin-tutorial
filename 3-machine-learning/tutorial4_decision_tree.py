from tutorial4_read_data import *
from sklearn.tree import DecisionTreeClassifier
import category_encoders as ce
from sklearn import tree
#check data
print(df)
#split data into x and y 
x = df.iloc[:,:-1]
y = df.iloc[:,-1]

# find out which column's data type is not number
print(x.dtypes)

#transform non-number type to number
encoder = ce.OrdinalEncoder(cols=['sex', 'smoker', 'region'])
x = encoder.fit_transform(x)

#check x 
print(x)

#check y mean
print(y.mean())

#change y data to 0 if it less than y' means and 1 if greater
y = y.apply(lambda x : 1 if x>y.mean() else 0)
print(y)

# instantiate the DecisionTreeClassifier model with criterion gini index
clf_gini = DecisionTreeClassifier(criterion='gini', max_depth=3, random_state=0)

# fit the model
model = clf_gini.fit(x, y)

#plot the decision tree
tree.plot_tree(model) 
plt.show()