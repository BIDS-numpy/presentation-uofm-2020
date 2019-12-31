# 1. What is NumPy?
A Python package providing a *data structure* and *algorithms* for efficient numerical computation
 - `ndarray`: A generic, n-dimensional array data structure
 - Efficient implementations of many common numerical algorithms
   * `np.random`: Tools and algorithms for working with random numbers
   * `np.fft`: Fast Fourier transform for linear systems analysis
   * `np.linalg`: Tools for linear algebra
   * ... Many others

Foundational component of scientific python ecosystem:
  - `scipy`, the scikits (`scikit-learn`, scikit-image`), `matplotlib` all use
    the numpy `ndarray` as the basic data structure
  - The array interface has become a de facto standard amongst the wider
    data science community.

Where is NumPy used?
 - To produce the first image of a black hole 
   [Event Horizon Telescope Collaboration](https://github.com/achael/eht-imaging)
 - [To detect the gravitational wave signature from a neutron star merger](https://github.com/gwastro/pycbc)
 - [To discover fundamental particles like the Higgs Boson](https://github.com/cms-sw/cmssw)
   * Also [scikit-hep](https://scikit-hep.org/)
   

### Links/Resources
 - numpy.org (new site by then?)
### Questions
 - How many audience members are python users? Daily users?
 - How many audience members use scipy ecosystem? Daily?

# 2. History of NumPy
 - Mid 90's -> Desire for numerical computation in Python leads to Numeric
 - Early 2000's -> T. Oliphant adds packages build on top of Numeric array
 - 2001 -> SciPy project to unify above efforts in dev of scientific libs in 
   python
 - Early adopters include Space Telescope Science Institute (STScI) - Hubble folks
   - Specific needs result in development of Numarray package
 - 2005 -> Numeric & Numarray unified to become Numpy
 - N.b. originally called scipy.core (i.e. foundational component)
 - 2006 -> NumPy vers. 1.0
### Links/Resources
 - [Scipy paper](https://arxiv.org/pdf/1907.10121.pdf)
 - [Numeric/NumPy for Hubble](https://conference.scipy.org/scipy2011/slides/greenfield_keynote_astronomy.pdf)
 
# 3. Ultrabrief overview of some numpy features
 - ndarray
   - vectorization
   - brodcasting
   - views
     * basic/advanced indexing
   - flexible typing system
 - libraries of methods for common numerical tasks
   - np.random - random number generation
   - np.linalg - routines for linear algebra
   - np.fft    - discrete fourier transform

### Examples
 * Apollo image denoising example from elegant scipy

# 4. NumPy Now
 - Show packages that depend on numpy
   - Scientific python ecosystem
   - Data science/AI libraries
   - TODO: Find research projects @ UM

# NumPy Future

 - Community-driven project: the community decides where NumPy goes
   * mailing list
   * slack
   * github
   * bi-weekly community meetings
 - Mentorship program?

### Resources
 - [Preparing for next decade](https://www.slideshare.net/RalfGommers/inside-numpy-preparing-for-the-next-decade)
 - [NumPy/SciPy What's Now](https://www.slideshare.net/RalfGommers/pydata-nyc-whatsnew-numpyscipy-2019)

 
# 5. Acknowledgements
 - Sloan (ask Stefan for wiki link to grant strings)
 
### TODO
 - GH label for *semester project*?
