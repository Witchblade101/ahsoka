# ahsoka

Developing a pipeline for JWST near-IR transiting exoplanet data

Mostly steps adapted from existing pipelines

## Installation

Clone the repository:  
`git clone https://github.com/Witchblade101/ahsoka`  

Install ahsoka:  
`cd ahsoka`  
`pip install .`

Install in Develop Mode
`pip install -e .`

## Note

The core of Ahsohka is the [JWST Calibration pipeline](https://github.com/spacetelescope/jwst). Recent versions of the pipeline have changed how it handles 'bad' pixels, to mixed reviews. If you install Ahsoka using python 3.9 or 3.10 it will use the JWST pipeline with the old behavior (flagged pixels are set to 0). If you install Ahsoka with python 3.11 it will use the new behavior (flagged pixels are set to NaN).
