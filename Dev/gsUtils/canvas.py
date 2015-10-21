def get_namespace_health(self, namespace_config = ''):
        namespaces_health = dict()
        namespace_config = {'bar': { '10.71.71.187:3000': {'min-avail-pct': '50',
                                                           'high-water-disk-pct': '50',
                                                           'high-water-memory-pct': '60',
                                                           'hwm-breached': 'false',
                                                           'memory-size': '4294967296',
                                                           'repl-factor': '2',
                                                           'set-evicted-objects': '0',
                                                           'stop-writes': 'false',
                                                           'stop-writes-pct': '90'},
                                     '10.71.71.49:3000': {'min-avail-pct': '10',
                                                          'high-water-disk-pct': '40',
                                                          'high-water-memory-pct': '60',
                                                          'hwm-breached': 'false',
                                                          'memory-size': '4294967296',
                                                          'repl-factor': '2',
                                                          'set-evicted-objects': '0',
                                                          'stop-writes': 'false',
                                                          'stop-writes-pct': '90'}},
                             'test': {'10.71.71.187:3000': {'min-avail-pct': '50',
                                                            'high-water-disk-pct': '50',
                                                            'high-water-memory-pct': '60',
                                                            'hwm-breached': 'false',
                                                            'memory-size': '4294967296',
                                                            'repl-factor': '2',
                                                            'set-evicted-objects': '0',
                                                            'stop-writes': 'false',
                                                            'stop-writes-pct': '90'},
                                      '10.71.71.49:3000': {'min-avail-pct': '0',
                                                           'high-water-disk-pct': '50',
                                                           'high-water-memory-pct': '60',
                                                           'hwm-breached': 'false',
                                                           'memory-size': '4294967296',
                                                           'repl-factor': '2',
                                                           'set-evicted-objects': '0',
                                                           'stop-writes': 'true',
                                                           'stop-writes-pct': '90'}}}

        for ns, nodes in namespace_config.items():
            health_params = {   'min-avail-pct' : 'OK', 
                                'stop-writes' : 'OK',
                                'hwm-breached' : 'OK',
                                'memory-size' : 'OK',
                                'high-water-disk-pct' : 'OK',
                                'high-water-memory-pct' : 'OK',
                                'stop-writes-pct' : 'OK',
                                'repl-factor' : 'OK',
                                'set-evicted-objects' : 'OK'
                            }
            memory_size = ''
            high_water_disk_pct = ''
            high_water_memory_pct = ''
            stop_wirtes_pct = ''
            repl_factor = ''
            set_evicted_objects = ''
            min_avail_pct = ''       
                
            for i, ip in enumerate(nodes.keys()):
                # TODO: check for missing key.
                if i == 0:
                    memory_size = namespace_config[ns][ip].get('memory-size')
                    high_water_disk_pct = namespace_config[ns][ip].get('high-water-disk-pct')
                    high_water_memory_pct = namespace_config[ns][ip].get('high-water-memory-pct')
                    stop_wirtes_pct = namespace_config[ns][ip].get('stop-wirtes-pct')
                    repl_factor = namespace_config[ns][ip].get('repl-factor')
                    set_evicted_objects = namespace_config[ns][ip].get('set-evicted-objects')
                    min_avail_pct = namespace_config[ns][ip].get('min-avail-pct')
                
                def update_health(param, comparator, result):
                    if namespace_config[ns][ip].get(param) != comparator:
                        health_params[param] = result
                try:
                    if int(min_avail_pct) < 20 and int(min_avail_pct) > 5:
                        health_params['min-avail-pct'] = 'WARNING'
                    elif not int(min_avail_pct)  > 20: 
                        health_params['min-avail-pct'] = 'CRITICAL'
                except:
                    # TODO: Missing 'min-avail-pct' key entry for any of the node
                    pass
                    
                update_health('stop-writes', 'false', 'CRITICAL')
                update_health('hwm-breached', 'false', 'WARNING')
                update_health('memory-size', memory_size, 'WARNING')
                update_health('high-water-disk-pct', high_water_disk_pct, 'WARNING')
                update_health('high-water-memory-pct', high_water_memory_pct, 'WARNING')
                update_health('stop-wirtes-pct', stop_wirtes_pct, 'WARNING')
                update_health('repl-factor', repl_factor, 'CRITICAL')
                update_health('set-evicted-objects', set_evicted_objects, 'WARNING')  
                
            namespaces_health[ns] = health_params
        return namespaces_health
            
def test_namespace_health_test():
    namespace_config = {'test': {'10.71.71.187:3000': {'high-water-disk-pct': '50',
                                                        'high-water-memory-pct': '60',
                                                        'hwm-breached': 'false',
                                                        'memory-size': '4294967296',
                                                        'repl-factor': '2',
                                                        'set-evicted-objects': '0',
                                                        'stop-writes': 'false',
                                                        'stop-writes-pct': '90'},
                                  '10.71.71.49:3000': {'high-water-disk-pct': '50',
                                                       'high-water-memory-pct': '6',
                                                       'hwm-breached': 'false',
                                                       'memory-size': '4294967296',
                                                       'repl-factor': '2',
                                                       'set-evicted-objects': '0',
                                                       'stop-writes': 'true',
                                                       'stop-writes-pct': '90'}}}
    health_params = {   'min-avail-pct' : 'OK', 
                        'stop-writes' : 'OK',
                        'hwm-breached' : 'OK',
                        'memory-size' : 'OK',
                        'high-water-disk-pct' : 'OK',
                        'high-water-memory-pct' : 'WARNING',
                        'stop-writes-pct' : 'CRITICAL',
                        'repl-factor' : 'OK',
                        'set-evicted-objects' : 'OK'
                    }

def test_namespace_health_bar():
    pass


if __name__ ==  '__main__':
   health =  get_namespace_health(None)
   for k, v in health.items():
       print k 
       print v 
    
    
    
    
        
        