# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://support.direct.ingenico.com/documentation/api/reference/
#
from ingenico.direct.sdk.param_request import ParamRequest
from ingenico.direct.sdk.request_param import RequestParam


class GetProductDirectoryParams(ParamRequest):
    """
    Query parameters for Get payment product directory

    See also https://support.direct.ingenico.com/documentation/api/reference#operation/GetProductDirectoryApi
    """

    __country_code = None
    __currency_code = None

    @property
    def country_code(self):
        """
        Type: str
        """
        return self.__country_code

    @country_code.setter
    def country_code(self, value):
        self.__country_code = value

    @property
    def currency_code(self):
        """
        Type: str
        """
        return self.__currency_code

    @currency_code.setter
    def currency_code(self, value):
        self.__currency_code = value

    def to_request_parameters(self):
        """
        :return: list[RequestParam]
        """
        result = []
        if self.country_code is not None:
            result.append(RequestParam("countryCode", self.country_code))
        if self.currency_code is not None:
            result.append(RequestParam("currencyCode", self.currency_code))
        return result
