# Data Science Class Notes, 1-7-14

# Check out sklearn in python

# Machine learning: concstruction and study of systems that can learn from data

# Two key lieces:
# representation - extracting structure form data
# generalization - making predictions from data

# Two groups: supervised v. unsupervised learning
# supervised : labeled examples
# unsupervised : no labeled examples

# continuous v. categorical
# continuous - quantitative
# categorical - qualitative

# continuous + supervised = regression
# categorical + supervised = classification
# unsupervised + continuous = dimension reduction
# unsupervised + categorical = clustering

# Supervised Learning

# Classification problems
# Must split data set into two sets: training set and test set
# Training set is used to create model.  Test set is used to determine whether midel is accurate
# Then should test on new data, the 'out of sample data'.  Out of sample data must be substantively the same as the original data set.

# Example of supervised learning problem: Iris dataset
# Continuous data with categorical outcome.  
# Independent variables are continuous with class outcomes.

# KNN Learning, aka Nearest Neighbors Classification
# Example: Suppose we want to predict color of grey dot
# 1) Pick a value of key
# 2) Find colors of k nearest Neighbors (implicit uses Euclidean distance)
    # Could also just use the total distance between each distance, without use of Pythagorean system.  Also known as 'Manhattan distance'
# 3) Assign the most common color to the grey dot

# NOTE: No 'fit' step in KNN.  Nothing is ever 'learned'.  Always need entire dataset.

# 'OVerfitting': problem of 'memorizing' entire dataset to get training error down to 0

# Can improve training by splitting training/test sets in different ways then taking the average
    # Called 'cross-validation'

# confusion_matrix, gives an n by n matrix, which gives categorical accounting of how many times something was identified for each category, or mis-identified

# Algorithm evaluation

# Common metrics to evaluate algorithms
  #  precision metric: (number of predicated positive cases, where cases were positive) / (number of predicted positive cases)
  #  recall metric: (number of predicted positive cases, where cases were positive) / (number of actual positive cases)

  # AUC = 'Area under receiver operator curve'
  # Varies from 0 to 1.  Serves as a measure of the tradeoff between precision and recall
  # Where false positives are dangerous, want high precision.  Where false negatives are dangerous, want high recall 
  # Usually the only metric available s accuracy

# Linear regression

  # Regression model: a functonal relationship between input and response variables
  # simple linear regression model captures a linear relationship between a single input x and response variable y:
    # y = alpha + beta * x + epsilon

  # y = response variable (one we want to predict)
  # x = input variable (the one we use to train the model)
  # alpha = intercept (where the line crosses the y-axis)
  # beta = regression coefficient (the model 'parameter', i.e., what the model adjusts to yield a decent preduction)
  # epsilon = residual (the prediction error)
  # NOTE: The intercept (alpha) is the base case.  THat is, where all features are 0.
  # OLS: seek to minimize distance between y and y.hat
      # SUM((y-y.hat)^2)

      # Seek to minimize (y - x * b)

  # multiple linear regression model will have multiple beta * x models

  # How do we fit a regression model to a dataset?
  # Typically, minimize the sum of the squared residuals (OLS)

  # Be careful of multicolinnearity.  Causes models as a causal predictor to break down.  Still works as a categorical predictor though

  # Complexity: defined?
    # could be defined as a function of the size of the coefficients
      # L1-norm: Sum(abs(beta values))
      # L2-norm: Sum((beta values)^2)
  # Manner by which the regularization is controlled
    # L1 regularization (aka Lasso regularization): y = Sum(Beta * x + epsilon) AND Minimize(Sum(beta values))
    # L2 regularization (aka Ridge regularization): y = Sum(Beta * x + epsilon) AND Minimize(Sum(beta values)^2)

    # L1 regularization favors Betas at 0
    # L2 regularization favors Betas that are < 1
    # this feature is due to the presence of the square in L2, since values below 1 are shrunk faster than the value is decreased

# Fitting the equations to allow for regularization by introducing the lambda term:
    # L1 regularization min(|y - x * beta|^2 + lambda * |x|)
    # L2 regularization min(|y - x * beta|^2 + lambda * |x|^2)

    # L1 reg. typically used in problems with high number of features b/c it encourages model to drop features

    # 'Elasticnet' = L1 + L2 regularizaton