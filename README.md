# accela-code-test

# How to execute:
Dump access_log.txt file ( sample file attached)  in the same directory as the python code (get_data.py)
run : python get_data.py.
The output will be show in screen. Also it will dump a json file with information as apache_data.json in the same directory.

To pretty print the content of the json file.
run python -m json.tool apache_data.json

TODO:
  take a filename as an argument istead of a hardcode filename.
  Error handling if the access_code or time is not in apache log.
  
