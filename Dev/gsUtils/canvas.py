actual_header = "Percentage of records having ttl less than or equal to value measured in Seconds Node       10%       20%       30%       40%       50%       60%       70%       80%       90%      100%"
actual_header = ' '.join([item for item in actual_header.split()
                                  if not item.startswith('\x1b')])
print "Node" in actual_header