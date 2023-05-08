import PDGenerator as pdg
import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy.stats import chi2, norm, normaltest, kstest, expon, triang, uniform, chisquare, gamma, erlang, lognorm, ttest_1samp, nbinom, weibull_min, geom, poisson
from scipy.special import comb

# Define the function for the expected line
def expected_triangular(x, a, b, c):
    if x < c:
        return 2*(x-a) / ((b-a)*(c-a))
    else:
        return 2*(b-x) / ((b-a)*(b-c))

if __name__ == '__main__':

    # Set up random seed
    pd_generator = pdg.PDGenerator(seed=3)

    # Generate 10,000 random numbers and store them in a list
    unif_data = pd_generator.unif(n=100000)
    plt.hist(unif_data, bins=100,   density=True, label='Generated Data Unif(0,1)')
    x = np.linspace(0, 1, 1000)
    y = np.ones_like(x)
    plt.plot(x, y, color='r', linestyle='--', lw=2, alpha=0.5, label='Expected Distribution 1')
    plt.grid(alpha=0.5)

    # Generate 10,000 random numbers from 2 to 4 and store them in a list
    unif_2_4_data = pd_generator.unif(n=100000, a=2, b=4 )
    plt.hist(unif_2_4_data, bins=100, alpha=0.5, density=True, label='Generated Data Unif(2,4)')
    x = np.linspace(2, 4, 1000)
    y = np.ones_like(x)/(4-2)
    plt.plot(x, y, color='r', linestyle='--', lw=2, alpha=0.5, label='Expected Distribution 2')
    # Visualization
    plt.grid(alpha=0.5)
    plt.xlabel('Random Variable')
    plt.ylabel('Probability')
    plt.title('Unif(0,1) and Unif(2,4) Distribution')
    plt.legend()
    plt.savefig('unif01_unif24.png')
    plt.show()

    # Generate 10,000 random numbers from 2 to 4 and store them in a list
    unif_2_5_data = pd_generator.disc_unif(n=100000, a=2, b=5)
    counts, bin_edges = np.histogram(unif_2_5_data, bins=4, range=(1.5, 5.5), density=False)
    probs = counts / len(unif_2_5_data)
    plt.bar(np.arange(2, 6), probs, width=0.5, label='Generated Data')
    plt.axhline(y=0.25, color='r', linestyle='--', alpha=0.5, label='Expected Probability')
    plt.grid(alpha=0.5)
    plt.xlabel('Random Variable')
    plt.ylabel('Probability')
    plt.title('DiscUnif(2,5) Distribution')
    plt.legend()
    plt.savefig('dunif25.png') 
    plt.show()

    tri_data = pd_generator.triangular(n=100000, a=0, b=2, c=1)
    # Plot a histogram of the random numbers
    plt.hist(tri_data, bins=100, density=True, label='Generated Data')
    x = np.linspace(0, 2, 1000)
    y = [expected_triangular(xi, 0, 2, 1) for xi in x]
    plt.plot(x, y, color='r', linestyle='--', lw=2, alpha=0.5, label='Expected Distribution')
    plt.grid(alpha=0.5)
    plt.xlabel('Random Variable')
    plt.ylabel('Probability')
    plt.title('Triangular Distribution(0,1,2)')
    plt.legend()
    plt.savefig('tri012.png') 
    plt.show()

    tri_data = pd_generator.triangular(n=100000, a=0, b=4, c=1)
    # Plot a histogram of the random numbers
    plt.hist(tri_data, bins=100, density=True, label='Generated Data')
    x = np.linspace(0, 4, 1000)
    y = [expected_triangular(xi, 0, 4, 1) for xi in x]
    plt.plot(x, y, color='r', linestyle='--', lw=2, alpha=0.5, label='Expected Distribution')
    plt.grid(alpha=0.5)
    plt.xlabel('Random Variable')
    plt.ylabel('Probability')
    plt.title('Triangular Distribution(0,1,4)')
    plt.legend()
    plt.savefig('tri014.png') 
    plt.show()

    expo_data = pd_generator.expo(n=100000, lamb=1)
    # Plot a histogram of the random numbers
    plt.hist(expo_data, bins=100, density=True, label='Generated Data')
    # Create the exponential distribution with lambda=2
    x = np.linspace(0, 10, 1000)
    y = expon.pdf(x, scale=1 )
    plt.plot(x, y, color='r', linestyle='--',  alpha=0.5, label='Expected Distribution')
    plt.grid(alpha=0.5)
    plt.xlabel('Random Variable')
    plt.ylabel('Probability')
    plt.title('Expo(1) Distribution')
    plt.legend()
    plt.savefig('expo1.png') 
    plt.show()

    expo_data = pd_generator.expo(n=100000, lamb=2)
    # Plot a histogram of the random numbers
    plt.hist(expo_data, bins=100, density=True, label='Generated Data')
    # Create the exponential distribution with lambda=2
    x = np.linspace(0, 10, 1000)
    y = expon.pdf(x, scale=1 / 2)
    plt.plot(x, y, color='r', linestyle='--',  alpha=0.5, label='Expected Distribution')
    plt.grid(alpha=0.5)
    plt.xlabel('Random Variable')
    plt.ylabel('Probability')
    plt.title('Expo(2) Distribution')
    plt.legend()
    plt.savefig('expo2.png') 
    plt.show()

    weibull_data = pd_generator.weibull(n=100000, lamb=0.8, beta=1.2)
    # Plot a histogram of the random numbers
    plt.hist(weibull_data, bins=100, density=True, label='Generated Data')
    x = np.linspace(0, 10, 1000)
    y = weibull_min.pdf(x, c=1.2, scale=1 / 0.8)
    plt.plot(x, y, color='r', linestyle='--', alpha=0.5, label='Expected Distribution')
    plt.grid(alpha=0.5)
    plt.xlabel('Random Variable')
    plt.ylabel('Probability')
    plt.title('Weibull(0.8, 1.2) Distribution')
    plt.legend()
    plt.savefig('weibull.png') 
    plt.show()

    erlang_data = pd_generator.erlang(n=100000, m=3, lamb=2)
    # Plot a histogram of the random numbers
    plt.hist(erlang_data, bins=100, density=True, label='Generated Data')
    # Create the gamma distribution with shape=3 and scale=1/2
    x = np.linspace(0, 25, 1000)
    y = gamma.pdf(x, a=3, scale=1 / 2)
    plt.plot(x, y, color='r', linestyle='--', alpha=0.5, label='Expected Distribution')
    plt.grid(alpha=0.5)
    plt.xlabel('Random Variable')
    plt.ylabel('Probability')
    plt.title('Erlang-3(2) Distribution')
    plt.legend()
    plt.savefig('gamma32.png') 
    plt.show()

    norm_data = pd_generator.norm(n=100000, mu=6, sigma=2)
    # Plot a histogram of the random numbers
    plt.hist(norm_data, bins=100, density=True, label='Generated Data')
    # Calculate the expected normal distribution
    x = np.linspace(np.array(norm_data).min(), np.array(norm_data).max(), 1000)
    y = norm.pdf(x, loc=6, scale=2)
    plt.plot(x, y, color='r', linestyle='--', lw=2,  alpha=0.5, label='Expected Distribution')
    # Visualization
    plt.grid(alpha=0.5)
    plt.xlabel('Random Variable')
    plt.ylabel('Probability')
    plt.title('Normal Distribution(6,4)')
    plt.legend()
    plt.savefig('norm64.png') 
    plt.show()

    lognorm_data = pd_generator.lognorm(n=10000, mu=0, sigma=1)
    # Plot a histogram of the random numbers
    plt.hist(lognorm_data, bins=100, density=True, label='Generated Data')
    # Calculate the expected log-normal distribution
    x = np.linspace(np.array(lognorm_data).min(), np.array(lognorm_data).max(), 10000)
    y = lognorm.pdf(x, s=1, loc=0, scale=np.exp(0))
    plt.plot(x, y, color='r', linestyle='--', lw=2, alpha=0.5, label='Expected Distribution')
    # Visualization
    plt.grid(alpha=0.5)
    plt.xlabel('Random Variable')
    plt.ylabel('Probability')
    plt.title('Log-Normal Distribution(0,1)')
    plt.legend()
    plt.savefig('lognorm01.png')
    plt.show()

    chi2_data = pd_generator.chi2(n=100000, m=3)
    # Plot a histogram of the random numbers
    plt.hist(chi2_data, bins=100, density=True, label='Generated Data')
    # Generate the expected density curve using scipy.stats.chi2.pdf()
    x = np.linspace(0, 20, 1000)
    y = chi2.pdf(x, df=3)
    plt.plot(x, y, color='r', linestyle='--', lw=2, alpha=0.5, label='Expected Distribution')
    plt.grid(alpha=0.5)
    plt.xlabel('Random Variable')
    plt.ylabel('Probability')
    plt.title('χ-squared(3) Distribution')
    plt.legend()
    plt.savefig('chisquared3.png') 
    plt.show()

    bern_data = pd_generator.bern(n=100000, p=0.6)
    counts, bin_edges = np.histogram(bern_data, bins=2, range=(-0.5, 1.5), density=False)
    probs = counts / len(bern_data)
    plt.bar([0, 1], probs, width=0.5, label='Generated Data')
    plt.plot([0, 1], [1-0.6, 0.6], color='r', linestyle='--', alpha=0.5, label='Expected Probability')
    plt.grid(alpha=0.5)
    plt.xlabel('Random Variable')
    plt.ylabel('Probability')
    plt.title('Bernoulli(0.6) Distribution')
    plt.legend()
    plt.savefig('bern.png') 
    plt.show()

    bino_data = pd_generator.bino(n=100000, m=3, p=0.6)
    k_vals, counts = np.unique(bino_data, return_counts=True)
    probs = counts / len(bino_data)
    plt.bar(k_vals, probs, width=0.5, label='Generated Data')
    exp_probs = [scipy.stats.binom.pmf(k, n=3, p=0.6) for k in k_vals]
    x = np.arange(len(exp_probs)) + min(k_vals)
    plt.plot(x, exp_probs, color='r', linestyle='--', alpha=0.5, label='Expected Probability')
    plt.grid(alpha=0.5)
    plt.xlabel('Random Variate')
    plt.ylabel('Probability')
    plt.title('Binomial(3,0.6) Distribution')
    plt.legend()
    plt.savefig('bino3.png') 
    plt.show()

    geom_data = pd_generator.geom(n=100000, p=0.5)
    counts, bin_edges = np.histogram(geom_data, bins=max(geom_data), density=False)
    probs = counts/len(geom_data)
    k_vals = np.arange(1, max(geom_data)+1)
    plt.bar(k_vals, probs, width=0.5, label='Generated Data')
    probs = geom.pmf(k_vals, p=0.5)
    plt.plot(k_vals, probs, color='r', linestyle='--', alpha=0.5, label='Expected Probability')
    plt.grid(alpha=0.5)
    plt.xlabel('Random Variate')
    plt.ylabel('Probability')
    plt.title('Geom(0.5) Distribution')
    plt.legend()
    plt.savefig('geom.png') 
    plt.show()

    negbin_data = pd_generator.negbin(n=10000, m=3, p=0.6)
    counts, bin_edges = np.histogram(negbin_data, bins=max(negbin_data), density=False)
    mask = counts != 0
    counts = counts[mask]
    probs = counts / len(negbin_data)
    print(probs)
    k_vals = np.arange(min(negbin_data), max(negbin_data)+1)
    plt.bar(k_vals, probs, width=0.5, label='Generated Data')
    k2_vals = np.arange(0, len(k_vals))
    probs_expected = nbinom.pmf(k2_vals, n=3, p=0.6)
    plt.plot(k_vals, probs_expected, color='r', linestyle='--', alpha=0.5, label='Expected Probability')
    plt.grid(alpha=0.5)
    plt.xlabel('Random Variate')
    plt.ylabel('Probability')
    plt.title('Negative Binomial Distribution (n=3, p=0.6)')
    plt.legend()
    plt.savefig('negbin3.png') 
    plt.show()

    pois_data = pd_generator.pois(n=100000, lamb=2)
    counts, bin_edges = np.histogram(pois_data, bins=max(pois_data), density=False)
    probs = counts / len(pois_data)
    k_vals = np.arange(0, max(pois_data))
    plt.bar(k_vals, probs, width=0.5, label='Generated Data')
    pois_probs = poisson.pmf(k_vals, mu=2)
    plt.plot(k_vals, pois_probs, color='r', linestyle='--', alpha=0.5, label='Expected Probability')
    plt.grid(alpha=0.5)
    plt.xlabel('Random Variate')
    plt.ylabel('Probability')
    plt.title('Poisson(2) Distribution')
    plt.legend()
    plt.savefig('poisson2.png') 
    plt.show()
