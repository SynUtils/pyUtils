'''
Created on 05-Oct-2015

@author: pavan
'''
qnode_config = {'10.71.71.169:3000':"""
                dmp:510:97405:S:BB97EFD707AC40C:MQ:0:0;
                dmp:510:0:A:BB95883057AC40C:RQ:0:0;
                dmp:510:97405:S:BB95883057AC40C:M:0:97405;
                dmp:510:0:A:BB97EFD707AC40C:RQ:0:30"""}
# output:
# MQWD:[510]
expected_output = {'10.71.71.169:3000': {'dmp': {'MQ_without_data': [510],
                               'RQ_data': [510, 510],
                               'RQ_without_data': [510]}}}


def get_qnode_data(self, qnode_config=''):
    qnode_data = dict()
    for _node, config in qnode_config.items():
        if isinstance(config, Exception):
            continue        
        node_qnode = dict()
        for item in config.split(';'):           
            fields = item.split(':')
            ns, pid, node_type, pdata = fields[0], int(fields[1]), fields[5], int(fields[7])            
            # assuming entries for namespaces would be continues  
            if ns not in node_qnode:
                node_qnode[ns] = { 'MQ_without_data' : 0,
                                  'RQ_data' : 0,
                                  'RQ_without_data' : []
                                 }
            if node_type == 'MQ' and pdata == 0:
                node_qnode[ns]['MQ_without_data'] += 1
            elif node_type == 'RQ' and pdata == 0:
                node_qnode[ns]['RQ_without_data'].append(pid)
                node_qnode[ns]['RQ_data'] += 1
            elif node_type == 'RQ':
                node_qnode[ns]['RQ_data'] += 1
             
        qnode_data[_node] = node_qnode
    return qnode_data

#             if  pindex == 0:
#                 node_qnode[ns]['pri_index'] += 1
#             else:
#                 node_qnode[ns]['sec_index'] += 1
#                 
#             try:
#                 if pid in node_qnode[ns]['missing_part']:
#                     node_qnode[ns]['missing_part'].remove(pid)
#             except IndexError:
#                 pass        get_qnode_data(None, qnode_config)

if __name__ == '__main__':
    expected_output == get_qnode_data(None, qnode_config)
    print get_qnode_data(None, qnode_config)
    pass