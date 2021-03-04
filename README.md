# Class Materials

Hi!

This is the repository to find all everything about data visualization. You will find tutorials we did in the class, class notes, python files, etc.

The content of this repository will be updated between **March 1st to May 22nd, 2021**, on a weekly basis.

### Contents

The content on this repository is organized based on the topic. 

| Directory                                        | Description                                                                                                                            |
| -------                                          | -------------------------------------------------------------------------------------------------------------------------------------- |
| [contents/python-warmup](contents/python-warmup) | Functions, classes, decorators and more                                                                                                |
| Upcoming...                                      | VAD Chapter 1. What's Vis, and Why Do It?                                                                                              |
| Upcoming...                                      | Theoretical Intro (Types of Charts, etc.) and Viz with Python 1 (matplotlib, pandas, seaborn)                                          |
<!-- |                                                  | VAD Chapter 2. What: Data Abstraction, Chapter 3. Why: Task Abstraction and Viz with Python 2 (plotly, bokeh, networkx)                |
|                                                  | VAD Chapter 4. Validation, Chapter 5. Marks and Channels, Chapter 6. Rules of Thumb, Visualization Tools (Tableau, Qlik, Lookup, etc.) |
|                                                  | VAD Chapter 7. Arrange Tables, Chapter 10. Map Color and Other Channels, Tableau 1                                                     |
|                                                  | VAD Chapter 8. Arrange Spatial Data, Chapter 9. Arrange Networks, Tableau 2                                                            |
|                                                  | Midterm (VAD Chapters), FP Session 1                                                                                                   |
|                                                  | Solving all assignments in class, FP Session 2                                                                                         |
|                                                  | Tableau 3, FP Session 3                                                                                                                |
|                                                  | Tableau 4, FP Session 4                                                                                                                |
|                                                  | Final Project Presentations, What's Next                                                                                               | -->

### How to use this Repository?

You should do the following while going over this repository.

1. Download this repository to your local machine using `git clone https://github.com/spu-dataviz-211/class-materials.git`.
2. Download python 3 from [python.org](https://www.python.org/), if you don't have python already on your computer.
3. [Create a virtual environment](#how-to-create-a-new-virtual-environment) and activate this environment everytime you need to use it.
4. Install [requirements.txt](requirements.txt) file using `pip install -r requirements.txt`.
5. That's it. 

Following are the recommendations.

6. Read the README file for each section.
7. For some sections, there will be `Examples.ipynb` and `Examples-Solutions.ipynb` files. These will have some examples, and their solutions on the related topic.
8. There will also be `Notes.ipynb`, which may have some more content about the topic.
9. Follow up with the assignments to practice more.

### How to create a new Virtual Environment?

Environment is a container for your application to run isolated with safely and without interrupting any other existing applications in the same machine.

Make sure you have python installed on your system.

```
python --version; pip --version
```

To create a virtual environment, you need a virtual environment manager. By default, python comes up with [venv](https://docs.python.org/3/library/venv.html) module. There are more modules like [virtualenv](https://virtualenv.pypa.io/en/latest/), etc.

In below command, using python, you are invoking `venv` module to create a new virtual environment folder with name `.venv`, in the current directory that you are in.

``` sh
python -m venv .venv
```

To activate the environment, you do the following.

``` ps
# on windows
 me@MacBook-Pro ~ .\.venv\Scripts\Activate

# on mac
 me@MacBook-Pro ~ source .venv/bin/activate

# your console will change to this
(.venv) me@MacBook-Pro ~ 
```

### Instructor's Note

All topics will be shared in here. Please review the content and course materials in here first. If you still have questions, please feel free to reach me by email or from GitHub at @metinsenturk.
