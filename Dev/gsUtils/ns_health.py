'''
Created on 15-Oct-2015

@author: pavan
'''
import copy
namespace_config1 = {'bar': { '10.71.71.187:3000': {'min-avail-pct': '50',
                                                   'high-water-disk-pct': '50',
                                                   'high-water-memory-pct': '60',
                                                   'hwm-breached': 'false',
                                                   'memory-size': '4294967296',
                                                   'repl-factor': '2',
                                                   'set-evicted-objects': '0',
                                                   'stop-writes': 'false',
                                                   'stop-writes-pct': '90',
                                                   'free-pct-memory' : '80'},
                             '10.71.71.49:3000': {'min-avail-pct': '10',
                                                  'high-water-disk-pct': '40',
                                                  'high-water-memory-pct': '60',
                                                  'hwm-breached': 'false',
                                                  'memory-size': '4294967296',
                                                  'repl-factor': '2',
                                                  'set-evicted-objects': '0',
                                                  'stop-writes': 'false',
                                                  'stop-writes-pct': '90',
                                                  'free-pct-memory' : '80'}},
                     'test': {'10.71.71.187:3000': {'min-avail-pct': '50',
                                                    'high-water-disk-pct': '50',
                                                    'high-water-memory-pct': '60',
                                                    'hwm-breached': 'false',
                                                    'memory-size': '4294967296',
                                                    'repl-factor': '2',
                                                    'set-evicted-objects': '5',
                                                    'stop-writes': 'false',
                                                    'stop-writes-pct': '90',
                                                    'free-pct-memory' : '80'},
                              '10.71.71.49:3000': {'min-avail-pct': '0',
                                                   'high-water-disk-pct': '50',
                                                   'high-water-memory-pct': '60',
                                                   'hwm-breached': 'false',
                                                   'memory-size': '4294967296',
                                                   'repl-factor': '7',
                                                   'set-evicted-objects': '0',
                                                   'stop-writes': 'true',
                                                   'stop-writes-pct': '90',
                                                   'free-pct-memory' : '80'}}}

namespace_config2 = {'bar2': { '10.71.71.187:3000': {'min-avail-pct': '50',
                                                   'high-water-disk-pct': '50',
                                                   'high-water-memory-pct': '60',
                                                   'hwm-breached': 'ABC',
                                                   'memory-size': '4294967296',
                                                   'repl-factor': '2',
                                                   'set-evicted-objects': '0',
                                                   'stop-writes': 'false',
                                                   'stop-writes-pct': '90',
                                                   'free-pct-memory' : '80'},
                             '10.71.71.49:3000': {'min-avail-pct': '10',
                                                  'high-water-disk-pct': '40',
                                                  'high-water-memory-pct': '60',
                                                  'hwm-breached': 'false',
                                                  'memory-size': '4294967296',
                                                  'repl-factor': '2',
                                                  'set-evicted-objects': '0',
                                                  'stop-writes': 'false',
                                                  'stop-writes-pct': '90',
                                                  'free-pct-memory' : '80'}},
                     'test2': {'10.71.71.187:3000': {'min-avail-pct': '50',
                                                    'high-water-disk-pct': '50',
                                                    'high-water-memory-pct': '60',
                                                    'hwm-breached': 'XYZ',
                                                    'memory-size': '4294967296',
                                                    'repl-factor': '2',
                                                    'set-evicted-objects': '0',
                                                    'stop-writes': 'false',
                                                    'stop-writes-pct': '90',
                                                    'free-pct-memory' : '80'},
                              '10.71.71.49:3000': {'min-avail-pct': '0',
                                                   'high-water-disk-pct': '50',
                                                   'high-water-memory-pct': '60',
                                                   'hwm-breached': 'false',
                                                   'memory-size': '4294967296',
                                                   'repl-factor': '5',
                                                   'set-evicted-objects': '0',
                                                   'stop-writes': 'true',
                                                   'stop-writes-pct': '90',
                                                   'free-pct-memory' : '80'}}}

exp_output1 = {'bar': {'10.71.71.187:3000': {'high-water-disk-pct': 'WARNING',
                                               'high-water-memory-pct': 'OK',
                                               'hwm-breached': 'OK',
                                               'memory-size': 'OK',
                                               'min-avail-pct': 'OK',
                                               'repl-factor': 'OK',
                                               'set-evicted-objects': 'OK',
                                               'stop-writes': 'OK',
                                               'stop-writes-pct': 'OK',
                                               'type': 'OK'},
                         '10.71.71.49:3000': {'high-water-disk-pct': 'WARNING',
                                              'high-water-memory-pct': 'OK',
                                              'hwm-breached': 'OK',
                                              'memory-size': 'OK',
                                              'min-avail-pct': 'WARNING',
                                              'repl-factor': 'OK',
                                              'set-evicted-objects': 'OK',
                                              'stop-writes': 'OK',
                                              'stop-writes-pct': 'OK',
                                              'type': 'OK'}},
                 'test': {'10.71.71.187:3000': {'high-water-disk-pct': 'OK',
                                                'high-water-memory-pct': 'OK',
                                                'hwm-breached': 'OK',
                                                'memory-size': 'OK',
                                                'min-avail-pct': 'OK',
                                                'repl-factor': 'CRITICAL',
                                                'set-evicted-objects': 'WARNING',
                                                'stop-writes': 'CRITICAL',
                                                'stop-writes-pct': 'OK',
                                                'type': 'OK'},
                          '10.71.71.49:3000': {'high-water-disk-pct': 'OK',
                                               'high-water-memory-pct': 'OK',
                                               'hwm-breached': 'OK',
                                               'memory-size': 'OK',
                                               'min-avail-pct': 'CRITICAL',
                                               'repl-factor': 'CRITICAL',
                                               'set-evicted-objects': 'WARNING',
                                               'stop-writes': 'CRITICAL',
                                               'stop-writes-pct': 'OK',
                                               'type': 'OK'}}}


exp_output2 = {'bar2': {'10.71.71.187:3000': {'high-water-disk-pct': 'WARNING',
                                               'high-water-memory-pct': 'OK',
                                               'hwm-breached': 'WARNING',
                                               'memory-size': 'OK',
                                               'min-avail-pct': 'OK',
                                               'repl-factor': 'OK',
                                               'set-evicted-objects': 'OK',
                                               'stop-writes': 'OK',
                                               'stop-writes-pct': 'OK'},
                         '10.71.71.49:3000': {'high-water-disk-pct': 'OK',
                                              'high-water-memory-pct': 'OK',
                                              'hwm-breached': 'OK',
                                              'memory-size': 'OK',
                                              'min-avail-pct': 'WARNING',
                                              'repl-factor': 'OK',
                                              'set-evicted-objects': 'OK',
                                              'stop-writes': 'OK',
                                              'stop-writes-pct': 'OK'}},
                 'test2': {'10.71.71.187:3000': {'high-water-disk-pct': 'OK',
                                                'high-water-memory-pct': 'OK',
                                                'hwm-breached': 'WARNING',
                                                'memory-size': 'OK',
                                                'min-avail-pct': 'OK',
                                                'repl-factor': 'CRITICAL',
                                                'set-evicted-objects': 'OK',
                                                'stop-writes': 'OK',
                                                'stop-writes-pct': 'OK'},
                          '10.71.71.49:3000': {'high-water-disk-pct': 'OK',
                                               'high-water-memory-pct': 'OK',
                                               'hwm-breached': 'OK',
                                               'memory-size': 'OK',
                                               'min-avail-pct': 'CRITICAL',
                                               'repl-factor': 'CRITICAL',
                                               'set-evicted-objects': 'OK',
                                               'stop-writes': 'CRITICAL',
                                               'stop-writes-pct': 'OK'}}}

class ShowHealthController():
    
    FREE_PCT_MEMORY = 'free-pct-memory'
    MIN_AVAIL_PCT = 'min-avail-pct'
    STOP_WRITES = 'stop-writes' 
    HWM_BREACHED = 'hwm-breached' 
    MEMORY_SIZE = 'memory-size' 
    HIGH_WATER_DISK_PCT = 'high-water-disk-pct' 
    HIGH_WATER_MEMEORY_PCT = 'high-water-memory-pct'
    STOP_WRITES_PCT = 'stop-writes-pct'
    REPL_FACTOR = 'repl-factor' 
    SET_EVICTED_OBJECTS = 'set-evicted-objects'
    TYPE = 'type'
    NAMESPACE_COUNT = 'Namespace-Count'
    
    HWM_WARN_CHECK_PCT = 10

    NAMESPACE_PARAMS = {
                        HIGH_WATER_DISK_PCT : 'OK', 
                        HIGH_WATER_MEMEORY_PCT : 'OK', 
                        HWM_BREACHED : 'OK', 
                        MIN_AVAIL_PCT : 'OK',
                        MEMORY_SIZE : 'OK', 
                        REPL_FACTOR : 'OK', 
                        STOP_WRITES_PCT : 'OK',                       
                        STOP_WRITES : 'OK',  
                        SET_EVICTED_OBJECTS : 'OK', 
                        TYPE: 'OK',
                        NAMESPACE_COUNT : 'OK'
                       } 
    
    
    def __init__(self):
        self.modifiers = set(['with', 'like'])
    
#     @CommandHelp('Displays namespace health')
    def _do_default(self, line):
        self.do_namespace(line)   
        pass
    
#     @CommandHelp('get namespaces health dictionary')
    def get_namespaces_health(self, namespace_config = ''):
        ns_count = {}
        namespaces_health = dict()
        for ns, nodes in namespace_config.items():
            broken = {}
            is_first = True
            namespaces_health[ns] = dict()
            for ip, params in nodes.items():
                if params:
                    if ip not in ns_count:
                        ns_count[ip] = [ns]
                    else:
                        ns_count[ip].append(ns)
                    health_params = copy.deepcopy(ShowHealthController.NAMESPACE_PARAMS)
                    if is_first:
                        high_water_disk_pct = params.get(ShowHealthController.HIGH_WATER_DISK_PCT)
                        memory_size =  params.get(ShowHealthController.MEMORY_SIZE)
                        repl_factor =  params.get(ShowHealthController.REPL_FACTOR)
                        stop_writes_pct =  params.get(ShowHealthController.STOP_WRITES_PCT)
                        set_evicted_objects = params.get(ShowHealthController.SET_EVICTED_OBJECTS)
                        type = params.get(ShowHealthController.TYPE)
                        is_first = False
                    def update_health(param, comparator, result):
                        if params.get(param) != comparator:
                            if ip not in broken:
                                broken[ip] = {}
                            broken[ip][param] =  result

                    update_health(ShowHealthController.HIGH_WATER_DISK_PCT, high_water_disk_pct, 'WARNING')
    #                 update_health(ShowHealthController.HIGH_WATER_MEMEORY_PCT, high_water_memory_pct, 'WARNING')
                    update_health(ShowHealthController.HWM_BREACHED, 'false', 'WARNING')
                    update_health(ShowHealthController.MEMORY_SIZE, memory_size, 'WARNING')
                    update_health(ShowHealthController.REPL_FACTOR, repl_factor, 'CRITICAL')
                    update_health(ShowHealthController.STOP_WRITES, 'false', 'CRITICAL')
                    update_health(ShowHealthController.STOP_WRITES_PCT, stop_writes_pct, 'WARNING')
                    update_health(ShowHealthController.SET_EVICTED_OBJECTS, set_evicted_objects, 'WARNING')
                    update_health(ShowHealthController.TYPE, type, 'WARNING')
                    
                    high_water_memory_pct = params.get(ShowHealthController.HIGH_WATER_MEMEORY_PCT)
                    min_avail_pct = params.get(ShowHealthController.MIN_AVAIL_PCT)
                    if high_water_memory_pct is not None:
                        high_water_memory_pct = int(high_water_memory_pct)
                        used_memory_pct = 100 - int(params[ShowHealthController.FREE_PCT_MEMORY])
                        hwm_warn_range = range(high_water_memory_pct - (high_water_memory_pct * ShowHealthController.HWM_WARN_CHECK_PCT / 100) , high_water_memory_pct)
                        if used_memory_pct >= high_water_memory_pct:
                            health_params[ShowHealthController.HIGH_WATER_MEMEORY_PCT] = 'CRITICAL'
                        elif high_water_memory_pct > 65 or used_memory_pct in hwm_warn_range:
                            health_params[ShowHealthController.HIGH_WATER_MEMEORY_PCT] = 'WARNING'
                    if min_avail_pct is not None:
                        min_avail_pct = int(min_avail_pct)
                        if min_avail_pct < 5:
                                health_params[ShowHealthController.MIN_AVAIL_PCT] = 'CRITICAL'
                        elif min_avail_pct <= 20 and min_avail_pct >= 5:
                                health_params[ShowHealthController.MIN_AVAIL_PCT] = 'WARNING'
                    namespaces_health[ns][ip] = health_params
            for _ip, _params in namespaces_health[ns].items():
                for broken_param in broken.values():
                    for param, status in broken_param.items():
                        _params[param] = status
        
        ns_count_iter = iter(ns_count.values())                 #Checking Namespace values for IP
        first = ns_count_iter.next()
        if not all(item == first for item in ns_count_iter):
            for nodes in namespaces_health.values():
                for params in nodes.values():
                    params[ShowHealthController.NAMESPACE_COUNT] = "WARNING"
        
        # Check all keys of ns_count have same value if not then
        # add namespace_count in broken dict
        return namespaces_health

if __name__ == '__main__':
    shc = ShowHealthController()
    
    result = shc.get_namespaces_health(namespace_config1)
    print exp_output1 == result
    print result
    print exp_output1
    
#     print exp_output2 == shc.get_namespaces_health(namespace_config2)
    