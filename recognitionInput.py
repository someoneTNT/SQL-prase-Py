# author: dzj
# date: 2023-03-08
# desc: 内容识别


def recSQL(sql):
    '''
        对输入的SQL内容进行分段识别
    '''
    
    sql_list=[]
    sql_list = sql.split(';')
    
    l_len=len(sql_list)

    if l_len == 0 :
        print('未识别成功') 
    
    sql_list =[ item.strip() for item in sql_list if item.strip() ]
    return sql_list
    
if __name__ == "__main__":
    sql=''''''
    print(recSQL(sql) )