import math

class MersenneTwister:
    def __init__(self, seed):
        self.index = 0
        self.MT = [0] * 624
        self.MT[0] = seed
        for i in range(1, 624):
            self.MT[i] = (1812433253 * (self.MT[i - 1] ^ (self.MT[i - 1] >> 30)) + i) & 0xFFFFFFFF

    def generate_numbers(self):
        for i in range(624):
            y = (self.MT[i] & 0x80000000) + (self.MT[(i + 1) % 624] & 0x7FFFFFFF)
            self.MT[i] = self.MT[(i + 397) % 624] ^ (y >> 1)
            if y % 2 != 0:
                self.MT[i] ^= 2567483615

    def extract_number(self):
        if self.index == 0:
            self.generate_numbers()
        y = self.MT[self.index]
        y ^= (y >> 11)
        y ^= ((y << 7) & 0x9D2C5680)
        y ^= ((y << 15) & 0xEFC60000)
        y ^= (y >> 18)
        self.index = (self.index + 1) % 624
        return y / 0xFFFFFFFF # Divided 2^32 - 1
class PDGenerator:
    def __init__(self, seed=0):
        self.random_seed = seed
        self.random = MersenneTwister(seed)

    def unif(self, n=1, a=0, b=1):
        unif_rvs = [(a + (b-a)*self.random.extract_number()) for i in range(n)]
        return unif_rvs
    def disc_unif(self, n=1, a=0, b=1):
        unif_rvs = self.unif(n=n)
        disc_unif_rvs = [int(a + (b-a+1) * U) for U in unif_rvs]
        return disc_unif_rvs
    def triangular(self, n=1, a=0, b=1, c=None):
        if c is None:
            c = (a + b) / 2
        unif_rvs = self.unif(n=n)
        tri_rvs = []
        for U in unif_rvs:
            if U < ((c - a) / (b - a)):
                tri_rvs.append(a + math.sqrt(U * (b - a) * (c - a)))
            else:
                tri_rvs.append(b - math.sqrt((1 - U) * (b - a) * (b - c)))
        return tri_rvs

    def expo(self, n=1, lamb=1):
        expo_rvs = self.weibull(n=n, lamb=lamb, beta=1)
        return expo_rvs

    def weibull(self, n=1, lamb=1, beta=1):
        unif_rvs = self.unif(n=n)
        weibull_rvs = [((-math.log(U))**(1/beta)/lamb) for U in unif_rvs]
        return weibull_rvs

    def erlang(self, n=1, m=2, lamb=1):
        erlang_rvs = [sum(self.expo(n=m, lamb=lamb)) for i in range(n)]
        return erlang_rvs


    def sign(self, x):
        if x > 0: return 1
        elif x < 0: return -1
        else: return 0

    def t(self, U):
        ln_u = math.log(min(U, 1 - U))
        t = (-2 * ln_u)**0.5
        return t

    def norm(self, n=1, mu=0, sigma=1):
        unif_rvs = []
        while len(unif_rvs) < n:
            unif_rvs += [u for u in self.unif(n=n*2) if 0 <= u <= 1]
        z_norm_rvs = [(self.sign(U-0.5)*(self.t(U) - ((2.515517 + 0.802853*self.t(U) + 0.010328*self.t(U)**2)/(1 + 1.432788*self.t(U) + 0.189269*self.t(U)**2 + 0.001308*self.t(U)**3)))) for U in unif_rvs[:n]]
        norm_rvs = [mu + sigma*Z for Z in z_norm_rvs]
        return norm_rvs

    def chi2(self, n=1, m=2):
        chi2_rvs = [sum(x ** 2 for x in self.norm(n=m)) for i in range(n)]
        return chi2_rvs

    def lognorm(self, n=1, mu=0, sigma=1):
        norm_rvs = self.norm(n=n, mu=mu, sigma=sigma)
        lognorm_rvs = [math.exp(N) for N in norm_rvs]
        return lognorm_rvs

    def t_student(self, n=1, m=1):
        norm_rvs = self.norm(n=n * m, mu=0, sigma=1)
        t_rvs = [(N / (self.chi2(n=m)[0] / m) ** 0.5) for N in norm_rvs]
        return t_rvs

    def bern(self, n=1, p=0.5):
        unif_rvs = self.unif(n=n)
        bern_rvs = [1 if U<=p else 0 for U in unif_rvs]
        return bern_rvs

    def bino(self, n=1, m=2, p=0.5):
        bino_rvs = [sum(self.bern(n=m, p=p)) for i in range(n)]
        return bino_rvs

    def geom(self, n=1, p=0.5):
        unif_rvs = self.unif(n=n)
        geom_rvs = [math.ceil((math.log(U))/(math.log(1-p))) for U in unif_rvs]
        return geom_rvs

    def negbin(self, n=1, m=2, p=0.5):
        negbin_rvs = [sum(self.geom(n=m, p=p)) for i in range(n)]
        return negbin_rvs

    def pois_pmf(self, n=0,lamb=1):
        return (math.e**(-lamb))*((lamb)**n)/(math.factorial(n))

    def pois(self, n=1, lamb=1):
        pois_rvs = []
        while len(pois_rvs) < n:
            U = self.unif(n=1)[0]
            X = 0
            P = self.pois_pmf(X, lamb)
            while U >= P:
                X += 1
                P += self.pois_pmf(X, lamb)
            pois_rvs.append(X)
        return pois_rvs


if __name__ == '__main__':
    print("Hello World")
    pd_generator = PDGenerator()
    pd_generator.unif()

