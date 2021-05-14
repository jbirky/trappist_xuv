import numpy as np
import h5py
import emcee
import corner
import warnings
import matplotlib.pyplot as plt
import matplotlib.colors as colors
from matplotlib import rc
rc('text', usetex=True)
rc('xtick', labelsize=16)
rc('ytick', labelsize=16)
import matplotlib as mpl
import time
import os
import glob


# =============================================
# Plot setup
# =============================================

BASE = ''
INPATH  = BASE + 'results/'
plotDir = BASE + 'plots/'
if not os.path.exists(plotDir):
    os.mkdir(plotDir)

labels = [r"$m_{\star}$ [M$_{\odot}$]", r"$f_{sat}$",
          r"$t_{sat}$ [Gyr]", r"Age [Gyr]", r"$\beta_{XUV}$"]
m0 = 50

# =============================================
# MCMC corner plot
# =============================================

def plotPosterior(file, **kwargs):
    reader = emcee.backends.HDFBackend(file)
    burn = kwargs.get('burn', None)
    thin = kwargs.get('thin', None)
    
    chain = reader.get_chain(flat=True, discard=burn, thin=thin)
    print(chain.shape)

    range = kwargs.get('range', None)

    warnings.simplefilter("ignore")
    fig = corner.corner(chain, labels=labels, range=range, plot_contours=True,
                        plot_density=True, plot_points=True,
                        quantiles=[0.16, 0.5, 0.84], 
                        show_titles=True, title_kwargs={"fontsize": 18}, 
                        label_kwargs={"fontsize": 22})
    return chain, fig
    
# ----------------------------

# get hdf5 file of last MCMC iteration
# hdFiles = glob.glob(os.path.join(INPATH, 'apRun*.h5'))
# lastF = max([f.split('apRun')[1].split('.h5')[0] for f in hdFiles])

# chain, fig = plotPosterior(os.path.join(INPATH, 'apRun%s.h5'%(lastF)), burn=int(1e3), thin=100)
# fig.savefig(os.path.join(plotDir, 'emcee_corner.png'))


# =============================================
# lnP vs approxposterior iteration
# =============================================

sims = np.load(os.path.join(INPATH, 'apRunAPFModelCache.npz'))
y = -sims['y']

plt.figure(figsize=[10,8])
itr = np.arange(len(y))
plt.scatter(itr, y)
plt.ylim(1, 10**12)
plt.yscale('log')
plt.xlabel('iteration', fontsize=20)
plt.ylabel(r'$-\ln P$', fontsize=20)
plt.savefig(os.path.join(plotDir, 'bape_lnp_iter.png'))
plt.show()


# =============================================
# Dist of training samples - density plot
# =============================================

# fig = corner.corner(sims['theta'][0:m0], labels=labels, plot_contours=True,
#                     plot_density=True, plot_points=True,
#                     quantiles=[0.16, 0.5, 0.84], 
#                     show_titles=True, title_kwargs={"fontsize": 18}, 
#                     label_kwargs={"fontsize": 22})
# fig.savefig(os.path.join(plotDir, 'init_samples.png'))


# fig = corner.corner(sims['theta'][m0:], labels=labels, plot_contours=True,
#                     plot_density=True, plot_points=True,
#                     quantiles=[0.16, 0.5, 0.84], 
#                     show_titles=True, title_kwargs={"fontsize": 18}, 
#                     label_kwargs={"fontsize": 22},
#                     truths=sims['theta'][np.argmax(sims['y'])])
# fig.savefig(os.path.join(plotDir, 'bape_samples.png'))


# =============================================
# Dist of training samples - colored by lnP value
# =============================================

def plotCornerLnp(tt, yy, **kwargs):

    fig = corner.corner(tt, c=yy, labels=labels, 
                  plot_datapoints=False, plot_density=False, plot_contours=False,
                  show_titles=True, title_kwargs={"fontsize": 18}, 
                  label_kwargs={"fontsize": 22})

    ndim = tt.shape[1]
    axes = np.array(fig.axes).reshape((ndim, ndim))
    cb_rng = kwargs.get('cb_rng', [yy.min(), yy.max()])
    
    print(cb_rng)

    for yi in range(ndim):
        for xi in range(yi):
            ax = axes[yi, xi]
            im = ax.scatter(tt.T[xi], tt.T[yi], c=yy, s=2, cmap='coolwarm', norm=colors.LogNorm(vmin=cb_rng.min(), vmax=cb_rng.max()))

    cb = fig.colorbar(im, ax=axes.ravel().tolist(), orientation='horizontal', shrink=.98, pad=.1)
    cb.set_label(r'$-\ln P$', fontsize=20)
    if 'cb_rng' in kwargs:
        cb.set_ticks(cb_rng)
    cb.ax.tick_params(labelsize=18)
    return fig

# ----------------------------

cb_rng = (-1,4)
cb_ticks = np.logspace(cb_rng[0], cb_rng[1], cb_rng[1]-cb_rng[0]+1)

fig = plotCornerLnp(sims['theta'], -sims['y'], cb_rng=cb_ticks)
fig.savefig(os.path.join(plotDir, 'all_samples_lnp.png'))

fig = plotCornerLnp(sims['theta'][m0:], -sims['y'][m0:], cb_rng=cb_ticks)
fig.savefig(os.path.join(plotDir, 'bape_samples_lnp.png'))

fig = plotCornerLnp(sims['theta'][:m0], -sims['y'][:m0], cb_rng=cb_ticks)
fig.savefig(os.path.join(plotDir, 'init_samples_lnp.png'))