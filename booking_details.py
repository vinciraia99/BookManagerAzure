# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.


class BookingDetails:
    def __init__(
            self,
            titleorisbn: str = None,
            index: str = None,
            unsupported_airports=None,
    ):
        if unsupported_airports is None:
            unsupported_airports = []
        self.titleorisbn = titleorisbn
        self.index = index
