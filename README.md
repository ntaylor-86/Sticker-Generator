# Sticker-Label-Creater
A Python script that genereates a PDF file that can be used to print labels with the AVERY Removable Multi-Purpose Labels (L7157REV). This script uses pylabels - https://github.com/bcbnz/pylabels and reportlab - https://pypi.org/project/reportlab/ . Thanks to these two projects!

## Getting Started

You will need a .txt file for the script to scrape all the information from. In iTMS, open Jobs (5), Print Job Ticket (3), enter the job number, click on print, choose Number. This will open the iTMS Print Preview, click on Export, choose Text as the file type and save the .txt file in the same location as the python script.

### Prerequisites

This script relies on two python libraries to be installed, pylabels and reportlab

```
pylabels

pip install pylabels
```

```
reportlab

pip install reportlab
```

### Installing

Copy the script to your home directory preferably its own folder and make the script executable

```
Change into the directory where the script is located,
$ chmod +x label-maker.py
```


### Runnings the Script

Once you have exported a job into a .txt format you can now run the script


```
Change into the directory where the script is located,
$ ./label-maker.py
```
