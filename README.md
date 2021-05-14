## Improved Constraints for the XUV Luminosity Evolution of Trappist-1

Jessica Birky, Rory Barnes, and David P. Fleming

We re-examine the XUV luminosity evolution of TRAPPIST-1 utilizing new observational constraints on the current stellar parameters XUV and bolometric luminosity from multi-epoch X-ray/UV photometry. Following the formalism presented on ![fleming_xuv_2020](https://iopscience.iop.org/article/10.3847/1538-4357/ab77ad/meta), we infer that TRAPPIST-1 maintained a saturated XUV luminosity, relative to the bolometric luminosity, of $\log_{10}$(\lxuv/\lbol) $= -3.03_{-0.23}^{+0.25}$ at early times for a period of \tsat $= 3.14_{-1.46}^{+2.22}$ Gyr. After the saturation phase, we find \lxuv\ exponentially decayed with an $e$-folding timescale of \bxuv $= -1.17_{-0.28}^{+0.27}$. Compared to our inferred age of the system $\age = 7.96_{-1.87}^{+1.78}$ Gyr, our result for \tsat\ suggests that there is only a $\sim4\%$~chance that TRAPPIST-1 still remains in the saturated phase today, which is significantly lower than the previous estimate of 40\%. Despite this reduction in \tsat, our results remain consistent in the conclusion that the TRAPPIST-1 planets likely received an extreme amount XUV energy---an estimated integrated XUV energy of $\sim10^{30}-10^{32} {\rm \, erg}$ over the star's lifetime, which is $\sim15\%$~lower than the original result.

## Code

### Repositories

Updated study: https://github.com/jbirky/trappist_xuv
Original study: https://github.com/dflemin3/trappist

### Dependencies

* ![vplanet](https://github.com/VirtualPlanetaryLaboratory/vplanet)
* ![vplot](https://github.com/VirtualPlanetaryLaboratory/vplot)
* ![approxposterior](https://github.com/dflemin3/approxposterior)
* ![george](https://github.com/dfm/george)
* ![emcee](https://github.com/dfm/emcee) 

### Using the posterior samples

See https://github.com/jbirky/trappist_xuv/mcmc/corner.ipynb