import pymysql
from settings import database

"""
SELECT {fields} FROM {table} {where} {groupby} {having} {orderby} {limit}.format(table='stduent',fields='sno,sname')
"""


class Manager:
    def __init__(self, tableName):
        self.tableName = tableName  # 表名
        self.conn = self.__connect(**database)  # 链接数据库
        self.cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)  # 游标
        self.options = self.__initOptions()  # 初始化查询参数

    def __del__(self):
        self.cursor.close()
        self.conn.close()

    def __connect(self, **kwargs):
        """
        自定义的链接数据库方法
        :param kwargs: 数据库链接参数字典
        :return: 链接对象
        """
        return pymysql.Connect(**kwargs)

    def __initOptions(self, **kwargs):
        """
        初始化查询参数字典
        :param kwargs: 字典，保存查询参数
        :return:
        """
        return {
            'fields': '*',
            'table': self.tableName,
            'where': '',
            'groupby': '',
            'having': '',
            'orderby': '',
            'limit': '',
            'values': ''
        }

    def where(self, **kwargs):
        """"
        {'user':'root','password':'123}
        user__like='李'  user like '李%'
        where user='root' and password='123
        """
        # print(kwargs)
        if len(kwargs) <= 0:  # 如果不传任何参数，直接返回
            return self
        if not self.options['where']:  # 没有where条件
            self.options['where'] = " where "
        else:
            self.options['where'] += ' and '
        ops = {
            'gt':'>',
            'gte':'>=',
            'lt':'<',
            'lte':'<=',
            'ne':'<>'
        }
        # 拼接参数
        for key in kwargs:
            op = key.split("__")  # 得到键和运算符
            if isinstance(kwargs[key], str):
                if len(op) > 1:
                    self.options['where'] += op[0] + ops[op[1]] +"'" +pymysql.escape_string(kwargs[key])+"'" + ' and '
                else:
                    self.options['where'] += op[0] + "=" +"'" +pymysql.escape_string(kwargs[key])+"'" + ' and '
                # self.options['where'] += key + " = '" + pymysql.escape_string(kwargs[key]) + "'" + ' and '
            else:
                if len(op) > 1:
                    self.options['where'] += op[0] + ops[op[1]] + str(kwargs[key]) + ' and '
                else:
                    self.options['where'] += op[0] + "="  + str(kwargs[key])  + ' and '

                # self.options['where'] += key + " = " + str(kwargs[key]) + ' and '
        self.options['where'] = self.options['where'].rstrip('and ')  # 去除最后的and

        return self

    def limit(self, *args):
        """
        (10,20)
        :param args:
        :return:
        """
        self.options['limit'] = ' limit '
        for value in args:
            self.options['limit'] += str(value) + ' , '
        self.options['limit'] = self.options['limit'].rstrip(', ')
        return self

    def orderby(self, *args):
        """

        :param args: 'sno','sname'
        :return:
        """
        if len(args) <= 0:
            return self
        if not self.options['orderby']:
            self.options['orderby'] = ' order by '
        else:
            self.options['orderby'] += ' , '
        # 生成字典列表
        self.options['orderby'] += ','.join(args)

        return self

    def values(self, *args):
        """
        生成字段列表
        :param args:
        :return:
        """
        if len(args) <= 0:
            return self;
        self.options['fields'] = ','.join(args)
        return self

    def select(self):
        sql = "SELECT {fields} FROM {table} {where} {groupby} {having} {orderby} {limit}".format(**self.options)

        return self.query(sql)  # 调用query方法查询

    def query(self, sql):
        if not sql:
            return None
        self.sql = sql  # 保存sql
        self.options = self.__initOptions()  # 参数字典初始化
        try:
            rows = self.cursor.execute(sql)
            if rows > 0:
                return self.cursor.fetchall()
            else:
                return None
        except Exception as e:
            # print(e)
            return None

    def addQuote(self, data):
        """
        给字符串添加单引号
        :param data:字典
        :return:
        """
        for key in data:
            if isinstance(data[key], str):
                data[key] = "'" + data[key] + "'"

    def getKeyValuseList(self, data):
        """
        获取键列表和值列表
        :param data: 参数字典
        :return:
        """
        keys = ''
        values = ''
        for key in data:
            keys += key + ','
            values += str(data[key]) + ','
        return keys.rstrip(','), values.rstrip(',')

    def insert(self, data):
        """
        插入记录
        :param data: 字典，{'sno':'009','sname':'tom'}
        :return: 成功返回True，失败返回False
        """
        # 1. 如果值是字符串，要添加单引号
        self.addQuote(data)

        # 2.生成键列表和值列表
        keys, values = self.getKeyValuseList(data)
        self.options['fields'] = keys
        self.options['values'] = values

        sql = "INSERT INTO {table}({fields}) VALUES({values})".format(**self.options)
        return self.excute(sql)

    def excute(self,sql):
        """
        执行增删改
        :param sql:
        :return: 成功返回True，失败返回False
        """
        if not sql:
            return False
        self.options = self.__initOptions()
        self.sql = sql
        try:
            rows = self.cursor.execute(sql)
            if rows > 0:
                self.conn.commit()
                return True
            else:
                self.conn.rollback()
                return False
        except Exception as e:
            # print(e)
            self.conn.rollback()
            return False
    def delete(self):
        """
        删除记录
        :return:
        """
        sql = "DELETE FROM {table} {where}".format(**self.options)
        return self.excute(sql)

    def update(self,data):
        """
        更新记录
        :param data: 字典
        :return:
        """
        self.addQuote(data)
        self.options['values'] = ','.join([key+"="+str(value) for key,value in data.items()])
        sql = "UPDATE {table} SET {values} {where}".format(**self.options)
        return self.excute(sql)
    """
    all() 获取所有记录
    get 根据主键获取一条记录
    getByxxx  xxx sname
    count max  min sum avg    获取一个值
    
    """


if __name__ == "__main__":
    db = Manager('student')
    # sql ="SELECT {fields} FROM {table} {where} {groupby} {having} {orderby} {limit}".format(**db.options)
    # print(db.options)
    # print(sql)
    # data = db.where(sname='李婷').select()
    # data = db.query("select * from student where sclass='1812'")
    # print(data)
    # db.where(username='admin').select()
    # data = db.values('sno','sname').where(sclass='1812').orderby('sno desc','sname').select()
    # print(data)
    # print(db.sql)
    # db.addQuote({'sno':'009','sname':'tom'})
    # flag = db.insert({'sno': '013', 'sname': 'tom', 'sclass': '1812'})
    # print(flag)
    # flag = db.where(sno='013').delete()
    # print(flag)
    # flag = db.update({'sbirthday':"2009-3-12"})
    # print(flag)
    data = db.where(sno__gt='003').select()
    # print(data)