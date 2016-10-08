import subprocess
import os
import glob
import re

def python():
    subprocess.Popen(['/bin/sh', '-c', 'open -a terminal ~/Google\ Drive/Software/Python'])

def terminal():
    subprocess.Popen(['/bin/sh', '-c', 'open -a terminal ~/'])

def same_terminal():
    subprocess.Popen(['/bin/sh', '-c', 'open -a terminal ./'])

def spanish_warmup():
    path_to_warmups = "../../Classes/Spanish/WarmUps/"

    # ignore ~$ightly.docx file by checking for 'knightly'
    warmup_file_names = [file for file in os.listdir(path_to_warmups) if "knightly" in file.lower()]

    # get dates from each file name
    pattern = r'(\d+-\d)'
    dates = [re.search(pattern, file_name).group(1) for file_name in warmup_file_names]

    # turn dates into mm-dd format for easy sort
    formatted_dates = []
    for date in dates:
        date_values = date.split('-')
        formatted_date = date_values[0].zfill(2)+ '-' + date_values[1].zfill(2)  # Add leading zeroes to two places
        formatted_dates.append(formatted_date)

    # sort dates, find most recent date
    formatted_most_recent_date = sorted(formatted_dates)[-1]
    # remove traling zeroes from most recent date
    most_recent_date_values = [date_value.lstrip("0") for date_value in formatted_most_recent_date.split("-")]
    most_recent_date = most_recent_date_values[0] + "-" + most_recent_date_values[1]

    # get name of file the contains the date
    for file_name in warmup_file_names:
        if most_recent_date in file_name:
            current_warmup_file = file_name
            break

    # open file
    os.system("start "+ path_to_warmups + current_warmup_file)

def spanish_powerpoint():
    powerpoint_path = "../../Classes/Spanish/actividadDelDia.pptx"
    os.system("start " + powerpoint_path)
