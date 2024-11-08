def cube_checker(volume, side):
    # should satisfy all conditions
    # is a cube and the must be a valid number
    # volume and side must be greater than zero
    return volume == side * side * side and (volume > 0 or side > 0)