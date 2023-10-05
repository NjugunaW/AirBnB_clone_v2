#!/usr/bin/python3
# A Fabric script that generates a .tgz archive from the contents of the web_static

import os.path
from datetime import datetime
#!/usr/bin/python3
# A Fabric script that generates a .tgz archive from the contents of the web_static

import os.path
from datetime import datetime
from fabric.api import local, env

env.user = 'ubuntu'
env.hosts = ['34.224.2.52', '54.173.45.189']


def do_pack():
    """
    script that generates a .tgz archive from the contents of the web_static
    Returns:

    """
    pres_mmt = datetime.now().strftime("%Y%m%d%H%M%S")
    file = "versions/web_static_{}.tgz".format(pres_mmt)
    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local("tar -cvzf {} web_static".format(file)).failed is True:
        return None
    return file
