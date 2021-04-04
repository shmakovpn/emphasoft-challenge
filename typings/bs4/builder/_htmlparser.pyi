"""
This type stub file was generated by pyright.
"""

from html.parser import HTMLParser
from bs4.builder import HTMLTreeBuilder

"""Use the HTMLParser library to parse HTML files that aren't too bad."""
__license__ = ...
CONSTRUCTOR_TAKES_STRICT = ...
CONSTRUCTOR_STRICT_IS_DEPRECATED = ...
CONSTRUCTOR_TAKES_CONVERT_CHARREFS = ...
HTMLPARSER = ...
class BeautifulSoupHTMLParser(HTMLParser):
    """A subclass of the Python standard library's HTMLParser class, which
    listens for HTMLParser events and translates them into calls
    to Beautiful Soup's tree construction API.
    """
    IGNORE = ...
    REPLACE = ...
    def __init__(self, *args, **kwargs) -> None:
        """Constructor.

        :param on_duplicate_attribute: A strategy for what to do if a
            tag includes the same attribute more than once. Accepted
            values are: REPLACE (replace earlier values with later
            ones, the default), IGNORE (keep the earliest value
            encountered), or a callable. A callable must take three
            arguments: the dictionary of attributes already processed,
            the name of the duplicate attribute, and the most recent value
            encountered.           
        """
        ...
    
    def error(self, msg):
        """In Python 3, HTMLParser subclasses must implement error(), although
        this requirement doesn't appear to be documented.

        In Python 2, HTMLParser implements error() by raising an exception,
        which we don't want to do.

        In any event, this method is called only on very strange
        markup and our best strategy is to pretend it didn't happen
        and keep going.
        """
        ...
    
    def handle_startendtag(self, name, attrs):
        """Handle an incoming empty-element tag.

        This is only called when the markup looks like <tag/>.

        :param name: Name of the tag.
        :param attrs: Dictionary of the tag's attributes.
        """
        ...
    
    def handle_starttag(self, name, attrs, handle_empty_element=...):
        """Handle an opening tag, e.g. '<tag>'

        :param name: Name of the tag.
        :param attrs: Dictionary of the tag's attributes.
        :param handle_empty_element: True if this tag is known to be
            an empty-element tag (i.e. there is not expected to be any
            closing tag).
        """
        ...
    
    def handle_endtag(self, name, check_already_closed=...):
        """Handle a closing tag, e.g. '</tag>'
        
        :param name: A tag name.
        :param check_already_closed: True if this tag is expected to
           be the closing portion of an empty-element tag,
           e.g. '<tag></tag>'.
        """
        ...
    
    def handle_data(self, data):
        """Handle some textual data that shows up between tags."""
        ...
    
    def handle_charref(self, name):
        """Handle a numeric character reference by converting it to the
        corresponding Unicode character and treating it as textual
        data.

        :param name: Character number, possibly in hexadecimal.
        """
        ...
    
    def handle_entityref(self, name):
        """Handle a named entity reference by converting it to the
        corresponding Unicode character and treating it as textual
        data.

        :param name: Name of the entity reference.
        """
        ...
    
    def handle_comment(self, data):
        """Handle an HTML comment.

        :param data: The text of the comment.
        """
        ...
    
    def handle_decl(self, data):
        """Handle a DOCTYPE declaration.

        :param data: The text of the declaration.
        """
        ...
    
    def unknown_decl(self, data):
        """Handle a declaration of unknown type -- probably a CDATA block.

        :param data: The text of the declaration.
        """
        ...
    
    def handle_pi(self, data):
        """Handle a processing instruction.

        :param data: The text of the instruction.
        """
        ...
    


class HTMLParserTreeBuilder(HTMLTreeBuilder):
    """A Beautiful soup `TreeBuilder` that uses the `HTMLParser` parser,
    found in the Python standard library.
    """
    is_xml = ...
    picklable = ...
    NAME = ...
    features = ...
    TRACKS_LINE_NUMBERS = ...
    def __init__(self, parser_args=..., parser_kwargs=..., **kwargs) -> None:
        """Constructor.

        :param parser_args: Positional arguments to pass into 
            the BeautifulSoupHTMLParser constructor, once it's
            invoked.
        :param parser_kwargs: Keyword arguments to pass into 
            the BeautifulSoupHTMLParser constructor, once it's
            invoked.
        :param kwargs: Keyword arguments for the superclass constructor.
        """
        ...
    
    def prepare_markup(self, markup, user_specified_encoding=..., document_declared_encoding=..., exclude_encodings=...):
        """Run any preliminary steps necessary to make incoming markup
        acceptable to the parser.

        :param markup: Some markup -- probably a bytestring.
        :param user_specified_encoding: The user asked to try this encoding.
        :param document_declared_encoding: The markup itself claims to be
            in this encoding.
        :param exclude_encodings: The user asked _not_ to try any of
            these encodings.

        :yield: A series of 4-tuples:
         (markup, encoding, declared encoding,
          has undergone character replacement)

         Each 4-tuple represents a strategy for converting the
         document to Unicode and parsing it. Each strategy will be tried 
         in turn.
        """
        ...
    
    def feed(self, markup):
        """Run some incoming markup through some parsing process,
        populating the `BeautifulSoup` object in self.soup.
        """
        ...
    


if major == 3 and minor == 2 and not CONSTRUCTOR_TAKES_STRICT:
    attrfind_tolerant = ...
    locatestarttagend = ...
    def parse_starttag(self, i):
        ...
    
    def set_cdata_mode(self, elem):
        ...
    
    CONSTRUCTOR_TAKES_STRICT = ...
