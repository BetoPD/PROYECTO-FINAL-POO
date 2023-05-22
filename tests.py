def lineSegments(p0, p1, p2, p3):
    A1 = p1[1] - p0[1]
    B1 = p0[0] - p1[0]
    C1 = A1 * p0[0] + B1 * p0[1]
    A2 = p3[1] - p2[0]
    B2 = p2[0] - p3[0]
    C2 = A2 * p2[0] + B2 * p2[1]

    print("A1:", A1, "B1:",B1,"C1:",C1)
    print("A2:", A2, "B2:",B2,"C2:",C2)

    denominator = A1 * B2 - A2 * B1
    
    if denominator == 0:
        return False 
    
    # if (C1 / B1) == (C2 / B2):
    #     return True
    
    intersectx = (B2 * C1 - B1 * C2) / denominator
    intersecty = (A1 * C2 - A2 * C1) / denominator
    rx0 = (intersectx - p0[0]) / (p1[0] - p0[0])
    ry0 = (intersecty - p0[1]) / (p1[1] - p0[1])
    rx1 = (intersectx - p2[0]) / (p3[0] - p2[0])
    ry1 = (intersecty - p2[1]) / (p3[1] - p2[1])
    if((rx0 >= 0 and rx0 <=1) or (ry0 >= 0 and ry0 <=1)) and ((rx1 >= 0 and rx1 <=1) or (ry1 >= 0 and ry1 <=1)):
        return True
    else:
        return False

print(lineSegments((0,0),(0,5),(0,1),(5,1)))