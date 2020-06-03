def generate_binary(index, base, list):
    if index >= len(list):
        print(list)
        return
    for i in range(0,base):
        list[index] = i
        generate_binary(index+1, base, list)
    return
list = [0, 0, 0, 0, 0]
if __name__ == "__main__":
    generate_binary(0, 2, list)