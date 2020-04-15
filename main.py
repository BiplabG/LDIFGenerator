import random

from loader import *
from generator import *

def get_random_integer(limit):
    return int(random.random() * limit)

if __name__ == '__main__':
    config_file="./config.json"
    config = load_config(config_file=config_file)
    
    limit = get_limit(config['number_of_entries'])
    groups = get_groups(path=config['data_path']+'group.txt', num_groups=limit)
    users = get_users(path=config['data_path']+'user.txt', num_users=limit)
    sns = get_sns(path=config['data_path']+'sn.txt', num_sns=limit)

    user_sn_set = set()
    group_user_tracking = {group.strip():[] for group in groups}

    while len(user_sn_set) <= config['number_of_entries']:
        user_sn_instance = (users[get_random_integer(len(users)-1)].strip(), sns[get_random_integer(len(sns)-1)].strip())
        previous_count = len(user_sn_set)
        user_sn_set.add(user_sn_instance)

        if len(user_sn_set) == previous_count:
            #previous user_sn pair was not unique
            continue
        group_instance = groups[random.randint(0, len(groups)-1)].strip()
        group_user_tracking[group_instance].append(user_sn_instance)
        
    generate_group(group_user_tracking.keys(), config['domain'], config['out_file'])
    generate_member(group_user_tracking, config['domain'], config['out_file'])
    finalize_members(group_user_tracking, config['domain'], config['group_modify_file'])



    
