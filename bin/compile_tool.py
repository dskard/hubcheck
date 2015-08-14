import argparse
import getpass
import hubcheck
import logging
import logging.config
import os
import sys


def parseoptions():
    usage = "usage: %prog [options]"
    parser = argparse.ArgumentParser(usage=usage)

    parser.add_argument('--hub',
                      help='name of the hub',
                      action="store",
                      dest="hub",
                      type=str)

    parser.add_argument('--toolname',
                      help='name of the tool to compile',
                      action="store",
                      dest="toolname",
                      type=str)

    parser.add_argument('--toolversion',
                      help='version of the tool to compile',
                      action="store",
                      dest="toolversion",
                      default="dev",
                      type=str)

    parser.add_argument('--username',
                      help='login of user in the apps group',
                      action="store",
                      dest="username",
                      type=str)

    parser.add_argument('--loglevel',
                      help='log level',
                      action="store",
                      dest="loglevel",
                      default="INFO",
                      type=str)

    parser.add_argument('--logfile',
                      help='log file',
                      action="store",
                      dest="logfile",
                      default="compile_tool.log",
                      type=str)

    parser.add_argument('remainder', nargs=argparse.REMAINDER)

    options = parser.parse_args()

    return options,options.remainder


def main():

    options,remainder = parseoptions()

    if sys.stdin.isatty():
        password = getpass.getpass('password: ')
    else:
        sys.stdout.write('password: ')
        password = sys.stdin.readline().rstrip()

    # setup a log file
    options.logfile = os.path.abspath(os.path.expanduser(
                        os.path.expandvars(options.logfile)))
    dc = hubcheck.utils.create_dictConfig(options.logfile,options.loglevel)
    logging.config.dictConfig(dc)
    logger = logging.getLogger(__name__)

    logger.info("starting %s" % sys.argv[0])
    logger.info("options: %s" % sys.argv[1:])


    # create a tool session object
    # that holds our connection info.
    session = hubcheck.ToolSession(options.hub,
                                   username=options.username,
                                   password=password)

    # get into a tool session container.
    ws = session.access()

    ws.execute('echo $SESSION')

    # become the apps user
    ws.send('sudo su - apps')
    ws.start_bash_shell()
    output,es = ws.execute('whoami')
    if output != 'apps':
        # doesn't look like we were able to become the apps user
        ws.stop_bash_shell()
        # shut down the ssh connection
        ws.close()

    try:
        # navigate to the tool directory
        cmd = 'cd /apps/%(toolname)s/%(toolversion)s/src' \
                % { 'toolname'      : options.toolname,
                    'toolversion'   : options.toolversion,
                  }
        ws.execute(cmd)

        # if there is a makefile available
        # run:
        # make clean
        # make all
        # make install
        # don't fail if there is no clean target
        if ws.bash_test('-e Makefile'):
            # allow 30 minutes for the code to compile
            ws.timeout = 1800
            output,es = ws.execute('make clean',False)
            output,es = ws.execute('make all',False)
            output,es = ws.execute('make install')
            ws.timeout = 10
        else:
            print "No Makefile found"

    except Exception as detail:
        print detail


    # exit sudo
    ws.stop_bash_shell()
    ws.send('exit')

    # shut down the ssh connection
    ws.close()


if __name__ == '__main__':
    sys.exit(main())

