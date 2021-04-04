"""
This type stub file was generated by pyright.
"""

"""Beautiful Soup bonus library: Unicode, Dammit

This library converts a bytestream to Unicode through any means
necessary. It is heavily based on code from Mark Pilgrim's Universal
Feed Parser. It works best on XML and HTML, but it does not rewrite the
XML or HTML to reflect a new encoding; that's the tree builder's job.
"""
__license__ = ...
chardet_type = ...
xml_encoding = ...
html_meta = ...
encoding_res = ...
class EntitySubstitution(object):
    """The ability to substitute XML or HTML entities for certain characters."""
    CHARACTER_TO_XML_ENTITY = ...
    BARE_AMPERSAND_OR_BRACKET = ...
    AMPERSAND_OR_BRACKET = ...
    @classmethod
    def quoted_attribute_value(self, value):
        """Make a value into a quoted XML attribute, possibly escaping it.

         Most strings will be quoted using double quotes.

          Bob's Bar -> "Bob's Bar"

         If a string contains double quotes, it will be quoted using
         single quotes.

          Welcome to "my bar" -> 'Welcome to "my bar"'

         If a string contains both single and double quotes, the
         double quotes will be escaped, and the string will be quoted
         using double quotes.

          Welcome to "Bob's Bar" -> "Welcome to &quot;Bob's bar&quot;
        """
        ...
    
    @classmethod
    def substitute_xml(cls, value, make_quoted_attribute=...):
        """Substitute XML entities for special XML characters.

        :param value: A string to be substituted. The less-than sign
          will become &lt;, the greater-than sign will become &gt;,
          and any ampersands will become &amp;. If you want ampersands
          that appear to be part of an entity definition to be left
          alone, use substitute_xml_containing_entities() instead.

        :param make_quoted_attribute: If True, then the string will be
         quoted, as befits an attribute value.
        """
        ...
    
    @classmethod
    def substitute_xml_containing_entities(cls, value, make_quoted_attribute=...):
        """Substitute XML entities for special XML characters.

        :param value: A string to be substituted. The less-than sign will
          become &lt;, the greater-than sign will become &gt;, and any
          ampersands that are not part of an entity defition will
          become &amp;.

        :param make_quoted_attribute: If True, then the string will be
         quoted, as befits an attribute value.
        """
        ...
    
    @classmethod
    def substitute_html(cls, s):
        """Replace certain Unicode characters with named HTML entities.

        This differs from data.encode(encoding, 'xmlcharrefreplace')
        in that the goal is to make the result more readable (to those
        with ASCII displays) rather than to recover from
        errors. There's absolutely nothing wrong with a UTF-8 string
        containg a LATIN SMALL LETTER E WITH ACUTE, but replacing that
        character with "&eacute;" will make it more readable to some
        people.

        :param s: A Unicode string.
        """
        ...
    


class EncodingDetector:
    """Suggests a number of possible encodings for a bytestring.

    Order of precedence:

    1. Encodings you specifically tell EncodingDetector to try first
    (the override_encodings argument to the constructor).

    2. An encoding declared within the bytestring itself, either in an
    XML declaration (if the bytestring is to be interpreted as an XML
    document), or in a <meta> tag (if the bytestring is to be
    interpreted as an HTML document.)

    3. An encoding detected through textual analysis by chardet,
    cchardet, or a similar external library.

    4. UTF-8.

    5. Windows-1252.
    """
    def __init__(self, markup, override_encodings=..., is_html=..., exclude_encodings=...) -> None:
        """Constructor.

        :param markup: Some markup in an unknown encoding.
        :param override_encodings: These encodings will be tried first.
        :param is_html: If True, this markup is considered to be HTML. Otherwise
            it's assumed to be XML.
        :param exclude_encodings: These encodings will not be tried, even
            if they otherwise would be.
        """
        ...
    
    @property
    def encodings(self):
        """Yield a number of encodings that might work for this markup.

        :yield: A sequence of strings.
        """
        ...
    
    @classmethod
    def strip_byte_order_mark(cls, data):
        """If a byte-order mark is present, strip it and return the encoding it implies.

        :param data: Some markup.
        :return: A 2-tuple (modified data, implied encoding)
        """
        ...
    
    @classmethod
    def find_declared_encoding(cls, markup, is_html=..., search_entire_document=...):
        """Given a document, tries to find its declared encoding.

        An XML encoding is declared at the beginning of the document.

        An HTML encoding is declared in a <meta> tag, hopefully near the
        beginning of the document.

        :param markup: Some markup.
        :param is_html: If True, this markup is considered to be HTML. Otherwise
            it's assumed to be XML.
        :param search_entire_document: Since an encoding is supposed to declared near the beginning
            of the document, most of the time it's only necessary to search a few kilobytes of data.
            Set this to True to force this method to search the entire document.
        """
        ...
    


class UnicodeDammit:
    """A class for detecting the encoding of a *ML document and
    converting it to a Unicode string. If the source encoding is
    windows-1252, can replace MS smart quotes with their HTML or XML
    equivalents."""
    CHARSET_ALIASES = ...
    ENCODINGS_WITH_SMART_QUOTES = ...
    def __init__(self, markup, override_encodings=..., smart_quotes_to=..., is_html=..., exclude_encodings=...) -> None:
        """Constructor.

        :param markup: A bytestring representing markup in an unknown encoding.
        :param override_encodings: These encodings will be tried first,
           before any sniffing code is run.

        :param smart_quotes_to: By default, Microsoft smart quotes will, like all other characters, be converted
           to Unicode characters. Setting this to 'ascii' will convert them to ASCII quotes instead.
           Setting it to 'xml' will convert them to XML entity references, and setting it to 'html'
           will convert them to HTML entity references.
        :param is_html: If True, this markup is considered to be HTML. Otherwise
            it's assumed to be XML.
        :param exclude_encodings: These encodings will not be considered, even
            if the sniffing code thinks they might make sense.
        """
        ...
    
    @property
    def declared_html_encoding(self):
        """If the markup is an HTML document, returns the encoding declared _within_
        the document.
        """
        ...
    
    def find_codec(self, charset):
        """Convert the name of a character set to a codec name.

        :param charset: The name of a character set.
        :return: The name of a codec.
        """
        ...
    
    MS_CHARS = ...
    MS_CHARS_TO_ASCII = ...
    WINDOWS_1252_TO_UTF8 = ...
    MULTIBYTE_MARKERS_AND_SIZES = ...
    FIRST_MULTIBYTE_MARKER = ...
    LAST_MULTIBYTE_MARKER = ...
    @classmethod
    def detwingle(cls, in_bytes, main_encoding=..., embedded_encoding=...):
        """Fix characters from one encoding embedded in some other encoding.

        Currently the only situation supported is Windows-1252 (or its
        subset ISO-8859-1), embedded in UTF-8.

        :param in_bytes: A bytestring that you suspect contains
            characters from multiple encodings. Note that this _must_
            be a bytestring. If you've already converted the document
            to Unicode, you're too late.
        :param main_encoding: The primary encoding of `in_bytes`.
        :param embedded_encoding: The encoding that was used to embed characters
            in the main document.
        :return: A bytestring in which `embedded_encoding`
          characters have been converted to their `main_encoding`
          equivalents.
        """
        ...
    


