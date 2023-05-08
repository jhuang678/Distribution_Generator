# PDGenerator: Probability Distribution Generation Python Library Package
## Description
This is the python package for the **PDGenerator** Python library package that allows users to generate random variates from a wide range of probability distributions.  To use the library package, you can download it and import it in any python script without complicated installation process.

The pdGenerator package contains 4 files: 
1. PDGenerator.py
   1. Generate more than 15 types of random variables quickly and efficiently
   2. Require library:`math`.


2. GOFTester.py
   1. Contains goodness-of-fit tests for each type of random variable generated from PDGenerator.py.
   2. Require library:`numpy`, `scipy`.


3. plot.py
   1. Provides histograms from the random variables generated from PDGenerator.py.
   2. Require library:`numpy`, `scipy`, and `matplotlib`.


4. README.md.

## Installation
1. Download the zip file.

2. Install any library that you don't have in your environment 
```commandline
pip install math
pip install numpy
pip install scipy
pip install matplotlib
```
3. Create or open any python script. 
   1. You need an integrated development environment (IDE) which able to run python. Here are some options:
      1. VSCode - https://code.visualstudio.com/
      2. PyCharm - https://www.jetbrains.com/pycharm/
      3. There are many more options.
   2. You may use the provided `GOFTester.py` or `plot.py` to test `PDGenerator.py`.

4. Place PDGenerator.py in the same file with your script and import it in the script. For example: `import PDGenerator as pdg`

## How to run it 
Here are all the examples of generate random variant through PDGenerator.
### Set up random seed 
1. Once you have import PDGenerator, first you need to set up a random seed 
by code `pd_generator = pdg.PDGenerator(seed=int)`
   1. You may input any integer for the seed.
2. Then you are good to generate any random variant. 
### Examples
#### Uniform
To generate uniform random variables,  run `pd_generator.unif(n=1, a=0, b=1)`
* It returns a list of uniform random variables.
* n is the number of random variables that been returned.
* a is the lower bound of the uniform random variables.
* b is the upper bound of the uniform random variables.


#### Discrete Uniform
To generate discrete uniform random variables,  run `pd_generator.disc_unif(n=1, a=0, b=1)`
* It returns a list of discrete uniform random variables.
* n is the number of random variables that been returned.
* a is the lower bound of the uniform random variables.
* b is the upper bound of the uniform random variables.

#### Triangular
To generate triangular random variables,  run `pd_generator.triangular(n=1, a=0, b=2, c=1)`
* It returns a list of triangular random variables.
* n is the number of random variables that been returned.
* a is the lower point of the triangular random variables.
* b is the upper point of the triangular random variables.
* c is the most common point of the triangular random variables. It is optional input. If it is blanked, it will assume that c is (a+b)/2 .


#### Exponential 
To generate exponential random variables,  run `pd_generator.expo(n=1, lamb=1)`
* It returns a list of exponential random variables.
* n is the number of random variables that been returned.
* lamb is the rate parameter of the exponential random variables.


#### Weibull
To generate weibull random variables, run `pd_generator.weibull(n=1, lamb=1, beta=0.9)`
* It returns a list of weibull random variables.
* n is the number of random variables that been returned.
* lamb is the scale parameter of the weibull random variables.
* beta is the shape parameter of the weibull random variables.


#### Gamma/Erlang-n
To generate gamma random variables, run `pd_generator.erlang(n=1, m=1, lamb=1)`
* It returns a list of gamma random variables.
* n is the number of random variables that been returned.
* m is the number of Expo(λ)  which been added.
* lamb is the scale parameter of the gamma random variables.


#### Normal
To generate normal random variables, run `pd_generator.norm(n=1, mu=0, sigma=1)`
* It returns a list of normal random variables.
* n is the number of random variables that been returned.
* mu is the mean of the normal distribution.
* sigma is the standard deviation of the normal distribution.


#### Chi-squared 
To generate chi-squared random variables, run `pd_generator.chi2(n=1, m=1)`
* It returns a list of chi-squared random variables.
* n is the number of random variables that been returned.
* m is the number of Z^2  which been added.


#### Lognormal 
To generate log normal random variables, run `pd_generator.lognorm(n=1, mu=0, sigma=1)`
* It returns a list of log normal random variables.
* n is the number of random variables that been returned.
* mu is the mean of the normal distribution.
* sigma is the standard deviation of the normal distribution.


#### Student's t 
To generate t random variables,  run `pd_generator.t_student(n=1, m=1)`
* It returns a list of discrete uniform random variables.
* n is the number of random variables that been returned.
* m is the shape parameter of chi^2.



#### Bernoulli 
To generate Bernoulli  random variables,  run `pd_generator.bern(n=1, p=0.6)`
* It returns a list of Bernoulli  random variables.
* n is the number of random variables that been returned.
* p is the the probability of success.


#### Binomial 
To generate Binomial random variables,  run `pd_generator.bino(n=1, m=2, p=0.6)`
* It returns a list of Binomial random variables.
* n is the number of random variables that been returned.
* p is the the probability of success.
* m is the number of Bern(p)  which been added.


#### Geometric 
To generate Geometric random variables, run `pd_generator.geom(n=1, p=0.6)`
* It returns a list of Geometricrandom variables.
* n is the number of random variables that been returned.
* p is the the probability of success.


#### Negative Binomial 
To generate NegBin random variables, run `pd_generator.negbin(n=1, m=2, p=0.6)`
* It returns a list of NegBin  random variables.
* n is the number of random variables that been returned.
* p is the the probability of success.
* m is the number of Geom(p)  which been added.


#### Poisson 
To generate poisson random variables, run `pd_generator.pois(n=1, lamb=1)`
* It returns a list of poisson random variables.
* n is the number of random variables that been returned.
* lamb is the expected value of each time unit.


## Plot Example
