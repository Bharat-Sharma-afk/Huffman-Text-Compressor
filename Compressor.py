import string
from array import array
import math

def tree(tn,s,dict,dict1):
    if tn not in dict:
        dict1[tn]=s
    else:
        a=dict[tn][0];b=dict[tn][1]
        return [tree(a,(s+'0'),dict,dict1),tree(b,(s+'1'),dict,dict1)]

def sort(data_items):
    for i in range(len(data_items)):
        for j in range(len(data_items)-1):
            if data_items[j][1]>data_items[j+1][1]:
                data_items[j+1],data_items[j]=data_items[j],data_items[j+1]
    return data_items

def compress(input_file_name, output_file_name=-1):
    input_file=open(input_file_name, "rb")
    bin=input_file.read()
    input_file.close()

    text = ''
    for i in bin:
        if(i<128):
            text += chr(i)
    
    data={}
    for i in text:
        if i not in data:
            data[i]=1
        elif i in data:
            data[i]+=1

    data_items=list(data.items())
    for i in range(len(data_items)):
        data_items[i]=list(data_items[i])
    data_items=sort(data_items)
    dict={}
    for i in range(len(data_items)-1):
        name=data_items[0][0]+data_items[1][0]
        we=data_items[0][1]+data_items[1][1]
        a=data_items.pop(0)
        b=data_items.pop(0)
        dict[name]=[a[0],b[0]]
        data_items.append([name,we])
        data_items=sort(data_items)
    dict1={}
    input_file.close()
    
    print(name,'',dict,dict1)
    (tree(name,'',dict,dict1))
    
    ft=""
    for i in range(len(text)):
        ft=ft+dict1[text[i]]
    
    if(output_file_name == -1):
        g=open(input_file_name + ".cmp",'w+')
        g.write('')
        g=open(input_file_name + ".cmp",'ab')
    else:
        g=open(output_file_name + ".cmp",'w+')
        g.write('')
        g=open(output_file_name + ".cmp",'ab')

    dict_str = ""
    for i in dict1:
        dict_str = dict_str + str(i) + str(int("1"+dict1[i],2)) + " "
      
    dict_bin = ""

    for i in dict_str:
        temp = ("{0:008b}".format(ord(i)))
        if(len(temp) != 8):
            temp = "01000000"
        dict_bin += temp
        

    
    g.write(bytes(to_bin(dict_bin, True)))
    g.write(bytes(to_bin(ft)))
    
    g.close()

def to_bin(data, isheader = False):
    rem = 8 - (len(data)%8)
    data = data + ("0"*rem)  
    bin_arr = array("B")
    chunk_len = math.ceil(len(data)/8)
    
    if(isheader):
        chunk_len = ("{0:032b}".format(chunk_len))

        for i in range(4):
            i *= 8
            bin_arr.insert(0, int(chunk_len[i : i+8],2))
        
    bin_arr.append(rem)

    for i in range(math.ceil(len(data)/8)):
        i = 8*i
        bin = data[i:i+8]
        bin_arr.append(int(bin,2))
    
    return bin_arr


if __name__ == "__main__":
    compress(input('Name of File to Compress: '))
