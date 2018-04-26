#!/usr/bin/env python

###################################################
#  sticker-generator.py
#  Author:  nathan
#  Date:    26/04/2018
#  Brief:   a python program to scrape a jobs txt file, save
#           all the parts into arrays and then generate a pdf file
#           that is to be printed on the AVERY *(L7157REV)* sticker labels
###################################################


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


Part = namedtuple(
    'Part',
    ['gci_group', 'customer', 'division_kit_number', 'part_number', 'rev_qty'])

def draw_part(label, width, height, part):
    lines = [
        part.rev_qty,
        part.part_number,
        part.division_kit_number,
        part.customer,
        part.gci_group
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

sheet = labels.Sheet(specs, draw_part, border=False)


job_number = '87906'
kit_no = 'WC-3'

# counter = 1
# while counter <= 10:
#     part = Part("GCI GROUP" + (" "*55) + job_number + "-" + str(counter),
#                 "CUSTOMER: VARLEY - TOMAGO",
#                 "DIVISION: DEFENCE & AERO" + (" "*10) + "KIT NUMBER: " + kit_no,
#                 "PART NUMBER: " + str(counter),
#                 "REV: " + str(counter) + (" "*25) + "QTY: " + str(counter))
#     sheet.add_label(part)
#     counter += 1

counter = 1
second_counter = 1
while counter <= 20:
    second_counter = 1
    while second_counter <= counter:
        part = Part("GCI GROUP" + (" "*55) + job_number + "-" + str(counter),
                    "CUSTOMER: VARLEY - TOMAGO",
                    "DIVISION:  DEFENCE & AERO" + (" "*10) + "KIT NUMBER:  " + kit_no,
                    "PART NUMBER:  " + str(counter),
                    "REV:  " + str(counter) + (" "*25) + "QTY:  " + str(second_counter) + "  of  " + str(counter))
        sheet.add_label(part)
        second_counter += 1

    counter += 1

pdf_name = job_number + '.pdf'
sheet.save(pdf_name)
