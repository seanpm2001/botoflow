# Copyright 2013 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License").
# You may not use this file except in compliance with the License.
# A copy of the License is located at
#
#  http://aws.amazon.com/apache2.0
#
# or in the "license" file accompanying this file. This file is distributed
# on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
# express or implied. See the License for the specific language governing
# permissions and limitations under the License.

class EventBase(object):
    def __init__(self, event_id, timestamp, attributes):
        self.id = event_id
        self.timestamp = float(timestamp)
        self.attributes = attributes

    def __repr__(self):
        return "<%s id=%d, time=%f, attributes=%s>" % (
            self.__class__.__name__, self.id, self.timestamp,
            repr(self.attributes))


class ActivityEventBase(EventBase):
    pass


class ChildWorkflowEventBase(EventBase):
    pass


class DecisionEventBase(EventBase):
    """
    To be used as a mixin with events that represent decisions
    """
    pass


class DecisionTaskEventBase(EventBase):
    pass


class ExternalWorkflowEventBase(EventBase):
    pass


class MarkerEventBase(EventBase):
    pass


class TimerEventBase(EventBase):
    pass


class WorkflowEventBase(EventBase):
    pass
