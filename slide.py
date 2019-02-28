
class Slide():
    def __init__(self, v_tags_1=None, v_tags_2=None, h_tags=None, v_image_1=None, v_image_2=None, h_image=None):
        self.v_image_1 = v_image_1
        self.v_image_2 = v_image_2
        self.h_image = h_image
        self.v_tags_1 = v_tags_1
        self.v_tags_2 = v_tags_2
        self.h_tags = h_tags

    def __str__(self):
        if self.h_image:
            return 'Horizontal image, id = {0}, tags = {1}'.format(self.h_image, self.h_tags)
        else:
            return 'Vertical image, id = {0}, tags = {1}'.format(self.v_image_1, self.v_tags_1)
