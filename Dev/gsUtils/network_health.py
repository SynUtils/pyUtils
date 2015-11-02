'''
Created on 19-Oct-2015

@author: pavan
'''
import copy

network_config1 = {  '10.71.71.159:3000': {},
                     '10.71.71.179:3000': {'allow-inline-transactions': 'true',
                                          'auto-dun': 'false',
                                          'auto-undun': 'false',
                                          'batch-max-requests': '5000',
                                          'batch-priority': '200',
                                          'batch-threads': '4',
                                          'dump-message-above-size': '134217728',
                                          'fabric-workers': '16',
                                          'fb-health-bad-pct': '0',
                                          'fb-health-good-pct': '50',
                                          'fb-health-msg-per-burst': '0',
                                          'fb-health-msg-timeout': '200',
                                          'heartbeat-address': '239.1.99.222',
                                          'heartbeat-interval': '150',
                                          'heartbeat-mode': 'multicast',
                                          'heartbeat-port': '9948',
                                          'heartbeat-protocol': 'v2',
                                          'heartbeat-timeout': '10',
                                          'info-threads': '16',
                                          'ldt-benchmarks': 'false',
                                          'max-msgs-per-type': '-1',
                                          'memory-accounting': 'false',
                                          'microbenchmarks': 'false',
                                          'migrate-max-num-incoming': '256',
                                          'migrate-read-priority': '10',
                                          'migrate-read-sleep': '500',
                                          'migrate-rx-lifetime-ms': '60000',
                                          'migrate-threads': '1',
                                          'migrate-xmit-hwm': '10',
                                          'migrate-xmit-lwm': '5',
                                          'migrate-xmit-priority': '40',
                                          'migrate-xmit-sleep': '500',
                                          'nsup-delete-sleep': '100',
                                          'nsup-period': '120',
                                          'nsup-startup-evict': 'true',
                                          'paxos-max-cluster-size': '32',
                                          'paxos-protocol': 'v3',
                                          'paxos-recovery-policy': 'manual',
                                          'paxos-retransmit-period': '5',
                                          'paxos-single-replica-limit': '1',
                                          'pidfile': '/var/run/aerospike/asd.pid',
                                          'prole-extra-ttl': '0',
                                          'proto-fd-idle-ms': '60000',
                                          'proto-fd-max': '15',
                                          'proto-slow-netio-sleep-ms': '1',
                                          'query-batch-size': '100',
                                          'query-bufpool-size': '256',
                                          'query-in-transaction-thread': '0',
                                          'query-job-tracking': 'false',
                                          'query-long-q-max-size': '500',
                                          'query-priority': '10',
                                          'query-rec-count-bound': '4294967295',
                                          'query-req-in-query-thread': '0',
                                          'query-req-max-inflight': '100',
                                          'query-short-q-max-size': '500',
                                          'query-sleep': '1',
                                          'query-threads': '6',
                                          'query-threshold': '10',
                                          'query-untracked-time': '1000000',
                                          'query-worker-threads': '15',
                                          'replication-fire-and-forget': 'false',
                                          'respond-client-on-master-completion': 'false',
                                          'scan-priority': '200',
                                          'scan-sleep': '1',
                                          'service-threads': '4',
                                          'sindex-data-max-memory': '18446744073709551615',
                                          'sindex-populator-scan-priority': '3',
                                          'snub-nodes': 'false',
                                          'storage-benchmarks': 'false',
                                          'ticker-interval': '10',
                                          'transaction-duplicate-threads': '0',
                                          'transaction-max-ms': '1000',
                                          'transaction-pending-limit': '20',
                                          'transaction-queues': '4',
                                          'transaction-repeatable-read': 'false',
                                          'transaction-retry-ms': '1000',
                                          'transaction-threads-per-queue': '4',
                                          'udf-runtime-gmax-memory': '18446744073709551615',
                                          'udf-runtime-max-memory': '18446744073709551615',
                                          'use-queue-per-device': 'false',
                                          'write-duplicate-resolution-disable': 'false'},
                     '172.17.42.1:3000': {'allow-inline-transactions': 'true',
                                          'auto-dun': 'false',
                                          'auto-undun': 'false',
                                          'batch-max-requests': '5000',
                                          'batch-priority': '200',
                                          'batch-threads': '4',
                                          'dump-message-above-size': '134217728',
                                          'fabric-workers': '16',
                                          'fb-health-bad-pct': '0',
                                          'fb-health-good-pct': '50',
                                          'fb-health-msg-per-burst': '0',
                                          'fb-health-msg-timeout': '200',
                                          'heartbeat-address': '239.1.99.222',
                                          'heartbeat-interval': '150',
                                          'heartbeat-mode': 'multicast',
                                          'heartbeat-port': '9948',
                                          'heartbeat-protocol': 'v2',
                                          'heartbeat-timeout': '10',
                                          'info-threads': '16',
                                          'ldt-benchmarks': 'false',
                                          'max-msgs-per-type': '-1',
                                          'memory-accounting': 'false',
                                          'microbenchmarks': 'false',
                                          'migrate-max-num-incoming': '256',
                                          'migrate-read-priority': '10',
                                          'migrate-read-sleep': '500',
                                          'migrate-rx-lifetime-ms': '60000',
                                          'migrate-threads': '1',
                                          'migrate-xmit-hwm': '10',
                                          'migrate-xmit-lwm': '5',
                                          'migrate-xmit-priority': '40',
                                          'migrate-xmit-sleep': '500',
                                          'nsup-delete-sleep': '100',
                                          'nsup-period': '120',
                                          'nsup-startup-evict': 'true',
                                          'paxos-max-cluster-size': '32',
                                          'paxos-protocol': 'v3',
                                          'paxos-recovery-policy': 'manual',
                                          'paxos-retransmit-period': '5',
                                          'paxos-single-replica-limit': '1',
                                          'pidfile': '/var/run/aerospike/asd.pid',
                                          'prole-extra-ttl': '0',
                                          'proto-fd-idle-ms': '60000',
                                          'proto-fd-max': '15000',
                                          'proto-slow-netio-sleep-ms': '1',
                                          'query-batch-size': '100',
                                          'query-bufpool-size': '256',
                                          'query-in-transaction-thread': '0',
                                          'query-job-tracking': 'false',
                                          'query-long-q-max-size': '500',
                                          'query-priority': '10',
                                          'query-rec-count-bound': '4294967295',
                                          'query-req-in-query-thread': '0',
                                          'query-req-max-inflight': '100',
                                          'query-short-q-max-size': '500',
                                          'query-sleep': '1',
                                          'query-threads': '6',
                                          'query-threshold': '10',
                                          'query-untracked-time': '1000000',
                                          'query-worker-threads': '15',
                                          'replication-fire-and-forget': 'false',
                                          'respond-client-on-master-completion': 'false',
                                          'scan-priority': '200',
                                          'scan-sleep': '1',
                                          'service-threads': '4',
                                          'sindex-data-max-memory': '18446744073709551615',
                                          'sindex-populator-scan-priority': '3',
                                          'snub-nodes': 'false',
                                          'storage-benchmarks': 'false',
                                          'ticker-interval': '10',
                                          'transaction-duplicate-threads': '0',
                                          'transaction-max-ms': '1000',
                                          'transaction-pending-limit': '20',
                                          'transaction-queues': '4',
                                          'transaction-repeatable-read': 'false',
                                          'transaction-retry-ms': '1000',
                                          'transaction-threads-per-queue': '4',
                                          'udf-runtime-gmax-memory': '18446744073709551615',
                                          'udf-runtime-max-memory': '18446744073709551615',
                                          'use-queue-per-device': 'false',
                                          'write-duplicate-resolution-disable': 'false'}}


network_config2={'10.71.71.159:3000': {'network.heartbeat': {'heartbeat-address': '239.1.99.222',
                                                             'heartbeat-interval': '151',
                                                             'heartbeat-mode': 'multicast',
                                                             'heartbeat-port': '9948',
                                                             'heartbeat-protocol': 'v2',
                                                             'heartbeat-timeout': '10'}},
                 '10.71.71.169:3000': {'network.heartbeat': {'heartbeat-address': '239.1.99.222',
                                                             'heartbeat-interval': '150',
                                                             'heartbeat-mode': 'multicast',
                                                             'heartbeat-port': '9948',
                                                             'heartbeat-protocol': 'v2',
                                                             'heartbeat-timeout': '10'}},
                 '10.71.71.179:3000': {'network.heartbeat': {'heartbeat-address': '239.1.99.222',
                                                             'heartbeat-interval': '150',
                                                             'heartbeat-mode': 'multicast',
                                                             'heartbeat-port': '9948',
                                                             'heartbeat-protocol': 'v2',
                                                             'heartbeat-timeout': '11'}}}


class ShowHealthController():
    HEARTBEAT_INTERVAL = 'heartbeat-interval'
    HEARTBEAT_TIMEOUT = 'heartbeat-timeout'
    PROTO_FD_MAX = 'proto-fd-max'
    
    NETWORK_PARAMS = {
                      HEARTBEAT_INTERVAL : 'OK',
                      HEARTBEAT_TIMEOUT : 'OK',
                      PROTO_FD_MAX : 'OK'
                     }

    def get_network_health(self, network_config = ''):
        network_health = dict()
        is_first = True
        for ip, params in network_config.items():
            if params:
                network_health[ip] = dict()
                health_params = copy.deepcopy(ShowHealthController.NETWORK_PARAMS)
                if is_first:
                   heartbeat_interval = params.get(ShowHealthController.HEARTBEAT_INTERVAL)
                   heartbeat_timeout =  params.get(ShowHealthController.HEARTBEAT_TIMEOUT)
                   proto_fd_max = params.get(ShowHealthController.PROTO_FD_MAX)
                   is_first = False
                def update_health(param, comparator, result):
                    if params.get(param) != comparator:
                        health_params[param] = result
                update_health(ShowHealthController.HEARTBEAT_INTERVAL, heartbeat_interval, 'CRITICAL')
                update_health(ShowHealthController.HEARTBEAT_TIMEOUT, heartbeat_timeout, 'CRITICAL')
                update_health(ShowHealthController.PROTO_FD_MAX, proto_fd_max, 'CRITICAL')
                network_health[ip] = health_params
        return network_health


if __name__ == '__main__':
    shc = ShowHealthController()
    print shc.get_network_health(network_config1)
    
    
    