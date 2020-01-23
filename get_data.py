#!/usr/bin/env python

import logging
import json

class apachelog():
    def __init__(self, logfile):
       self.logfile = logfile

    def get_logs(self):
         apache_dict = {}
         fh = open(self.logfile,'r')
         for line, data in enumerate(fh,1):
               logging.debug("accessing line number {} content {}:: ".format(line, data))
               access_data = data.split(' ')
               access_code = access_data[8]
               access_time = access_data[3]
               access_time = access_time.strip('[').strip(']')
               access_time_list = access_time.split(':')
               access_time = '-'.join(access_time_list[:-1]) 
               logging.debug("access_time :: {}".format(access_time))
               if access_time in apache_dict:
                   data = apache_dict[access_time]
                   if access_code in data:
                          data[access_code] = int(data[access_code])+1
                   else:
                        data[access_code] = 1
               else:
                    apache_dict[access_time] = {access_code: 1}
                  
         return apache_dict
       
    def print_data(self):
           apache_data = self.get_logs()
           print(json.dumps(apache_data, indent=4))
           for data,values in apache_data.iteritems():
               for error, times in values.iteritems(): 
                   print("At time {} code {} occured {} times".format(data,error, times))
           with open('apache_data.json', 'w') as fh:
                fh.write(json.dumps(apache_data))
      
def main():
    logfile ="access_log.txt"
    parser = apachelog(logfile)
    parser.print_data()
    
    
if __name__ == "__main__":
     FORMAT = '%(asctime)-15s  %(message)s'
     logging.basicConfig(format=FORMAT, level=logging.INFO)
     main()
 
