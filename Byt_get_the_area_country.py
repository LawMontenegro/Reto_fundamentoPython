def area_of_country(name, area):
    world_area = 148940000
    resulta = round(area / world_area,4 )
    # print(resulta)
    return (f"{name} is {resulta:.2%}% of the total world's landmass")

print(area_of_country("USA", 9372610))