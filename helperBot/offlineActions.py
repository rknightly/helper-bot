import subprocess
import os
import glob
import re

from action import Action


class Python(Action):
    aliases = ["python"]

    @staticmethod
    def do_action():
        subprocess.Popen(['/bin/sh', '-c',
                          'open -a terminal ~/Google\ Drive/Software/Python'])


class Terminal(Action):
    aliases = ["terminal"]

    @staticmethod
    def do_action():
        subprocess.Popen(['/bin/sh', '-c', 'open -a terminal ~/'])


class SameTerminal(Action):
    aliases = ["same terminal"]

    @staticmethod
    def do_action():
        """Open a terminal in the same directory as the current one"""
        subprocess.Popen(['/bin/sh', '-c', 'open -a terminal ./'])


class SpanishWarmup(Action):
    aliases = ["spanish warmup"]

    @staticmethod
    def do_action():
        path_to_warmups = "../../Classes/Spanish/WarmUps/"

        if os.path.exists(path_to_warmups):
            # ignore files with ~$file_name.docx
            warmup_file_names = [file for file in os.listdir(path_to_warmups)
                                 if "~" not in file.lower()]

            # get dates from each file name
            pattern = r'(\d{1,2}-\d{1,2})'
            dates = [re.search(pattern, file_name).group(1)
                     for file_name in warmup_file_names]

            # turn dates into mm-dd format for easy sort
            formatted_dates = []
            for date in dates:
                date_values = date.split('-')

                # Add leading zeroes to two places
                formatted_date = date_values[0].zfill(2) + '-' +\
                    date_values[1].zfill(2)
                formatted_dates.append(formatted_date)

            # sort dates, find most recent date
            formatted_most_recent_date = sorted(formatted_dates)[-1]
            # remove traling zeroes from most recent date
            most_recent_date_values = [date_value.lstrip("0")
                                       for date_value in
                                       formatted_most_recent_date.split("-")]
            most_recent_date = most_recent_date_values[0] + "-" +\
                most_recent_date_values[1]

            # get name of file the contains the date
            for file_name in warmup_file_names:
                if most_recent_date in file_name:
                    current_warmup_file = file_name
                    break

            # open file
            os.system("start " + path_to_warmups + current_warmup_file)

        else:
            self.interface.output("No spanish warmup folder at the correct "
                                  "location")
            self.interface.output("Make a folder at ../../Classes/Spanish/"
                                  "Warmups/ if you wish to use this feature")


class SpanishPowerpoint():
    aliases = ["spanish ppt"]

    @staticmethod
    def do_action():
        powerpoint_path = "../../Classes/Spanish/actividadDelDia.pptx"
        os.system("start " + powerpoint_path)
