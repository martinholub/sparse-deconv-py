from sparse_recon.sparse_deconv import sparse_deconv
from skimage import io
from matplotlib import pyplot as plt
from sparse_recon.utils.imutils import imcrop, implot, imsave

if __name__ == '__main__':
    im = io.imread('test.tif')
    im = imcrop(im)
    implot(im)

    pixelsize = 199 #(nm)
    resolution = 600 #(nm)

    #img_recon = sparse_deconv(im, [5,5])
    img_recon = sparse_deconv(im, [resolution / pixelsize] * 2)
    implot(img_recon / img_recon.max() * 255)
    imsave(img_recon)
