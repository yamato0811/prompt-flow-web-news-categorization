from promptflow import tool


@tool
def grade(groundtruth: str, prediction: str):
    return "Correct" if groundtruth == prediction else "Incorrect"
