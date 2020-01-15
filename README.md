# NumPy: A look at the past, present, and future of array computation

Presentation on NumPy to the University of Michigan EECS Department, Jan. 2020.

# Running the notebook

The presentation is in the form of a Jupyter notebook.
[Rise](https://rise.readthedocs.io/en/maint-5.6/) is used to turn the 
notebook into a live presentation. 
There are two steps to making this work: getting an environment set up with 
all of the necessary dependencies, then running the slide show.

## Step 1: Setting up the environment

Start by installing all of the dependencies for the presentation using your 
preferred environment manager (`virtualenv`, `conda`, etc.).
The dependencies are listed in `requirements.txt`.

### Detailed instructions

If you don't have a favorite environment manager, use python's builtin
`venv` module:

```bash
mkdir -p venv/presentation
python -m venv venv/presentation
```

Once the environment has been created, enter it with:

```bash
source venv/presentation/bin/activate
# The following isn't necessary, but will suppress warnings if you happen to
# be using an older version of `pip`
pip install --upgrade pip
```

Now, finally, install the dependencies:

```bash
pip install -r requirements.txt
```

## Step 2: Viewing the presentation

Launch `jupyter notebook` in the top-level directory and open 
`presentation.ipynb` in the browser.
Use `alt+r` to toggle between "presentation mode" and the traditional
notebook view.
When in "presentation mode", use `spacebar` to navigate forward and 
`shift+spacebar` to navigate backwards.
More advanced navigation commands can be found in the
[Rise documentation](https://rise.readthedocs.io/en/maint-5.6/) or by clicking
on the help button (question mark in the lower-left corner of the slides) when
in presentation mode.
