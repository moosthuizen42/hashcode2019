from score import getScore, scoreArray
from input import read_input, write_output
from slide import Slide
from random import randint
from order import repeatRandomness
from tqdm import tqdm
import itertools
import time


def main():
    # input_file = 'b_lovely_landscapes.txt'
    # input_file = 'c_memorable_moments.txt'
    input_file = 'd_pet_pictures.txt'
    # input_file = 'e_shiny_selfies.txt'
    P, v, h = read_input('inputs/' + input_file)

    v_count = len(v)
    h_count = len(h)

    print(P)
    print(v_count)
    print(h_count)

    slideshow = []
    max_score = 0
    max_score_slideshow = []
    start = time.time()
    idx = 0
    while time.time() - start < 60:
        idx += 1
        repeatRandomness(slideshow, h, v, P)
        if idx % 5000 == 0:
            score = scoreArray(slideshow)
            print('\r', score, '/', max_score, ' - ', len(slideshow), end="")
            if score > max_score:
                max_score = score
                max_score_slideshow = slideshow

    write_output('outputs/' + input_file, max_score_slideshow)


if __name__ == '__main__':
    main()
