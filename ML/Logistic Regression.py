import math
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from sklearn.datasets import load_digits
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# 이미지, 라벨 총 2가지 데이터 유형
digits = load_digits(n_class=2) # digits data load
print("Image Data Shape", digits.data.shape) # 350: the number of images, 64: shape (8 by 8 image)
print("Label Data Shape", digits.target.shape)

print(digits.target) #label 출력

plt.figure(figsize=(20,4))
for index, (image, label) in enumerate(zip(digits.data[0:5], digits.target[0:5])):
  plt.subplot(1, 5, index + 1)
  plt.imshow(np.reshape(image, (8,8)), cmap=plt.cm.gray)
  plt.title('Training: %i\n' % label, fontsize = 20)

digits.data = digits.data/np.max(digits.data)

# train/test data split
x_train, x_test, y_train, y_test = train_test_split(digits.data, digits.target, test_size=0.25, random_state=0)
y_train = y_train[:,np.newaxis] # (270,) => (270,1)
y_test = y_test[:,np.newaxis] # (90,) => (90,1)

# logistic_regression
model = LogisticRegression()
model.fit(x_train, y_train)


# fitted model testing
predictions = model.predict(x_test)
score = model.score(x_test, y_test) # accuracy


# Logistic Regression 직접 구현
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def compute_cost(x_train,y_train,beta_hat):
  m = len(y_train)
  epsilon = 1e-5
  cost = 0
  for i in range(m):
    x_beta = np.dot(x_train[i],beta_hat)
    y_hat = sigmoid(x_beta)
    cost = cost + -(y_train[i]*np.log(y_hat+epsilon)+(1-y_train[i])*np.log(1-y_hat+epsilon))
  cost = cost/m
  return cost 

def gradient_descent(x_train, y_train, params, learning_rate, iterations):
    m = len(y_train)
    cost_history = np.zeros((iterations,1))
    for i in range(iterations):
        params = params - (learning_rate/m) * (np.dot(x_train.T, (sigmoid(np.dot(x_train, params)) - y_train))) 
        cost_history[i] = compute_cost(x_train, y_train, params)
    return (cost_history, params)

def predict(x_test, params):
    return np.round(sigmoid(np.dot(x_test,params)))

# 초기 손실값 plotting
iterations = 100
learning_rate = 0.03
n = np.size(x_train,1)
beta_hat = np.zeros((n,1))
initial_cost = compute_cost(x_train, y_train, beta_hat)
(cost_history, beta_hat) = gradient_descent(x_train, y_train, beta_hat, learning_rate, iterations)
plt.plot(range(len(cost_history)),cost_history,'r')


# 최적화된 parameter를 가지고 test 데이터 예측
y_pred = predict(x_test, beta_hat)
score = float(sum(y_pred == y_test))/ float(len(y_test))
print(score)
