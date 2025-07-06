import json
from datetime import datetime
import FileManager as fm
import uuid
import os
from Version import Version

class Repository:
    def __init__(self):
        self.current_path = os.getcwd()
        self.wit_path = os.path.join(self.current_path, ".wit")
        self.path_commit = os.path.join(self.wit_path, "commit")
        self.path_stage = os.path.join(self.wit_path, "stage")
        self.data_path = os.path.join(os.path.join(self.wit_path, 'data.json'))

    # הופך את המאגר ל repository
    def wit_init(self):
        fm.create_folder(self.wit_path)
        fm.create_folder(self.path_commit)
        fm.create_folder(self.path_stage)
        fm.create_file(self.wit_path,'data.json')

    #מוסיף את הקובץ שהתקבל לתוך תקיית stage
    def wit_add(self,path_file):
        print(f"Received path_file: {path_file}")
        if not path_file:
             raise ValueError("The source file path is empty.")
        fm.copy_file(path_file,os.path.join(self.current_path, ".wit", "stage"))

    # לוקח את כל הקבצים שנמצאים ב stage וכן את הקבצים מה commit האחרון
    # ומעביר אותם לתוך תקייה חדשה שנוצרת בתוך תקיית commit
    def wit_commit(self,message):
        path_last_commit = self.path_commit + r'\\{}'.format(fm.get_latest_directory(self.path_commit))
        new_uuid = uuid.uuid4()
        v = Version(str(new_uuid), datetime.now(), message)
        version_dict = v.to_dict()
        fm.create_folder(self.path_commit + r"\\{}".format(version_dict['hashcode']))
        fm.insert_object_into_json(os.path.join(self.current_path, ".wit", 'data.json'), version_dict)
        if path_last_commit.endswith('None'):
            list_file_commit = fm.list_files(self.current_path)
            path_list_to_commit = self.current_path
        else:
            list_file_commit = fm.list_files(path_last_commit)
            path_list_to_commit = path_last_commit

        for l in list_file_commit:
            if not l == '.wit':
                fm.copy_file(path_list_to_commit + r"\\{}".format(l),
                             self.path_commit + r"\\{}".format(version_dict['hashcode']))

        list_file = fm.list_files(self.path_stage)
        for l in list_file:
            fm.copy_file(self.path_stage + r"\\{}".format(l),
                         self.path_commit + r"\\{}".format(version_dict['hashcode']))
            fm.delete_file(self.path_stage + r"\\{}".format(l))

    # מדפיס את כל המידע על ה coomit ים
    def wit_log(self):
        with open(self.data_path, 'r') as file:
            data = json.load(file)
            print(json.dumps(data, indent=4, ensure_ascii=False))

    # מדפיס סטטוס ב stage
    def wit_status(self):
        if fm.check_if_file_exists_in_folder(self.path_stage):
            print("the stage empty")
        else:
            print("the stage full")
            list_status = fm.list_files(self.path_stage)
            for l in list_status:
              print (l)

    # מחליף גרסה נוכחית בגרסה אחרת לפי hashcode - שם התקיה
    def wit_check_out(self,commit_id):
        hash_commit = ""
        list_commit = fm.list_files(self.path_commit)
        for c in list_commit:
           if c == commit_id:
             hash_commit = c
        list_commit_file = fm.list_files(self.path_commit + r"\\{}".format(hash_commit))
        list_project_file = fm.list_files(self.current_path)
        for l in list_project_file:
           if not l == '.wit':
             fm.delete_file(self.current_path+r"\\{}".format(l))
        for l in list_commit_file:
             fm.copy_file(self.path_commit+r"\\{}\\{}".format(hash_commit,l),self.current_path)

