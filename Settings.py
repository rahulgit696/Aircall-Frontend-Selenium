import os


def get_root_directory():
    """
    Get the root directory of the project.

    Returns:
        str: Absolute path of the project's root directory.
    """
    return os.path.abspath(os.path.dirname(__file__))


def get_log_file_directory():
    """
    Get the directory for log files.

    Returns:
        str: Absolute path of the log file directory.
    """
    return os.path.join(get_root_directory(), 'logfile.log')


def get_drivers_directory():
    """
    Get the directory for WebDriver executables.

    Returns:
        str: Absolute path of the drivers directory.
    """
    return os.path.join(get_root_directory(), 'AircallTest', 'Resources', 'Drivers')
