
class NoStandardsError(ValueError):
    """Exception raised when a quantity needs to be standardized but there are no standards
    declared.

    This exception is raised when a quantity needs to be standardized but the conversion can not be
    executed. There is at least a unit involved without standard declared.

    Raises
    ------
    NoStandardError
        A message is printed out with the name of the class or the method raising the exception,
        the possible wrong argument, the link to the API documentation, and the link to the
        issues board of PyUnitWizard's GitHub repository.

    Examples
    --------
    >>> import pyunitwizard as puw
    >>> puw.configure.set_standard_units(['nm', 'ps', 'kJ'])
    >>> standard = get_standard_units('10 litres')
    >>> if standard is None:
    ...    raise NoStandardError()

    .. admonition:: See Also
       :class: attention

        :ref:`Developer Guide \> Exceptions \> BadCallError <developer:exceptions:NoStandardError>`

    """

    def __init__(self):

        from pyunitwizard import __github_issues_web__
        from inspect import stack

        all_stack_frames = stack()
        caller_stack_frame = all_stack_frames[1]
        caller_name = caller_stack_frame[3]

        api_doc = ''

        message = (f"The input quantity method has no standard. "
                   f"A complete set of standard units need to be defined. "
                   f"Check {api_doc} for more information. "
                   f"If you still need help, open a new issue in {__github_issues_web__}."
                   )
        super().__init__(message)


class UnknownFormError(ValueError):
    """Exception raised when the input quantity or unit has an unknown form and thereby not supported.

    This exception is raised when PyUnitWizard does not recognize a quantity or unit as a supported form.

    Note
    ----
    This exception does not require input arguments.

    Raises
    ------
    UnknownFormError
        A message is printed out with the name of the class or the method raising the exception,
        the link to the API documentation with the list of supported forms, and the link to the
        issues board of PyUnitWizard's GitHub repository.

    Examples
    --------
    >>> from pyunitwizard._private.exceptions import UnknownFormError
    >>> from pyunitwizard import get_form
    >>> try:
    ...    _ = get_form(item)
    ... except:
    ...    raise UnknownFormError

    .. admonition:: See Also
       :class: attention

        :ref:`Developer Guide \> Exceptions \> UnknownFormError <developer:exceptions:UnknownFormError>`

    """

    def __init__(self):

        from sabueso import __github_issues_web__
        from inspect import stack

        all_stack_frames = stack()
        caller_stack_frame = all_stack_frames[1]
        caller_name = caller_stack_frame[3]

        api_doc = ''

        message = (
                f"The input quantity in \"{method_name}\" has an unknown form. "
                f"Check {api_doc} for more information. "
                f"If you still need help, open a new issue in {__github_issues_web__}."
                )

        super().__init__(message)


class LibraryNotFoundError(NotImplementedError):
    """Exception raised when a library required by the user is not found.

    Some libraries are not considered as dependencies by PyUnitWizard. These libraries are required if
    the user choose to work with a specific quantities' package. In this case, the user hat to
    install it previousy. It that's not the case, the method will raise this exceptions suggesting
    the manual installation.

    Parameters
    ----------
    argument : str
        The name of the not found library.

    Raises
    ------
    LibraryNotFoundError
        A message is printed out with the name of the class or the method raising the exception,
        the name of the not found library, the link to the API documentation, and the link to the
        issues board of PytUnitWizard's GitHub repository.

    Examples
    --------
    >>> from pyunitwizard._private.exceptions import LibraryNotFoundError
    >>> def method_name(item, argument='pint'):
    ...    if argument == 'pint':
    ...       try:
    ...          import pint
    ...       except:
    ...          raise LibraryNotFoundError('pint')
    ...    pass

    .. admonition:: See Also
       :class: attention

        :ref:`Developer Guide \> Exceptions \> LibraryNotFoundError <developer:exceptions:LibraryNotFoundError>`

    """

    def __init__(self, library):

        from pyunitwizard import __github_issues_web__
        from inspect import stack

        all_stack_frames = stack()
        caller_stack_frame = all_stack_frames[1]
        caller_name = caller_stack_frame[3]

        api_doc = ''

        message = (
                f"The python library {library} was not found. "
                f"Although {library} is not considered a dependency, it needs "
                f"to be installed to execute the {caller_name} method the way you require. "
                f"If you still need help, open a new issue in {__github_issues_web__}."
                )

        super().__init__(message)

class LibraryWithoutParserError(NotImplementedError):
    """Exception raised when a library can not parse strings.

    Some libraries cannot convert strings to quantities. This error will be raised by the API methods
    `string_to_quantity` and `string_to_unit` of those libraries without strings' parser.

    Parameters
    ----------
    argument : str
        The name of the library without parser.

    Raises
    ------
    LibraryWithoutParserError
        A message is printed out with the name of the library wihtout parser, the link to the
        section in the documentation regarding parser regarding parsers, and the link to the
        issues board of PytUnitWizard's GitHub repository.

    Examples
    --------
    >>> import pyunitwizard as puw
    >>> from pyunitwizard._private.exceptions import LibraryWithoutParserError
    >>> from pyunitwizard._private.exceptions import LibraryWithoutParserError
    >>> def method_name(item, argument='pint'):
    ...    if argument == 'pint':
    ...       try:
    ...          import pint
    ...       except:
    ...          raise LibraryNotFoundError('pint')
    ...    pass

    .. admonition:: See Also
       :class: attention

        :ref:`Developer Guide \> Exceptions \> LibraryWithoutStringsParserError <developer:exceptions:LibraryWithoutStringsParserError>`

    """

    def __init__(self, library):

        from pyunitwizard import __github_issues_web__
        from inspect import stack

        all_stack_frames = stack()
        caller_stack_frame = all_stack_frames[1]
        caller_name = caller_stack_frame[3]

        api_doc = ''

        message = (
                f"The python library {library} was not found. "
                f"Although {library} is not considered a dependency, it needs "
                f"to be installed to execute the {caller_name} method the way you require. "
                f"If you still need help, open a new issue in {__github_issues_web__}."
                )

        super().__init__(message)


