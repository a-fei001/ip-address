"""
工具函数
"""
import ipaddress
from typing import Union, Optional


def is_valid_ip(ip_address: str) -> bool:
    """
    检查是否为有效的IP地址
    
    Args:
        ip_address: 要检查的IP地址
        
    Returns:
        布尔值，表示IP地址是否有效
    """
    try:
        ipaddress.ip_address(ip_address)
        return True
    except ValueError:
        return False 