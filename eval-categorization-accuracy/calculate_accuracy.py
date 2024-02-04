from typing import List

from promptflow import log_metric, tool


@tool
def calculate_accuracy(grades: List[str]):
    # calculate accuracy for each variant
    accuracy = round((grades.count("Correct") / len(grades)), 2)
    log_metric("accuracy", accuracy)

    return accuracy
