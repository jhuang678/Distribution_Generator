import PDGenerator as pdg
import math
import numpy as np
import scipy
import scipy.stats as stats
from scipy.stats import chi2, norm, normaltest, kstest, expon, triang, uniform, chisquare, gamma, erlang, lognorm, ttest_1samp, nbinom

def unif_gof_test(data, k=10, alpha=0.05, display=True):
    E = len(data)/k
    intervals = [i/k for i in range(k+1)]
    O = [0]*k
    for i in range(k):
        if i == 0:
            O[0] = len([j for j in data if intervals[0] <= j <= intervals[1]])
        else:
            O[i] = len([j for j in data if intervals[i] < j <= intervals[i+1]])
    chi_2 = sum([((O[i]-E)**2)/E for i in range(k)])
    chi_2_alpha = chi2.ppf(q=1-alpha, df=k-1)
    p_value = 1 - chi2.cdf(x=chi_2, df=k-1)
    if display:
        print(f"critical value: {chi_2_alpha}")
        print(f"p-value: {p_value}")
        if chi_2 < chi_2_alpha:
            print("ACCEPT null hypothesis: the data follows a Uniformly distribution.")
        else:
            print("REJECT null hypothesis: the data does NOT follows a Uniformly distribution.")
    return chi_2 < chi_2_alpha

def disc_uniform_gof_test(data, alpha=0.05, display=True):
    num_bins = len(set(data))
    observed, _ = np.histogram(data, bins=num_bins)
    expected = np.ones(num_bins) * (len(data) / num_bins)
    _, p_value = chisquare(observed, expected)
    if display:
        print(f"p-value: {p_value}")
        if p_value > alpha:
            print("ACCEPT null hypothesis: the data follows a Discrete Uniform distribution.")
        else:
            print("REJECT null hypothesis: the data does NOT follow a Discrete Uniform distribution.")
    return p_value > alpha

def tria_gof_test(data, alpha=0.05, a=None, b=None, c=None, display=True):
    if a is None:
        a = np.min(data)
    if b is None:
        b = np.max(data)
    if c is None:
        c = np.median(data)
    k2, p_value = kstest(data, triang(c=(c-a)/(b-a), loc=a, scale=b-a).cdf)
    if display:
        print(f"Kolmogorov-Smirnov test statistic: {k2}")
        print(f"p-value: {p_value}")
        if p_value > alpha:
            print("ACCEPT null hypothesis: the data follows a Triangular distribution.")
        else:
            print("REJECT null hypothesis: the data does NOT follow a Triangular distribution.")
    return p_value > alpha

def expo_gof_test(data, alpha=0.05, lamb=None, display=True):
    if lamb is None:
        lamb = 1 / (sum(data) / len(data))
    k2, p_value = kstest(data, expon(scale=1 / lamb).cdf)
    if display:
        print(f"Kolmogorov-Smirnov test statistic: {k2}")
        print(f"p-value: {p_value}")
        if p_value > alpha:
            print("ACCEPT null hypothesis: the data follows an Exponential distribution.")
        else:
            print("REJECT null hypothesis: the data does NOT follow an Exponential distribution.")
    return p_value > alpha

def weibull_gof_test(data, alpha=0.05, beta=1, lamb=1, display=True):
    k2, p_value = stats.kstest(data, stats.weibull_min(c=beta, scale=1/lamb).cdf)
    if display:
        print(f"Kolmogorov-Smirnov test statistic: {k2}")
        print(f"p-value: {p_value}")
        if p_value > alpha:
            print("ACCEPT null hypothesis: the data follows a Weibull distribution.")
        else:
            print("REJECT null hypothesis: the data does not follow a Weibull distribution.")
    return p_value > alpha

def erlang_gof_test(data, alpha=0.05, display=True):
    # Fit the Erlang distribution to the data using MLE
    fit_params = gamma.fit(data)
    # Compute the KS test statistic and p-value
    ks_stat, p_val = kstest(data, 'gamma', fit_params)
    # Print the results
    if display:
        print(f"KS test statistic: {ks_stat}")
        print(f"p-value: {p_val}")
        if p_val > alpha:
            print("ACCEPT null hypothesis: the data follows an Erlang distribution.")
        else:
            print("REJECT null hypothesis: the data does NOT follow an Erlang distribution.")
    return p_val > alpha


def norm_gof_test(data, alpha=0.05, display=True):
    k2, p_value = normaltest(data)
    if display:
        print(f"normal test statistic: {k2}")
        print(f"p-value: {p_value}")
        if p_value > alpha:
            print("ACCEPT null hypothesis: the data follows a Normally distributed.")
        else:
            print("REJECT null hypothesis: the data does NOT follow a Normally distributed.")
    return p_value > alpha


def chi2_gof_test(data, alpha=0.05, m=2, display=True):
    df = m
    fit_params = chi2.fit(data, df)
    ks_stat, p_val = kstest(data, 'chi2', fit_params)
    # Print the results
    if display:
        print(f"KS test statistic: {ks_stat}")
        print(f"p-value: {p_val}")
        if p_val > alpha:
            print("ACCEPT null hypothesis: the data follows a chi-square distribution.")
        else:
            print("REJECT null hypothesis: the data does NOT follow a chi-square distribution.")
    return p_val > alpha

def lognorm_gof_test(data, alpha=0.05, display=True):
    # Fit the lognormal distribution to the data using MLE
    fit_params = lognorm.fit(data)
    # Compute the KS test statistic and p-value
    ks_stat, p_val = kstest(data, 'lognorm', fit_params)
    # Print the results

    if display:
        print(f"KS test statistic: {ks_stat}")
        print(f"p-value: {p_val}")
        if p_val > alpha:
            print("ACCEPT null hypothesis: the data follows a Lognormal distribution.")
        else:
            print("REJECT null hypothesis: the data does NOT follow a Lognormal distribution.")
    return p_val > alpha

def t_gof_test(data, alpha=0.05, display=True):
    t_stat, p_val = ttest_1samp(data, popmean=0)
    if display:
        print("Test Statistic: ", t_stat)
        print("p-value: ", p_val)
        if p_val > alpha:
            print("ACCEPT null hypothesis: the data follows a t-student distribution.")
        else:
            print("REJECT null hypothesis: the data does NOT follow a t-student distribution.")
    return p_val > alpha

def bern_gof_test(data, p=0.5, alpha = 0.05, display=True):
    n = len(data)
    expected_counts = [p*n, (1-p)*n]
    observed_counts = [sum(data), n-sum(data)]
    _, p_val = chisquare(observed_counts, f_exp=expected_counts)
    if display:
        print("p-value: ", p_val)
        if p_val > alpha:
            print("ACCEPT null hypothesis: the data follows a Bernoulli distribution.")
        else:
            print("REJECT null hypothesis: the data does NOT follow a Bernoulli distribution.")
    return p_val > alpha

def bino_gof_test(data, m=2, p=0.5, alpha=0.05, display=True):
    n = len(data)
    expected_counts = [scipy.special.comb(m, k) * p**k * (1-p)**(m-k) * n for k in range(m+1)]
    observed_counts = [data.count(k) for k in range(m+1)]
    _, p_val = chisquare(observed_counts, f_exp=expected_counts)
    if display:
        print("p-value: ", p_val)
        if p_val > alpha:
            print("ACCEPT null hypothesis: the data follows a Binomial distribution.")
        else:
            print("REJECT null hypothesis: the data does NOT follow a Binomial distribution.")
    return p_val > alpha

def geom_gof_test(data, p=0.5, alpha=0.05, display=True):
    data = np.array(data)
    n = len(data)
    expected_counts = np.array([p * (1 - p) ** (k - 1) * n for k in range(1, n + 1)])
    expected_counts += 1e-10  # add a small constant to avoid zero values
    observed_counts, _ = np.histogram(data, bins=np.arange(1, n + 2))
    _, p_val = chisquare(observed_counts, f_exp=expected_counts)
    if display:
        print("p-value: ", p_val)
        if p_val > alpha:
            print("ACCEPT null hypothesis: the data follows a Geometric distribution.")
        else:
            print("REJECT null hypothesis: the data does NOT follow a Geometric distribution.")
    return p_val > alpha

'''
def negbin_gof_test(data, m=2, p=0.5, alpha=0.05, display=True):
    n = len(data)
    # Calculate the expected counts
    k = max(data) + 1
    print(k)
    f_exp = nbinom.pmf(np.arange(k), n=m, p=p) * n

    # Calculate the observed counts
    f_obs, _ = np.histogram(data, bins=np.arange(k + 1))
    f_obs = f_obs[m:]
    print(sum(f_obs))
    f_exp = f_exp * f_obs.sum() / f_exp.sum()  # normalize f_exp to match f_obs
    f_exp = f_exp[:-m]
    f_exp = f_exp + ((sum(f_obs)-sum(f_exp))/(len(f_exp )))
    print(sum(f_exp))

    # Perform the chi-square test
    f_exp_int = np.round(f_exp).astype(int)
    _, p_val = chisquare(f_obs, f_exp=f_exp_int)
    if display:
        print("p-value: ", p_val)
        if p_val > alpha:
            print("ACCEPT null hypothesis: the data follows a Negative Binomial distribution.")
        else:
            print("REJECT null hypothesis: the data does NOT follow a Negative Binomial distribution.")
    return p_val > alpha



def negbin_ks_test(data, m=2, p=0.5, alpha=0.05, display=True):
    n = len(data)
    data = [x - m for x in data]  # subtract m from each element in data

    # Generate expected CDF values from the NegBin distribution
    k = max(data) + 1
    cdf = nbinom.cdf(np.arange(k), n=m, p=p)

    # Calculate the empirical CDF
    ecdf_x = np.sort(data)
    ecdf_y = np.arange(1, n + 1) / n
    ks_stat, p_val = stats.kstest(ecdf_x, lambda x: nbinom.cdf(x+m, n=m, p=p))
    if display:
        print("KS test statistic:", ks_stat)
        print("p-value:", p_val)
        if p_val > alpha:
            print("ACCEPT null hypothesis: the data follows a Negative Binomial distribution.")
        else:
            print("REJECT null hypothesis: the data does NOT follow a Negative Binomial distribution.")
    return p_val > alpha
'''

def pois_gof_test(data, lamb=1, alpha=0.05, display=True):
    def pois_pmf(n=0, lamb=1):
        pmf = 1
        for i in range(1, n + 1):
            pmf *= lamb / i
        pmf *= math.exp(-lamb)
        return pmf

    n = len(data)
    # Calculate expected counts for each bin
    expected_counts = [n * pois_pmf(n=i, lamb=lamb) for i in range(n)]
    # Combine the last bin with the second-to-last bin to ensure enough observations in each bin
    expected_counts[-2] += expected_counts[-1]
    expected_counts = expected_counts[:-1]
    # Add a small constant value to all expected counts to avoid dividing by zero
    expected_counts = [count + 1e-10 for count in expected_counts]
    # Calculate observed counts for each bin
    observed_counts, _ = np.histogram(data, bins=len(expected_counts), range=(0, len(expected_counts)))
    # Combine the last bin with the second-to-last bin in the observed counts
    observed_counts[-2] += observed_counts[-1]
    # Perform chi-squared test for goodness-of-fit
    _, p_val = chisquare(observed_counts, f_exp=expected_counts, ddof=0)
    if display:
        print("p-value: ", p_val)
        if p_val > alpha:
            print("ACCEPT null hypothesis: the data follows a Poisson distribution with lambda =", lamb)
        else:
            print("REJECT null hypothesis: the data does NOT follow a Poisson distribution with lambda =", lamb)
    return p_val > alpha

def correlation_test(data, alpha = 0.05, display=True):
    rho = (12/(len(data)-1))*sum([data[k]*data[k+1] for k in range(len(data)-1)]) - 3
    rho_est_var = (13*len(data)-19)/(len(data)-1)**2
    z = rho/ math.sqrt(rho_est_var)
    p = 2 * norm.cdf(-abs(z))
    z_alpha = norm.ppf(1 - alpha / 2)
    if display:
        print("correlation coefficient (rho):", rho)
        print("estimated variance:", rho_est_var)
        print("z-score:", z)
        print("critical value", z_alpha)
        print("p-value:", p)
        if abs(z) > z_alpha:
            print("REJECT null hypothesis: low correlation. The correlation is significant.")
        else:
            print("ACCEPT null hypothesis: low correlation. The correlation is NOT significant.")
    return abs(z) > z_alpha

if __name__ == '__main__':

    print("Single test with 10000 obs")
    pd_generator = pdg.PDGenerator(seed=3)

    # Uniform(0, 1)
    unif_data = pd_generator.unif(n=10000)
    print("Goodness of Fit Test - Unif(0,1)")
    unif_gof_test(data=unif_data, k=100)
    print()
    print("Correlation Test - Unif(0,1)")
    correlation_test(data=unif_data)
    print()

    # Discrete Uniform (0,10)
    disc_unif_data = pd_generator.disc_unif(n=10000, a=0, b=10)
    print("Goodness of Fit Test - DiscUnif(0,10)")
    disc_uniform_gof_test(disc_unif_data)
    print()

    # Discrete Uniform (2,4)
    disc_unif_data = pd_generator.disc_unif(n=10000, a=2, b=4)
    print("Goodness of Fit Test - DiscUnif(2,4)")
    disc_uniform_gof_test(disc_unif_data)
    print()
    
    tria_data = pd_generator.triangular(n=10000, a=0, b=2, c=1)
    print("Goodness of Fit Test - Tria(0,1,2)")
    tria_gof_test(tria_data, a=0, b=2, c=1)
    print()

    tria_data = pd_generator.triangular(n=10000, a=1, b=4, c=3)
    print("Goodness of Fit Test - Tria(1,3,4)")
    tria_gof_test(tria_data, a=1, b=4, c=3)
    print()

    expo_data = pd_generator.expo(n=10000, lamb=1)
    print("Goodness of Fit Test - Expo(1)")
    expo_gof_test(data=expo_data, lamb=1)
    print()

    expo_data = pd_generator.expo(n=10000, lamb=2)
    print("Goodness of Fit Test - Expo(2)")
    expo_gof_test(data=expo_data, lamb=2)
    print()

    weibull_data = pd_generator.weibull(n=10000, lamb=1, beta=0.9)
    print("Goodness of Fit Test - Weibull(1, 0.9)")
    weibull_gof_test(data=weibull_data, lamb=1, beta=0.9)
    print()

    weibull_data = pd_generator.weibull(n=10000, lamb=0.8, beta=0.9)
    print("Goodness of Fit Test - Weibull(0.8, 0.9)")
    weibull_gof_test(data=weibull_data, lamb=0.8, beta=0.9)
    print()

    erlang_data = pd_generator.erlang(n=10000, m=3, lamb=2)
    print("Goodness of Fit Test - Erlang(3, 2)")
    erlang_gof_test(erlang_data)
    print()

    norm_data = pd_generator.norm(n=10000, mu=0, sigma=1)
    print("Goodness of Fit Test - Norm(0,1)")
    norm_gof_test(norm_data)
    print()

    norm_data = pd_generator.norm(n=10000, mu=1, sigma=2)
    print("Goodness of Fit Test - Norm(1,2)")
    norm_gof_test(norm_data)
    print()

    chi2_data = pd_generator.chi2(n=10000, m=3)
    print("Goodness of Fit Test - Chi2(3)")
    chi2_gof_test(chi2_data)
    print()
    
    lognorm_data = pd_generator.lognorm(n=10000, mu=0, sigma=1)
    print("Goodness of Fit Test - Lognorm(0,1)")
    lognorm_gof_test(lognorm_data)
    print()

    t_data =  pd_generator.t_student(n=10000, m=1)
    print("Goodness of Fit Test - t(1)")
    t_gof_test(t_data)
    print()

    t_data =  pd_generator.t_student(n=10000, m=2)
    print("Goodness of Fit Test - t(2)")
    t_gof_test(t_data)
    print()

    bern_data = pd_generator.bern(n=10000, p=0.6)
    print("Goodness of Fit Test - Bernoulli(0.6)")
    bern_gof_test(bern_data, p =0.6)
    print()

    bino_data = pd_generator.bino(n=100, m=3, p=0.6)
    print("Goodness of Fit Test - Binomial(3, 0.6)")
    bino_gof_test(bino_data, m=3, p=0.6)
    print()

    geom_data = pd_generator.geom(n=10000, p=0.6)
    print("Goodness of Fit Test - Geometric(0.6)")
    geom_gof_test(geom_data, p=0.6)
    print()

    pois_data = pd_generator.pois(n=10000, lamb=3)
    print("Goodness of Fit Test - Poisson(3)")
    pois_gof_test(pois_data, lamb=3)
    print()
    '''
    print("1000 test with 1000 obs")
    print()
    unif_count = 0
    tria_count = 0
    expo_count = 0
    weibull_count = 0
    erlang_count = 0
    norm1_count = 0
    norm2_count = 0
    chi2_count = 0
    lognorm_count = 0
    t1_count = 0
    t2_count = 0
    bern_count = 0
    bino_count = 0
    geom_count = 0
    pois_count = 0


    for i in range(4,1004):
        print(i)
        pd_generator = pdg.PDGenerator(seed=i)
        unif_data = pd_generator.unif(n=1000)
        unif_count += unif_gof_test(data=unif_data, k=100, display=False)

        tria_data = pd_generator.triangular(n=1000, a=0, b=2, c=1)
        tria_count += tria_gof_test(tria_data, a=0, b=2, c=1, display=False)

        expo_data = pd_generator.expo(n=1000, lamb=1)
        expo_count += expo_gof_test(data=expo_data, lamb=1, display=False)

        weibull_data = pd_generator.weibull(n=1000, lamb=0.8, beta=0.9)
        weibull_count += weibull_gof_test(data=weibull_data, lamb=0.8, beta=0.9, display=False)

        erlang_data = pd_generator.erlang(n=1000, m=3, lamb=1)
        erlang_count += erlang_gof_test(erlang_data, display=False)

        norm_data = pd_generator.norm(n=1000, mu=0, sigma=1)
        norm1_count += norm_gof_test(norm_data, display=False)

        norm_data = pd_generator.norm(n=1000, mu=1, sigma=2)
        norm2_count += norm_gof_test(norm_data, display=False)

        chi2_data = pd_generator.chi2(n=1000, m=2)
        chi2_count += chi2_gof_test(chi2_data, display=False)

        lognorm_data = pd_generator.lognorm(n=1000, mu=0, sigma=1)
        lognorm_count += lognorm_gof_test(lognorm_data, display=False)

        t_data = pd_generator.t_student(n=1000, m=1)
        t1_count += t_gof_test(t_data, display=False)

        t_data = pd_generator.t_student(n=1000, m=2)
        t2_count += t_gof_test(t_data, display=False)

        bern_data = pd_generator.bern(n=1000, p=0.7)
        bern_count += bern_gof_test(bern_data, p=0.7, display=False)

        bino_data = pd_generator.bino(n=1000, m=2, p=0.7)
        bino_count += bino_gof_test(bino_data, m=2, p=0.7, display=False)

        geom_data = pd_generator.geom(n=1000, p=0.7)
        geom_count += geom_gof_test(geom_data, p=0.7, display=False)

        pois_data = pd_generator.pois(n=1000, lamb=2)
        pois_count += pois_gof_test(pois_data, lamb=2, display=False)

    print("Goodness of Fit Test - Unif(0,1)")
    print(unif_count/1000)
    print()
    print("Goodness of Fit Test - Tria(0,1,2)")
    print(tria_count / 1000)
    print()
    print("Goodness of Fit Test - Expo(1)")
    print(expo_count / 1000)
    print()
    print("Goodness of Fit Test - Weibull(0.8,0.9)")
    print(weibull_count/ 1000)
    print()
    print("Goodness of Fit Test - Erlang(3,1)")
    print(erlang_count / 1000)
    print()
    print("Goodness of Fit Test - Norm(0,1)")
    print(norm1_count / 1000)
    print()
    print("Goodness of Fit Test - Norm(1,2)")
    print(norm2_count / 1000)
    print()
    print("Goodness of Fit Test - Chi2(2)")
    print(chi2_count / 1000)
    print()
    print("Goodness of Fit Test - LogNorm(0,1)")
    print(lognorm_count / 1000)
    print()
    print("Goodness of Fit Test - t(1)")
    print(t1_count / 1000)
    print()
    print("Goodness of Fit Test - t(2)")
    print(t2_count / 1000)
    print()
    print("Goodness of Fit Test - Bern(0.7)")
    print(bern_count / 1000)
    print()
    print("Goodness of Fit Test - Bino(2, 0.7)")
    print(bino_count / 1000)
    print()
    print("Goodness of Fit Test - Geom(0.7)")
    print(geom_count / 1000)
    print()
    print("Goodness of Fit Test - Poisson(2)")
    print(pois_count/ 1000)
    print()
    '''