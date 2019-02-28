from score import getScore, scoreArray
from input import read_input, write_output
from slide import Slide
from random import randint
from order import repeatRandomness
from tqdm import tqdm
import itertools
import time


def main():
    # P, v, h = read_input('inputs/b_lovely_landscapes.txt')
    # P, v, h = read_input('inputs/c_memorable_moments.txt')
    P, v, h = read_input('inputs/d_pet_pictures.txt')
    # P, v, h = read_input('inputs/e_shiny_selfies.txt')

    v_count = len(v)
    h_count = len(h)

    print(P)
    print(v_count)
    print(h_count)

    slideshow = []
    # for i, _h in enumerate(itertools.islice(h, 0, int(h_count/10))):
    #     slideshow.append(_h)
    #     del h[i]

    # v_temp = v[:int(v_count/20)]
    # for _v, _v2 in zip(v_temp[0::2], v_temp[1::2]):
    #     index = randint(1, len(slideshow))

    #     slideshow.insert(index, Slide(v_tags_1=_v.v_tags_1, v_tags_2=_v2.v_tags_1,
    #                                   v_image_1=_v.v_image_1, v_image_2=_v2.v_image_1))

    # h = h[int(h_count/10):]
    # v = v[int(v_count/20):]

    start = time.time()
    idx = 0
    while time.time() - start < 120:
        idx += 1
        repeatRandomness(slideshow, h, v, P)
        if idx % 50000 == 0:
            print('\r', scoreArray(slideshow), ' - ', len(slideshow), end="")

    write_output('fuck_grant.txt', slideshow)


if __name__ == '__main__':
    main()
