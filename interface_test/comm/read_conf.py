from configparser import ConfigParser
from comm.get_project_path import Project_path
import os 
class Read_conf():
    def __init__(self):
        self.conf_path=Project_path().project_path()+"conf"+os.sep
    def read_log(self,log_name):
        log_conf={}
        log_path=self.conf_path+log_name
        log_info=ConfigParser()
        log_info.read(log_path,encoding="utf8")
        for i in log_info.options("log"):
            log_conf[i]=log_info.get("log",i)
        return log_conf
