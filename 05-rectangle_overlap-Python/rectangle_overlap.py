# rectanglesOverlap(left1, top1, width1, height1, left2, top2, width2, height2)
# A rectangle can be described by its left, top, width, and height. This function 
# takes two rectangles described this way, and returns True if the rectangles 
# overlap at all (even if just at a point), and False otherwise. 
# Note: here we will represent coordinates the way they are usually represented in 
# computer graphics, where (0,0) is at the left-top corner of the screen, and while 
# the x-coordinate goes up while you head right, the y-coordinate goes up while you 
# head down (so we say that "up is down")


def getCoordinates(left, top, width, height):
    right = left + width
    bottom = top + height
    return (left, right, top, bottom)

def fun_rectangle_overlap(left1, top1, width1, height1, left2, top2, width2, height2):
    (l1, r1, t1, b1) = getCoordinates(left1, top1, width1, height1)
    (l2, r2, t2, b2) = getCoordinates(left2, top2, width2, height2)
    if l1 <= l2 and r1 >= l2:
        return True
    if l1 <= r2 and r1 >= r2:
        return True
    if t1 <= t2 and b1 >= t2:
        return True
    if t1 <= b2 and b1 >= b2:
        return True
    return False
        