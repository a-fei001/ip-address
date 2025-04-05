"""
使用MaxMind GeoIP2数据库的IP地址查询提供商
"""
from typing import Dict, Any, Optional

from .base import BaseProvider


class MaxMindProvider(BaseProvider):
    """使用MaxMind GeoIP2数据库的IP地址查询提供商"""
    
    def __init__(self, db_path: str):
        """
        初始化MaxMind GeoIP2提供商
        
        Args:
            db_path: MaxMind GeoIP2数据库文件路径
        """
        self.db_path = db_path
        self._reader = None
    
    @property
    def reader(self):
        """懒加载MaxMind GeoIP2数据库读取器"""
        if self._reader is None:
            try:
                import geoip2.database
                self._reader = geoip2.database.Reader(self.db_path)
            except ImportError:
                raise ImportError("请安装geoip2库: pip install geoip2")
        return self._reader
    
    def locate(self, ip_address: str) -> Dict[str, Any]:
        """
        通过MaxMind GeoIP2数据库查询IP地址的地理位置信息
        
        Args:
            ip_address: IP地址
            
        Returns:
            包含地理位置信息的字典
            
        Raises:
            RuntimeError: 如果查询失败
        """
        try:
            response = self.reader.city(ip_address)
            
            return {
                "ip": ip_address,
                "country": response.country.name,
                "country_code": response.country.iso_code,
                "region": response.subdivisions.most_specific.name if response.subdivisions else None,
                "region_code": response.subdivisions.most_specific.iso_code if response.subdivisions else None,
                "city": response.city.name,
                "postal_code": response.postal.code,
                "latitude": response.location.latitude,
                "longitude": response.location.longitude,
                "provider": "MaxMind GeoIP2"
            }
        except Exception as e:
            raise RuntimeError(f"MaxMind查询失败: {str(e)}") 