import numpy as np
from collections import defaultdict


def kfold_split(num_objects, num_folds):
    array = np.arange(num_objects)
    fold_len = num_objects // num_folds
    ans = []
    for i in range(num_folds):
        tmp = np.array(array.copy())
        if i != num_folds - 1:
            ans += [(np.delete(tmp, [_ for _ in range(i*fold_len, (i+1)*fold_len)]), tmp[i*fold_len:(i+1)*fold_len])]
        else:
            ans += [(tmp[:i*fold_len], tmp[i*fold_len:])]
    return ans


def knn_cv_score(X, y, parameters, score_function, folds, knn_class):
    d = {}
    for normalizer_name in parameters['normalizers']:
        for n_neighbors in parameters['n_neighbors']:
            for metric in parameters['metrics']:
                for weight in parameters['weights']:
                    key = (normalizer_name[1], n_neighbors, metric, weight)
                    model = knn_class(n_neighbors=n_neighbors, weights=weight, metric=metric)
                    tmp = []
                    for train, test in folds:
                        x_train, y_train = X[train], y[train]
                        x_test, y_test = X[test], y[test]
                        if not normalizer_name[0] is None:
                            normalizer = normalizer_name[0]
                            normalizer.fit(x_train)
                            x_train = normalizer.transform(x_train)
                            x_test = normalizer.transform(x_test)
                        model.fit(x_train, y_train)
                        predict = model.predict(x_test)
                        tmp += [score_function(y_test, predict)]
                    d[key] = sum(tmp)/len(tmp)
    return d
