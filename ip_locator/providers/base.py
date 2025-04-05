"""
IP地址查询提供商基类
"""
from abc import ABC, abstractmethod
from typing import Dict, Any


class BaseProvider(ABC):
    """IP地址查询提供商基类"""
    
    @abstractmethod
    def locate(self, ip_address: str) -> Dict[str, Any]:
        """
        查询IP地址的地理位置信息
        
        Args:
            ip_address: IP地址
            
        Returns:
            包含地理位置信息的字典
        """
        pass 