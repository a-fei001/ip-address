from ip_locator import IPLocator

# 创建IP地址查询器，使用默认提供商（ip-api.com）
locator = IPLocator()

# 查询IP地址的地理位置信息
try:
    location = locator.locate("188.253.112.105")
    print("IP信息:")
    for key, value in location.items():
        print(f"{key}: {value}")
except Exception as e:
    print(f"查询失败: {e}")

# 如果你有MaxMind数据库，可以这样使用
# locator = IPLocator(maxmind_db_path="/path/to/GeoLite2-City.mmdb")
# location = locator.locate("8.8.8.8") 