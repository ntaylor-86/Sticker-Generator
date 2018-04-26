#!/usr/bin/env python

import labels
from reportlab.graphics import shapes
from collections import namedtuple

# Create an A4 portrait (210mm x 297mm) sheet with 3 columns and 11 rows of
# labels. Each label is 64mm x 24.3mm with a 2mm rounded corner. The margins are
# automatically calculated.
# left_margin is 7, top_margin is 15, column_gap is 2.7
specs = labels.Specification(210, 297, 3, 11, 63.6, 24.1, corner_radius=2,
                             left_padding=3, bottom_padding=1.5, left_margin=6.5, top_margin=16,
                             row_gap=0.5, column_gap=2.7)

part_number_array = ['vars2000', 'vars2001', 'vars2002', 'vars2003', 'vars2004', 'vars2005']
rev_array = ['A', 'B', 'C', 'F', 'A', 'D']
qty_array = ['10', '15', '20', '8', '10', '12']

Part = namedtuple(
    'Part',
    ['first_line', 'division', 'kit_number', 'part_number', 'rev', 'qty'])

def draw_part(label, width, height, part):
    lines = [
        part.qty,
        part.rev,
        part.part_number.upper(),
        part.kit_number,
        part.division,
        part.first_line
    ]

    group = shapes.Group()
    x, y = 0, 0

    for line in lines:
        if not line:
            continue
        shape = shapes.String(x, y, line, textAnchor="start", fontName="Helvetica", fontSize=6)
        # _, _, _, y = shape.getBounds()
        y += 11
        group.add(shape)
    # _, _, lx, ly = label.getBounds()
    # _, _, gx, gy = group.getBounds()

    label.add(group)

sheet = labels.Sheet(specs, draw_part, border=True)

# for counter, item in enumerate(part_number_array):
#     part = Part("PART NUMBER: " + str(part_number_array[counter]), "REV: " + str(rev_array[counter]), "QTY: " + str(qty_array[counter]))
#     print part
#     sheet.add_label(part)

job_number = '87906'
kit_no = 'WC-3'

counter = 1
while counter <= 100:
    part = Part("VARLEY-TOMAGO" + (" "*45) + job_number + "-" + str(counter),
                "DIVISION: DEFENCE & AERO",
                "KIT NUMBER: " + kit_no,
                "PART NUMBER: " + str(counter),
                "REV: " + str(counter),
                "QTY: " + str(counter))
    sheet.add_label(part)
    counter += 1

sheet.save('new-label.pdf')