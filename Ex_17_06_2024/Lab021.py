# tuple with user defined function
def make_pizza(*topings):
    print(topings)
    for topins in topings:
        print(topins)
sipu= make_pizza("paneer")
bishnu=make_pizza("mushrooms","tomatos","cucumbers")

'''O/P: ('paneer',)
paneer
('mushrooms', 'tomatos', 'cucumbers')
mushrooms
tomatos
cucumbers'''