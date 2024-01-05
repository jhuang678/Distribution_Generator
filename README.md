# PDGenerator: Probability Distribution Generation Python Library Package

## Table of Contents
- [Abstract](#abstract)
- [Description](#description)
- [Installation](#installation)
- [How to run it](#how-to-run-it)
   - [Set up random seed](#set-up-random-seed)
   - [Examples](#examples)
      - [Uniform](#uniform)
      - [Discrete Uniform](#discrete-uniform)
      - [Triangular](#triangular)
      - [Exponential](#exponential)
      - [Weibull](#weibull)
      - [Gamma/Erlang-n](#gammaerlang-n)
      - [Normal](#normal)
      - [Chi-squared](#chi-squared)
      - [Lognormal](#lognormal)
      - [Student's t](#lognormal)
      - [Bernoulli](#Bernoulli)
      - [Binomial](#Binomial)
      - [Geometric](#Geometric)
      - [Negative Binomial](#Geometric)
      - [Poisson](#Poisson)
- [Conclusion](#conclusion)
- [Reference](#reference)

## Abstract

RVGenerator is a Python library package that allows users to generate random variates from a wide range of probability distributions. With support for over 15 distributions, including Uniform(a,b), Triangular(a,b,c), Exponential(λ), Weibull (λ, β), Gamma(α,λ)/Erlang_n (λ), Chi-squared(n), Normal (μ, σ^2), Lognormal(µ,σ^2), Student's t(n), Bernoulli(p), Binomial(n,p), Geometric(p), Poisson (λ), RVGenerator is a versatile tool for simulation and modeling tasks in engineering and science. 

To ensure accuracy and reliability, the library uses well-established methods for generating pseudo-random variants and applying the Inverse Transform Theorem and Convolution Method to generate other distributed random variates. These methods are described in detail in *Simulation Modeling and Analysis, 5th (Law, 2015)* [1]. 

Additionally, all distributions in RVGenerator have been thoroughly tested using rigorous goodness of fit tests, including Chi-squared and Kolmogorov-Smirnov tests, and have passed with a 95% confidence level, confirming that the generated data conforms to the distribution defined by the user. 

Overall, RVGenerator is a valuable resource for anyone seeking to generate random variates from a range of probability distributions, with reliable results that have been rigorously tested and validated.

## Description
This is the Python package for the **PDGenerator** Python library package that allows users to generate random variates from a wide range of probability distributions.  To use the library package, you can download it and import it in any Python script without a complicated installation process.

The PDGenerator package contains 4 files: 
1. PDGenerator.py
   1. Generate more than 15 types of random variables quickly and efficiently
   2. Require library: `math`.

2. GOFTester.py
   1. Contains goodness-of-fit tests for each type of random variable generated from PDGenerator.py.
   2. Require library: `numpy`, `scipy`.

3. plot.py
   1. Provides histograms from the random variables generated from PDGenerator.py.
   2. Require library: `numpy`, `scipy`, and `matplotlib`.

4. README.md.

## Installation
1. Download the zip file.

2. Install any library that you don't have in your environment 
```sh
pip install math
pip install numpy
pip install scipy
pip install matplotlib
```
3. Create or open any Python script. 
   1. You need an integrated development environment (IDE) which able to run Python. Here are some options:
      1. VSCode - https://code.visualstudio.com/
      2. PyCharm - https://www.jetbrains.com/pycharm/
      3. There are many more options.
   2. You may use the provided `GOFTester.py` or `plot.py` to test `PDGenerator.py`.

4. Place PDGenerator.py in the same file as your script and import it into the script. For example: 
```python
import PDGenerator as pdg
```

## How to run it 
Here are all the examples of generating random variants through PDGenerator.
### Set up random seed 
1. Once you have imported PDGenerator, you first need to set up a random seed 
by code 
```python
pd_generator = pdg.PDGenerator(seed=int)
```
   1. You may input any integer for the seed.
2. Then you are good to generate any random variant. 
### Examples
#### Uniform
To generate uniform random variables,  run 
```python
pd_generator.unif(n=1, a=0, b=1)
```
* It returns a list of uniform random variables.
* n is the number of random variables that have been returned.
* a is the lower bound of the uniform random variables.
* b is the upper bound of the uniform random variables.

<img src="unif01_unif24.png" alt="hist" width="500"/>


#### Discrete Uniform
To generate discrete uniform random variables,  run 
```python
pd_generator.disc_unif(n=1, a=0, b=1)
```
* It returns a list of discrete uniform random variables.
* n is the number of random variables that have been returned.
* a is the lower bound of the uniform random variables.
* b is the upper bound of the uniform random variables.

<img src="dunif25.png" alt="hist" width="500"/>

#### Triangular
To generate triangular random variables,  run 
```python
pd_generator.triangular(n=1, a=0, b=2, c=1)
```
* It returns a list of triangular random variables.
* n is the number of random variables that have been returned.
* a is the lower point of the triangular random variables.
* b is the upper point of the triangular random variables.
* c is the most common point of the triangular random variables. It is the optional input. If it is blanked, it will assume that c is (a+b)/2.

<img src="tri012.png" alt="hist" width="500"/>

<img src="tri014.png" alt="hist" width="500"/>

#### Exponential 
To generate exponential random variables,  run 
```python
pd_generator.expo(n=1, lamb=1)
```
* It returns a list of exponential random variables.
* n is the number of random variables that have been returned.
* lamb is the rate parameter of the exponential random variables.

<img src="expo1.png" alt="hist" width="500"/>

<img src="expo2.png" alt="hist" width="500"/>

#### Weibull
To generate weibull random variables, run 
```python
pd_generator.weibull(n=1, lamb=1, beta=0.9)
```
* It returns a list of Weibull random variables.
* n is the number of random variables that have been returned.
* lamb is the scale parameter of the Weibull random variables.
* beta is the shape parameter of the Weibull random variables.

<img src="weibull.png" alt="hist" width="500"/>

#### Gamma/Erlang-n
To generate gamma random variables, run 
```python
pd_generator.erlang(n=1, m=1, lamb=1)
```
* It returns a list of gamma random variables.
* n is the number of random variables that have been returned.
* m is the number of Expo(λ)  which been added.
* lamb is the scale parameter of the gamma random variables.

<img src="gamma32.png" alt="hist" width="500"/>

#### Normal
To generate normal random variables, run 
```python
pd_generator.norm(n=1, mu=0, sigma=1)
```
* It returns a list of normal random variables.
* n is the number of random variables that have been returned.
* mu is the mean of the normal distribution.
* sigma is the standard deviation of the normal distribution.

<img src="norm64.png" alt="hist" width="500"/>

#### Chi-squared 
To generate chi-squared random variables, run 
```python
pd_generator.chi2(n=1, m=1)
```
* It returns a list of chi-squared random variables.
* n is the number of random variables that have been returned.
* m is the number of Z^2  which been added.

<img src="chisquared3.png" alt="hist" width="500"/>

#### Lognormal 
To generate log normal random variables, run 
```python
pd_generator.lognorm(n=1, mu=0, sigma=1)
```
* It returns a list of log-normal random variables.
* n is the number of random variables that have been returned.
* mu is the mean of the normal distribution.
* sigma is the standard deviation of the normal distribution.


<img src="lognorm01.png" alt="hist" width="500"/>

#### Student's t 
To generate t random variables,  run 
```python
pd_generator.t_student(n=1, m=1)
```
* It returns a list of discrete uniform random variables.
* n is the number of random variables that have been returned.
* m is the shape parameter of chi^2.


#### Bernoulli 
To generate Bernoulli  random variables,  run 
```python
pd_generator.bern(n=1, p=0.6)
```
* It returns a list of Bernoulli  random variables.
* n is the number of random variables that have been returned.
* p is the probability of success.

<img src="bern.png" alt="hist" width="500"/>

#### Binomial 
To generate Binomial random variables,  run 
```python
pd_generator.bino(n=1, m=2, p=0.6)
```
* It returns a list of Binomial random variables.
* n is the number of random variables that have been returned.
* p is the probability of success.
* m is the number of Bern(p)  which been added.

<img src="bino3.png" alt="hist" width="500"/>

#### Geometric 
To generate Geometric random variables, run 
```python
pd_generator.geom(n=1, p=0.6)
```
* It returns a list of geometric random variables.
* n is the number of random variables that have been returned.
* p is the probability of success.

<img src="geom.png" alt="hist" width="500"/>


#### Negative Binomial 
To generate NegBin random variables, run 
```python
pd_generator.negbin(n=1, m=2, p=0.6)
```
* It returns a list of NegBin  random variables.
* n is the number of random variables that have been returned.
* p is the the probability of success.
* m is the number of Geom(p)  which been added.

<img src="negbin3.png" alt="hist" width="500"/>

#### Poisson 
To generate Poisson random variables, run 
```python
pd_generator.pois(n=1, lamb=1)
```
* It returns a list of poisson random variables.
* n is the number of random variables that have been returned.
* lamb is the expected value of each time unit.

<img src="poisson2.png" alt="hist" width="500"/>

## Conclusion
Random variable generation is a crucial area of study with applications in numerous fields ranging from simulation and engineering to computer science, finance, physics, and healthcare. The RVGenerator package provides a convenient solution to generate various types of random variables. The package has been optimized for efficient and fast execution, and its performance has been validated through various goodness-of-fit tests. Although the RVGenerator package has achieved satisfactory results, there is always room for improvement. For example, it would be beneficial to conduct stability time tests for each random variant, perform additional goodness-of-fit tests, and complete the Negative Binomial test function. Nonetheless, RVGenerator provides an excellent starting point for generating random variables and can be an asset for researchers and practitioners alike.

## REFERENCE

- Law, A. M. (2015). Simulation modeling and analysis (5th Edition). New York: McGraw-Hill. [\[1\]](https://www.mcgrawhill.ca/)
- Mersenne Twister: A 623-Dimensionally Equidistributed Uniform Pseudo-Random Number Generator [\[2\]](https://dl.acm.org/doi/pdf/10.1145/272991.272995)
- Mersenne Twister [\[3\]](https://en.wikipedia.org/wiki/Mersenne_Twister)
- NumPy. (2022). Retrieved 1 April 2022 [\[4\]](https://numpy.org/)
- SciPy.org — SciPy.org. (2022). Retrieved 1 April 2022 [\[5\]](https://www.scipy.org/)
- Matplotlib: Python plotting — Matplotlib. (2022). Retrieved 1 April 2022 [\[6\]](https://matplotlib.org/)
