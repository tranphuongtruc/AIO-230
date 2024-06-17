# EXERCISE 1
import random
import math


def classify_model_by_f1_score(tp, fp, fn):
    # Checking if tp and fp and fn are int
    if isinstance(tp, int):
        print('tp must be int')
    if isinstance(fp, int):
        print('fp must be int')
    if isinstance(fn, int):
        print('fn must be int')
        exit()

    # Checking if tp and fp and fn are greater than zero
    if tp <= 0 or fp <= 0 or fn <= 0:
        print('tp and fp and fn must be greater than zero')
        exit()

    # Classifying process
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    f1_score = 2 * ((precision * recall) / (precision + recall))
    print(f'precision is {precision}')
    print(f'recall is {recall}')
    print(f'f1-score is {f1_score}')
# classify_model_by_f1_score(tp =2 , fp =3 , fn =4)


# EXERCISE 2

# Given

def is_number(n):
    try:
        float(n)    # Type - casting the string to ‘float ‘.
        # If string is not a valid ‘float ‘ ,
        # it ’ll raise ‘ValueError ‘ exception
    except ValueError:
        return False
    return True


def sigmoid(x):
    return 1 / (1 + math.e ** -x)


def relu(x):
    if x <= 0:
        return 0
    else:
        return x


def elu(x):
    if x <= 0:
        return 0.01 * (math.e ** x - 1)
    else:
        return x


def activation_function():
    # Checking if x is a number
    x = input()
    if not is_number(x):
        print('x must be a number')
        exit()
    x = float(x)

    # Processing
    reply = input(
        'Activation Function ( sigmoid | relu | elu ): ').strip().lower()
    if reply == 'sigmoid':
        print(f'sigmoid: f({x}) = {sigmoid(x)}')
    elif reply == 'relu':
        print(f'relu: f({x}) = {relu(x)}')
    elif reply == 'elu':
        print(f'elu: f({x}) = {elu(x)}')
    else:
        print(f'{reply} is not supported')

# activation_function()


# EXCERISE 3


def mae(n):
    total = 0
    for i in range(n):
        predict = random.uniform(0.0, 10.0)
        target = random.uniform(0.0, 10.0)
        loss = abs(target - predict)
        total += loss
        print(f'loss name: MAE, sample: {i}, pred: {
              predict}, target: {target}, loss: {loss}')
    print(f'final MAE {(1/n) * total}')


def mse(n):
    total = 0
    for i in range(n):
        predict = random.uniform(0.0, 10.0)
        target = random.uniform(0.0, 10.0)
        loss = (target - predict) ** 2
        total += loss
        print(f'loss name: MSE, sample: {i}, pred: {
              predict}, target: {target}, loss: {loss}')
    print(f'final MSE {(1/n) * total}')


def rmse(n):
    total = 0
    for i in range(n):
        predict = random.uniform(0.0, 10.0)
        target = random.uniform(0.0, 10.0)
        loss = (target - predict) ** 2
        total += loss
        print(f'loss name: RMSE, sample: {i}, pred: {
              predict}, target: {target}, loss: {loss}')
    print(f'final RMSE: {math.sqrt((1/5) * total)}')


def regression_loss():
    # Checking if n is an integer number
    n = input()
    if not n.isnumeric():
        print('number of samples must be an integer number')
        exit()
    n = int(n)

    reply = input('Loss name ( MAE | MSE | RMSE ): ').strip().upper()
    if reply == 'MAE':
        mae(n)
    elif reply == 'MSE':
        mse(n)
    elif reply == 'RMSE':
        rmse(n)

# regression_loss()

# EXCERISE 4


def factorial(n):
    answer = 1
    for i in range(n, 0, -1):
        answer *= i
    return answer


def approx_sin(x, n):
    answer = 0
    for i in range(n + 1):
        giai_thua = factorial(2 * i + 1)
        answer += (-1)**i * ((x ** (2 * i + 1)) / giai_thua)
    print(answer)
# approx_sin(x = 3.14, n = 10)


def approx_cos(x, n):
    answer = 0
    for i in range(n + 1):
        giai_thua = factorial(2 * i)
        answer += (-1)**i * ((x ** (2 * i)) / giai_thua)
    print(answer)
# approx_cos(x =3.14 , n =10)


def approx_sinh(x, n):
    answer = 0
    for i in range(n + 1):
        giai_thua = factorial(2 * i + 1)
        answer += (x ** (2 * i + 1)) / giai_thua
    print(answer)
# approx_sinh(x =3.14 , n =10)


def approx_cosh(x, n):
    answer = 0
    for i in range(n + 1):
        giai_thua = factorial(2 * i)
        answer += (x ** (2 * i)) / giai_thua
    print(answer)
# approx_cosh(x =3.14 , n =10)

# EXCERISE 5


def md_nre(y, y_hat, n, p):
    print((y ** (1/n) - y_hat ** (1/n)) ** p)
