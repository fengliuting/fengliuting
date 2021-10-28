import yaml
'''data01 中是list列表；data02和data04中是dict字典,data02是字典套字典，data04是集合套字典'''
f=open('../data/data03',mode='r',encoding='utf-8')
data=yaml.load(stream=f,Loader=yaml.FullLoader)

print(type(data))
print(data)
# print(data[0])
print(data[1]['年龄'])