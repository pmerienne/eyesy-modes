from vsl import atom, system

from vsl.color import *


def grid(
        nb_columns=2,
        nb_rows=2,
        cell=lambda row, col: atom.rectangle((0.1, 0.1), 0.9, 0.9, WHITE)
    ):
    full_width, full_height = system.screen.get_size()
    cell_width = int(full_width / nb_columns)
    cell_height = int(full_height / nb_rows)

    for row in range(nb_rows):
        for col in range(nb_columns):
            x = int(col * cell_width)
            y = int(row * cell_height)
            position = (x, y)
            with system.sub_screen(position, cell_width, cell_height):
                cell(row, col)

