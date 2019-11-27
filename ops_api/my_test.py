
#!/usr/bin/env python
import redis
from redis.sentinel import Sentinel

# 连接哨兵服务器(主机名也可以用域名)
sentinel = Sentinel([('adidas-sentinel01-prod.cloud.bz', 26379),
                     ('adidas-sentinel02-prod.cloud.bz', 26379),
                     ('adidas-sentinel03-prod.cloud.bz', 26379)
		     ],
                    socket_timeout=0.5)



# 获取主服务器地址
master = sentinel.discover_master('adidas_hype')
print(master)
# 输出：('172.31.0.2', 5001)


# 获取从服务器地址
slave = sentinel.discover_slaves('adidas_hype')
print(slave)
# 输出：[('172.31.3', 5001), ('172.31.0.4', 5001), ('172.31.0.5', 5001)]
