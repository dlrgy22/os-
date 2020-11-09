import os
import query

feature_tb = query.mysql_db('root', 'cs$)*$)*cs', 'localhost', 'malware_data', 3306)

def number_of_attribute(path):
        f = open(path, 'r')
        num = f.read()
        num = num.split(' ')
        num = len(num) - 1
        return num

dir1_path = '/media/samlon09/HDD2/malware_for_es/src/Data/feature'
dir1_list = os.listdir(dir1_path)
for dir1_name in dir1_list:
        dir2_path = dir1_path + '/' + dir1_name
        dir2_list =  os.listdir(dir2_path)
        for dir2_name in dir2_list:

                make_tb = 'create table if not exists {} (ID char(150) PRIMARY KEY, FEATURE_PATH char(250), NUMBER_OF_ATTRIBUTE INT)'.format(dir2_name)
                feature_tb.execute_query(make_tb)

                file_path = dir2_path + '/' + dir2_name
                file_list = os.listdir(file_path)
                for file_name in file_list:
                        ID = file_name.split('.')[0]
                        feature_path = file_path + '/' + file_name
                        att_num = number_of_attribute(feature_path)
                        sql = "INSERT INTO {0} VALUES('{1}', '{2}', {3});".format(dir2_name, ID, feature_path, att_num)
                        feature_tb.execute_query(sql)