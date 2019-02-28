def swapIfBetter (current_slides):

    length = current_slides.length;

    index_1 = randint(0, length-2);

    if (shouldSwap(current_slides, index_1, index_2)):
        



def insertImprovement (current_slides, insert_index, insert_slide):

    old_score = getScore( current_slides[insert_index], current_slides[insert_index+1] );
    new_score = getScore( current_slides[insert_index], insert_slide ) + 
        getScore( insert_slide, current_slides[insert_index+1] ) / 2;

    return new_score - old_score;



def removeImprovement (current_slides, remove_index):

    old_score = getScore( current_slides[insert_index], insert_slide ) + 
        getScore( insert_slide, current_slides[insert_index+1] ) / 2;
    new_score = getScore( current_slides[insert_index], current_slides[insert_index+1] );

    return new_score - old_score;



def verticalSwapImprovement ():

    