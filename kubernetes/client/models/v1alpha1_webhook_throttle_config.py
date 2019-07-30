# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.13.9
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V1alpha1WebhookThrottleConfig(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'burst': 'int',
        'qps': 'int'
    }

    attribute_map = {
        'burst': 'burst',
        'qps': 'qps'
    }

    def __init__(self, burst=None, qps=None):
        """
        V1alpha1WebhookThrottleConfig - a model defined in Swagger
        """

        self._burst = None
        self._qps = None
        self.discriminator = None

        if burst is not None:
          self.burst = burst
        if qps is not None:
          self.qps = qps

    @property
    def burst(self):
        """
        Gets the burst of this V1alpha1WebhookThrottleConfig.
        ThrottleBurst is the maximum number of events sent at the same moment default 15 QPS

        :return: The burst of this V1alpha1WebhookThrottleConfig.
        :rtype: int
        """
        return self._burst

    @burst.setter
    def burst(self, burst):
        """
        Sets the burst of this V1alpha1WebhookThrottleConfig.
        ThrottleBurst is the maximum number of events sent at the same moment default 15 QPS

        :param burst: The burst of this V1alpha1WebhookThrottleConfig.
        :type: int
        """

        self._burst = burst

    @property
    def qps(self):
        """
        Gets the qps of this V1alpha1WebhookThrottleConfig.
        ThrottleQPS maximum number of batches per second default 10 QPS

        :return: The qps of this V1alpha1WebhookThrottleConfig.
        :rtype: int
        """
        return self._qps

    @qps.setter
    def qps(self, qps):
        """
        Sets the qps of this V1alpha1WebhookThrottleConfig.
        ThrottleQPS maximum number of batches per second default 10 QPS

        :param qps: The qps of this V1alpha1WebhookThrottleConfig.
        :type: int
        """

        self._qps = qps

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, V1alpha1WebhookThrottleConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other