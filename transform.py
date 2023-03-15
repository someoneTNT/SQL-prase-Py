# author: dzj
# date: 2023-03-08
# desc: 内容转换，包裹数据

import recognitionInput as rip
import re

import os, sys

def base_path(path):
    if getattr(sys, 'frozen', None):
        basedir = sys._MEIPASS  # type: ignore
# 用 pyinstaller 打包生成的 exe 文件，在运行时动态生成依赖文件，sys._MEIPASS 就是这些依赖文件所在文件夹的路径
# 通常  C:\Windows\Temp\_MEIxxxx 或 C:\Users\用户名\AppData\Local\Temp\_MEIxxxx
#  仅在 exe 运行时有效，IDE运行时报错：

    else:
        basedir = os.path.dirname(__file__)
    return os.path.join(basedir, path)

def transContent(sql_list):
    '''
        将传入的sql列表转为spark.sql执行的语句
    '''
        
    tmd = base_path('') # 这是解压路径
    cwd = os.getcwd() # 这是程序的所在路径 
    os.chdir(tmd)  
    file_content=''
    for _sql in sql_list:
        # print(_sql)
        # _sql = _sql.replace('${VAR:ETL_DT}','{ETL_DT}')
        _sql = re.sub(r'\${VAR:ETL_DT}', '{etl_dt}', _sql, flags=re.IGNORECASE)
        # print(_sql)
        file_content = file_content+'\n\n'+f'    spark.sql(f"""{_sql}""")'

    contents=''
    with open(r'generic_model.txt', encoding='utf-8') as file_obj:
        contents = file_obj.read()
        contents = contents.replace('{{替换内容}}',file_content)      
  
    return contents


if __name__ == "__main__":
    sql='''       
        insert into tabB 
        select * from tabA;
        -- 测试demo
        select * from tabB
    '''
    sql_list=rip.recSQL(sql)
    print(transContent(sql_list)) 