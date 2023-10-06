#!/usr/bin/python3
# A Fabric script that deletes out-of-date archives, using the function do_clean 
import os
from fabric.api import env, local, put, run

env.user = 'ubuntu'
env.hosts = ["34.224.2.52", "54.173.45.189"]


def do_pack():
    """
    This function generates an archive from the web static content
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


def do_deploy(archive_path):
    """
    This function distributes archive to servers
    Args:
        archive_path:

    Returns:

    """
    try:
        archive = archive_path.split('/')[-1]
        path = '/data/web_static/releases/' + archive.strip('.tgz')
        current = '/data/web_static/current'
        put(archive_path, '/tmp')
        run('mkdir -p {}/'.format(path))
        run('tar -xzf /tmp/{} -C {}'.format(archive, path))
        run('rm /tmp/{}'.format(archive))
        run('mv {}/web_static/* {}'.format(path, path))
        run('rm -rf {}/web_static'.format(path))
        run('rm -rf {}'.format(current))
        run('ln -s {} {}'.format(path, current))
        print('New version deployed!')
        return True
    except FileNotFoundError:
        return False


def deploy():
    """
    This function creates and distributes archive
    Returns:

    """
    archive_path = do_pack()
    answer = do_deploy(archive_path)
    return answer


def do_clean(number=0):
    """
    This function deletes out-of-date archives
    Args:
        number:

    Returns:

    """
    if number == 0 or number == 1:
        with lcd('./versions/'):
            local("ls -lv | rev | cut -f 1 | rev | \
                head -n +1 | xargs -d '\n' rm -rf")
        with cd('/data/web_static/releases/'):
            run("sudo ls -lv | rev | cut -f 1 | \
                rev | head -n +1 | xargs -d '\n' rm -rf")
    else:
        with lcd('./versions/'):
            local("ls -lv | rev | cut -f 1 | rev | \
                head -n +{} | xargs -d '\n' rm -rf".format(number))
        with cd('/data/web_static/releases/'):
            run("sudo ls -lv | rev | cut -f 1 | \
                rev | head -n +{} | xargs -d '\n' rm -rf".format(number))
