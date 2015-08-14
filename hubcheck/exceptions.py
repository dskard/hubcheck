# hubcheck python exceptions

class HCException(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)

class LocatorException(HCException):
    pass

class NoSuchFileAttachmentError(HCException):
    pass

class NoSuchMemberException(HCException):
    pass

class NoSuchTagException(HCException):
    pass

class NoSuchUserException(HCException):
    pass

class TimeoutException(HCException):
    pass

class ProxyPortError(HCException):
    pass

class ConnectionClosedError(HCException):
    """
    Raise this exception if the connection closed unexpectedly
    """
    pass

class ExitCodeError(HCException):
    """
    Raise this exception if the exit code of running a command is not 0
    """
    pass


class NavigationError(HCException):
    """
    Raise this exception if there was trouble navigating the web browser.
    """
    pass


class FormSubmissionError(HCException):
    """
    Raise this exception if there was trouble submitting a web form.
    """
    pass


class CatalogError(HCException):
    """
    Raise this exception if there was trouble using the page object catalog.
    """
    pass


class SessionCreateError(HCException):
    """
    Raise this exception if there was trouble creating a tool session container.
    """
    pass


