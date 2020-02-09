import matplotlib
matplotlib.use("pgf")
matplotlib.rcParams.update({
    "pgf.texsystem": "pdflatex",
    'font.family': 'serif',
    'text.usetex': True,
    'pgf.rcfonts': False,
})


import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":
    x = np.random.normal(loc=0, scale=1.0, size=(1000,))
    fig = plt.figure()
    
    plt.hist(x,bins=50)
    plt.title("Normal Distribution")
    plt.xlabel('$x$')
    plt.ylabel('Density')

    # Export as PGF
    plt.savefig('histogram.pgf')
    
    
    

