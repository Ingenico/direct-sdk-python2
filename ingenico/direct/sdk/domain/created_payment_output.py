# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://support.direct.ingenico.com/documentation/api/reference/
#
from ingenico.direct.sdk.data_object import DataObject
from ingenico.direct.sdk.domain.payment_response import PaymentResponse


class CreatedPaymentOutput(DataObject):
    """
    | When a payment has been created during the hosted checkout session this object will return the details
    """

    __payment = None
    __payment_status_category = None

    @property
    def payment(self):
        """
        | Object that holds the payment related properties

        Type: :class:`ingenico.direct.sdk.domain.payment_response.PaymentResponse`
        """
        return self.__payment

    @payment.setter
    def payment(self, value):
        self.__payment = value

    @property
    def payment_status_category(self):
        """
        Type: str
        """
        return self.__payment_status_category

    @payment_status_category.setter
    def payment_status_category(self, value):
        self.__payment_status_category = value

    def to_dictionary(self):
        dictionary = super(CreatedPaymentOutput, self).to_dictionary()
        if self.payment is not None:
            dictionary['payment'] = self.payment.to_dictionary()
        if self.payment_status_category is not None:
            dictionary['paymentStatusCategory'] = self.payment_status_category
        return dictionary

    def from_dictionary(self, dictionary):
        super(CreatedPaymentOutput, self).from_dictionary(dictionary)
        if 'payment' in dictionary:
            if not isinstance(dictionary['payment'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['payment']))
            value = PaymentResponse()
            self.payment = value.from_dictionary(dictionary['payment'])
        if 'paymentStatusCategory' in dictionary:
            self.payment_status_category = dictionary['paymentStatusCategory']
        return self
