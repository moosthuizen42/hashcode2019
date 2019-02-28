import random
from score import getScore
from slide import Slide

def repeatRandomness (current_slides, unused_slides_H, unused_slides_V, max_slides):
    # print("repeatRandomness")

    completion_factor = len(current_slides) / max_slides

    option = random.randint(0, 2)

    if (option == 0):
        force = random.randint(0,100) > completion_factor*2 + 98
        doRandomInsert(current_slides, unused_slides_H, unused_slides_V, force)

    elif (option == 1):
        force = random.randint(0,100) > (100 - completion_factor*2)
        doRandomRemove(current_slides, unused_slides_H, unused_slides_V, force)

    elif (option == 2):
        removeLowestScore(current_slides, unused_slides_H, unused_slides_V)


    # elif (option == 2):
    #     doRandomSwap(current_slides, unused_slides_V);


def removeLowestScore (current_slides, unused_slides_H, unused_slides_V):

    minimum_score = 1000000;
    minimum_index = -1;
    
    for i in range(len(current_slides)-3):
        current_score = ( getScore(current_slides[i], current_slides[i+1]) +
            getScore(current_slides[i+1], current_slides[i+2]) );
        if ( current_score < minimum_score ):
            minimum_score = current_score
            minimum_index = i + 1


    if (minimum_index > -1):
        removed_slide = current_slides[minimum_index];

        if (removed_slide.h_image is None):
            unused_slides_H.append(removed_slide)
        else:
            unused_slides_V.append(Slide(
                v_image_1 = removed_slide.v_image_1,
                v_tags_1 = removed_slide.v_tags_1,
            ))
            unused_slides_V.append(Slide(
                v_image_1 = removed_slide.v_image_2,
                v_tags_1 = removed_slide.v_tags_2
            ))



def doRandomInsert (current_slides, unused_slides_H, unused_slides_V, force):
    # print("doRandomInsert")

    if (not force and len(current_slides) < 2):
        # print("2 or more current slides needed for insert check.")
        return

    if (len(current_slides) > 3):
        insert_index = random.randint(0, len(current_slides)-2)
    else:
        insert_index = 0


    # Randomly check a V-insert or H-insert
    v_case = random.randint(0,100) > 50 * ( ( len(unused_slides_H) + 1) / (len(unused_slides_V)+1) )
    h_case = not v_case

    if (v_case):

        if (len(unused_slides_V) < 3):
            # print("2 or more unused slides needed for V insert.")
            return

        # V-case
        random_unused_index_1 = random.randint(0, len(unused_slides_V)-2)
        # print("random_unused_index_1: " + str(random_unused_index_1))
        random_unused_index_2 = random.randint(0, len(unused_slides_V)-2)
        # print("random_unused_index_2: " + str(random_unused_index_2))
        while (random_unused_index_1 == random_unused_index_2):
            random_unused_index_2 = random.randint(0, len(unused_slides_V)-2)


        # Build a new slide temporarily
        random_unused_slide = Slide(
            v_image_1 = unused_slides_V[ random_unused_index_1 ].v_image_1,
            v_image_2 = unused_slides_V[ random_unused_index_2 ].v_image_1,
            v_tags_1 = unused_slides_V[ random_unused_index_2 ].v_tags_1,
            v_tags_2 = unused_slides_V[ random_unused_index_2 ].v_tags_1 )

        if ( force or insertImprovement(current_slides, insert_index, random_unused_slide) > 0 ):
            current_slides.insert(insert_index, random_unused_slide)
            if (random_unused_index_1 > random_unused_index_2):
                del unused_slides_V[random_unused_index_1]
                del unused_slides_V[random_unused_index_2]
            else:
                del unused_slides_V[random_unused_index_2]
                del unused_slides_V[random_unused_index_1]


    if (h_case):

        if (len(unused_slides_H) < 1):
            # print("1 or more unused slides needed for H insert.")
            return

        # H-slides are being used
        random_unused_index = random.randint(0, len(unused_slides_H)-1)
        random_unused_slide = unused_slides_H[random_unused_index]

        if ( force or insertImprovement(current_slides, insert_index, random_unused_slide) > 0 ):
            current_slides.insert(insert_index, random_unused_slide)
            del unused_slides_H[random_unused_index]



def doRandomRemove(current_slides, unused_slides_H, unused_slides_V, force):
    # print("doRandomRemove")

    if (len(current_slides) < 3):
        # print("3 or more slides needed for remove.")
        return

    remove_index = random.randint(1, len(current_slides)-2)

    if ( force or removeImprovement(current_slides, remove_index) > 0 ):
        removed_slide = current_slides[remove_index]

        if (removed_slide.h_image is not None):
            unused_slides_H.append(removed_slide)
        else:
            unused_slides_V.append(Slide(
                v_image_1 = removed_slide.v_image_1,
                v_tags_1 = removed_slide.v_tags_1,
            ))
            unused_slides_V.append(Slide(
                v_image_1 = removed_slide.v_image_2,
                v_tags_1 = removed_slide.v_tags_2
            ))

        del current_slides[remove_index]

    return




# def doRandomSwap (current_slides, unused_slides_V):

#     if (current_slides.length < 3):
#         print "3 or more slides needed for swap check."
#         return;

#     if (unsused_slides_V.length < 2):
#         print "2 or more unused slides needed for V swap check."
#         return;

#     check_index = randint(1, current_slides.length-2);

#     random_unused_index_1 = random.randint(0, unused_slides_V.length-1);
#     random_unused_index_2 = random.randint(0, unused_slides_V.length-1);
#     while (random_unused_index_1 == random_unused_index_2):
#         random_unused_index_2 = random.randint(0, unused_slides_V.length-1);

#     # Build a new slide temporarily
#     # random_unused_slide = new slide(random_unused_index_1, random_unused_index_2);

#     if ( verticalSwapImprovement(current_slides, check_index, random_unused_slide) > 0):

#         del unused_slides_V[random_unused_index_1];
#         del unused_slides_V[random_unused_index_2];

#         unused_slides_V.append( current_slides[check_index].ids[0] );
#         unused_slides_V.append( current_slides[check_index].ids[1] );

#         del current_slides[check_index];

#         current_slides.insert(check_index, random_unused_slide);




def insertImprovement (current_slides, insert_index, insert_slide):
    # print("insertImprovement")

    old_score = getScore( current_slides[insert_index], current_slides[insert_index + 1] )
    new_score = (getScore( current_slides[insert_index], insert_slide ) +
        getScore( insert_slide, current_slides[insert_index + 1] ) / 2)

    return new_score - old_score



def removeImprovement (current_slides, remove_index):
    # print("removeImprovement")

    old_score = (getScore( current_slides[remove_index - 1], current_slides[remove_index] ) +
        getScore( current_slides[remove_index], current_slides[remove_index + 1] ) / 2)
    new_score = getScore( current_slides[remove_index - 1], current_slides[remove_index + 1] )

    return new_score - old_score



# def verticalSwapImprovement (current_slides, check_index, swapped_slide):


#     new_score = getScore( current_slides[check_index - 1], swapped_slide ) +
#         getScore( swapped_slide, current_slides[insert_index + 1] );


#     old_score = getScore( current_slides[check_index - 1], current_slides[check_index] ) +
#         getScore( current_slides[check_index], current_slides[insert_index + 1] );

#     return new_score - old_score;

