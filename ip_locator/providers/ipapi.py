"""
使用ip-api.com的IP地址查询提供商
"""
import json
from typing import Dict, Any
import urllib.request

from .base import BaseProvider


class IPAPIProvider(BaseProvider):
    """使用ip-api.com的IP地址查询提供商"""
    
    def __init__(self, timeout: int = 5):
        """
        初始化ip-api.com提供商
        
        Args:
            timeout: 请求超时时间（秒）
        """
        self.base_url = "http://ip-api.com/json/{ip}?fields=status,message,country,regionName,city,lat,lon,isp,org,as,query"
        self.timeout = timeout
    
    def locate(self, ip_address: str) -> Dict[str, Any]:
        """
        通过ip-api.com查询IP地址的地理位置信息
        
        Args:
            ip_address: IP地址
            
        Returns:
            包含地理位置信息的字典
            
        Raises:
            RuntimeError: 如果查询失败
        """
        url = self.base_url.format(ip=ip_address)
        
        try:
            with urllib.request.urlopen(url, timeout=self.timeout) as response:
                data = json.loads(response.read().decode())
                
                if data.get("status") == "success":
                    return {
                        "ip": data.get("query"),
                        "country": data.get("country"),
                        "region": data.get("regionName"),
                        "city": data.get("city"),
                        "latitude": data.get("lat"),
                        "longitude": data.get("lon"),
                        "isp": data.get("isp"),
                        "organization": data.get("org"),
                        "asn": data.get("as"),
                        "provider": "ip-api.com"
                    }
                else:
                    raise RuntimeError(f"IP-API查询失败: {data.get('message', '未知错误')}")
        except Exception as e:
            raise RuntimeError(f"IP-API查询过程中出错: {str(e)}") 