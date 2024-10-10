from pydantic import BaseModel
from datetime import date, time
from typing import List
from .signal import SignalScheme


class RecordingScheme(BaseModel):
    """
    Схема полученных измерений
    """
    date: date = None
    time: time = None
    lower_frequency: int
    upper_frequency: int
    bin_width: float
    count_selection: int
    signals: List[SignalScheme] = []

    class Config:
        from_attributes = True
