import argparse
import sys
def change_dict(my_dict):
    my_new_dict = {}
    unique_values = list(set(my_dict.values()))
    vpn_ip = my_dict["vpn"]
    for key, value in my_dict.items():
        for i, unique_value in enumerate(unique_values):
            if value == unique_value:
                if value == vpn_ip:
                    my_new_dict[key] = "10.8.0.1"
                else:
                    my_new_dict[key] = "10.8.0." + str(i+2)
    return my_new_dict

def remove_value(my_dict):

    unique_values = []
    for key, value in my_dict.items():
        if value not in unique_values and value is not None and value != my_dict["vpn"]:
            unique_values.append(value)


    return unique_values
def merge_dicts(dict1, dict2): 
    result = {} 
    for key in dict1: 
        if dict1[key] != my_dict["vpn"]:
            result[dict1[key]] = dict2[key] 

    return result     
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    my_dict = {}
    for i in range(1, len(sys.argv), 2):
        my_dict[sys.argv[i]] = sys.argv[i+1]
 

    vpn_ips = change_dict(my_dict)
    certs   = remove_value(my_dict)
    map_vpn = merge_dicts(my_dict , vpn_ips)
    print(vpn_ips)
    print(certs)
    print(map_vpn)
    # if args.command == "dns":
    #     my_new_dict = change_dict(my_dict)
    #     print(my_new_dict)
    # if args.command == "certs": 
    #     my_new_dict = remove_value(my_dict)
    #     print(my_new_dict)
    # if args.command == "sip": 
    #     my_new_dict = change_dict(my_dict)
    #     print(my_new_dict)
    #     my_new_dict = merge_dicts(my_dict, my_new_dict)
    #     print(my_dict)
    #     print(my_new_dict)
    