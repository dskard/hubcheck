import errno
import glob
import hubcheck.conf
import logging
import os
import re
import shutil
import smtplib
import socket
import sys

from email.mime.text import MIMEText
from urlparse import urlsplit, urlunsplit, SplitResult


# http://stackoverflow.com/questions/377017/test-if-executable-exists-in-python
def which(program):
    def is_exe(fpath):
        return os.path.exists(fpath) and os.access(fpath, os.X_OK)

    fpath, fname = os.path.split(program)
    if fpath:
        if is_exe(program):
            return program
    else:
        for path in os.environ["PATH"].split(os.pathsep):
            exe_file = os.path.join(path, program)
            if is_exe(exe_file):
                return exe_file

    return None


def get_css_path(browser,e,fullpath=False):
    from selenium.common.exceptions import \
        NoSuchElementException, NoAlertPresentException

    javascript = """
/*
 *  cssPath function originally from
 *  http://stackoverflow.com/questions/4588119/
 *      get-elements-css-selector-without-element-id/4588211#4588211
 */
function hcGetCssPath(el,fullpath) {
    var names = [];
    while (el.parentNode){
        var tagName = el.tagName.toLowerCase();
        if (el.hasAttribute("id")) {
            names.unshift(tagName+'#'+el.getAttribute("id"));
            if (!fullpath) {
                break;
            }
            el=el.parentNode;
        } else {
            var c = 1;
            for (c=1,e=el; e.previousElementSibling;
                    e=e.previousElementSibling,c++);
            names.unshift(tagName+":nth-child("+c+")");
            el=el.parentNode;
        }
    }
    return names.join(" > ");
}
return hcGetCssPath(arguments[0],arguments[1])
"""

    return browser.execute_script(javascript,e,fullpath)

def count_connection_types(connType='TIME_WAIT'):
    # code from:
    # http://voorloopnul.com/blog/a-python-netstat-in-less-than-100-lines-of-code/

    STATE = {
        '01':'ESTABLISHED',
        '02':'SYN_SENT',
        '03':'SYN_RECV',
        '04':'FIN_WAIT1',
        '05':'FIN_WAIT2',
        '06':'TIME_WAIT',
        '07':'CLOSE',
        '08':'CLOSE_WAIT',
        '09':'LAST_ACK',
        '0A':'LISTEN',
        '0B':'CLOSING'
    }

    # read the table of tcp connections & remove header
    with open('/proc/net/tcp','r') as f:
        content = f.readlines()
        content.pop(0)

    counter = 0
    for line in content:
        # split lines and remove empty spaces.
        line_array = [x for x in line.split(' ') if x != '']
        if connType == 'ALL':
            counter += 1
        elif connType == STATE[line_array[3]]:
            counter += 1

    return counter

def href_normalize(href):
    if not href:
        return href
    lu = urlsplit(href)
    href = urlunsplit(SplitResult(lu.scheme,lu.netloc,lu.path,lu.query,''))
    return href

def switch_netloc(new_netloc,url):
    if not url:
        return url
    lu = urlsplit(url)
    url = urlunsplit(SplitResult(lu.scheme,new_netloc,lu.path,lu.query,lu.fragment))
    return url

def create_dictConfig(logfile,loglevel):
    dictLogConfig = {
        "version" : 1,
        "handlers" : {
            "fileHandler" : {
                "class" : "logging.FileHandler",
                "formatter" : "time_msg",
                "filename" : logfile,
            },
            "consoleHandler" : {
                "class" : "logging.StreamHandler",
                "formatter" : "time_msg",
                "stream" : sys.stdout,
            }
        },
        "loggers" : {
            '' : {
                "handlers" : ["fileHandler"],
                "level" : loglevel,
            }
        },
        "formatters" : {
            "time_msg" : {
                "format" : "%(asctime)s: %(message)s"
            },
            "full" : {
                "format" : "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
            }
        }
    }

    return dictLogConfig



def is_port_listening(host,port,protocol='tcp4'):

    port = int(port)

    if protocol == 'tcp4':
        tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcp.settimeout(2)
        r = 1
        try:
            ip = socket.gethostbyname(host)
            r = tcp.connect_ex((ip, port))
        except (socket.timeout, socket.error):
            pass
        tcp.close()
        return  r == 0
    elif protocol == 'udp4':
        udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        udp.settimeout(2)
        r = ''
        try:
            udp.connect((host, port))
            udp.send('Hello!\n')
            r = udp.recv(15)
        except (socket.timeout, socket.error):
            pass
        return len(r) > 0
    else:
        raise RuntimeError('unsupported protocol: %s' % protocol)


def cleanup_temporary_files(files=[],filere=[]):
    logger = logging.getLogger('clean_temporary_files')
    try:
        names = ['/tmp/native_ff_events_log']
        names.extend(files)

        for name in names:
            if os.path.isfile(name):
                logger.info('removing %s' % (name))
                os.remove(name)

        names = []
        names.extend(glob.glob('/tmp/seleniumSslSupport*'))
        names.extend(glob.glob('/tmp/ffconf*'))
        names.extend(filere)
        # names.extend(glob.glob('/tmp/tmp*'))

        for name in names:
            logger.info('removing %s' % (name))
            shutil.rmtree(name,ignore_errors=True)

    except:
        logger.info('error removing tmp files', exc_info=True)


def email_report(smtpserver,fromaddr,tolist,subject,msgtext):
    """
    email an error report.

    smtpserver is the address of the smtp server sending the mail
    fromaddr is the address mail is being sent from
    tolist is a list of email addresses mail will be sent to.
    subject is the subject of the email
    msgtext is the text of the email
    """

    logger = logging.getLogger('email_report')

    if fromaddr is None:
        user = os.environ.get('USER','hcmaster')
        host = socket.gethostbyaddr(socket.gethostname())[0]
        fromaddr = user + '@' + host

    msg = MIMEText(msgtext)
    msg['Subject'] = subject
    msg['From'] = fromaddr
    msg['To'] = ', '.join(tolist)

    logger.debug('sending email: %s' % (msg.as_string()))
    s = smtplib.SMTP(smtpserver)
    s.sendmail(fromaddr,tolist,msg.as_string())
    s.quit()
