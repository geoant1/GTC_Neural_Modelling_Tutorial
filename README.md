# GTC Neural Modelling Tutorial
This repository contains the assignment for Peter Dayan's MF/MB lecture. In the repository, you will find the following folders:
- `code`. This folder containes the jupyter notebook `assignment.ipynb` which has all the instructions you need for this assignment.
- `envs`. This folder contains environment configuration files for your simulations.
- `papers`. This folder contains pdf files of the papers you will need to read/skim through.
- `slides`. This folder contains the slides for the presentation shown during the tutorial session.

To get started, you can clone this git repository by navigating to whatever folder you want it to be in, then executing the following piece of code in command line:

`git clone https://github.com/geoant1/GTC_Neural_Modelling_Tutorial.git`

Finally, there is also a file named `requirements.txt`. This file can be used to create a virtual conda environment which will also install all the dependencies you need for this assignment. Navigate to the folder containing this file and execute:

`conda create -n <your name> --file requirements.txt && conda activate <your name>`

Note that I'm using linux (as you can see in the `requirements.txt` file). I haven't tested this on other operating systems. If it doesn't work for you then please manually install the necessary packages using `conda` or `pip`. Below is the complete list:

- `numpy`
- `scipy`
- `matplotlib`
- `jupyterlab`

Good luck!
