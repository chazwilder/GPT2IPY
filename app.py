import json


def format_markdown(chunck):
    return {
        "cell_type": "markdown",
        "metadata": {},
        "source": [chunck],
    }


def format_code(chunck):
    return {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [f"{chunck[6:]}"],
    }


def create_cell(chunck):
    if chunck.startswith("python"):
        return format_code(chunck)
    else:
        return format_markdown(chunck)


def process_chunks(chuncks):
    return [create_cell(chunck) for chunck in chuncks]


def format_notebook(chuncks):
    return {
        "cells": process_chunks(chuncks),
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3",
            },
            "language_info": {
                "codemirror_mode": {"name": "ipython", "version": 3},
                "file_extension": ".py",
                "mimetype": "text/x-python",
                "name": "python",
                "nbconvert_exporter": "python",
                "pygments_lexer": "ipython3",
                "version": "3.8.5",
            },
        },
        "nbformat": 4,
        "nbformat_minor": 4,
    }


def md_to_ipynb(md_file, destination_file):
    with open(md_file, "r") as file:
        chuncks = file.read().split("```")
    notebook = format_notebook(chuncks)
    with open(destination_file, "w") as file:
        file.write(json.dumps(notebook))


md_to_ipynb("Lesson2.md", "Lesson2.ipynb")