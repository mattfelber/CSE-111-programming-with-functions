def main():
    
    text_list = read_list("provinces.txt")
    replaced_list = replace_names(text_list)
    print(replaced_list)
    

def read_list(filename):
    
    clean_list = []
    
    with open(filename) as text_list:

        for line in text_list:
            clean_line = line.strip()
            clean_list.append(clean_line)
    
    return clean_list


def replace_names(text_list):
    replaced_list = []

    for item in text_list:
        if item == "AB" or item == "Ab":
            item = "Alberta"
            replaced_list.append(item)
        else:
            replaced_list.append(item)
    
    return replaced_list
     

if __name__ == "__main__":
    main()

