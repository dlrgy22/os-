import os
import json_parsing
import query

os_tb = query.mysql_db('root', '*', '*', 'malware_data', 3306)

dir_path = '/media/samlon09/HDD/malware_for_es/src/Data/original'
dir_list = os.listdir(dir_path)
for dir_name in dir_list:
        file_path = dir_path + '/' + dir_name
        try:
                file_list = os.listdir(file_path)
        except:
                continue

        if dir_name[-1] == '1' or dir_name[-1] == '2':
                json_dir = dir_name[:len(dir_name) - 2]
        else:
                json_dir = dir_name

        for file_name in file_list:
                ID = file_name
                BINARY_PATH = '/Data/original/' + dir_name + '/' + file_name

                if dir_name == 'exe_malware' or dir_name == 'exe_normal':
                        JSON_PATH = '/home/samlon09/json/' + json_dir + '/' + file_name + '.json'
                else:
                        JSON_PATH = '/home/samlon09/json/' + json_dir + '/' + file_name

                try:
                        OS_TYPE, IS_MALWARE, MALWARE_TYPE = json_parsing.parsing_json(JSON_PATH)
                        sql = "INSERT INTO OS_tb VALUES('{0}', '{1}', '{2}', '{3}', {4}, '{5}');".format(ID, OS_TYPE, BINARY_PATH, JSON_PATH, IS_MALWARE, MALWARE_TYPE)
                        os_tb.execute_query(sql)
                except:
                        continue
