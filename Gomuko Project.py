# Nivetha Sathish - Gomoku

"""Gomoku starter code
You should complete every incomplete function,
and add more functions and variables as needed.

Note that incomplete functions have 'pass' as the first statement:
pass is a Python keyword; it is a statement that does nothing.
This is a placeholder that you should remove once you modify the function.

Author(s): Michael Guerzhoy with tests contributed by Siavash Kazemian.  Last modified: Oct. 26, 2020
"""

# SEE IF THE ,0s need to be changed to -1s

def is_empty(board): # checks if the board is empty

    for k in range(len(board)):
        for i in range(len(board[0])):
            #print(board[k][i])
            if board[k][i] == " ":
                pass
            else:
                return False

    return True

def index_x(list, index):        # checks to see if an x value is within a list
    if len(list[0]) - 1 < index:
        return False
    else:
        return True

def index_y(list, index):        # checks to see if a y value is within a list
    if len(list) - 1 < index:
        return False
    else:
        return True

def is_bounded(board, y_end, x_end, length, d_y, d_x):
    # board is given, end coordinates are given, and the direction is given
    # if the function isn't blocked on both ends, then open
    # if the function is blocked at one end, then semiopen
    # if function is blocked at both ends, then closed

    # if direction is left_to_right (0,1) - (DONE)
    # check if the sequence is blocked on the coordinate to the left/right

    if d_y == 0 and d_x == 1:

        # determine y_start and x_start
        y_start = y_end
        x_start = x_end - (length - 1)

        #print("y_end: " + str(y_end))
        #print("x_end: " + str(x_end))
        #print("x_start: " + str(x_start))
        #print("y_start: " + str(y_start))


        #check for corner/out of range
        if (x_start - 1 < 0 or x_start - 1 > 7):
            if x_end + 1 > 7:
                return "CLOSED"
            elif board[y_end][x_end + 1] == " ":
                return "SEMIOPEN"

        if (x_end + 1 < 0 or x_end + 1 > 7):
            if x_start - 1 > 7:
                return "CLOSED"
            elif board[y_start][x_start - 1] == " ":
                return "SEMIOPEN"

        if board[y_start][x_start - 1] == " " and board[y_end][x_end + 1] == " ":
            return "OPEN"
        elif board[y_start][x_start - 1] != " " and board[y_end][x_end + 1] != " ":
            return "CLOSED"
        elif board[y_start][x_start - 1] == " " and board[y_end][x_end + 1] != " ":
            #print(str(board[y_start][x_start - 1]))
            #print("here's the mistake")
            return "SEMIOPEN"

        elif board[y_start][x_start - 1] != " " and board[y_end][x_end + 1] == " ":
            return "SEMIOPEN"

    # if direction is top_to_botton (1,0) | (DONE)
    # check if the sequence is blocked on the coordinate to the top/bottom

    if d_y == 1 and d_x == 0:

        # determine y_start and x_start
        y_start = y_end - (length - 1)
        x_start = x_end

        # check for corner/out of range
        if (y_start - 1 < 0 or y_start - 1 > 7) or (y_end + 1 < 0 or y_end + 1 > 7):
            if (y_start - 1 < 0 or y_start - 1 > 7) and (y_end + 1 < 0 or y_end + 1 > 7):
                return "CLOSED"
            if y_start - 1 < 0 or y_start - 1 > 7:
                if board[y_end + 1][x_end] == " ":
                    return "SEMIOPEN"
            if y_end + 1 < 0 or y_end + 1 > 7:
                if board[y_start - 1][x_start] == " ":
                    return "SEMIOPEN"

        if board[y_start - 1][x_start] == " " and board[y_end + 1][x_end] == " ":
            return "OPEN"
        elif board[y_start - 1][x_start] != " " and board[y_end + 1][x_end] != " ":
            return "CLOSED"
        elif board[y_start - 1][x_start] == " " and board[y_end + 1][x_end] != " ":
            return "SEMIOPEN"
        elif board[y_start - 1][x_start] != " " and board[y_end + 1][x_end] == " ":
            return "SEMIOPEN"

    # if direction is upper_left_to_lower_right (1,1) \ (DONE)
    # check if the coordinate on the row above the first and to the left is blocked
    # check if the coordinate on the row below and to the right is blocked

    if d_y == 1 and d_x == 1:

        # determine y_start and x_start

        y_start = y_end - (length - 1)

        x_start = x_end - (length - 1)

        #print("y_start: " + str(y_start))
        #print("x_start: " + str(x_start))
        #print("y_end: " + str(y_end))
        #print("x_end" + str(x_end))


        # check for corner/out of range

        if (y_start - 1 < 0 or y_start - 1 > 7) or (y_end + 1 < 0 or y_end + 1 > 7) or (x_start - 1 < 0 or x_start - 1 > 7) or (x_end + 1 < 0 or x_end + 1 > 7):


            if (y_start - 1 < 0 or y_start - 1 > 7) or (x_start - 1 < 0 or x_start - 1 > 7): # the start is out of grid
                if (y_end + 1 >= 0 and y_end + 1 <= 7) and (x_end + 1 >= 0 and x_end + 1 <= 7): # the end is in the grid
                    if board[y_end + 1][x_end + 1] == " ":
                        return "SEMIOPEN"
                    else:
                        return "CLOSED"
                else:
                    return "CLOSED"

            if (y_end + 1 < 0 or y_end + 1 > 7) or (x_end + 1 < 0 or x_end + 1 > 7): # the end is out of grid

                if (y_start - 1 >= 0 and y_start <= 7) and (x_start - 1 >= 0 and x_start <= 7):

                    if board[y_start - 1][x_start - 1] == " ":
                        return "SEMIOPEN"
                    else:
                        return "CLOSED"
                else:
                    return "CLOSED"


        if board[y_start - 1][x_start - 1] == " " and board[y_end + 1][x_end + 1] == " ":
            return "OPEN"
        elif board[y_start - 1][x_start - 1] != " " and board[y_end + 1][x_end + 1] != " ":
            return "CLOSED"
        elif board[y_start - 1][x_start - 1] == " " and board[y_end + 1][x_end + 1] != " ":
            return "SEMIOPEN"
        elif board[y_start - 1][x_start - 1] != " " and board[y_end + 1][x_end + 1] == " ":
            return "SEMIOPEN"



    # if direction is upper_right_to_lower_left (1,-1) / (DONE)
    # check if the coordinate on the row above the first and to the right is blocked
    # check if the coordinate on the row below and to the left is blocked

    if d_y == 1 and d_x == -1:

        # determine y_start and x_start

        y_start = y_end - (length - 1)
        x_start = x_end + (length - 1)

        # if the starting coordinates are off the grid because the sequence is in a corner

        # check for corner/out of range
        #print("up to here")
        #print(str(y_start - 1) + " " + str(x_start + 1) + " " + str(y_end + 1) + " " + str(x_end - 1))
        if (y_start - 1 < 0 or y_start - 1 > 7) or (y_end + 1 < 0 or y_end + 1 > 7) or (x_start + 1 < 0 or x_start + 1 > 7) or (x_end - 1 < 0 or x_end - 1 > 7):
            #print("not working")
            if (y_start - 1 < 0 or y_start - 1 > 7) or (x_start + 1 < 0 or x_start + 1 > 7): # the start is out of grid
                if (y_end + 1 >= 0 and y_end + 1 <= 7) and (x_end - 1 >= 0 and x_end - 1 <= 7): # the end is in the grid
                    if board[y_end + 1][x_end - 1] == " ":
                        return "SEMIOPEN"
                    else:
                        return "CLOSED"
                else:
                    return "CLOSED"

            if (y_end + 1 < 0 or y_end + 1 > 7) or (x_end - 1 < 0 or x_end - 1 > 7): # the end is out of grid
                if (y_start - 1 >= 0 and y_start <= 7) and (x_start + 1 >= 0 and x_start <= 7):
                    if board[y_start - 1][x_start + 1] == " ":
                        return "SEMIOPEN"
                    else:
                        return "CLOSED"
                else:
                    return "CLOSED"

        #print("WORKING")


        if board[y_start - 1][x_start + 1] == " " and board[y_end + 1][x_end - 1] == " ":
            return "OPEN"
        elif board[y_start - 1][x_start + 1] != " " and board[y_end + 1][x_end - 1] != " ":
            return "CLOSED"
        elif board[y_start - 1][x_start + 1] == " " and board[y_end + 1][x_end - 1] != " ":
            return "SEMIOPEN"
        elif board[y_start - 1][x_start + 1] != " " and board[y_end + 1][x_end - 1] == " ":
            return "SEMIOPEN"

    pass

def detect_row(board, col, y_start, x_start, length, d_y, d_x):
    # looks for sequences with empty spots around them to put down a col

    # function gives board, col, start coordinates, length of sequence, and direction
    # with the start coordinates, find out the sequence

    # loop through the row, and when a sequence of length length is found
    # put the end coordinates through the is_bounded function, and if they return
    # open or semi-open add 1 to the number of sequences that can be added to in that row in that direction of that length

    #print("X_Start: " + str(x_start))
    #print("Y_Start: " + str(y_start))
    #print("Length: " + str(length))
    #print("Direction: " + str(d_y) + "," + str(d_x))

    num_open_sequences = 0
    num_semiopen_sequences = 0
    x_end = 0
    y_end = 0

    stones = 0 # when stones reaches length, add 1 to either num

    # LEFT TO RIGHT DIRECTION

    if d_y == 0 and d_x == 1:   # -

        # while it's the right colour, loop through, stop the loop if you get to a diff colour or space

        for i in range (x_start, len(board[y_start]), 1):
            #print("going through " + str(y_start) + " " + str(i))

            if board[y_start][i] == col:
                stones = stones + 1 # keep adding the stone to stones as long as it's the right colour
                #print("stones: " + str(stones))
                if i == len(board[y_start]) - 1:
                    #print("Stones: " + str(stones))
                    if stones == length:
                        # check if the sequence is open or closed
                        #print("i is: " + str(i))
                        #print("ends are: " + str(y_start) + " " + str(i - 1))
                        if is_bounded(board, y_start, i - 1, length, 0, 1) == "OPEN":
                            num_open_sequences = num_open_sequences + 1
                        elif is_bounded(board, y_start, i - 1, length, 0, 1) == "SEMIOPEN":
                            num_semiopen_sequences = num_semiopen_sequences + 1
                        elif is_bounded(board, y_start, i - 1, length, 0, 1) == "CLOSED":
                            pass
                    stones = 0

            else:
                #print("Stones: " + str(stones))
                if stones == length:
                    # check if the sequence is open or closed
                    #print("i is: " + str(i))
                    #print("ends are: " + str(y_start) + " " + str(i - 1))
                    if is_bounded(board, y_start, i - 1, length, 0, 1) == "OPEN":
                        num_open_sequences = num_open_sequences + 1
                    elif is_bounded(board, y_start, i - 1, length, 0, 1) == "SEMIOPEN":
                        num_semiopen_sequences = num_semiopen_sequences + 1
                    elif is_bounded(board, y_start, i - 1, length, 0, 1) == "CLOSED":
                        pass
                stones = 0
                #num_open_sequences = num_open_sequences
                #num_semiopen_sequences = num_semiopen_sequences

        output = (num_open_sequences, num_semiopen_sequences)
        return output

    # TOP TO BOTTOM DIRECTION

    elif d_y == 1 and d_x == 0: # |

        for i in range (y_start, len(board), 1):

            #print("going through " + str(i))


            if board[i][x_start] == col:
                stones = stones + 1

                if i == len(board) - 1: # if you reach the end of the board
                    #print("Stones: " + str(stones))

                    if stones == length:
                        # check if the sequence is open or closed
                        #print("i is: " + str(i))
                        if is_bounded(board, i - 1, x_start, length, 1, 0) == "OPEN":
                            num_open_sequences = num_open_sequences + 1
                        elif is_bounded(board, i - 1, x_start, length, 1, 0) == "SEMIOPEN":
                            num_semiopen_sequences = num_semiopen_sequences + 1
                        elif is_bounded(board, i - 1, x_start, length, 1, 0) == "CLOSED":
                            pass
                        stones = 0

            else:

                #print("Stones: " + str(stones))
                if stones == length:
                    #print("i is: " + str(i))
                    if is_bounded(board, i - 1, x_start, length, 1, 0) == "OPEN":
                        num_open_sequences = num_open_sequences + 1
                    elif is_bounded(board, i - 1, x_start, length, 1, 0) == "SEMIOPEN":
                        num_semiopen_sequences = num_semiopen_sequences + 1
                    elif is_bounded(board, i - 1, x_start, length, 1, 0) == "CLOSED":
                        pass
                stones = 0

                #print(num_open_sequences)

                #num_open_sequences = num_open_sequences
                #num_semiopen_sequences = num_semiopen_sequences

        output = (num_open_sequences, num_semiopen_sequences)
        return output

    # UPPER LEFT TO LOWER RIGHT DIRECTION
    # UPPER LEFT TO LOWER RIGHT DIRECTION
    # UPPER LEFT TO LOWER RIGHT DIRECTION

    elif d_y == 1 and d_x == 1: # \

        # both variables need to change at the same time, so keep them both in one for loop

        #if y_start >= x_start: # if y is greater, LOOP THROUGH Y

        #print(y_start)
        #print(x_start)
        while y_start >= 0 and y_start <= 7 and x_start >= 0 and x_start <= 7:

            # loop through one row

            #print("Going through " + str(y_start) + " " + str(x_start))

            if board[y_start][x_start] == col:
                stones = stones + 1
                #print("Stone detected")

            else: # if the board and col doesn't match

                #print("num stones: " + str(stones))
                if stones == length: # if stones is the right length

                    # is_bounded needs the end of the sequence, not the start

                    #print("working")
                    x_end = x_start - 1 # CHANGED THIS AND LINE BELOW

                    y_end = y_start - 1

                    if is_bounded(board, y_end, x_end, length, 1, 1) == "OPEN":
                        num_open_sequences = num_open_sequences + 1
                        #print("added to num open")

                    elif is_bounded(board, y_end, x_end, length, 1, 1) == "SEMIOPEN":
                        num_semiopen_sequences = num_semiopen_sequences + 1
                        #print("added to num semiopen")

                    elif is_bounded(board, y_end, x_end, length, 1, 1) == "CLOSED":
                        pass

                stones = 0

            x_start = x_start + 1
            y_start = y_start + 1

        else: # if the end of the board is reached
            #print("end: " + str(y_start) + " " + str(x_start))
            #print("num stones: " + str(stones))
            #print("length: " + str(length))

            if stones == length:
                x_end = x_start - 1
                y_end = y_start - 1

                #print("y_end: " + str(y_end))
                #print("x_end: " + str(x_end))

                if is_bounded(board, y_end, x_end, length, 1, 1) == "OPEN":
                    num_open_sequences = num_open_sequences + 1
                    #print("added to num open")

                elif is_bounded(board, y_end, x_end, length, 1, 1) == "SEMIOPEN":
                    num_semiopen_sequences = num_semiopen_sequences + 1
                    #print("added to num semiopen")

                elif is_bounded(board, y_end, x_end, length, 1, 1) == "CLOSED":
                    pass

            stones = 0


        output = (num_open_sequences, num_semiopen_sequences)
        return output


    # UPPER RIGHT TO LOWER LEFT DIRECTION
    # UPPER RIGHT TO LOWER LEFT DIRECTION
    # UPPER RIGHT TO LOWER LEFT DIRECTION


    elif d_y == 1 and d_x == -1: # /


        # both variables need to change at the same time, so keep them both in one for loop
        # both variables need to change at the same time, so keep them both in one for loop

        #if y_start >= x_start: # if y is greater, LOOP THROUGH Y

        #print(y_start)
        #print(x_start)
        while y_start >= 0 and y_start <= 7 and x_start >= 0 and x_start <= 7:

            # loop through one row

            #print("Going through " + str(y_start) + " " + str(x_start))

            if board[y_start][x_start] == col:
                stones = stones + 1
                #print("Stone detected")

            else: # if the board and col doesn't match

                #print("num stones: " + str(stones))

                if stones == length: # if stones is the right length

                    # is_bounded needs the end of the sequence, not the start
                    #print("stones: " + str(stones))
                    x_end = x_start + 1
                    y_end = y_start - 1
                    #print_board(board)

                    #print(str(y_start) + " " + str(x_start))
                    #print(str(y_end) + " " + str(x_end))

                    # is bounded gets the ends
                    if is_bounded(board, y_end, x_end, length, 1, -1) == "OPEN":
                        num_open_sequences = num_open_sequences + 1
                        #print("added to num open")

                    elif is_bounded(board, y_end, x_end, length, 1, -1) == "SEMIOPEN":
                        num_semiopen_sequences = num_semiopen_sequences + 1
                        #print("added to num semiopen")

                    elif is_bounded(board, y_end, x_end, length, 1, -1) == "CLOSED":
                        pass

                stones = 0

            x_start = x_start - 1
            y_start = y_start + 1

        else: # if the end of the board is reached
            #print("end: " + str(y_start) + " " + str(x_start))
            #print("num stones: " + str(stones))
            #print("length: " + str(length))

            if stones == length:
                x_end = x_start
                y_end = y_end

                if is_bounded(board, y_end, x_end, length, 1, -1) == "OPEN":
                    num_open_sequences = num_open_sequences + 1
                    #print("added to num open")

                elif is_bounded(board, y_end, x_end, length, 1, -1) == "SEMIOPEN":
                    num_semiopen_sequences = num_semiopen_sequences + 1
                    #print("added to num semiopen")

                elif is_bounded(board, y_end, x_end, length, 1, -1) == "CLOSED":
                    pass

            stones = 0


        output = (num_open_sequences, num_semiopen_sequences)
        #print("upper right to lower left: " + str(output))
        return output


    pass








def detect_closed_row(board, col, y_start, x_start, length, d_y, d_x):
    # looks for closed sequences as well as semiopen and open

    # function gives board, col, start coordinates, length of sequence, and direction
    # with the start coordinates, find out the sequence

    # loop through the row, and when a sequence of length length is found
    # put the end coordinates through the is_bounded function, and if they return
    # open or semi-open add 1 to the number of sequences that can be added to in that row in that direction of that length

    num_open_sequences = 0
    num_semiopen_sequences = 0
    num_closed_sequences = 0
    stones = 0 # when stones reaches length, add 1 to either num
    x_end = 0
    y_end = 0

    # LEFT TO RIGHT DIRECTION
    # LEFT TO RIGHT DIRECTION

    if d_y == 0 and d_x == 1:   # -

        # while it's the right colour, loop through, stop the loop if you get to a diff colour or space

        for i in range (x_start, len(board[y_start]), 1):
            #print("going through " + str(i))

            if board[y_start][i] == col:
                stones = stones + 1 # keep adding the stone to stones as long as it's the right colour

                if i == len(board[y_start]) - 1:
                    #print("Stones: " + str(stones))
                    if stones == length:
                        # check if the sequence is open or closed
                        #print("i is: " + str(i))
                        if is_bounded(board, y_start, i - 1, length, 0, 1) == "OPEN":
                            num_open_sequences = num_open_sequences + 1
                        elif is_bounded(board, y_start, i - 1, length, 0, 1) == "SEMIOPEN":
                            num_semiopen_sequences = num_semiopen_sequences + 1
                        elif is_bounded(board, y_start, i - 1, length, 0, 1) == "CLOSED":
                            num_closed_sequences = num_closed_sequences + 1
                            pass
                    stones = 0

            else:
                #print("Stones: " + str(stones))
                if stones == length:
                    # check if the sequence is open or closed
                    #print("i is: " + str(i))
                    if is_bounded(board, y_start, i - 1, length, 0, 1) == "OPEN":
                        num_open_sequences = num_open_sequences + 1
                    elif is_bounded(board, y_start, i - 1, length, 0, 1) == "SEMIOPEN":
                        num_semiopen_sequences = num_semiopen_sequences + 1
                    elif is_bounded(board, y_start, i - 1, length, 0, 1) == "CLOSED":
                        num_closed_sequences = num_closed_sequences + 1
                        pass
                stones = 0
                #num_open_sequences = num_open_sequences
                #num_semiopen_sequences = num_semiopen_sequences

        output = (num_open_sequences, num_semiopen_sequences, num_closed_sequences)
        return output

    # TOP TO BOTTOM DIRECTION

    elif d_y == 1 and d_x == 0: # |

        for i in range (y_start, len(board), 1):

            #print("going through " + str(i))


            if board[i][x_start] == col:
                stones = stones + 1

                if i == len(board) - 1: # if you reach the end of the board
                    #print("Stones: " + str(stones))

                    if stones == length:
                        # check if the sequence is open or closed
                        #print("i is: " + str(i))
                        if is_bounded(board, i - 1, x_start, length, 1, 0) == "OPEN":
                            num_open_sequences = num_open_sequences + 1
                        elif is_bounded(board, i - 1, x_start, length, 1, 0) == "SEMIOPEN":
                            num_semiopen_sequences = num_semiopen_sequences + 1
                        elif is_bounded(board, i - 1, x_start, length, 1, 0) == "CLOSED":
                            num_closed_sequences = num_closed_sequences + 1
                            pass
                        stones = 0

            else:

                #print("Stones: " + str(stones))
                if stones == length:
                    #print("i is: " + str(i))
                    if is_bounded(board, i - 1, x_start, length, 1, 0) == "OPEN":
                        num_open_sequences = num_open_sequences + 1
                    elif is_bounded(board, i - 1, x_start, length, 1, 0) == "SEMIOPEN":
                        num_semiopen_sequences = num_semiopen_sequences + 1
                    elif is_bounded(board, i - 1, x_start, length, 1, 0) == "CLOSED":
                        num_closed_sequences = num_closed_sequences + 1
                        pass
                stones = 0

                #print(num_open_sequences)

                #num_open_sequences = num_open_sequences
                #num_semiopen_sequences = num_semiopen_sequences

        output = (num_open_sequences, num_semiopen_sequences, num_closed_sequences)
        return output

    # UPPER LEFT TO LOWER RIGHT DIRECTION
    # UPPER LEFT TO LOWER RIGHT DIRECTION
    # UPPER LEFT TO LOWER RIGHT DIRECTION

    elif d_y == 1 and d_x == 1: # \

        # both variables need to change at the same time, so keep them both in one for loop

        #if y_start >= x_start: # if y is greater, LOOP THROUGH Y

        #print(y_start)
        #print(x_start)
        while y_start >= 0 and y_start <= 7 and x_start >= 0 and x_start <= 7:

            # loop through one row

            #print("Going through " + str(y_start) + " " + str(x_start))

            if board[y_start][x_start] == col:
                stones = stones + 1
                #print("Stone detected")

            else: # if the board and col doesn't match

                #print("num stones: " + str(stones))
                if stones == length: # if stones is the right length

                    # is_bounded needs the end of the sequence, not the start


                    x_end = x_start - 1

                    y_end = y_start - 1



                    if is_bounded(board, y_end, x_end, length, 1, 1) == "OPEN":
                        num_open_sequences = num_open_sequences + 1
                        #print("added to num open")

                    elif is_bounded(board, y_end, x_end, length, 1, 1) == "SEMIOPEN":
                        num_semiopen_sequences = num_semiopen_sequences + 1
                        #print("added to num semiopen")

                    elif is_bounded(board, y_end, x_end, length, 1, 1) == "CLOSED":
                        num_closed_sequences = num_closed_sequences + 1
                        pass

                stones = 0

            x_start = x_start + 1
            y_start = y_start + 1

        else: # if the end of the board is reached
            #print("end: " + str(y_start) + " " + str(x_start))
            #print("num stones: " + str(stones))
            #print("length: " + str(length))

            if stones == length:
                x_end = x_start
                y_end = y_end

                if is_bounded(board, y_end, x_end, length, 1, 1) == "OPEN":
                    num_open_sequences = num_open_sequences + 1
                    #print("added to num open")

                elif is_bounded(board, y_end, x_end, length, 1, 1) == "SEMIOPEN":
                    num_semiopen_sequences = num_semiopen_sequences + 1
                    #print("added to num semiopen")

                elif is_bounded(board, y_end, x_end, length, 1, 1) == "CLOSED":
                    num_closed_sequences = num_closed_sequences + 1
                    pass

            stones = 0


        output = (num_open_sequences, num_semiopen_sequences, num_closed_sequences)
        return output


    # UPPER RIGHT TO LOWER LEFT DIRECTION
    # UPPER RIGHT TO LOWER LEFT DIRECTION
    # UPPER RIGHT TO LOWER LEFT DIRECTION


    elif d_y == 1 and d_x == -1: # /


        # both variables need to change at the same time, so keep them both in one for loop
        # both variables need to change at the same time, so keep them both in one for loop

        #if y_start >= x_start: # if y is greater, LOOP THROUGH Y

        #print(y_start)
        #print(x_start)
        while y_start >= 0 and y_start <= 7 and x_start >= 0 and x_start <= 7:

            # loop through one row

            #print("Going through " + str(y_start) + " " + str(x_start))

            if board[y_start][x_start] == col:
                stones = stones + 1
                #print("Stone detected")

            else: # if the board and col doesn't match

                #print("num stones: " + str(stones))
                if stones == length: # if stones is the right length

                    # is_bounded needs the end of the sequence, not the start

                    x_end = x_start + 1

                    y_end = y_start - 1

                    if is_bounded(board, y_end, x_end, length, 1, -1) == "OPEN":
                        num_open_sequences = num_open_sequences + 1
                        #print("added to num open")

                    elif is_bounded(board, y_end, x_end, length, 1, -1) == "SEMIOPEN":
                        num_semiopen_sequences = num_semiopen_sequences + 1
                        #print("added to num semiopen")

                    elif is_bounded(board, y_end, x_end, length, 1, -1) == "CLOSED":
                        num_closed_sequences = num_closed_sequences + 1
                        pass

                stones = 0

            x_start = x_start - 1
            y_start = y_start + 1

        else: # if the end of the board is reached
            #print("end: " + str(y_start) + " " + str(x_start))
            #print("num stones: " + str(stones))
            #print("length: " + str(length))

            if stones == length:
                x_end = x_start
                y_end = y_end

                if is_bounded(board, y_end, x_end, length, 1, -1) == "OPEN":
                    num_open_sequences = num_open_sequences + 1
                    #print("added to num open")

                elif is_bounded(board, y_end, x_end, length, 1, -1) == "SEMIOPEN":
                    num_semiopen_sequences = num_semiopen_sequences + 1
                    #print("added to num semiopen")

                elif is_bounded(board, y_end, x_end, length, 1, -1) == "CLOSED":
                    num_closed_sequences = num_closed_sequences + 1
                    pass

            stones = 0


        output = (num_open_sequences, num_semiopen_sequences, num_closed_sequences)
        #print("upper right to lower left: " + str(output))
        return output


    pass



def detect_rows(board, col, length):
    open_seq_count, semi_open_seq_count = 0, 0

    # go through entire board and see the open and semiopen sequences
    sequences = [0, 0]

    # look for horizontal sequences across the board

    for i in range(len(board)):


        horizontal = list(detect_row(board, col, i, 0, length, 0, 1))
        #print("going through: " + str(i) + " " + str(0))
        open = horizontal[0]
        semi = horizontal[1]
        sequences[0] = sequences[0] + open
        sequences[1] = sequences[1] + semi
        #print(semi)

        #if sequences[0] > 0:
            #print("got an open horizontal of length : " + str(length))
            #print("open total of length " + str(length) + " is " + str(sequences[0]))

       # if sequences[1] > 0:
            #print("got a semiopen horizontal of length : " + str(length))


    # look for vertical sequences across the board

    for i in range(len(board[0])):
        vertical = list(detect_row(board, col, 0, i, length, 1, 0))
        open = vertical[0]
        semi = vertical[1]
        sequences[0] = sequences[0] + open
        sequences[1] = sequences[1] + semi
        #if sequences[0] > 0:
            #print("got an open horizontal of length : " + str(length))
            #print("open total of length " + str(length) + " is " + str(sequences[0]))

        #if sequences[1] > 0:
            #print("got a semiopen vertical of length : " + str(length))

    # look for \ sequences across the board


    '''for i in range(len(board) - 1, -1, -1): # start from 7,7 to 0,7 (
        upper_left_lower_right = list(detect_row(board, col, i, len(board) - 1, length, 1, 1))
        #print("going through: " + str(i) + " " + str(len(board) - 1))
        open = upper_left_lower_right[0]
        semi = upper_left_lower_right[1]
        sequences[0] = sequences[0] + open
        sequences[1] = sequences[1] + semi
        #print(semi)
        #if sequences[0] > 0:
            #print("got an open horizontal of length : " + str(length))
            #print("open total of length " + str(length) + " is " + str(sequences[0]))

       # if sequences[1] > 0:
            #print("got a semiopen \\ of length : " + str(length))'''

    for i in range(1, len(board), 1): # start from 7,7 to 0,7 (changed to 1,0 to 7,0)
        upper_left_lower_right = list(detect_row(board, col, i, 0, length, 1, 1))
        #print("going through: " + str(i) + " " + str(len(board) - 1))
        open = upper_left_lower_right[0]
        semi = upper_left_lower_right[1]
        sequences[0] = sequences[0] + open
        sequences[1] = sequences[1] + semi
        #print(semi)
        #if sequences[0] > 0:
            #print("got an open horizontal of length : " + str(length))
            #print("open total of length " + str(length) + " is " + str(sequences[0]))

       # if sequences[1] > 0:
            #print("got a semiopen \\ of length : " + str(length))

    for i in range(len(board) - 2, -1, -1): # start from 0,6 to 0,0 (0,0 to 0,6)
        upper_left_lower_right = list(detect_row(board, col, 0, i, length, 1, 1))
        #print(upper_left_lower_right)
        #print("going through: " + str(0) + " " + str(i))
        open = upper_left_lower_right[0]
        semi = upper_left_lower_right[1]
        sequences[0] = sequences[0] + open
        sequences[1] = sequences[1] + semi
        #print(semi)
        #if sequences[0] > 0:
            #print("got an open horizontal of length : " + str(length))
        #    print("open total of length " + str(length) + " is " + str(sequences[0]))

        #if sequences[1] > 0:
        #    print("got a semiopen \\ of length : " + str(length))


    # look for / sequences across the board


    for i in range(len(board) - 2, -1, -1): # start from 0,6 to 0,0
        #print(str(0) + " " + str(i))
        upper_right_lower_left = list(detect_row(board, col, 0, i, length, 1, -1))
        #print(detect_row(board, col, 0, i, length, 1, -1))
        open = upper_right_lower_left[0]
        semi = upper_right_lower_left[1]
        sequences[0] = sequences[0] + open
        sequences[1] = sequences[1] + semi
        #if sequences[0] > 0:
            #print("got an open horizontal of length : " + str(length))
        #    print("open total of length " + str(length) + " is " + str(sequences[0]))

        #if sequences[1] > 0:
         #   print("got a semiopen // of length : " + str(length))

    for i in range(0, len(board), 1): # start from 0,7 to 7,7
        #print(str(i) + " " + str(len(board) - 1))
        upper_right_lower_left = list(detect_row(board, col, i, len(board) - 1, length, 1, -1))
        #print(detect_row(board, col, i, len(board) - 1, length, 1, -1))
        #print("taking: " + str())
        open = upper_right_lower_left[0]
        semi = upper_right_lower_left[1]
        sequences[0] = sequences[0] + open
        sequences[1] = sequences[1] + semi
       # if sequences[0] > 0:
            #print("got an open horizontal of length : " + str(length))
        #    print("open total of length " + str(length) + " is " + str(sequences[0]))

       # if sequences[1] > 0:
        #    print("got a semiopen // of length : " + str(length))


   # print("TOTAL OPEN: for length " + str(length) + " is " + str(sequences[0]))
    #print("TOTAL SEMIOPEN: for length " + str(length) + " is " + str(sequences[1]))


    total = (0,0)
    total = (sequences[0], sequences[1])

    return total
    #return open_seq_count, semi_open_seq_count

def detect_closed_rows(board, col, length):
    open_seq_count, semi_open_seq_count = 0, 0

    # go through entire board and see the open and semiopen sequences
    sequences = [0, 0, 0]

    # look for horizontal sequences across the board

    for i in range(len(board)):
        horizontal = list(detect_closed_row(board, col, i, 0, length, 0, 1))
        open = horizontal[0]
        semi = horizontal[1]
        closed = horizontal[2]
        sequences[0] = sequences[0] + open
        sequences[1] = sequences[1] + semi
        sequences[2] = sequences[2] + closed


    # look for vertical sequences across the board

    for i in range(len(board[0])):
        vertical = list(detect_closed_row(board, col, 0, i, length, 1, 0))
        open = vertical[0]
        semi = vertical[1]
        closed = vertical[2]
        sequences[0] = sequences[0] + open
        sequences[1] = sequences[1] + semi
        sequences[2] = sequences[2] + closed

    # look for \ sequences across the board
    '''for i in range(len(board) - 1, -1, -1): # start from 7,0
        upper_left_lower_right = detect_row(board, col, i, 0, length, 1, 1)
        open = upper_left_lower_right[0]
        semi = upper_left_lower_right[1]
        sequences[0] = sequences[0] + open
        sequences[1] = sequences[1] + semi

    for i in range(0, len(board), 1): # start from 0,0 to 0,7
        upper_left_lower_right = detect_row(board, col, 0, i, length, 1, 1)
        open = upper_left_lower_right[0]
        semi = upper_left_lower_right[1]
        sequences[0] = sequences[0] + open
        sequences[1] = sequences[1] + semi'''



    '''for i in range(len(board) - 1, -1, -1): # start from 7,7 to 0,7
        upper_left_lower_right = list(detect_closed_row(board, col, i, len(board) - 1, length, 1, 1))
        open = upper_left_lower_right[0]
        semi = upper_left_lower_right[1]
        closed = upper_left_lower_right[2]
        sequences[0] = sequences[0] + open
        sequences[1] = sequences[1] + semi
        sequences[2] = sequences[2] + closed'''

    for i in range(1, len(board), 1): # start from 7,7 to 0,7 (changed to 1,0 to 7,0)
        upper_left_lower_right = list(detect_closed_row(board, col, i, 0, length, 1, 1))
        #print("going through: " + str(i) + " " + str(len(board) - 1))
        open = upper_left_lower_right[0]
        semi = upper_left_lower_right[1]
        closed = upper_left_lower_right[2]
        sequences[0] = sequences[0] + open
        sequences[1] = sequences[1] + semi
        sequences[2] = sequences[2] + closed
        #print(semi)

    for i in range(len(board) - 2, -1, -1): # start from 0,6 to 0,0
        upper_left_lower_right = list(detect_closed_row(board, col, 0, i, length, 1, 1))
        open = upper_left_lower_right[0]
        semi = upper_left_lower_right[1]
        closed = upper_left_lower_right[2]
        sequences[0] = sequences[0] + open
        sequences[1] = sequences[1] + semi
        sequences[2] = sequences[2] + closed


    # look for / sequences across the board
    '''for i in range(0, len(board), 1): # start from 0,0 to 0,7
        print(str(0) + " " + str(i))
        upper_right_lower_left = detect_row(board, col, 0, i, length, 1, -1)
        open = upper_left_lower_right[0]
        semi = upper_left_lower_right[1]
        sequences[0] = sequences[0] + open
        sequences[1] = sequences[1] + semi

    for i in range(len(board) - 1, -1, -1): # start from 7,0 to 0,0
        print(str(i) + " " + str(0))
        upper_right_lower_left = detect_row(board, col, i, 0, length, 1, -1)
        open = upper_left_lower_right[0]
        semi = upper_left_lower_right[1]
        sequences[0] = sequences[0] + open
        sequences[1] = sequences[1] + semi'''

    for i in range(len(board) - 2, -1, -1): # start from 0,6 to 0,0
        #print(str(0) + " " + str(i))
        upper_right_lower_left = list(detect_closed_row(board, col, 0, i, length, 1, -1))
        #print(detect_row(board, col, 0, i, length, 1, -1))
        open = upper_right_lower_left[0]
        semi = upper_right_lower_left[1]
        closed = upper_right_lower_left[2]
        sequences[0] = sequences[0] + open
        sequences[1] = sequences[1] + semi
        sequences[2] = sequences[2] + closed

    for i in range(0, len(board), 1): # start from 0,7 to 7,7
        #print(str(i) + " " + str(len(board) - 1))
        upper_right_lower_left = list(detect_closed_row(board, col, i, len(board) - 1, length, 1, -1))
        #print(detect_row(board, col, i, len(board) - 1, length, 1, -1))
        #print("taking: " + str())
        open = upper_right_lower_left[0]
        semi = upper_right_lower_left[1]
        closed = upper_right_lower_left[2]
        sequences[0] = sequences[0] + open
        sequences[1] = sequences[1] + semi
        sequences[2] = sequences[2] + closed





    total = (0,0,0)
    total = (sequences[0], sequences[1], sequences[2])

    return total
    #return open_seq_count, semi_open_seq_count

def search_max(board): # find the location (y,x) where black can move for the highest score

    # find available empty squares where black can go

    available_squares = []
    sample_board = board
    highest_score = 0

    for i in range(0, 8, 1):
        for k in range(0, 8, 1):
            if board[i][k] == " ":
                #print("here: " + str(board[i][k]))
                available_squares.append([i, k])
                #print(available_squares)

    best_move = available_squares[0]

    # move to those squares on the sample board and test their scores

    for i in range(len(available_squares)):
        sample_board[available_squares[i][0]][available_squares[i][1]] = "b"
        current_score = score(board) # find the total score with that move on the sample board

        #print("Highest Score: " + str(highest_score) + " Current_Score: " + str(current_score))

        if current_score > highest_score: # keep a running variable of the highest score
            highest_score = current_score
            best_move = available_squares[i]

        sample_board[available_squares[i][0]][available_squares[i][1]] = " "


    best = (best_move[0], best_move[1])

    return best
    return move_y, move_x

def score(board): # assuming black has just moved (the computer), gives you the score for the position of the board

    MAX_SCORE = 100000

    open_b = {}
    semi_open_b = {}
    open_w = {}
    semi_open_w = {}

    for i in range(2, 6):
        open_b[i], semi_open_b[i] = detect_rows(board, "b", i)
        open_w[i], semi_open_w[i] = detect_rows(board, "w", i)


    if open_b[5] >= 1 or semi_open_b[5] >= 1:
        return MAX_SCORE

    elif open_w[5] >= 1 or semi_open_w[5] >= 1:
        return -MAX_SCORE

    return (-10000 * (open_w[4] + semi_open_w[4])+
            500  * open_b[4]                     +
            50   * semi_open_b[4]                +
            -100  * open_w[3]                    +
            -30   * semi_open_w[3]               +
            50   * open_b[3]                     +
            10   * semi_open_b[3]                +
            open_b[2] + semi_open_b[2] - open_w[2] - semi_open_w[2])

def is_full(board):
    for k in range(len(board)):
        for i in range(len(board[0])):
            #print(board[k][i])
            if board[k][i] != " ":
                pass
            else:
                return False

    return True

def is_win(board):

    # if black wins

    black = detect_closed_rows(board, "b", 5) # check for open, semiopen, closed
    black_list = list(black)
    if black_list[0] >= 1:
        return "Black won"
    elif black_list[1] >= 1:
        return "Black won"
    elif black_list[2] >= 1:
        return "Black won"

    # if white wins

    white = detect_closed_rows(board, "w", 5) # check for open, semiopen, closed
    white_list = list(white)
    if white_list[0] >= 1:
        return "White won"
    elif white_list[1] >= 1:
        return "White won"
    elif white_list[2] >= 1:
        return "White won"

    # if the board is empty

    if is_empty(board) == True:
        return "Continue playing"

    if is_full(board) == True:
        return "Draw" # if board is full and no winner

    return "Continue playing"


def print_board(board):

    s = "*"
    for i in range(len(board[0])-1):
        s += str(i%10) + "|"
    s += str((len(board[0])-1)%10)
    s += "*\n"

    for i in range(len(board)):
        s += str(i%10)
        for j in range(len(board[0])-1):
            s += str(board[i][j]) + "|"
        s += str(board[i][len(board[0])-1])

        s += "*\n"
    s += (len(board[0])*2 + 1)*"*"

    print(s)


def make_empty_board(sz):
    board = []
    for i in range(sz):
        board.append([" "]*sz)
    return board



def analysis(board):
    for c, full_name in [["b", "Black"], ["w", "White"]]:
        #print("%s stones" % (full_name))
        for i in range(2, 6):
            open, semi_open = detect_rows(board, c, i);
            #print("Open rows of length %d: %d" % (i, open))
            #print("Semi-open rows of length %d: %d" % (i, semi_open))






def play_gomoku(board_size):
    board = make_empty_board(board_size)
    board_height = len(board)
    board_width = len(board[0])

    while True:
        print_board(board)
        if is_empty(board):
            move_y = board_height // 2
            move_x = board_width // 2
        else:
            move_y, move_x = search_max(board)

        print("Computer move: (%d, %d)" % (move_y, move_x))
        board[move_y][move_x] = "b"
        print_board(board)
        analysis(board)

        game_res = is_win(board)
        if game_res in ["White won", "Black won", "Draw"]:
            return game_res





        print("Your move:")
        move_y = int(input("y coord: "))
        move_x = int(input("x coord: "))
        board[move_y][move_x] = "w"
        print_board(board)
        analysis(board)

        game_res = is_win(board)
        if game_res in ["White won", "Black won", "Draw"]:
            return game_res



def put_seq_on_board(board, y, x, d_y, d_x, length, col):
    for i in range(length):
        board[y][x] = col
        y += d_y
        x += d_x


def test_is_empty():
    board  = make_empty_board(8)
    if is_empty(board):
        print("TEST CASE for is_empty PASSED")
    else:
        print("TEST CASE for is_empty FAILED")

def test_is_bounded():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)

    y_end = 3
    x_end = 5

    if is_bounded(board, y_end, x_end, length, d_y, d_x) == 'OPEN':
        print("TEST CASE for is_bounded PASSED")
    else:
        print("TEST CASE for is_bounded FAILED")


def test_detect_row():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    if detect_row(board, "w", 0,x,length,d_y,d_x) == (1,0):
        print("TEST CASE for detect_row PASSED")
    else:
        print("TEST CASE for detect_row FAILED")

def test_detect_rows():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3; col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    if detect_rows(board, col,length) == (1,0):
        print("TEST CASE for detect_rows PASSED")
    else:
        print("TEST CASE for detect_rows FAILED")

def test_search_max():
    board = make_empty_board(8)
    x = 5; y = 0; d_x = 0; d_y = 1; length = 4; col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    x = 6; y = 0; d_x = 0; d_y = 1; length = 4; col = 'b'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    print_board(board)
    if search_max(board) == (4,6):
        print("TEST CASE for search_max PASSED")
    else:
        print("TEST CASE for search_max FAILED")

def easy_testset_for_main_functions():
    test_is_empty()
    test_is_bounded()
    test_detect_row()
    test_detect_rows()
    test_search_max()

def some_tests():
    board = make_empty_board(8)

    board[0][5] = "w"
    board[0][6] = "b"
    y = 5; x = 2; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    analysis(board)

    # Expected output:
    #       *0|1|2|3|4|5|6|7*
    #       0 | | | | |w|b| *
    #       1 | | | | | | | *
    #       2 | | | | | | | *
    #       3 | | | | | | | *
    #       4 | | | | | | | *
    #       5 | |w| | | | | *
    #       6 | |w| | | | | *
    #       7 | |w| | | | | *
    #       *****************
    #       Black stones:
    #       Open rows of length 2:      0
    #       Semi-open rows of length 2: 0
    #       Open rows of length 3:      0
    #       Semi-open rows of length 3: 0
    #       Open rows of length 4:      0
    #       Semi-open rows of length 4: 0
    #       Open rows of length 5:      0
    #       Semi-open rows of length 5: 0
    #       White stones:
    #       Open rows of length 2:      0
    #       Semi-open rows of length 2: 0
    #       Open rows of length 3:      0
    #       Semi-open rows of length 3: 1
    #       Open rows of length 4:      0
    #       Semi-open rows of length 4: 0
    #       Open rows of length 5:      0
    #       Semi-open rows of length 5: 0

    y = 3; x = 5; d_x = -1; d_y = 1; length = 2

    put_seq_on_board(board, y, x, d_y, d_x, length, "b")
    print_board(board)
    analysis(board)

    # Expected output:
    #        *0|1|2|3|4|5|6|7*
    #        0 | | | | |w|b| *
    #        1 | | | | | | | *
    #        2 | | | | | | | *
    #        3 | | | | |b| | *
    #        4 | | | |b| | | *
    #        5 | |w| | | | | *
    #        6 | |w| | | | | *
    #        7 | |w| | | | | *
    #        *****************
    #
    #         Black stones:
    #         Open rows of length 2:      1    #problem
    #         Semi-open rows of length 2: 0
    #         Open rows of length 3:      0
    #         Semi-open rows of length 3: 0
    #         Open rows of length 4:      0
    #         Semi-open rows of length 4: 0
    #         Open rows of length 5:      0
    #         Semi-open rows of length 5: 0
    #         White stones:
    #         Open rows of length 2:      0
    #         Semi-open rows of length 2: 0
    #         Open rows of length 3:      0
    #         Semi-open rows of length 3: 1
    #         Open rows of length 4:      0
    #         Semi-open rows of length 4: 0
    #         Open rows of length 5:      0
    #         Semi-open rows of length 5: 0
    #

    y = 5; x = 3; d_x = -1; d_y = 1; length = 1
    put_seq_on_board(board, y, x, d_y, d_x, length, "b");
    print_board(board);
    analysis(board);

    #        Expected output:
    #           *0|1|2|3|4|5|6|7*
    #           0 | | | | |w|b| *
    #           1 | | | | | | | *
    #           2 | | | | | | | *
    #           3 | | | | |b| | *
    #           4 | | | |b| | | *
    #           5 | |w|b| | | | *
    #           6 | |w| | | | | *
    #           7 | |w| | | | | *
    #           *****************
    #
    #
    #        Black stones:
    #        Open rows of length 2:      0
    #        Semi-open rows of length 2: 0
    #        Open rows of length 3:      0
    #        Semi-open rows of length 3: 1 # problem
    #        Open rows of length 4:      0
    #        Semi-open rows of length 4: 0
    #        Open rows of length 5:      0
    #        Semi-open rows of length 5: 0
    #        White stones:
    #        Open rows of length 2:      0
    #        Semi-open rows of length 2: 0
    #        Open rows of length 3:      0
    #        Semi-open rows of length 3: 1 # but this works for some reason why is that
    #        Open rows of length 4:      0
    #        Semi-open rows of length 4: 0
    #        Open rows of length 5:      0
    #        Semi-open rows of length 5: 0




if __name__ == '__main__':

    play_gomoku(8)
    #bb = make_empty_board(8)
    #print_board(bb)
    #print(is_empty(bb))
    #board = make_empty_board(8)

    '''board[4][5] = "w"
    board[5][5] = "w"
    board[6][5] = "w"
    board[7][5] = "w"

    board[2][0] = "w"
    board[2][1] = "w"

    board[1][3] = "b"
    board[2][4] = "b"
    board[1][5] = "b"
    board[2][6] = "b"

    board[4][6] = "b"
    board[5][7] = "b"

    board[5][1] = "b"
    board[4][2] = "b"

    board[3][2] = "b"
    board[4][1] = "b"
    #board[3][7] = "w"

    board[5][3] = "w"
    board[6][2] = "w"
    #board[7][1] = "w"

    #board[0][6] = "b"'''

    '''board[0][5] = "w"
    board[0][6] = "b"

    board[3][5] = "b"
    board[4][4] = "b"

    board[5][2] = "w"
    board[6][2] = "w"
    board[7][2] = "w"

    board[3][2] = "w"
    board[4][2] = "w"

    board[7][3] = "w"'''

    '''board[0][0] = "w"
    board[0][1] = "b"
    board[0][2] = "b"
    board[0][3] = "b"

    board[1][1] = "w"
    board[1][2] = "w"
    board[1][4] = "b"

    board[2][0] = "w"
    board[2][3] = "w"
    board[2][4] = "b"
    board[2][5] = "b"

    board[3][0] = "b"
    board[3][2] = "w"
    board[3][4] = "b"
    board[3][5] = "b"

    board[4][0] = "w"
    board[4][1] = "w"
    board[4][2] = "b"
    board[4][4] = "b"

    board[5][0] = "w"
    board[5][1] = "b"
    board[5][2] = "b"
    board[5][3] = "b"
    board[5][4] = "b"
    board[5][6] = "b"

    board[6][0] = "w"
    board[6][2] = "b"
    board[6][4] = "b"
    board[6][5] = "b"
    board[6][6] = "b"
    board[6][7] = "b"

    board[7][0] = "w"
    board[7][2] = "b"
    board[7][3] = "b"
    board[7][4] = "b"
    board[7][5] = "w"
    board[7][6] = "b"
    board[7][7] = "w"
    '''



    #print_board(board)
    #is_bounded(board, )

    # you won't need to use isbounded to find sequences of 2 if there are only sequences of 3
    #print(detect_row(board, "w", 0, 5, 4, 1, 0))
    #print("NEXT --------------------------------------")

    #print(detect_row(board, "w", 2, 0, 2, 0, 1 ))
    #print("NEXT NEXT ---------------------------------")

    #print(detect_row(board, "w", 0, 0, 3, 1, 1))
    #print(detect_row(board, "w", 1, 5, 3, 1, 1))
    #print(detect_row(board, "w", 2, 6, 3, 1, -1))
    #print(detect_row(board, "w", 0, 0, 3, 1, -1))
    #print(detect_row(board, "w", 0, 0, 3, 0, 1))
    #print_board(board)


    #test_detect_row()
    #test_detect_rows()
    #print(search_max(board))
    #test_search_max()
    #easy_testset_for_main_functions()
    #some_tests()



    #print_board(board)



    #detect_row(board, col, y_start, x_start, length, d_y, d_x)

    #print("First Test")
    #print(detect_row(board, "b", 0, 4, 2, 1, 1)) # \
    #print(detect_rows(board, "b", 2))

    #print("Second Test")
    #print(detect_row(board, "w", 1, 7, 2, 1, -1)) # /
    #print("result")
    #some_tests()

    #print("testing stuff")
    #print(detect_rows(board, "b", 2))

    #print(detect_row(board, "b", 0,5,2,1,-1))

    #print(detect_row(board, "b", 0, 6, 2, 1, -1))
    #print(detect_rows(board, "b", 2))

    '''print(detect_row(board, "b", 0, 2, 2, 1, 1))  # all three of the \ are working
    print(detect_row(board, "b", 0, 4, 2, 1, 1))

    print(detect_row(board, "b", 0, 6, 2, 1, -1)) # all three of this way / are working too
    print(detect_row(board, "b", 2, 3, 2, 1, -1))'''

    #some_tests()

    #print(detect_row(board, "b", 2, 6, 2, 1, -1))
    #easy_testset_for_main_functions()

    #analysis(board)
    #print(detect_rows(board, "b", 2))
    #easy_testset_for_main_functions()
    #print_board(board)
    #print(is_win(board))
    #print(detect_row(board, "w", 7, 0, 2, 0, 1))

    #analysis(board)
    #print(is_bounded(board, 3, 5, 2, 1, 0))
    #print(detect_rows(board, "b", 3))
    #print(detect_row(board, "b", 5, 6, 2, 1, 1))
    #print(detect_row(board, "w", 1, 1, 2, 0, 1))
    #print(is_bounded(board, 1, 2, 2, 0, 1))
    #is_bounded()

    #print(detect_row(board, "b", 4, 2, 2, 1, -1))
    #print(detect_row(board, "b", 2, 4, 2, 0, 1)) # left to right
    #print(detect_row(board, "b", 5, 4, 3, 1, 1))
    #print(detect_rows(board, "b", 3))
    #print(detect_rows(board, "w", 2))
    #print(is_bounded(board, 4,1 , 2, 0, 1))
    #print(board[-1][0])

    #some_tests()
    #easy_testset_for_main_functions()


    #print_board(board)
    #print_board(board[-1][0])

    #board = [[' ', ' ', ' ', 'w', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', 'b', ' ', ' ', ' ', ' '], [' ', ' ', ' ', 'b', ' ', ' ', ' ', 'b'], ['w', ' ', ' ', 'b', ' ', ' ', ' ', ' '], [' ', 'w', 'w', 'b', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]

    #print_board(board)

    #print(detect_row(board, "w", 5, 0, 2, 1, 1))
    #print(detect_row(board, "w", 6, 1, 2, 0, 1))

    #print(detect_rows(board, "w", 2))
    #easy_testset_for_main_functions()
    #some_tests()

    #board = [['w', ' ', ' ', ' ', ' ', ' ', ' ', 'w'], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', 'w', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], ['w', ' ', ' ', ' ', ' ', ' ', ' ', ' '], ['w', ' ', ' ', 'b', ' ', ' ', ' ', ' '], ['w', ' ', ' ', ' ', 'b', ' ', 'w', 'w'], ['w', ' ', 'w', ' ', 'b', ' ', ' ', ' ']]

    #print_board(board)
    #print(detect_rows(board, "w", 2))

    #print(is_bounded(board, 6, 7, 2, 0, 1))
    #some_tests()

    #print_board(board)
    #print(is_win(board))




