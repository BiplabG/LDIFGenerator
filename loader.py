import json
import math

def load_config(config_file):
    with open(config_file, "r") as file:
        config = json.load(file)
    return config


def get_limit(num_entries):
    if num_entries <= 30:
        return num_entries
    else:
        limit = num_entries/2
        return limit

def get_groups(path, num_groups):
    with open(path, "r") as file:
        groups_out=[]
        for i, user in enumerate(file):
            if i >= num_groups:
                break
            groups_out.append(user)
            i+=1
    return groups_out

def get_users(path, num_users):
    with open(path, "r") as file:
        users_out=[]
        for i, user in enumerate(file):
            if i >= num_users:
                break
            user=user.replace(' ', '').replace('-','')
            users_out.append(user)
            i+=1
    return users_out

def get_sns(path, num_sns):
    with open(path, "r") as file:
        sn_out=[]
        for i, sn in enumerate(file):
            if i >= num_sns:
                break
            sn=sn.replace(' ', '').replace('-','')
            sn_out.append(sn)
            i+=1
    return sn_out
