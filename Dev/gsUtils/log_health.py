'''
Created on 18-Oct-2015

@author: pavan
'''
log_config1 = {'172.17.42.1:3000': 'cf:misc:Debug;cf:alloc:INFO;cf:hash:INFO;cf:rchash:INFO;cf:shash:INFO;cf:queue:INFO;cf:msg:INFO;cf:redblack:INFO;cf:socket:INFO;cf:timer:INFO;cf:ll:INFO;cf:arenah:INFO;cf:arena:INFO;config:INFO;namespace:INFO;as:INFO;bin:INFO;record:INFO;proto:INFO;particle:INFO;demarshal:INFO;write:INFO;rw:INFO;tsvc:INFO;test:INFO;nsup:INFO;proxy:INFO;hb:INFO;fabric:INFO;partition:INFO;paxos:INFO;migrate:INFO;info:INFO;info-port:INFO;storage:INFO;drv_mem:INFO;drv_fs:INFO;drv_files:INFO;drv_ssd:INFO;drv_kv:INFO;scan:INFO;index:INFO;batch:INFO;trial:INFO;xdr:INFO;cf:rbuffer:INFO;fb_health:INFO;cf:arenax:INFO;compression:INFO;sindex:INFO;udf:INFO;query:INFO;smd:INFO;mon:INFO;ldt:INFO;cf:jem:INFO;security:INFO;aggr:INFO'}

log_config2 = {'10.71.71.159:3000': 'cf:misc:INFO;cf:alloc:INFO;cf:hash:INFO;cf:rchash:INFO;cf:shash:INFO;cf:queue:INFO;cf:msg:INFO;cf:redblack:INFO;cf:socket:INFO;cf:timer:INFO;cf:ll:INFO;cf:arenah:INFO;cf:arena:INFO;config:INFO;namespace:INFO;as:INFO;bin:INFO;record:INFO;proto:INFO;particle:INFO;demarshal:INFO;write:INFO;rw:INFO;tsvc:INFO;test:INFO;nsup:INFO;proxy:INFO;hb:INFO;fabric:INFO;partition:INFO;paxos:INFO;migrate:INFO;info:INFO;info-port:INFO;storage:INFO;drv_mem:INFO;drv_fs:INFO;drv_files:INFO;drv_ssd:INFO;drv_kv:INFO;scan:INFO;index:INFO;batch:INFO;trial:INFO;xdr:INFO;cf:rbuffer:INFO;fb_health:INFO;cf:arenax:INFO;compression:INFO;sindex:INFO;udf:INFO;query:INFO;smd:INFO;mon:INFO;ldt:INFO;cf:jem:INFO;security:INFO;aggr:INFO',
 '10.71.71.179:3000': 'cf:misc:DEBUG;cf:alloc:INFO;cf:hash:INFO;cf:rchash:ERROR;cf:shash:INFO;cf:queue:INFO;cf:msg:INFO;cf:redblack:INFO;cf:socket:INFO;cf:timer:INFO;cf:ll:INFO;cf:arenah:INFO;cf:arena:INFO;config:INFO;namespace:INFO;as:INFO;bin:INFO;record:INFO;proto:INFO;particle:INFO;demarshal:INFO;write:INFO;rw:INFO;tsvc:INFO;test:INFO;nsup:INFO;proxy:INFO;hb:INFO;fabric:INFO;partition:INFO;paxos:INFO;migrate:INFO;info:INFO;info-port:INFO;storage:INFO;drv_mem:INFO;drv_fs:INFO;drv_files:INFO;drv_ssd:INFO;drv_kv:INFO;scan:INFO;index:INFO;batch:INFO;trial:INFO;xdr:INFO;cf:rbuffer:INFO;fb_health:INFO;cf:arenax:INFO;compression:INFO;sindex:INFO;udf:INFO;query:INFO;smd:INFO;mon:INFO;ldt:INFO;cf:jem:INFO;security:INFO;aggr:INFO;job:INFO',
 '10.74.76.73:3000': 'cf:misc:INFO;cf:alloc:WARNING;cf:hash:INFO;cf:rchash:INFO;cf:shash:INFO;cf:queue:INFO;cf:msg:INFO;cf:redblack:INFO;cf:socket:INFO;cf:timer:INFO;cf:ll:INFO;cf:arenah:INFO;cf:arena:INFO;config:INFO;namespace:INFO;as:INFO;bin:INFO;record:INFO;proto:INFO;particle:INFO;demarshal:INFO;write:INFO;rw:INFO;tsvc:INFO;test:INFO;nsup:INFO;proxy:INFO;hb:INFO;fabric:INFO;partition:INFO;paxos:INFO;migrate:INFO;info:INFO;info-port:INFO;storage:INFO;drv_mem:INFO;drv_fs:INFO;drv_files:INFO;drv_ssd:INFO;drv_kv:INFO;scan:INFO;index:INFO;batch:INFO;trial:INFO;xdr:INFO;cf:rbuffer:INFO;fb_health:INFO;cf:arenax:INFO;compression:INFO;sindex:INFO;udf:INFO;query:INFO;smd:INFO;mon:INFO;ldt:INFO;cf:jem:INFO;security:INFO;aggr:INFO'}

"""cf:misc:INFO
   cf:alloc:INFO
   cf:hash:INFO
   cf:rchash:INFO
   cf:shash:INFO
   cf:queue:INFO
   cf:msg:INFO
   cf:redblack:INFO
   cf:socket:INFO
   cf:timer:INFO
   cf:ll:INFO
   cf:arenah:INFO
   cf:arena:INFO
   config:INFO
   namespace:INFO
   as:INFO
   bin:INFO
   record:INFO
   proto:INFO
   particle:INFO
   demarshal:INFO
   write:INFO
   rw:INFO
   tsvc:INFO
   test:INFO
   nsup:INFO
   proxy:INFO
   hb:INFO
   fabric:INFO
   partition:INFO
   paxos:INFO
   migrate:INFO
   info:INFO
   info-port:INFO
   storage:INFO
   drv_mem:INFO
   drv_fs:INFO
   drv_files:INFO
   drv_ssd:INFO
   drv_kv:INFO
   scan:INFO
   index:INFO
   batch:INFO
   trial:INFO
   xdr:INFO
   cf:rbuffer:INFO
   fb_health:INFO
   cf:arenax:INFO
   compression:INFO
   sindex:INFO
   udf:INFO
   query:INFO
   smd:INFO
   mon:INFO
   ldt:INFO
   cf:jem:INFO
   security:INFO
   aggr:INFO"""
                

class ShowHealthController():
    def get_logs_health(self, logs_config = ''):
        KEY_NAME = 'contexts'
        log_health = dict()
        log_health_missing = dict()
        for ip, params in logs_config.items():
            context_dict = {KEY_NAME : 'OK'}
            context_missing = {}
            for param in params.split(';'):
                context_info =  param.rsplit(':', 1)
                if context_info[1] != 'INFO':
                    context_dict[KEY_NAME] = 'WARNING'
                    context_missing[context_info[0]] = context_info[1]
            log_health[ip]= context_dict
            log_health_missing[ip] = context_missing
        return(log_health, log_health_missing)

if __name__ == '__main__':
    shc = ShowHealthController()
    health, health_missing =  shc.get_log_health(log_config2)
    print health
    print health_missing
    


