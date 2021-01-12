def reRange(point1, point2, point3, point4):
    pointList = [point1, point2, point3, point4]
    leftBottomPoint = point1
    rightBottomPoint = point1
    leftTopPoint = [0, 0]
    rightTopPoint = [0, 0]
    for point in pointList:
        print(point[0], leftBottomPoint[0])
        # find the leftest point in the imageView
        if point[0] < leftBottomPoint[0]:
            leftBottomPoint = point
        # find the rightest point in the imageView
        elif point[0] > rightBottomPoint[0]:
            rightBottomPoint = point

    for point in pointList:
        if point != leftBottomPoint and point != rightBottomPoint:

            # if the point doesn't belong to both of them
            # it's one of the top points
            if leftTopPoint != [0, 0]:
                if leftTopPoint[0] > point[0]:
                    rightTopPoint = leftTopPoint
                    leftTopPoint = point
                else:
                    rightTopPoint = point
            else:
                leftTopPoint = point
    point1 = leftTopPoint
    point2 = leftBottomPoint
    point3 = rightBottomPoint
    point4 = rightTopPoint
    return point1, point2, point3, point4
