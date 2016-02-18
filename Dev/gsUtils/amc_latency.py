import datetime as dt
import pprint

result = 'reads:13:44:00-GMT,ops/sec,>1ms,>8ms,>64ms;13:44:10,5172.7,0.83,0.02,0.00;writes_master:13:44:00-GMT,ops/sec,>1ms,>8ms,>64ms;13:44:10,5206.8,8.44,0.13,0.00;proxy:13:44:00-GMT,ops/sec,>1ms,>8ms,>64ms;13:44:10,0.0,0.00,0.00,0.00;writes_reply:13:44:00-GMT,ops/sec,>1ms,>8ms,>64ms;13:44:10,5206.8,8.44,0.13,0.00;udf:13:44:00-GMT,ops/sec,>1ms,>8ms,>64ms;13:44:10,0.0,0.00,0.00,0.00;query:13:44:00-GMT,ops/sec,>1ms,>8ms,>64ms;13:44:10,0.0,0.00,0.00,0.00;'

def text_to_list(text, delimiter=";"):

    if text.strip() == "":
        return []
    return text.split(delimiter)

def time_diffrence_in_sec(time1, time2):

    FMT = '%H:%M:%S'
    tdelta = dt.datetime.strptime(time1, FMT) - dt.datetime.strptime(time2, FMT)
    return tdelta.seconds

def time_average(time1, time2):

    diff = time_diffrence_in_sec(time1, time2)
    FMT = '%H:%M:%S'
    avg_time = dt.datetime.strptime(time2, FMT) + dt.timedelta(0, diff / 2)
    return avg_time.strftime("%H:%M:%S")


def lat(result):
    latency = dict()
    rows = text_to_list(result)
    for i in range(0, len(rows), 2):
        if not rows[i]:
            continue
        ind = rows[i].index(':')
        op = rows[i][:ind]
        if op == "writes_reply":
            continue
        rows[i] = rows[i][ind + 1:]

        keys = text_to_list(rows[i], ",")
        values = text_to_list(rows[i + 1], ",")

        keys[0] = keys[0].split("-")[0]
        ops_per_sec = float(values[1])

        latency[op] = {'timestamp': time_average(values[0], keys[0]),
            'data': [],
            'ops/sec': ops_per_sec
            }

        less_than_1 = 0.0 if ops_per_sec == 0 else 100.0

        previous_key = ""
        previous_value = 0.0
        for key, value in zip(list(reversed(keys))[:len(keys)-2], list(reversed(values))[:len(keys)-2]):
            pct = float(value) - previous_value
            previous_value = float(value)
            original_key = key
            if previous_key != "":
                key = ">" + key[1:] + " to &#x2264;" + previous_key[1:]
            previous_key = original_key
            less_than_1 -= pct
            value = ops_per_sec * pct / 100
            latency[op]['data'] = [{key: dict(value=value, pct=pct)}] + latency[op]['data']

        less_than_1_value = ops_per_sec * less_than_1 / 100
        latency[op]['data'] = [{"&#x2264;1ms": dict(value=less_than_1_value, pct=less_than_1)}] + latency[op]['data']
#     sys.stderr.write("\nLATENCY: %s" % pprint.pformat(latency))
    return latency


if __name__ ==  '__main__':
    print pprint.pformat(lat(result))

    
    
    
    
        
        