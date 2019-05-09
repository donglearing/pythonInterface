#coding:utf-8
import json
class OperrationJson:
    def __init__(self, file_path=None):
        if file_path == None:
            self.file_path = 'E:\\learn\\python\\InterFaceDev\\dataconfig\\user.json'
        else:
            self.file_path = file_path
        self.data = self.read_data()

    #读取json文件
    def read_data(self):
        with open(self.file_path) as fp:
            data = json.load(fp)
            return data
    #根据关键字获取数据
    def get_data(self,id):
        print(type(self.data))
        return self.data[id]
    #写入json数据
    def write_data(self,data):
        with open('E:\\learn\\python\\InterFaceDev\\dataconfig\\cookie.json', 'w') as fp:
            json.dump(data,fp)
            #fp.write(json.dumps(data))



if __name__ == '__main__':
    #file = 'E:\\user.json'
    opjson = OperrationJson()
    print(opjson.get_data('data')['token'])
    print(opjson.data)
    opjson.write_data(opjson.data)

    #print(opjson.data)
    #print(opjson.write_data("rrr"))
    #opjson.get_data('token')



