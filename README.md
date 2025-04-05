## 快速开始
1. 将代码clone到本地
2. 下库
要使用这个库，你需要安装以下依赖：
```
pip install requests
```
如果你想使用MaxMind本地数据库，还需要：
```
pip install geoip2
```
3. 进入example.py 替换为想查的ip地址

## 说明
这个库支持Python 3.7及以上版本，完全兼容Python 3.12.2
默认使用ip-api.com在线API服务查询，无需额外配置
支持可选的MaxMind本地数据库查询，需要额外安装geoip2库
可以轻松扩展添加更多IP地址查询提供商

## 完善
提供了简单易用的API，可以快速集成到其他项目中
如果需要更加精确的地理位置信息，你可以：
购买商业级IP地址数据库，如MaxMind的GeoIP2 City数据库
添加更多的第三方API提供商，如ipstack、ipinfo等
结合多个提供商的结果，提高地理位置信息的准确性
