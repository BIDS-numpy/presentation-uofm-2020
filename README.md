# NumPy: A look at the past, present, and future of array computation

Presentation on NumPy to the University of Michigan EECS Department, Jan. 2020.

# Installation

The presentation is in the form of a Jupyter notebook.
[Rise](https://rise.readthedocs.io/en/maint-5.6/) is used to turn the 
notebook into a live presentation. 
There are three steps to making this work: getting an environment set up with 
all of the necessary dependencies, and getting the code/data for the 
Event Horizon Telescope example.

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

### Known issues

* **Error when building `pynfft` wheels from source**

  If installing `pynfft` via `pip install -r requirements.txt`, you will likely
  see a build error complaining about not being able to find dependency
  libraries.
  The wheels must be built from source because those hosted on PyPI are out of
  incompatible with NFFT >= 3.3.
  The build process should continue past the error, ultimately resulting in
  the successful build of `pynfft`.

## Step 2: Getting data and code for the examples

**TL;DR** : `git submodule update --init`

The data and code for most of the examples in the presentation are included
in this repository.
At the very least the code to download necessary data is embedded in the 
presentation itself.
The exception is the data and imaging pipeline for reproducing the Event
Horizon Telescope image of the supermassive black hole at the center of M87.
I've included the imaging pipeline and data from the 
[official Event Horizon Github Organization](https://github.com/eventhorizontelescope)
as submodules of this repository.
In order for the EHT example to work, you must initialized the submodules:
`git submodule update --init`.

# Running/Viewing the presentation

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

### Known issues

 * For whatever reason, figures produced via code in the notebook aren't 
   always visible when they are produced. 
   The hacky-way around this problem is to simply go back a slide then forward
   again.
   Moving between slides seems to trigger a better repositioning of the 
   cell output.
