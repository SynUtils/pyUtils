'''
Created on 30-Sep-2015
@author: pavan
'''
import copy

pmap_info = {'10.5.4.3': """
test:0:S:0:0:0:0:0:0:0:0:0;
test:1:S:1:0:0:0:0:0:0:0:0;
test:2:S:1:0:0:0:0:0:0:0:0;
test:3:A:2:0:0:0:0:0:0:0:0;
test:4:S:1:0:0:0:0:0:0:0:0;
test:5:S:0:0:0:0:0:0:0:0:0;
test:6:S:0:0:0:0:0:0:0:0:0;
test:7:S:0:0:0:0:0:0:0:0:0;
test:8:S:0:0:0:0:0:0:0:0:0;
test:10:S:1:0:0:0:0:0:0:0:0;
test:11:S:1:0:0:0:0:0:0:0:0;
test:12:S:1:0:0:0:0:0:0:0:0;
bar:0:S:0:0:0:0:0:0:0:0:0;
bar:1:S:1:0:0:0:0:0:0:0:0;
bar:2:S:1:0:0:0:0:0:0:0:0;
bar:3:A:2:0:0:0:0:0:0:0:0;
bar:4:S:1:0:0:0:0:0:0:0:0;
bar:5:S:0:0:0:0:0:0:0:0:0;
bar:6:S:0:0:0:0:0:0:0:0:0;
bar:7:S:0:0:0:0:0:0:0:0:0;
bar:8:S:0:0:0:0:0:0:0:0:0;
bar:9:A:2:0:0:0:0:0:0:0:0;
bar:10:S:1:0:0:0:0:0:0:0:0;
bar:11:S:1:0:0:0:0:0:0:0:0;
bar:12:S:1:0:0:0:0:0:0:0:0
""",
'10.71.71.159' : """
test:0:S:1:0:0:0:0:0:0:0:0;
test:1:S:0:0:0:0:0:0:0:0:0;
test:2:S:0:0:0:0:0:0:0:0:0;
test:3:S:0:0:0:0:0:0:0:0:0;
test:4:A:2:0:0:0:0:0:0:0:0;
test:5:A:2:0:0:0:0:0:0:0:0;
test:6:S:1:0:0:0:0:0:0:0:0;
test:7:A:2:0:0:0:0:0:0:0:0;
test:8:S:1:0:0:0:0:0:0:0:0;
test:9:S:1:0:0:0:0:0:0:0:0;
test:10:A:2:0:0:0:0:0:0:0:0;
test:11:A:2:0:0:0:0:0:0:0:0;
test:12:A:2:0:0:0:0:0:0:0:0;
bar:0:S:1:0:0:0:0:0:0:0:0;
bar:1:S:0:0:0:0:0:0:0:0:0;
bar:2:S:0:0:0:0:0:0:0:0:0;
bar:3:S:0:0:0:0:0:0:0:0:0;
bar:4:A:2:0:0:0:0:0:0:0:0;
bar:5:A:2:0:0:0:0:0:0:0:0;
bar:6:S:1:0:0:0:0:0:0:0:0;
bar:7:A:2:0:0:0:0:0:0:0:0;
bar:8:S:1:0:0:0:0:0:0:0:0;
bar:9:S:1:0:0:0:0:0:0:0:0;
bar:10:A:2:0:0:0:0:0:0:0:0;
bar:11:A:2:0:0:0:0:0:0:0:0;
bar:12:A:2:0:0:0:0:0:0:0:0
"""
}

pmap_info_obj = {'10.71.71.169': """
test:0:S:0:0:0:0:0:112:8:0:0;
test:1:S:1:0:0:0:0:182:13:0:0;
test:2:S:1:0:0:0:0:224:16:0:0;
test:3:A:2:0:0:0:0:0:0:0:0;
test:4:S:1:0:0:0:0:98:7:0:0;
test:5:S:0:0:0:0:0:126:9:0:0;
test:6:S:0:0:0:0:0:112:8:0:0;
test:7:S:0:0:0:0:0:112:8:0:0;
test:8:S:0:0:0:0:0:98:7:0:0;
test:9:A:2:0:0:0:0:0:0:0:0;
test:10:S:1:0:0:0:0:168:12:0:0;
test:11:S:1:0:0:0:0:154:11:0:0;
test:12:S:1:0:0:0:0:168:12:0:0""",
'10.71.71.179': """
test:0:A:2:0:0:0:0:0:0:0:0;
test:1:A:2:0:0:0:0:0:0:0:0;
test:2:A:2:0:0:0:0:0:0:0:0;
test:3:S:1:0:0:0:0:154:11:0:0;
test:4:S:0:0:0:0:0:98:7:0:0;
test:5:S:1:0:0:0:0:126:9:0:0;
test:6:A:2:0:0:0:0:0:0:0:0;
test:7:S:1:0:0:0:0:112:8:0:0;
test:8:A:2:0:0:0:0:0:0:0:0;
test:9:S:0:0:0:0:0:182:13:0:0;
test:10:S:0:0:0:0:0:168:12:0:0;
test:11:S:0:0:0:0:0:154:11:0:0;
test:12:S:0:0:0:0:0:168:12:0:0""",
'10.71.71.159': """
test:0:S:1:0:0:0:0:112:8:0:0;
test:1:S:0:0:0:0:0:182:13:0:0;
test:2:S:0:0:0:0:0:224:16:0:0;
test:3:S:0:0:0:0:0:154:11:0:0;
test:4:A:2:0:0:0:0:0:0:0:0;
test:5:A:2:0:0:0:0:0:0:0:0;
test:6:S:1:0:0:0:0:112:8:0:0;
test:7:A:2:0:0:0:0:0:0:0:0;
test:8:S:1:0:0:0:0:98:7:0:0;
test:9:S:1:0:0:0:0:182:13:0:0;
test:10:A:2:0:0:0:0:0:0:0:0;
test:11:A:2:0:0:0:0:0:0:0:0;
test:12:A:2:0:0:0:0:0:0:0:0
"""
}

part_data = [[], [], [], [1], [0], [1], [], [1], [], [0], [0], [0]]
ns_info = {
           'test': {'repl_factor': 2,
                    'avg_master_objs':112,
                    'avg_replica_objs': 100
                    },
           'bar': {'repl_factor': 2,
                   'avg_master_objs':50,
                    'avg_replica_objs': 50
                    }
           }

def format_missing_part(part_data):
    missing_part = ''
    get_part = lambda pid, pindex: str(pid) + ':S:' + str(pindex) + ','
    for pid, part in enumerate(part_data):
        if part:
            for pindex in part:
                missing_part += get_part(pid, pindex)
    return missing_part[:-1]

def get_pmap_data(self, pmap_info, ns_info):
    # TODO: handle ZeroDivisionError 
    # TODO: check if node not have master & replica objects 
    pid_range = 13        # each namespace is devided into 4096 partition
    disc_pct_allowed = 1   # Considering Negative & Positive both discrepancy
    get_dist_delta = lambda exp, act: abs((exp - act) * 100 / exp) > disc_pct_allowed
    pmap_data = {}
    ns_missing_part = {}
    visited_ns = set()
    for _node, partitions in pmap_info.items():
        node_pmap = dict()
        if isinstance(partitions, Exception):
            continue
        for item in partitions.split(';'):           
            fields = item.split(':')
            ns, pid, state, pindex, master_obj = fields[0], int(fields[1]), fields[2], int(fields[3]), int(fields[8])
            # assuming entries for namespaces would be continues  
            if ns not in node_pmap:
                node_pmap[ns] = { 'pri_index' : 0,
                                  'sec_index' : 0,
                                  'master_disc_part': [],
                                  'replica_disc_part':[]
                                }
            if ns not in visited_ns:
                ns_missing_part[ns] = {}
                ns_missing_part[ns]['missing_part'] = [range(ns_info[ns.strip()]['repl_factor']) for i in range(pid_range)]
                visited_ns.add(ns)
            if state == 'S':
                try:
                    if  pindex == 0:
                        node_pmap[ns]['pri_index'] += 1
                        if get_dist_delta(ns_info[ns.strip()]['avg_master_objs'], master_obj):
                            node_pmap[ns]['master_disc_part'].append(pid)
                    if  pindex in range(1, ns_info[ns.strip()]['repl_factor']):
                        node_pmap[ns]['sec_index'] += 1
                        if get_dist_delta(ns_info[ns.strip()]['avg_replica_objs'], master_obj):
                            node_pmap[ns]['replica_disc_part'].append(pid)
                    ns_missing_part[ns]['missing_part'][pid].remove(pindex)
                except Exception as e:
                    print e
            if pid not in range(pid_range):
                print "For {0} found partition-ID {1} which is beyond legal partitions(0...4096)".format(ns, pid)
        for _ns, config in node_pmap.items():
            node_pmap[_ns]['distribution_pct'] = node_pmap[_ns]['pri_index'] * 100 / pid_range

        pmap_data[_node] = node_pmap
    for _node, _ns in pmap_data.items():
        for ns_name, params in _ns.items():
            params['missing_part'] = format_missing_part(ns_missing_part[ns_name]['missing_part'])
    return pmap_data

if __name__ == '__main__':
#     print format_missing_part(part_data)
    pmap_data = get_pmap_data(None, pmap_info, ns_info)
    for k, v in pmap_data.items():
        print k 
        for key, value in v.items():
            print key, value

           

