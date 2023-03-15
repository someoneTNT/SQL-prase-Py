import sys
import datetime

def validate(date_text):
    try:
        datetime.datetime.strptime(date_text, '%Y%m%d')
    except ValueError:
        raise ValueError("Incorrect data format, should be YYYYMMDD")

a='''
    aaa

'''

def print_input(a):
    aaa=f'''
aaaaaaaaaaaa {a}
    '''
    print(aaa)

if __name__ == "__main__":
    etl_dt=''
    if len(sys.argv)>1:
        etl_dt=sys.argv[1]
    else:
        print('请输入时间参数')
        exit()
    
    validate(etl_dt)
    

    a=''' bbb
aaa
    '''
    print_input(a)
    print(etl_dt)