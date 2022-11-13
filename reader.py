def get_from_txt(text:str):

    with open(text, "r") as f:
        
        lines = f.readlines()
        new_lines = [line.strip().split("->") for line in lines]
        lines = [[line_i.strip() for line_i in line] for line in new_lines]
        
        return lines