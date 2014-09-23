#!/usr/bin/python
#-*-coding:utf-8-*-
#2014/09/23 05:54:15 Shin Kanouchi
"""
入力
出力
"user_id","on_cid","p_topic_id"
539152,3421425341923550212,1036212,"article_read"
"""
import sys, csv

i=0
print '"user_id","on_cid","p_topic_id","Answer"'
dataReader = csv.reader(open(sys.argv[1]))
header = next(dataReader)
ID_list = []
on_cid_list = []
one_topic_list = []
time_list = []
for one_data in dataReader:
    ID_list.append(one_data[0])
    on_cid_list.append(one_data[1])
    one_topic_list.append(one_data[2])
    time_list.append(one_data[4])
    if len(time_list) < 3:
        pass
    elif len(time_list) < 5:
        print '%s,%s,%s,"%s"' % (one_data[0],one_data[1],one_data[2], "NULL")
    if len(time_list) == 5:
        if on_cid_list[2] == on_cid_list[0] or on_cid_list[2] == on_cid_list[1] or on_cid_list[2] == on_cid_list[3] or on_cid_list[2] == on_cid_list[4]:
            print '%s,%s,%s,"%s"' % (ID_list[2],on_cid_list[2],one_topic_list[2], "article_read")
        elif ID_list[0] == ID_list[1] and ID_list[1] == ID_list[2] and ID_list[2] == ID_list[3] and ID_list[3] == ID_list[4]:
            print '%s,%s,%s,"%s"' % (ID_list[2],on_cid_list[2],one_topic_list[2], "NULL")
        elif one_topic_list[0] == one_topic_list[1] and one_topic_list[1] == one_topic_list[2] and one_topic_list[2] == one_topic_list[3] and one_topic_list[3] == one_topic_list[4]:
            print '%s,%s,%s,"%s"' % (ID_list[2],on_cid_list[2],one_topic_list[2], "NULL")
        else:
            print '%s,%s,%s,"%s"' % (ID_list[2],on_cid_list[2],one_topic_list[2], "article_read")
        ID_list.pop(0)
        on_cid_list.pop(0)
        one_topic_list.pop(0)
        time_list.pop(0)
print '%s,%s,%s,"%s"' % (one_data[0],one_data[1],one_data[2], "NULL")
print '%s,%s,%s,"%s"' % (one_data[0],one_data[1],one_data[2], "NULL")