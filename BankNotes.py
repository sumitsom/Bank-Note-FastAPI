# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 02:02:47 2021

@author: Sumit
"""
from pydantic import BaseModel
# 2. Class which describes Bank Notes measurements
class BankNote(BaseModel):
    variance: float 
    skewness: float 
    curtosis: float 
    entropy: float