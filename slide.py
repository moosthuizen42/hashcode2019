
class Slide():
    def __init__ (self, tags, v_image_1=None, v_image_2=None, h_image=None):
        self.tags = tags
        ids = [v_image_1, v_image_2, h_image]
        self.ids = filter(None, ids)
