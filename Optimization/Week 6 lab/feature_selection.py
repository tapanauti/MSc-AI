import random
from sklearn.datasets import load_boston
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import mutual_info_regression
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from lahc import LAHC, init, nbr
from ga import GA, tournament_select, uniform_crossover
    
X, y = load_boston(return_X_y=True)
Xtrain, Xtest, ytrain, ytest = train_test_split(X, y, random_state=0)
LR = LinearRegression()

budget = 400
popsize = 20
ngens = budget // popsize


def C(x):
    if sum(x) == 0:
        # all zeros => Xtrain_tmp would be empty
        return 1 # a bad value!

    else:
        # the bitstring x chooses the features among the data X.
        # numpy requires x to be bool, not 0/1, for this.
        x = [bool(xi) for xi in x] 
        Xtrain_tmp = Xtrain[:, x]
        Xtest_tmp = Xtest[:, x]

        # fit and score
        LR.fit(Xtrain_tmp, ytrain)
        return -LR.score(Xtest_tmp, ytest) # R^2 -> larger is better, but we minimis


def Boston_Housing_feature_selection_LAHC(C, L):
    best, Cbest = LAHC(L, budget, C, init, nbr)
    return best

def Boston_Housing_feature_selection_SKLearn(k):
    # solve using SelectKBest as a baseline. it selects the k best
    # features as measured by mutual information between the feature
    # and y (on training data).
    sel = SelectKBest(mutual_info_regression, k=k)
    sel.fit(Xtrain, ytrain)
    Xtrain_tmp = sel.transform(Xtrain)
    Xtest_tmp = sel.transform(Xtest)
    LR.fit(Xtrain_tmp, ytrain)
    print("SelectKBest", k, LR.score(Xtest_tmp, ytest))
