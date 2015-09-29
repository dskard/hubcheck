import os
from pkg_resources import resource_filename

class Config(object):

    data_dir = resource_filename('hubcheck','data')
    profiles_dir = resource_filename('hubcheck','profiles')


    # user configuration variables
    screenshot_dir = None
    video_dir = None
    config_filename = None
    tdfname = ''
    tdpass = ''

    highlight_web_elements = False
    scroll_to_web_elements = False
    log_locator_updates = False
    log_widget_attachments = False

    proxy = None

    hub_hostname = None
    hub_version = None
    tool_container_version = None
    default_workspace_toolname = None
    apps_workspace_toolname = None

    # full path of the hub config file, used by toolcheck
    configpath = None

settings = Config()
