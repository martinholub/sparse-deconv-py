import numpy as np
import matplotlib.pyplot as plt
import tifffile

def imcrop(im):
    """Crop image to even size"""
    im = np.moveaxis(im, 0, -1) # roll time/z axis to end, if any
    # crop to even dimensions
    if im.shape[0] % 2:
        im = im[:im.shape[0]-1, :]
    if im.shape[1] % 2:
        im = im[:, :im.shape[1]-1]

    # roll axis back
    im = np.moveaxis(im, -1, 0)
    return im


def implot(im):
    """Plot potentially 3d image"""
    # assumes time/z axis is first
    if im.ndim == 2:
        plt.imshow(im, cmap = 'gray')
    else:
        plt.imshow(im[int(im.shape[0]/2), :, :], cmap = 'gray')
    plt.show()


def imsave(im, impath = 'test_out.tif'):
    """
    assumes the data is in XYZ.. shape
    """
    im = np.reshape(im, im.shape + (1,) * (4 - im.ndim))
    im = np.moveaxis(im, 0, 2) # move z axis to 3rd position
    opts = {'contiguous': True, 'metadata': {'axes': 'XYCZT'}}
    nonxy_dims = im.shape[2:]
    if len(nonxy_dims) == 1: nonxy_dims += (1,)
    with tifffile.TiffWriter(impath, imagej = True) as tif:
        for j in range(nonxy_dims[-1]):
            for i in range(nonxy_dims[-2]):
                im_ = im[:,:,i, j]
                try:
                    tif.write(im_, **opts)
                except AttributeError as e:
                    tif.save(im_, **opts)
