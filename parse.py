import re
import time
from time import strftime

log_file_path = r".\log4j-20190516-1618-02.log"
export_file_path = r".\filtered"

time_now = str(strftime("%Y%m%d-%H%M-%S", time.localtime()))

file = "\\" + "ParserOutput-" + time_now + "-" + ".txt"
export_file = export_file_path + file


regex = '(Using logging context)'

match_list = []

with open(log_file_path, "r") as file:
    for line in file:
        for match in re.finditer(regex, line, re.S):
            match_text = match.group()
            match_list.append(match_text)
            print(match_text)
            print(line)
            if re.finditer('(STANDALONE)', line, re.S):
                match_list.append("Standalone installation")
file.close()

with open(export_file, "w+") as file:
    file.write("EXPORTED DATA :\n")
    match_list_clean = list(set(match_list))
    for item in range(0, len(match_list_clean)):
        print(match_list_clean[item])
        file.write(match_list_clean[item] + "\n")
file.close()
