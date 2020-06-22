### Boilerplate code for email notifications from python script.

Code is taken and (marginally) added to from [real-python](https://realpython.com/python-send-email/).

##### Usage
- Edit **config_template.ini** file.
- Settings in **'[default]'** section should be left alone if gmail account being used to send e-mail.
- Change 'email' and 'password' in **['user_info']** and **rename file to config_ini**!
  - **config_ini** file needs to exist for code to execute.
  - Do not just change the input file because then your credentials will be available on GitHub... :)
 

##### TODO
- Add argument parsing.
- Allow e-mail body to be read in from separate file.
