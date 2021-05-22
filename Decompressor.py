import re
def Decompress(file, output_file=-1):
    
    com_data = read_bin(file)

    dic_t = com_data[0]
    data = com_data[1]
    
    dic_t = decode_encoded_dict(dic_t)

    y = re.split('(?<=\S)\s', dic_t )[:-1]
    newdict = {}
    for j in y:
        newdict[str(bin(int(j[1:]))[2:])[1:]] = j[0]

    dic_t  = newdict

    if(output_file == -1):
        h=open(input_file[:-4],'w+')
    else:
        h=open(output_file,'w+')
  
    keyword = ""
    t=""
    decom_data = ""
    for i in data:
        keyword += i
        if(keyword in newdict):
            try:
                t+=(newdict[keyword])
                
            except:
                t+=("")
            keyword = ""
    h.write(t)

    h.close()
    

def read_bin(file):
    file = open(file, "rb")
    
    data = []
    
    #Header
    new_byte = file.read(4)
    header_len = int.from_bytes(new_byte,"little")
   
    new_rem = file.read(1)
    rem = int.from_bytes(new_rem,"little")

    chunk = []
    for i in range(header_len):
        chunk.append(int.from_bytes(file.read(1),"little"))
    
    chunk = bytes_to_bin(chunk, rem)
    data.append(chunk)

    #Data
    new_rem = file.read(1)
    rem = int.from_bytes(new_rem,"little")

    chunk = []
    new_byte = file.read(1)
    while(new_byte != b""):
        chunk.append(int.from_bytes( new_byte,"little"))
        new_byte = file.read(1)

    chunk = bytes_to_bin(chunk, rem)
    data.append(chunk)
    return data

def bytes_to_bin(arr, rem):
    bin = ""
    for i in arr:
        bin += ("{0:008b}".format(i))
    
    if(rem>0):
        return bin[:-1*rem]
    else:
        return bin

def decode_encoded_dict(bin):
    string = ""
    for i in range(int(len(bin)/8)):
        i = 8*i
        string += chr(int(bin[i:i+8],2))
    return string

    
if __name__ == "__main__":
    input_file = input('Name of File to Decompress: ') 
    if(len(input_file)<5 or input_file[-4:]!=".cmp"):
        print("Enter a Valid File with (.cmp) extension")
    else:
        Decompress(input_file)
