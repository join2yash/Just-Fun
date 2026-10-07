def count_squares(floors):

    total = 0

    # size represents the size of the square
    #
    # size = 1 → 1x1 squares
    # size = 2 → 2x2 squares
    # size = 3 → 3x3 squares
    # ...
    for size in range(1, floors + 1):

        # If the big grid is 5x5 and we want
        # 2x2 squares:
        #
        # There are 4 possible positions
        # horizontally and 4 vertically.
        #
        # Therefore:
        # 4 * 4 = 16
        positions = (floors - size + 1) ** 2

        total += positions

    return total

def count_rectangles(floors):

    # A grid with 5 columns has 6 vertical lines.
    # A grid with 5 rows has 6 horizontal lines.
    lines = floors + 1

    # Number of ways to choose 2 things from N things:
    #
    # N * (N - 1) / 2
    #
    # We need to choose:
    # 2 vertical lines
    # 2 horizontal lines
    vertical_choices = lines * (lines - 1) // 2
    horizontal_choices = lines * (lines - 1) // 2

    # Every vertical pair can be combined with
    # every horizontal pair.
    total = vertical_choices * horizontal_choices

    return total

def count_triangles(floors):

    # -----------------------------------------
    # Count upward-pointing triangles.
    # -----------------------------------------
    upward = floors * (floors + 1) * (floors + 2) // 6


    # -----------------------------------------
    # Count downward-pointing triangles.
    #
    # Downward triangles only become possible
    # when the triangle is large enough.
    # -----------------------------------------
    downward = 0

    for size in range(1, floors // 2 + 1):

        downward += (
            (floors - 2 * size + 1)
            * (floors - 2 * size + 2)
            // 2
        )


    # -----------------------------------------
    # Both directions are triangles.
    # -----------------------------------------
    return upward + downward

def count_shapes(sides, floors, shape=None):

    # -----------------------------------------
    # STEP 1: Check whether the number of floors
    # is valid.
    #
    # We cannot have 0 or negative floors.
    # -----------------------------------------
    if floors < 1:
        raise ValueError("Floors must be at least 1.")


    # -----------------------------------------
    # STEP 2: Identify the shape.
    #
    # A triangle has exactly 3 sides,
    # so we don't need the user to tell us
    # "triangle".
    # -----------------------------------------
    if sides == 3:

        shape = "triangle"


    # -----------------------------------------
    # A 4-sided shape could be many things:
    #
    # square
    # rectangle
    # trapezium
    # parallelogram
    #
    # Therefore, the user MUST tell us
    # which one they mean.
    # -----------------------------------------
    elif sides == 4:

        if shape is None:
            raise ValueError(
                "For 4 sides, please specify "
                "'square' or 'rectangle'."
            )


    # -----------------------------------------
    # We currently don't support other shapes.
    # -----------------------------------------
    else:

       raise ValueError(
           "Currently only triangle, square and rectangle are supported."
        )


    # -----------------------------------------
    # STEP 3: Make sure the requested shape
    # is actually one that we support.
    # -----------------------------------------
    shape = shape.lower()
  
    if shape not in ["triangle", "square", "rectangle"]:

        raise ValueError(
            "Supported shapes are: triangle, square, rectangle."
        )


    # -----------------------------------------
    # STEP 4: Send the problem to the correct
    # mathematical function.
    #
    # We will write these functions next.
    # -----------------------------------------
    if shape == "triangle":

        return count_triangles(floors)

    elif shape == "square":

        return count_squares(floors)

    elif shape == "rectangle":

        return count_rectangles(floors)


# print(count_shapes(4,4,"RectAngLe")) 
