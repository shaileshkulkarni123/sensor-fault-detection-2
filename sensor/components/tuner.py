import logging
import sys

from sensor.exception import SensorException
from sensor.utils.main_utils import MainUtils
from sensor.utils.read_params import read_params


logger = logging.getLogger(__name__)


class ModelFinder:
    def __init__(self):
        self.config = read_params()

        self.utils = MainUtils()

    def get_trained_models(self, X_data, Y_data):

        logger.info("Entered the get_trained_models method of ModelFinder class")

        try:
            models_list = list(self.config["train_model"].keys())

            logger.info("Got model list from the config file")

            x_train, y_train, x_test, y_test = (
                X_data[:, :-1],
                X_data[:, -1],
                Y_data[:, :-1],
                Y_data[:, -1],
            )

            tuned_model_list = [
                (
                    self.utils.get_tuned_model(
                        model_name, x_train, y_train, x_test, y_test,
                    )
                )
                for model_name in models_list
            ]

            logger.info("Got trained model list")

            logger.info("Exited the get_trained_models method of ModelFinder class")
            return tuned_model_list

        except Exception as e:
            raise SensorException(e, sys) from e
