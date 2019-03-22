#
#  Copyright 2019 The FATE Authors. All Rights Reserved.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#
# -*- coding: utf-8 -*-

import ujson
import time
from arch.api.utils import snowflake


def get_fate_uuid():
    return snowflake.get_id()


def get_scene_key(scene_id, my_party_id, partner_party_id, my_role):
    local = locals()
    return '_'.join([str(local[arg]) for arg in get_scene_key.__code__.co_varnames if arg in local])


def get_commit_id():
    # the model may be larger, SHA1 is not used
    return get_fate_uuid()


def string_bytes(string, check=False):
    if check:
        return string if isinstance(string, bytes) else string.encode(encoding="utf-8")
    else:
        return string.encode(encoding="utf-8")


def bytes_string(byte):
    return byte.decode(encoding="utf-8")


def json_dumps(src, byte=False):
    if byte:
        return string_bytes(ujson.dumps(src))
    else:
        return ujson.dumps(src)


def json_loads(src):
    if isinstance(src, bytes):
        return ujson.loads(bytes_string(src))
    else:
        return ujson.loads(src)


def current_timestamp():
    return int(time.time()*1000)