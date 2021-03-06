# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://support.direct.ingenico.com/documentation/api/reference/
#
from ingenico.direct.sdk.data_object import DataObject


class ThreeDSecureData(DataObject):
    """
    | Object containing data regarding the customer authentication that occurred prior to the current transaction
    """

    __acs_transaction_id = None
    __method = None
    __utc_timestamp = None

    @property
    def acs_transaction_id(self):
        """
        | The ACS Transaction ID for a prior 3-D Secure authenticated transaction (for example, the first recurring transaction that was authenticated with the customer)

        Type: str
        """
        return self.__acs_transaction_id

    @acs_transaction_id.setter
    def acs_transaction_id(self, value):
        self.__acs_transaction_id = value

    @property
    def method(self):
        """
        | Authentication used by the customer on your website
        | Possible values are
        |  * guest = no login occurred, customer is logged in as guest
        |  * merchant-credentials = the customer logged in using credentials that are specific to you
        |  * federated-id = the customer logged in using a federated ID
        |  * issuer-credentials = the customer logged in using credentials from the card issuer (of the card used in this transaction)
        |  * third-party-authentication = the customer logged in using third-party authentication
        |  * fido-authentication = the customer logged in using a FIDO authenticator

        Type: str
        """
        return self.__method

    @method.setter
    def method(self, value):
        self.__method = value

    @property
    def utc_timestamp(self):
        """
        | Timestamp in UTC (YYYYMMDDHHmm) of the 3-D Secure authentication of this transaction

        Type: str
        """
        return self.__utc_timestamp

    @utc_timestamp.setter
    def utc_timestamp(self, value):
        self.__utc_timestamp = value

    def to_dictionary(self):
        dictionary = super(ThreeDSecureData, self).to_dictionary()
        if self.acs_transaction_id is not None:
            dictionary['acsTransactionId'] = self.acs_transaction_id
        if self.method is not None:
            dictionary['method'] = self.method
        if self.utc_timestamp is not None:
            dictionary['utcTimestamp'] = self.utc_timestamp
        return dictionary

    def from_dictionary(self, dictionary):
        super(ThreeDSecureData, self).from_dictionary(dictionary)
        if 'acsTransactionId' in dictionary:
            self.acs_transaction_id = dictionary['acsTransactionId']
        if 'method' in dictionary:
            self.method = dictionary['method']
        if 'utcTimestamp' in dictionary:
            self.utc_timestamp = dictionary['utcTimestamp']
        return self
