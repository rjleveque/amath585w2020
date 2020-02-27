import matplotlib.pyplot as plt
from IPython.display import HTML

def make_image(fig, **kwargs):
    """
    Take a matplotlib figure *fig* and convert it to an image *im* that
    can be viewed with imshow.
    """

    import io
    png = io.BytesIO()
    fig.savefig(png,format='png', **kwargs)
    png.seek(0)
    im = plt.imread(png)
    return im

def make_images(figs, **kwargs):
    """
    Take a list of matplotlib figures *figs* and convert to list of images.
    """

    images = []
    for fig in figs:
        im = make_image(fig, **kwargs)
        images.append(im)
    return images

def JSAnimate_images(images, figsize=(8,4), dpi=None):
    "Turn a list of images into a JSAnimation."

    import matplotlib
    from matplotlib import animation


    if matplotlib.backends.backend in ['MacOSX']:
        print("*** animation.FuncAnimation doesn't work with backend %s"
              % matplotlib.backends.backend)
        print("*** Suggest using 'Agg'")
        return

    fig = plt.figure(figsize=figsize, dpi=dpi)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.axis('off')  # so there's not a second set of axes

    im = plt.imshow(images[0])

    def init():
        im.set_data(images[0])
        return im,

    def animate(i):
        im.set_data(images[i])
        return im,

    anim = animation.FuncAnimation(fig, animate, init_func=init,
                                   frames=len(images), interval=200,
                                   blit=True)

    plt.close(fig)
    return anim.to_jshtml()

def animate_figs(figs):
    images = make_images(figs, dpi=300)
    anim = JSAnimate_images(images, figsize=(8,4), dpi=300)
    return HTML(anim)
