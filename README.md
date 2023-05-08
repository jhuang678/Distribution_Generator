# PDGenerator: Probability Distribution Generation Python Library Package

## Table of Contents
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
- [Plot Example](#Plot)

## Description
This is the python package for the **PDGenerator** Python library package that allows users to generate random variates from a wide range of probability distributions.  To use the library package, you can download it and import it in any python script without complicated installation process.

The pdGenerator package contains 4 files: 
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
3. Create or open any python script. 
   1. You need an integrated development environment (IDE) which able to run python. Here are some options:
      1. VSCode - https://code.visualstudio.com/
      2. PyCharm - https://www.jetbrains.com/pycharm/
      3. There are many more options.
   2. You may use the provided `GOFTester.py` or `plot.py` to test `PDGenerator.py`.

4. Place PDGenerator.py in the same file with your script and import it in the script. For example: 
```python
import PDGenerator as pdg
```

## How to run it 
Here are all the examples of generate random variant through PDGenerator.
### Set up random seed 
1. Once you have import PDGenerator, first you need to set up a random seed 
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
* n is the number of random variables that been returned.
* a is the lower bound of the uniform random variables.
* b is the upper bound of the uniform random variables.


#### Discrete Uniform
To generate discrete uniform random variables,  run 
```python
pd_generator.disc_unif(n=1, a=0, b=1)
```
* It returns a list of discrete uniform random variables.
* n is the number of random variables that been returned.
* a is the lower bound of the uniform random variables.
* b is the upper bound of the uniform random variables.

#### Triangular
To generate triangular random variables,  run 
```python
pd_generator.triangular(n=1, a=0, b=2, c=1)
```
* It returns a list of triangular random variables.
* n is the number of random variables that been returned.
* a is the lower point of the triangular random variables.
* b is the upper point of the triangular random variables.
* c is the most common point of the triangular random variables. It is optional input. If it is blanked, it will assume that c is (a+b)/2 .


#### Exponential 
To generate exponential random variables,  run 
```python
pd_generator.expo(n=1, lamb=1)
```
* It returns a list of exponential random variables.
* n is the number of random variables that been returned.
* lamb is the rate parameter of the exponential random variables.


#### Weibull
To generate weibull random variables, run 
```python
pd_generator.weibull(n=1, lamb=1, beta=0.9)
```
* It returns a list of weibull random variables.
* n is the number of random variables that been returned.
* lamb is the scale parameter of the weibull random variables.
* beta is the shape parameter of the weibull random variables.

#### Gamma/Erlang-n
To generate gamma random variables, run 
```python
pd_generator.erlang(n=1, m=1, lamb=1)
```
* It returns a list of gamma random variables.
* n is the number of random variables that been returned.
* m is the number of Expo(λ)  which been added.
* lamb is the scale parameter of the gamma random variables.


#### Normal
To generate normal random variables, run 
```python
pd_generator.norm(n=1, mu=0, sigma=1)
```
* It returns a list of normal random variables.
* n is the number of random variables that been returned.
* mu is the mean of the normal distribution.
* sigma is the standard deviation of the normal distribution.


#### Chi-squared 
To generate chi-squared random variables, run 
```python
pd_generator.chi2(n=1, m=1)
```
* It returns a list of chi-squared random variables.
* n is the number of random variables that been returned.
* m is the number of Z^2  which been added.


#### Lognormal 
To generate log normal random variables, run 
```python
pd_generator.lognorm(n=1, mu=0, sigma=1)
```
* It returns a list of log normal random variables.
* n is the number of random variables that been returned.
* mu is the mean of the normal distribution.
* sigma is the standard deviation of the normal distribution.


#### Student's t 
To generate t random variables,  run 
```python
pd_generator.t_student(n=1, m=1)
```
* It returns a list of discrete uniform random variables.
* n is the number of random variables that been returned.
* m is the shape parameter of chi^2.


#### Bernoulli 
To generate Bernoulli  random variables,  run 
```python
pd_generator.bern(n=1, p=0.6)
```
* It returns a list of Bernoulli  random variables.
* n is the number of random variables that been returned.
* p is the the probability of success.

#### Binomial 
To generate Binomial random variables,  run 
```python
pd_generator.bino(n=1, m=2, p=0.6)
```
* It returns a list of Binomial random variables.
* n is the number of random variables that been returned.
* p is the the probability of success.
* m is the number of Bern(p)  which been added.

#### Geometric 
To generate Geometric random variables, run 
```python
pd_generator.geom(n=1, p=0.6)
```
* It returns a list of Geometricrandom variables.
* n is the number of random variables that been returned.
* p is the the probability of success.

#### Negative Binomial 
To generate NegBin random variables, run 
```python
pd_generator.negbin(n=1, m=2, p=0.6)
```
* It returns a list of NegBin  random variables.
* n is the number of random variables that been returned.
* p is the the probability of success.
* m is the number of Geom(p)  which been added.

#### Poisson 
To generate Poisson random variables, run 
```python
pd_generator.pois(n=1, lamb=1)
```
* It returns a list of poisson random variables.
* n is the number of random variables that been returned.
* lamb is the expected value of each time unit.

## Plot

![unif01_unif24](https://user-images.githubusercontent.com/100253011/236730748-ff6c056e-042a-4572-958e-123eb4521373.png)

![dunif25](https://user-images.githubusercontent.com/100253011/236730967-591a46dd-abf6-4846-b429-3508687c8b07.png)

![tri012](https://user-images.githubusercontent.com/100253011/236731034-077bfc44-f68a-4d45-949a-834f0740e429.png)

![tri014](https://user-images.githubusercontent.com/100253011/236731089-2463ccb3-0de8-4d1c-b25c-ab42842a9646.png)

![expo1](https://user-images.githubusercontent.com/100253011/236731099-974139d0-a23d-4eb5-a4e0-cd5bf03a4f80.png)

![expo2](https://user-images.githubusercontent.com/100253011/236731107-daca010e-6ca5-48ee-9818-7393c9c176a7.png)

![weibull](https://user-images.githubusercontent.com/100253011/236731116-70d4a031-1870-41d4-a0e7-5e284e0a0bac.png)

![gamma32](https://user-images.githubusercontent.com/100253011/236731125-b10f7cd4-6a69-441c-af8d-69d551e84c81.png)

![norm64](https://user-images.githubusercontent.com/100253011/236731235-e7eb5b19-1c55-4a44-8187-b9f572cd57e1.png)

![lognorm01](https://user-images.githubusercontent.com/100253011/236731252-fbb06e4f-7878-4715-a94c-6dcf226851da.png)

![chisquared3](https://user-images.githubusercontent.com/100253011/236731299-0de3f489-7e58-4436-9d60-dcac67b56b55.png)

![bern](https://user-images.githubusercontent.com/100253011/236731307-43e1fa8d-ede6-4ac2-af69-c59cdf98d6d6.png)

![bino3](https://user-images.githubusercontent.com/100253011/236731326-441064a3-02d0-4978-a96a-5a2f72d5a881.png)

![geom](https://user-images.githubusercontent.com/100253011/236731346-f18fef50-a043-46cf-97d0-b4c8bc559a1e.png)

![negbin3](https://user-images.githubusercontent.com/100253011/236731364-82c5d44b-6357-49a7-b21c-370bec2401d2.png)

![poisson2](https://user-images.githubusercontent.com/100253011/236731389-8a67ebc2-8607-4fc6-9bca-7301c68e9bfc.png)
