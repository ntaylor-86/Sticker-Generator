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
import os.path
import sys
import re

print
print " N4tH4N's                          "
print "Single Label Maker..."
print
print " +------------------------------------------------------+"
print " |   (1) G H VARLEY - TOMAGO (McINTYRE ROAD - DEFENCE)  |"
print " |   (2) G H VARLEY - TOMAGO (SCHOOL DRIVE)             |"
print " +------------------------------------------------------+"
print
customer = raw_input("##  Please select who the customer is: ")

if customer == "1":
    customer = "VARLEY_TOMAGO_DEFENCE"
elif customer == "2":
    customer = "VARLEY_TOMAGO"

if customer == "VARLEY_TOMAGO_DEFENCE":
    # Getting the Kit Number from the USER, this changes with each order
    print "*  VARLEY - TOMAGO DEFENCE, require a kit number to be printed on each label."
    print "*  The kit number should be written on the 'CUSTOMER-LABELS' ticket."
    print "*  If there is no kit number on that ticket, see Jamie."
    print
    kit_number = raw_input("##  Please enter the Kit Number for this job: ")


#######################
####  Label Specs  ####
#######################

specs = labels.Specification(210, 297, 3, 11, 63.6, 24.1, corner_radius=2,
                             left_padding=3, bottom_padding=1.5, left_margin=6.5, top_margin=16,
                             row_gap=0.5, column_gap=2.7)

# setting up labels for VARLEY_TOMAGO_DEFENCE
if customer == "VARLEY_TOMAGO_DEFENCE":
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
            y += 11
            group.add(shape)

        label.add(group)


    sheet = labels.Sheet(specs, draw_part, border=False)

    make_sticker = True
    while make_sticker == True:
        job_number = raw_input("What is the job number: ")
        ticket_number = raw_input("What is the ticket number: ")
        part_number = raw_input("What is the client part number: ")
        qty = raw_input("What is the qty: ")
        revision = raw_input("What is the revision: ")

        counter = 1
        while counter <= int(qty):
            part = Part("GCI GROUP" + (" " * 55) + str(job_number) + "-" + str(ticket_number),
                        "CUSTOMER:  VARLEY - TOMAGO",
                        "DIVISION:  DEFENCE & AERO" + (" " * 10) + "KIT NUMBER:  " + str(kit_number),
                        "PART NUMBER:  " + str(part_number),
                        "REV:  " + str(revision) + (" " * 25) + "QTY:  " + str(counter) + "  of  " + str(qty)
                        )
            sheet.add_label(part)
            print "Generating label " + str(counter) + " of " + str(qty)
            counter += 1

        print
        make_sticker_prompt = raw_input("Would you like to make another label (y or n): ")
        make_sticker_prompt = make_sticker_prompt.lower()
        valid_answer = False
        while valid_answer == False:
            if make_sticker_prompt == 'y':
                make_sticker = True
                valid_answer = True
            elif make_sticker_prompt == 'n':
                make_sticker = False
                valid_answer = True
            else:
                print "That is not a valid answer!"
                print
                make_sticker_prompt = raw_input("Would you like to make another label (y or n): ")
                make_sticker_prompt = make_sticker_prompt.lower()

    pdf_name = job_number + '.pdf'
    sheet.save(pdf_name)

# setting up labels for VARLEY_TOMAGO
if customer == "VARLEY_TOMAGO":
    Part = namedtuple(
        'Part',
        ['gci_group', 'customer', 'order_number', 'part_number', 'rev_qty'])


    def draw_part(label, width, height, part):
        lines = [
            part.rev_qty,
            part.part_number,
            part.order_number,
            part.customer,
            part.gci_group
        ]

        group = shapes.Group()
        x, y = 0, 0


        for line in lines:
            if not line:
                continue
            shape = shapes.String(x, y, line, textAnchor="start", fontName="Helvetica", fontSize=6)
            y += 11
            group.add(shape)

        label.add(group)


    sheet = labels.Sheet(specs, draw_part, border=False)

    make_sticker = True
    while make_sticker == True:
        job_number = raw_input("What is the job number: ")
        order_no = raw_input("What is the order number: ")
        ticket_number = raw_input("What is the ticket number: ")
        part_number = raw_input("What is the client part number: ")
        qty = raw_input("What is the qty: ")
        revision = raw_input("What is the revision: ")

        part = Part("GCI GROUP" + (" " * 55) + str(job_number) + "-" + str(ticket_number),
                    "CUSTOMER:  VARLEY",
                    "ORDER NUMBER:  " + str(order_no),
                    "PART NUMBER:  " + str(part_number),
                    "REV:  " + str(revision) + (" " * 25) + "QTY:  " + str(qty)
                    )
        sheet.add_label(part)
        print "Generating label "

        print
        make_sticker_prompt = raw_input("Would you like to make another label (y or n): ")
        make_sticker_prompt = make_sticker_prompt.lower()
        valid_answer = False
        while valid_answer == False:
            if make_sticker_prompt == 'y':
                make_sticker = True
                valid_answer = True
            elif make_sticker_prompt == 'n':
                make_sticker = False
                valid_answer = True
            else:
                print "That is not a valid answer!"
                print
                make_sticker_prompt = raw_input("Would you like to make another label (y or n): ")
                make_sticker_prompt = make_sticker_prompt.lower()

    pdf_name = job_number + '.pdf'
    sheet.save(pdf_name)

print
print "Saving the pdf as " + str(job_number) + ".pdf"
print

print "Generating the labels is complete."
print "Open the PDF generated and print this onto the AVERY 'L7175REV' Labels"
print "Make sure you printer is printing at 'Actual Size' and not scaling the pdf :D"
print "If in doubt ask Nathan"
print

