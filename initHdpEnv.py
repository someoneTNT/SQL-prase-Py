from krbticket import KrbConfig, KrbCommand
import os

def init_env():
    '''
        初始化YARN需要的环境
    '''
    os.environ['SPARK_HOME'] = '/opt/cloudera/parcels/CDH/lib/spark'
    os.environ['PYSPARK_PYTHON'] = '/home/hadoop/.conda/envs/data_env/bin/python'
    os.environ['PYSPARK_DRIVER_PYTHON'] = '/home/hadoop/.conda/envs/data_env/bin/python'
    os.environ['HADOOP_CONF_DIR'] = '/etc/hadoop/conf'

    # os.environ['KRB5CCNAME'] =f'/tmp/krb5cc_hadoop'
    kconfig = KrbConfig(principal='hadoop@CDH.COM',keytab='/app/bigdata/etl_common/cfg/hadoop.keytab')
    KrbCommand.kinit(kconfig)

    print('完成环境信息声明') 
