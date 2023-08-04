#!/usr/bin/env python3
'''Task 100's module.
'''
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    '''Retrieving the first element of a sequence if it exists.
    '''
    if lst:
        return lst[0]
    else:
        return None
