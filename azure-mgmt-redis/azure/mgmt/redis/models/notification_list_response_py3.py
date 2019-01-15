# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class NotificationListResponse(Model):
    """The response of listUpgradeNotifications.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param value: List of all notifications.
    :type value: list[~azure.mgmt.redis.models.UpgradeNotification]
    :ivar next_link: Link for next set of notifications.
    :vartype next_link: str
    """

    _validation = {
        'next_link': {'readonly': True},
    }

    _attribute_map = {
        'value': {'key': 'value', 'type': '[UpgradeNotification]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(self, *, value=None, **kwargs) -> None:
        super(NotificationListResponse, self).__init__(**kwargs)
        self.value = value
        self.next_link = None
