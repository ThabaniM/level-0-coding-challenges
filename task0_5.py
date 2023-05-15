def area_of_triangle(side_a, side_b, side_c):
    semiperimeter = (1 / 2) * (side_a + side_b + side_c)
    area = (
        semiperimeter
        * (semiperimeter - side_a)
        * (semiperimeter - side_b)
        * (semiperimeter - side_c)
    ) ** (1 / 2)
    return area

answer = area_of_triangle(3, 4, 5)

print("The area is equal to", answer, "units squared")

if __name__ ==  "__main__":
    answer = area_of_triangle(3, 4, 5)
    print('The area is equal to', answer, 'units squared')