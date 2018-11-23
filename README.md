[![Build Status](https://dev.azure.com/ogrisel/text-mining-class/_apis/build/status/ogrisel.text-mining-class?branchName=master)](https://dev.azure.com/ogrisel/text-mining-class/_build/latest?definitionId=1)

# Introduction to web scraping and text mining

This class is meant to teach Data Science students how to work with text data
using tools from the Python ecosystem.

List of topics to be covered in this class:

- Dealing with text data: bytes, charsets and unicode symbols
- Scraping data from online resources
- Bag-of-words and supervised text classification
- Indexing full-text documents
- Clustering: grouping similar text documents
- Unsupervised Latent space models for semantic information retrieval

Some possible topics for future extended versions of this class:

- Word embeddings and supervised text classification with continuous bag of
  words
- Introduction to Knowledge Bases
- Using pre-trained Named entity detection and Semantic role labeling to
  extract knowledge from text
- Sequence to Sequence for machine translation
- Machine Reading

## Getting started

### Install git and clone this repository

Install [git](https://git-scm.com/), clone this repository and change the working
directory to the newly created folder:

    git clone https://github.com/ogrisel/text-mining-class
    cd text-mining-class/

If you forked this repository on github (recommended to be able to do the code
review exercises), you should register your own github fork as a remote
repository:

    git remote add myname https://github.com/myname/text-mining-class
    git remote -v

You should see 2 remote repo: one named "origin" and pointing to
`ogrisel/text-mining-class.git` and the other with your github name and
pointing to your own github fork.

### Install Python and the dependencies

Install Python 3.6 or later. If you have never installed Python before,
you can use the [Anaconda distribution](https://www.anaconda.com/download/).

Open a terminal and check that you can use your newly installed python3 command:

    python3 -V

Make sure that this command points to the location you where you installed
anaconda and not a system installation of Python.

To check where the `python3` command comes from (depending on your `PATH`
environment variable), use one of the following commands:

Under Windows:

    where python3

or under Linux and macOS:

    which python3

You can also do the same for `conda` and later for the `pip` command.

You can alternatively use the following commands:

    python3 -c "import sys; print(sys.executable)"

Finally you can check the configuration of conda with:

    conda info

Then install the project dependencies in a dedicated conda environment named
`tmclass` (see the content of the `environment.yml` file for details:

    conda env create -f environment.yml

Then [activate](https://conda.io/docs/user-guide/tasks/manage-environments.html#activating-an-environment) the `tmclass` conda environment:

Under Windows:

    activate tmclass

or under Linux / macOS:

    source activate tmclass

Alternatively, it is also possible to use a virtualenv and pip instead of
conda. See the end of this file for more details.

### Install the project packages in editable mode

Install the 'text-mining-class-exercises' python package in "editable" mode:

    pip install --editable exercises/

Also install the  'text-mining-class-solutions' python package side-by-side:

    pip install --editable solutions/

At this point it should be possible to run the tests of the solutions and they
should all pass:

    pytest solutions/

On the contrary the tests of the exercises should **not** pass (they are marked
`xfail`):

    pytest exercises/

### Download the datasets and pre-trained models

Some tests require test data to run properly and are skipped if the data is
missing. You can pre-download those datasets with the following command (a few
10s of MB in total).

    python -m tmclass_exercises.data_download

### Configure your code editor

Install [Visual Studio Code (vscode)](https://code.visualstudio.com/)
and the official [Python extension
](https://marketplace.visualstudio.com/items?itemName=ms-python.python).

Open this project folder ("text-mining-class") in the editor.

Make sur to select the `tmclass` conda environment in the bottom left of
the main window. You can switch with `Shitf-Ctrl-P` > `Python: Select
Interpreter`.

Configure you editor to enable the `flake8` linter (code checker)
instead of `pylint` and to run the tests with `pytest`.You can press
`Ctrl-,` to open the user settings editor. Set the following options:

```json
{
    "python.unitTest.pyTestEnabled": true,
    "python.unitTest.pyTestArgs": ["-vv"],
    "python.linting.pylintEnabled": false,
    "python.linting.flake8Enabled": true
}
```

## Doing an exercise

Open the `text-mining-class` folder in your editor. The exercises can be found
in the `exercises/tmclass_exercises/` folder.

Use the `Ctrl-P` command to open the file navigation menu, start to type
"manipulation" and select the open the following file in a new tab:

    exercises/tmclass_exercises/text_manipulation.py

Similarly open a new tab the test file named:

    exercises/tmclass_exercises/tests/test_text_manipulation.py

The first exercises is to implement the function named `code_points` in
`text_manipulation.py`.

Read the instructions in the file and run the first
test for this function:

    pytest -vv -k test_code_points exercises

Alternatively you can use `vscode` to launch the tests. Here are some useful
commands to try in the launch palette `Shift-Ctrl-P`:

- `>Python: Discover Unit Tests`
- `>Python: Run Current Unit Test File`
- `>Python: Run Unit Test Method...`
- `>Python: Debug Unit Test Method...`  (set a break point in the code first)

You can also use `Ctrl-j` to toggle the output view panel.

Notice that the test is marked `xfail`. To actually see the error message,
remove the `@pytest.mark.xfail` for the first test in `text_manipulation.py`
and try again.

Then implement the `code_points` function in `text_manipulation.py` and launch
the first test again and iterate until it passes

Once done, move to the next test. You can run all the tests of given group of
exercises as follows:

    pytest -vv exercises/tmclass_exercises/tests/test_text_manipulation.py

## Exercises overview

TODO:

## Installing with pip / virtualenv instead of conda

Instead of using a conda env and the conda command, it is also possible to use
a virtualenv and install dependencies using pip:

    python3 -m venv tmclass

Then under Windows:

    tmclass/Scripts/activate

or under Linux and macOS:

    source tmclass/bin/activate

Finally, install the dependencies:

    python3 -m pip install -r requirements.txt
