from yael import yael
from yael import ynumpy


# Each image will have 300 subimages
# In the step of extract fisher vector, we need to consder all subimages
# Expect: imdb is a list with 1st dimension is big image and 2nd dimension is all 300 subimages
class imdata(object):
    # contain all the images and features
    def __init__(self, imdb, dest):
        self.num_big_images = len(imdb)
        self.save_path = dest
        self.imdb = imdb
        self.all_images = self.concat_all()

    def get_im(self, i):
        im = self.images[i]
        return im

    def concat_all(self):
        im_list = []
        for i in range(self.num_big_images):
            im = self.get_im(i)
            im_list += im
        return im_list

    def extract_dsift(self):
        num = len(self.all_images)
        yael.
