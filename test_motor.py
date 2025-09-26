import pytest
import asyncio
from motor import getData, get_tw_date
from datetime import datetime


def test_get_tw_date():
    """測試台灣日期格式轉換"""
    tw_date = get_tw_date()
    # 確保返回的是字符串且格式正確（長度為7）
    assert isinstance(tw_date, str)
    assert len(tw_date) == 7
    # 確保是數字
    assert tw_date.isdigit()


@pytest.mark.asyncio
async def test_getData():
    """測試 getData 函數"""
    # 使用有效的參數進行測試
    result, location = await getData(20, 26)

    # 確保返回的是正確的類型
    assert isinstance(result, list)
    assert isinstance(location, str)

    # 如果有結果，檢查格式
    if result:
        for item in result:
            assert isinstance(item, str)
            assert " | 名額：" in item


def test_imports():
    """測試必要的模組是否能正確導入"""
    import requests
    import bs4
    import datetime
    import asyncio

    assert True  # 如果能執行到這裡，表示導入成功
