#  Ubuntu 22.04.1 LTS

### Python 3.10.6 or higher

 Open terminal with keyboard shortcut  Ctrl+Alt+T



## Downloading files
```sh
git clone git@github.com:zmitsek/Python_BI_2022.git
```
Then go to the directory with the script
```sh
cd Python_BI_2022/
git checkout hw_numpy
cd hw_numpy/
```
## Creating and activating environment
```sh
python -m venv venv
```
```sh
source venv/bin/activate
```

## Installing packages
```sh
pip install --upgrade pip
```
```sh
pip install -r requirements.txt
```



### The file numpy_challenge.py contains some examples of arrays creation and several functions for working with numpy arrays:
* matrix_multiplication - multiplies two matrices
* multiplication_check - return TRUE if it's possible to multiply matrices
* multiply_matrices - works like matrix_multiplication, but with list of matrices
* compute_2d_distance_complement - return the euclidean distance between two vectors in 2D space
* compute_multidimensional_distance - works like previous function
* compute_pair_distances - calculates and returns pair distances of rows from input matrix
