'''
Created on 19-Oct-2015

@author: pavan
'''
network_config1 = {'10.71.71.159:3000': 'heartbeat-mode=multicast;heartbeat-protocol=v2;heartbeat-address=239.1.99.222;heartbeat-port=9948;heartbeat-interval=150;heartbeat-timeout=10',
 '10.71.71.179:3000': 'heartbeat-mode=multicast;heartbeat-protocol=v2;heartbeat-address=239.1.99.222;heartbeat-port=9948;heartbeat-interval=150;heartbeat-timeout=10',
 '10.74.76.73:3000': 'heartbeat-mode=multicast;heartbeat-protocol=v2;heartbeat-address=239.1.99.222;heartbeat-port=9948;heartbeat-interval=150;heartbeat-timeout=10'}


class ShowHealthController():
    HEARTBEAT_INTERVAL = 'heartbeat-interval'
    HEARTBEAT_TIMEOUT = 'heartbeat-timeout'
    
    NETWORK_PARAMS = {
                      HEARTBEAT_INTERVAL : 'OK',
                      HEARTBEAT_TIMEOUT : 'OK'
                     }
    
    NETWORK_LOOKUP = [HEARTBEAT_INTERVAL,
                      HEARTBEAT_TIMEOUT
                     ]
    def get_network_health(self, network_config = ''):
        network_health = dict()
        for ip, params in network_config.items():
            is_first = True
            network_health[ip] = dict()
            for param in params.split(';'):                
                if is_first:
                    heartbeat_interval = param.get(ShowHealthController.HEARTBEAT_INTERVAL)
                    heartbeat_timeout =  param.get(ShowHealthController.HEARTBEAT_TIMEOUT)
                    is_first = False
        pass
        
#         KEY_NAME = 'contexts'
#         log_health = dict()
#         log_health_missing = dict()
#         for ip, params in logs_config.items():
#             context_dict = {KEY_NAME : 'OK'}
#             context_missing = {}
#             for param in params.split(';'):
#                 context_info =  param.rsplit(':', 1)
#                 if context_info[1] != 'INFO':
#                     context_dict[KEY_NAME] = 'WARNING'
#                     context_missing[context_info[0]] = context_info[1]
#             log_health[ip]= context_dict
#             log_health_missing[ip] = context_missing
#         return(log_health, log_health_missing)

if __name__ == '__main__':
    shc = ShowHealthController()
    print shc.get_network_health(network_config1)
    
    
    