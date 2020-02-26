'''kmp'''
def kmp(source = "", find = ""):
    PMT = [0 for x in range(0,len(find))]
    #先计算pmt数组
    PMT[0] = -1
    i,j = 0,-1
    while i < len(find) - 1:
        if j == -1 or find[i] == find[j]:
            i = i + 1
            j = j + 1
            PMT[i] = j
        else:
            j = PMT[j]

    i ,j = 0 , 0
    while i < len(source) and j < len(find):
        if j == -1 or source[i] == find[j]:
            i = i + 1
            j = j + 1
        else:
            j = PMT[j]
     
    if j == len(find):
        return i - j
    else:
        return -1

if __name__ == "__main__":
    print("haha")
    str1 = "abababcaa"
    str2 = "ababababcasacbababasbcaabababavbcaababaebabcaababababcaababababca"
    print(kmp(str2,str1))
