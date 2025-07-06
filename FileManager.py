# -*- coding: utf-8 -*-
import os,shutil,json,datetime
from datetime import datetime
from os.path import exists
from tkinter import FALSE


def create_folder(path):
    try:
        if not os.path.exists(path):
            os.makedirs(path)
            print("Folder created.")
    except:
        raise Exception("folder already exist")

def create_file(path, file_name):
    full_path = os.path.join(path, file_name)
    if not os.path.exists(full_path):
        with open(full_path, 'w') as file:
            file.write('')
    else:
        print(f"File already exists: {full_path}")



def copy_file(source,destination):
    try:
        print(f"Source: {source}, Destination: {destination}")
        shutil.copy(source, destination)
    except Exception as e:
        raise ValueError('An error occurred: {}'.format(e))

def check_if_file_exists_in_folder(path):
    if not os.listdir(path):
        return True
    else:
        return False

def delete_file(path):
    if os.path.exists(path):
      os.remove(path)
    else:
        raise ValueError("File does not exist: {}".format(path))

def list_files(path):
    p = [f for f in os.listdir(path)]
    return p


def serialize_datetime(o):
    if isinstance(o, datetime):
        return o.isoformat()  # ממיר את ה-datetime למחרוזת בפורמט ISO 8601
    raise TypeError("{} is not JSON serializable".format(repr(o)))


def size_json(file_path):
    if os.path.getsize(file_path) == 0:
        return True
    else:
        return False

def insert_object_into_json(file_path, new_object):
    if not os.path.exists(file_path):
        with open(file_path, 'w') as file:
            json.dump([], file)

    if size_json(file_path):
        with open(file_path, 'w') as file:
            json.dump([new_object], file, default=serialize_datetime)  # השתמש ב-default
    else:
        with open(file_path, 'r') as file:
            data = json.load(file)

        if not isinstance(data, list):
            raise ValueError("The JSON file does not contain a list.")

        data.append(new_object)

        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4, default=serialize_datetime)


def get_latest_directory(path):
    directories = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
    if not directories:
        return None

    # מציאת התיקייה שנוצרה לאחרונה
    latest_dir = max(directories, key=lambda d: os.path.getctime(os.path.join(path, d)))

    return latest_dir





