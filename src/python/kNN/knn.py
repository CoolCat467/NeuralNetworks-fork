"""knn.py

This module provides a class-based implementation of the k-Nearest Neighbors
(k-NN) algorithm for both classification and regression tasks, using the
scikit-learn library. The k-NN model can be trained, used for predictions, and
evaluated using this module.
"""

from sklearn.metrics import accuracy_score, mean_squared_error
from sklearn.neighbors import KNeighborsClassifier, KNeighborsRegressor


class KNearestNeighbors:
    """
    Implements the k-Nearest Neighbors (k-NN) algorithm for both classification
    and regression tasks.

    This class provides methods to train the model, make predictions, and
    evaluate the model's performance. The evaluation methods are designed
    separately for classification and regression tasks.
    """

    def __init__(self, k, problem_type="classification") -> None:
        """
        Initializes the KNearestNeighbors class with a specified number of
        neighbors (k).

        Args:
            k (int): The # of neighbors to use for predictions in k-NN algorithm.
            problem_type (str): The type of problem to solve.
                It can be either 'classification' or 'regression'.
        """
        if problem_type == "classification":
            self.knn = KNeighborsClassifier(n_neighbors=k)
        elif problem_type == "regression":
            self.knn = KNeighborsRegressor(n_neighbors=k)
        else:
            raise ValueError(
                "Invalid problem_type. Expected 'classification' or 'regression'."
            )

    @property
    def is_trained(self) -> bool:
        """
        Checks if the model has been trained.

        Returns:
            bool: True if the model has been trained, False otherwise.
        """
        return hasattr(f"{self.knn} _fit_method")

    def train(self, var_x, var_y):
        """
        Fits the k-NN model to the training data.

        Args:
            var_x (array-like): Training data, where n_samples is
                the number of samples and n_features is the number of features.
            var_y (array-like): Target values for the training data.
        """
        self.knn.fit(var_x, var_y)

    def predict(self, var_x):
        """
        Uses the trained k-NN model to make predictions on the provided data.

        Args:
            var_x (array-like): The input data to make predictions on.

        Returns:
            array: The predicted values for the input data.
        """
        return self.knn.predict(var_x)

    def evaluate_classification(self, var_x_test, y_test):
        """
        Evaluates the performance of the k-NN model on a test dataset for
        classification tasks.

        The performance is measured using the accuracy score.

        Args:
            X_test (array-like): The test data to evaluate the model on.
            y_test (array-like): The true classes for the test data.

        Returns:
            float: The accuracy score of the model on the test data.
        """
        y_pred = self.predict(var_x_test)
        return accuracy_score(y_test, y_pred)


    def evaluate_regression(self, var_x_test, var_y_tst):
        """
        Evaluates the performance of the k-NN model on a test dataset for
        regression tasks.

        The performance is measured using the mean squared error.

        Args:
            X_test (array-like): The test data to evaluate the model on.
            y_test (array-like): The true values for the test data.

        Returns:
            float: The mean squared error of the model on the test data.
        """
        y_pred = self.predict(var_x_test)
        return mean_squared_error(var_y_tst, y_pred)


    def compute_distances(self, var_x, return_distance=True):
        """
        Computes distances to the nearest neighbors

        Args:
            var_x (array-like): The input data to compute distances from.
            return_distance (bool): If True, returns distances,
                else returns indices of the neighbors.

        Returns:
            array: The distances or indices to the neighbors for each point
                in the input data.
        Raises:
            ValueError: If the model is not yet trained error is returned
        """
        if not self.is_trained:
            raise ValueError("Model is not trained yet.")

        if return_distance:
            distances, _ = self.knn.kneighbors(var_x)
            return distances
        else:
            _, indices = self.knn.kneighbors(var_x)
            return indices
