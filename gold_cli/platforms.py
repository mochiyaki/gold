"""
Shared platform registry for Gold Agent.

Single source of truth for platform metadata consumed by both
skills_config (label display) and tools_config (default toolset
resolution).  Import ``PLATFORMS`` from here instead of maintaining
duplicate dicts in each module.
"""

from collections import OrderedDict
from typing import NamedTuple


class PlatformInfo(NamedTuple):
    """Metadata for a single platform entry."""
    label: str
    default_toolset: str


# Ordered so that TUI menus are deterministic.
PLATFORMS: OrderedDict[str, PlatformInfo] = OrderedDict([
    ("cli",            PlatformInfo(label="🖥️  CLI",            default_toolset="gold-cli")),
    ("telegram",       PlatformInfo(label="📱 Telegram",        default_toolset="gold-telegram")),
    ("discord",        PlatformInfo(label="💬 Discord",         default_toolset="gold-discord")),
    ("slack",          PlatformInfo(label="💼 Slack",           default_toolset="gold-slack")),
    ("whatsapp",       PlatformInfo(label="📱 WhatsApp",        default_toolset="gold-whatsapp")),
    ("signal",         PlatformInfo(label="📡 Signal",          default_toolset="gold-signal")),
    ("bluebubbles",    PlatformInfo(label="💙 BlueBubbles",     default_toolset="gold-bluebubbles")),
    ("email",          PlatformInfo(label="📧 Email",           default_toolset="gold-email")),
    ("homeassistant",  PlatformInfo(label="🏠 Home Assistant",  default_toolset="gold-homeassistant")),
    ("mattermost",     PlatformInfo(label="💬 Mattermost",      default_toolset="gold-mattermost")),
    ("matrix",         PlatformInfo(label="💬 Matrix",          default_toolset="gold-matrix")),
    ("dingtalk",       PlatformInfo(label="💬 DingTalk",        default_toolset="gold-dingtalk")),
    ("feishu",         PlatformInfo(label="🪽 Feishu",          default_toolset="gold-feishu")),
    ("wecom",          PlatformInfo(label="💬 WeCom",           default_toolset="gold-wecom")),
    ("wecom_callback", PlatformInfo(label="💬 WeCom Callback",  default_toolset="gold-wecom-callback")),
    ("weixin",         PlatformInfo(label="💬 Weixin",          default_toolset="gold-weixin")),
    ("qqbot",          PlatformInfo(label="💬 QQBot",           default_toolset="gold-qqbot")),
    ("webhook",        PlatformInfo(label="🔗 Webhook",         default_toolset="gold-webhook")),
    ("api_server",     PlatformInfo(label="🌐 API Server",      default_toolset="gold-api-server")),
])


def platform_label(key: str, default: str = "") -> str:
    """Return the display label for a platform key, or *default*."""
    info = PLATFORMS.get(key)
    return info.label if info is not None else default
