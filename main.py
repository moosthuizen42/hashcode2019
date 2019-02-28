from score import getScore, scoreArray
from input import read_input
from slide import Slide
from random import randint
from order import repeatRandomness
from tqdm import tqdm
import itertools

def main():
    # read_input('inputs/b_lovely_landscapes.txt')
    P, v, h = read_input('inputs/c_memorable_moments.txt')
    # read_input('inputs/d_pet_pictures.txt')
    # read_input('inputs/e_shiny_selfies.txt')

    v_count = len(v)
    h_count = len(h)

    slideshow = []
    for i, _h in enumerate(itertools.islice(h, 0, int(h_count/10))):
        slideshow.append(_h)
        del h[i]

    v_temp = v[:int(v_count/10)]
    for _v, _v2 in zip(v_temp[0:: 2], v_temp[1:: 2]):
        index = randint(1, len(slideshow))

        slideshow.insert(index, Slide(v_tags_1=_v.v_tags_1, v_tags_2=_v2.v_tags_1, v_image_1=_v.v_image_1, v_image_2=_v2.v_image_1))

    h = h[100:]
    v = v[100:]

    print(len(slideshow))
    print(slideshow)

    for _ in tqdm(range(P *5)):
        repeatRandomness(slideshow, h, v)
        print(scoreArray(slideshow))

if __name__ == '__main__':
    main()
