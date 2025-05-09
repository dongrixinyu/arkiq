# Copyright (c) 2025 Bytedance Ltd. and/or its affiliates
# Licensed under the 【火山方舟】原型应用软件自用许可协议
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#     https://www.volcengine.com/docs/82379/1433703
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os

"""
for server
"""

# recommend to use DeepSeek-R1 model
LLM_BROWSING_MODEL_NAME = os.getenv('LLM_BROWSING_MODEL_NAME') or ""
LLM_BROWSING_MODEL_ENDPOINT_ID = os.getenv('LLM_BROWSING_MODEL_ENDPOINT_ID') or ""

VLM_MODEL_NAME = os.getenv('VLM_MODEL_NAME') or ""
VLM_MODEL_ENDPOINT_ID = os.getenv('VLM_MODEL_ENDPOINT_ID') or ""

LLM_MODEL_NAME = os.getenv('LLM_MODEL_NAME') or ""
LLM_MODEL_ENDPOINT_ID = os.getenv('LLM_MODEL_ENDPOINT_ID') or ""

# default set to volc bot, if using tavily, change it into "tavily"
SEARCH_ENGINE = os.getenv('SEARCH_ENGINE') or "volc_bot"
# optional, if you select tavily as search engine, please configure this
# TAVILY_API_KEY = os.getenv('TAVILY_API_KEY') or "{YOUR_TAVILY_API_KEY}"
# optional, if you select volc bot as search engine, please configure this
SEARCH_BOT_ID = os.getenv('SEARCH_BOT_ID') or "{YOUR_SEARCH_BOT_ID}"

"""
for webui
"""

# ark api key
ARK_API_KEY = os.getenv('ARK_API_KEY') or "{YOUR_ARK_API_KEY}"
# api server address for web ui

ARK_SERVER_IP = os.getenv('ARK_SERVER_IP')
ARK_SERVER_PORT = int(os.getenv('ARK_SERVER_PORT'))
ARK_API_ADDR = f"http://{ARK_SERVER_IP}:{ARK_SERVER_PORT}/api/v1/bots"

WEB_SERVER_IP = os.getenv('WEB_SERVER_IP')
WEB_SERVER_PORT = int(os.getenv('WEB_SERVER_PORT'))

# while using remote api, need bot id
API_BOT_ID = os.getenv("API_BOT_ID") or "{YOUR_API_BOT_ID}"
