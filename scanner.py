from socket import gethostbyaddr, herror


def list_hostnames_from_ips(ip_block, start_ip, end_ip):
    host_ips = []
    host_names = []
    current_host_name = ""
    global host_count
    host_count = 0

    print("")
    for i in range(start_ip, end_ip + 1):
        current_ip = f"192.168.{ip_block}.{i}"

        try:
            current_host_name = gethostbyaddr(current_ip)
            print("+ Ip: "+current_ip+" || Hostname: "+current_host_name[0])
            host_count += 1
        except herror:
            print("- Cannot reach "+current_ip+" Passed...")
            continue
        
        host_ips.append(current_ip)
        host_names.append(current_host_name[0])
    
    for i in range(len(host_ips)):
        host_info.append([])
        host_info[i].append(host_ips[i])
        host_info[i].append(host_names[i])


def write_info(information, filename):
    file_name = f'{filename}.txt'
    with open(file_name, 'w') as f:
        for info in information:
            f.write("Ip: "+info[0]+" || Hostname: "+info[1]+"\n")
        else:
            f.write(f"\n{host_count} host found at total...\n")


while True:
    block_number = input("\nDefine desired block for scan: ")
    while True:
        try:
            first_ip = int(input("Starting ip: "))
            break
        except ValueError:
            print("Only int numbers allowed...")
            continue
    while True:
        try:
            last_ip = int(input("Last ip: "))
            break
        except ValueError:
            print("Only int numbers allowed...")
            continue

    host_info = []
    list_hostnames_from_ips(block_number, first_ip, last_ip)
    
    print("\nAll ips that found:")
    for info in host_info:
        print("Ip: "+info[0]+" || Hostname: "+info[1])
    else:
        print(f"\n{host_count} hosts found at total...\n")
    

    scase = input("create .txt? (y)")
    if scase == 'y':
        cfilename = input("Filename (Without file extension): ")
        write_info(host_info, cfilename)
        print("Writed...")

        scase_three = input("Continue scanning? (y)")
        if scase_three == 'y':
            print("Continuing program...")
            continue
        else:
            scase_four = input("Exit program? (y)")
            if scase_four == 'y':
                print("Exiting program...")
                break
            else:
                print("Continuing program...")
    else:
        scase_two = input("Exit program? (y)")
        if scase_two == 'y':
            print("Exiting program...")
            break
        else:
            print("Continuing program...")
            continue



