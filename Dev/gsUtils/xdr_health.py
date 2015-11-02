'''    
Created on 19-Oct-2015

@author: pavan
'''
import copy

xdr_config1 = {  '10.71.71.159:3000': {},
                 '10.71.71.169:3000': {},
                 '10.71.71.179:3000': {'cur_throughput': '0',
                                       'err_ship_client': '0',
                                       'err_ship_conflicts': '0',
                                       'err_ship_server': '0',
                                       'esmt-bytes-shipped': '0',
                                       'esmt-bytes-shipped-compression': '0',
                                       'esmt-ship-compression': '0.00%',
                                       'free-dlog-pct': '100%',
                                       'latency_avg_dlogread': '0',
                                       'latency_avg_dlogwrite': '0',
                                       'latency_avg_ship': '0',
                                       'local_recs_fetch_avg_latency': '0',
                                       'local_recs_fetched': '0',
                                       'local_recs_migration_retry': '0',
                                       'local_recs_notfound': '0',
                                       'noship_recs_dup_intrabatch': '0',
                                       'noship_recs_expired': '0',
                                       'noship_recs_genmismatch': '0',
                                       'noship_recs_notmaster': '0',
                                       'noship_recs_unknown_namespace': '0',
                                       'perdc_timediff_lastship_cur_secs': '0',
                                       'stat_dlog_fread': '0',
                                       'stat_dlog_fseek': '0',
                                       'stat_dlog_fwrite': '0',
                                       'stat_dlog_read': '0',
                                       'stat_dlog_write': '0',
                                       'stat_pipe_reads_diginfo': '0',
                                       'stat_recs_dropped': '0',
                                       'stat_recs_localprocessed': '0',
                                       'stat_recs_logged': '0',
                                       'stat_recs_outstanding': '0',
                                       'stat_recs_relogged': '0',
                                       'stat_recs_replprocessed': '0',
                                       'stat_recs_shipped': '0',
                                       'stat_recs_shipping': '0',
                                       'timediff_lastship_cur_secs': '0',
                                       'total-recs-dlog': '1249375300',
                                       'used-recs-dlog': '0',
                                       'xdr-uptime': '945865',
                                       'xdr_deletes_canceled': '0',
                                       'xdr_deletes_relogged': '0',
                                       'xdr_deletes_shipped': '0'}}


class ShowHealthController():
    FREE_DLOG_PCT = 'free-dlog-pct'
    STAT_RECS_RELOGGED = 'stat_recs_relogged'
    TIMEDIFF_LASTSHIP_CUR_SECS = 'timediff_lastship_cur_secs'
    

    XDR_PARAMS = {
                      FREE_DLOG_PCT : 'OK',
#                       HEARTBEAT_TIMEOUT : 'OK',
#                       PROTO_FD_MAX : 'OK'
                 }

    def get_xdr_health(self, xdr_config = ''):
        xdr_health = {}
        for ip, params in xdr_config.items():
            if params:
                xdr_health[ip] = {}
                health_params = copy.deepcopy(ShowHealthController.XDR_PARAMS)
                
                def update_health(param, comparator, result):
                    if params.get(param) != comparator:
                        health_params[param] = result
                
                update_health(ShowHealthController.HEARTBEAT_INTERVAL, heartbeat_interval, 'CRITICAL')
        pass
    
#         network_health = dict()
#         is_first = True
#         for ip, params in network_config.items():
#             if params:
#                 network_health[ip] = dict()
#                 health_params = copy.deepcopy(ShowHealthController.NETWORK_PARAMS)
#                 if is_first:
#                    heartbeat_interval = params.get(ShowHealthController.HEARTBEAT_INTERVAL)
#                    heartbeat_timeout =  params.get(ShowHealthController.HEARTBEAT_TIMEOUT)
#                    proto_fd_max = params.get(ShowHealthController.PROTO_FD_MAX)
#                    is_first = False
#                 def update_health(param, comparator, result):
#                     if params.get(param) != comparator:
#                         health_params[param] = result
#                 update_health(ShowHealthController.HEARTBEAT_INTERVAL, heartbeat_interval, 'CRITICAL')
#                 update_health(ShowHealthController.HEARTBEAT_TIMEOUT, heartbeat_timeout, 'CRITICAL')
#                 update_health(ShowHealthController.PROTO_FD_MAX, proto_fd_max, 'CRITICAL')
#                 network_health[ip] = health_params
#         return network_health


if __name__ == '__main__':
    shc = ShowHealthController()
    print shc.get_network_health(network_config1)
    
    
    