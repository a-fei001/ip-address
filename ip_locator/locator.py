"""
IP地址地理位置查询库
"""
import ipaddress
from typing import Dict, Any, Optional, List

from .providers.base import BaseProvider
from .providers.ipapi import IPAPIProvider
from .providers.maxmind import MaxMindProvider
from .utils import is_valid_ip


class IPLocator:
    """IP地址地理位置查询类"""
    
    def __init__(self, providers: Optional[List[BaseProvider]] = None, maxmind_db_path: Optional[str] = None):
        """
        初始化IP地址查询器
        
        Args:
            providers: 提供商列表，如果为None，将使用默认提供商
            maxmind_db_path: MaxMind数据库路径，如果指定，将添加MaxMind本地查询提供商
        """
        self.providers = providers or []
        
        # 如果没有指定提供商，使用默认提供商
        if not self.providers:
            # 默认添加在线API提供商
            self.providers.append(IPAPIProvider())
            
            # 如果指定了MaxMind数据库路径，添加MaxMind提供商
            if maxmind_db_path:
                self.providers.append(MaxMindProvider(maxmind_db_path))
    
    def add_provider(self, provider: BaseProvider) -> None:
        """
        添加IP地址查询提供商
        
        Args:
            provider: IP地址查询提供商
        """
        self.providers.append(provider)
    
    def locate(self, ip_address: str) -> Dict[str, Any]:
        """
        查询IP地址的地理位置信息
        
        Args:
            ip_address: IP地址
            
        Returns:
            包含地理位置信息的字典
        
        Raises:
            ValueError: 如果IP地址无效
            RuntimeError: 如果所有提供商都查询失败
        """
        if not is_valid_ip(ip_address):
            raise ValueError(f"无效的IP地址: {ip_address}")
        
        # 尝试使用所有提供商查询IP地址
        errors = []
        for provider in self.providers:
            try:
                result = provider.locate(ip_address)
                if result:
                    return result
            except Exception as e:
                errors.append(f"{provider.__class__.__name__}: {str(e)}")
        
        # 如果所有提供商都失败，抛出异常
        raise RuntimeError(f"所有提供商查询失败: {', '.join(errors)}") 