def test(lst):
    result ={}
    for i in lst:
        result[i[0]] = item[1:]
    return result


student=[[1,'Jean castro','V'],[2,'lula Powell','V'],[  3,'Maggie Myers','V'],[4,'Dustin Howard','VI'],[5,'Mason Reed','VII']]

print("\n Oringianla lsit  of lsits :")
print(student)
print("\n Converted dict :")
print(test(student))