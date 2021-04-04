"""
This type stub file was generated by pyright.
"""

__license__ = ...
from typing import Any, Dict, Iterator

DEFAULT_OUTPUT_ENCODING = ...
PY3K = ...
nonwhitespace_re = ...
whitespace_re = ...
PYTHON_SPECIFIC_ENCODINGS = ...


class NamespacedAttribute(str):
    """A namespaced string (e.g. 'xml:lang') that remembers the namespace
    ('xml') and the name ('lang') that were used to create it.
    """
    def __new__(cls, prefix, name=..., namespace=...):
        ...


class AttributeValueWithCharsetSubstitution(str):
    """A stand-in object for a character encoding specified in HTML."""
    ...


class CharsetMetaAttributeValue(AttributeValueWithCharsetSubstitution):
    """A generic stand-in for the value of a meta tag's 'charset' attribute.

    When Beautiful Soup parses the markup '<meta charset="utf8">', the
    value of the 'charset' attribute will be one of these objects.
    """
    def __new__(cls, original_value):
        ...

    def encode(self, encoding):
        """When an HTML document is being encoded to a given encoding, the
        value of a meta tag's 'charset' is the name of the encoding.
        """
        ...


class ContentMetaAttributeValue(AttributeValueWithCharsetSubstitution):
    """A generic stand-in for the value of a meta tag's 'content' attribute.

    When Beautiful Soup parses the markup:
     <meta http-equiv="content-type" content="text/html; charset=utf8">

    The value of the 'content' attribute will be one of these objects.
    """
    CHARSET_RE = ...

    def __new__(cls, original_value):
        ...

    def encode(self, encoding):
        ...


class PageElement(object):
    """Contains the navigational information for some part of the page:
    that is, its current location in the parse tree.

    NavigableString, Tag, etc. are all subclasses of PageElement.
    """
    def setup(self,
              parent=...,
              previous_element=...,
              next_element=...,
              previous_sibling=...,
              next_sibling=...):
        """Sets up the initial relations between this element and
        other elements.

        :param parent: The parent of this element.

        :param previous_element: The element parsed immediately before
            this one.
        
        :param next_element: The element parsed immediately before
            this one.

        :param previous_sibling: The most recently encountered element
            on the same level of the parse tree as this one.

        :param previous_sibling: The next element to be encountered
            on the same level of the parse tree as this one.
        """
        ...

    def format_string(self, s, formatter):
        """Format the given string using the given formatter.

        :param s: A string.
        :param formatter: A Formatter object, or a string naming one of the standard formatters.
        """
        ...

    def formatter_for_name(self, formatter):
        """Look up or create a Formatter for the given identifier,
        if necessary.

        :param formatter: Can be a Formatter object (used as-is), a
            function (used as the entity substitution hook for an
            XMLFormatter or HTMLFormatter), or a string (used to look
            up an XMLFormatter or HTMLFormatter in the appropriate
            registry.
        """
        ...

    nextSibling = ...
    previousSibling = ...

    def replace_with(self, replace_with):
        """Replace this PageElement with another one, keeping the rest of the
        tree the same.
        
        :param replace_with: A PageElement.
        :return: `self`, no longer part of the tree.
        """
        ...

    replaceWith = ...

    def unwrap(self):
        """Replace this PageElement with its contents.

        :return: `self`, no longer part of the tree.
        """
        ...

    replace_with_children = ...
    replaceWithChildren = ...

    def wrap(self, wrap_inside):
        """Wrap this PageElement inside another one.

        :param wrap_inside: A PageElement.
        :return: `wrap_inside`, occupying the position in the tree that used
           to be occupied by `self`, and with `self` inside it.
        """
        ...

    def extract(self, _self_index=...):
        """Destructively rips this element out of the tree.

        :param _self_index: The location of this element in its parent's
           .contents, if known. Passing this in allows for a performance
           optimization.

        :return: `self`, no longer part of the tree.
        """
        ...

    _lastRecursiveChild = ...

    def insert(self, position, new_child):
        """Insert a new PageElement in the list of this PageElement's children.

        This works the same way as `list.insert`.

        :param position: The numeric position that should be occupied
           in `self.children` by the new PageElement. 
        :param new_child: A PageElement.
        """
        ...

    def append(self, tag):
        """Appends the given PageElement to the contents of this one.

        :param tag: A PageElement.
        """
        ...

    def extend(self, tags):
        """Appends the given PageElements to this one's contents.

        :param tags: A list of PageElements.
        """
        ...

    def insert_before(self, *args):
        """Makes the given element(s) the immediate predecessor of this one.

        All the elements will have the same parent, and the given elements
        will be immediately before this one.

        :param args: One or more PageElements.
        """
        ...

    def insert_after(self, *args):
        """Makes the given element(s) the immediate successor of this one.

        The elements will have the same parent, and the given elements
        will be immediately after this one.

        :param args: One or more PageElements.
        """
        ...

    def find_next(self, name=..., attrs=..., text=..., **kwargs):
        """Find the first PageElement that matches the given criteria and
        appears later in the document than this PageElement.

        All find_* methods take a common set of arguments. See the online
        documentation for detailed explanations.

        :param name: A filter on tag name.
        :param attrs: A dictionary of filters on attribute values.
        :param text: A filter for a NavigableString with specific text.
        :kwargs: A dictionary of filters on attribute values.
        :return: A PageElement.
        :rtype: bs4.element.Tag | bs4.element.NavigableString
        """
        ...

    findNext = ...

    def find_all_next(self,
                      name=...,
                      attrs=...,
                      text=...,
                      limit=...,
                      **kwargs):
        """Find all PageElements that match the given criteria and appear
        later in the document than this PageElement.

        All find_* methods take a common set of arguments. See the online
        documentation for detailed explanations.

        :param name: A filter on tag name.
        :param attrs: A dictionary of filters on attribute values.
        :param text: A filter for a NavigableString with specific text.
        :param limit: Stop looking after finding this many results.
        :kwargs: A dictionary of filters on attribute values.
        :return: A ResultSet containing PageElements.
        """
        ...

    findAllNext = ...

    def find_next_sibling(self, name=..., attrs=..., text=..., **kwargs):
        """Find the closest sibling to this PageElement that matches the
        given criteria and appears later in the document.

        All find_* methods take a common set of arguments. See the
        online documentation for detailed explanations.

        :param name: A filter on tag name.
        :param attrs: A dictionary of filters on attribute values.
        :param text: A filter for a NavigableString with specific text.
        :kwargs: A dictionary of filters on attribute values.
        :return: A PageElement.
        :rtype: bs4.element.Tag | bs4.element.NavigableString
        """
        ...

    findNextSibling = ...

    def find_next_siblings(self,
                           name=...,
                           attrs=...,
                           text=...,
                           limit=...,
                           **kwargs):
        """Find all siblings of this PageElement that match the given criteria
        and appear later in the document.

        All find_* methods take a common set of arguments. See the online
        documentation for detailed explanations.

        :param name: A filter on tag name.
        :param attrs: A dictionary of filters on attribute values.
        :param text: A filter for a NavigableString with specific text.
        :param limit: Stop looking after finding this many results.
        :kwargs: A dictionary of filters on attribute values.
        :return: A ResultSet of PageElements.
        :rtype: bs4.element.ResultSet
        """
        ...

    findNextSiblings = ...
    fetchNextSiblings = ...

    def find_previous(self, name=..., attrs=..., text=..., **kwargs):
        """Look backwards in the document from this PageElement and find the
        first PageElement that matches the given criteria.

        All find_* methods take a common set of arguments. See the online
        documentation for detailed explanations.

        :param name: A filter on tag name.
        :param attrs: A dictionary of filters on attribute values.
        :param text: A filter for a NavigableString with specific text.
        :kwargs: A dictionary of filters on attribute values.
        :return: A PageElement.
        :rtype: bs4.element.Tag | bs4.element.NavigableString
        """
        ...

    findPrevious = ...

    def find_all_previous(self,
                          name=...,
                          attrs=...,
                          text=...,
                          limit=...,
                          **kwargs):
        """Look backwards in the document from this PageElement and find all
        PageElements that match the given criteria.

        All find_* methods take a common set of arguments. See the online
        documentation for detailed explanations.

        :param name: A filter on tag name.
        :param attrs: A dictionary of filters on attribute values.
        :param text: A filter for a NavigableString with specific text.
        :param limit: Stop looking after finding this many results.
        :kwargs: A dictionary of filters on attribute values.
        :return: A ResultSet of PageElements.
        :rtype: bs4.element.ResultSet
        """
        ...

    findAllPrevious = ...
    fetchPrevious = ...

    def find_previous_sibling(self, name=..., attrs=..., text=..., **kwargs):
        """Returns the closest sibling to this PageElement that matches the
        given criteria and appears earlier in the document.

        All find_* methods take a common set of arguments. See the online
        documentation for detailed explanations.

        :param name: A filter on tag name.
        :param attrs: A dictionary of filters on attribute values.
        :param text: A filter for a NavigableString with specific text.
        :kwargs: A dictionary of filters on attribute values.
        :return: A PageElement.
        :rtype: bs4.element.Tag | bs4.element.NavigableString
        """
        ...

    findPreviousSibling = ...

    def find_previous_siblings(self,
                               name=...,
                               attrs=...,
                               text=...,
                               limit=...,
                               **kwargs):
        """Returns all siblings to this PageElement that match the
        given criteria and appear earlier in the document.

        All find_* methods take a common set of arguments. See the online
        documentation for detailed explanations.

        :param name: A filter on tag name.
        :param attrs: A dictionary of filters on attribute values.
        :param text: A filter for a NavigableString with specific text.
        :param limit: Stop looking after finding this many results.
        :kwargs: A dictionary of filters on attribute values.
        :return: A ResultSet of PageElements.
        :rtype: bs4.element.ResultSet
        """
        ...

    findPreviousSiblings = ...
    fetchPreviousSiblings = ...

    def find_parent(self, name=..., attrs=..., **kwargs):
        """Find the closest parent of this PageElement that matches the given
        criteria.

        All find_* methods take a common set of arguments. See the online
        documentation for detailed explanations.

        :param name: A filter on tag name.
        :param attrs: A dictionary of filters on attribute values.
        :kwargs: A dictionary of filters on attribute values.

        :return: A PageElement.
        :rtype: bs4.element.Tag | bs4.element.NavigableString
        """
        ...

    findParent = ...

    def find_parents(self, name=..., attrs=..., limit=..., **kwargs):
        """Find all parents of this PageElement that match the given criteria.

        All find_* methods take a common set of arguments. See the online
        documentation for detailed explanations.

        :param name: A filter on tag name.
        :param attrs: A dictionary of filters on attribute values.
        :param limit: Stop looking after finding this many results.
        :kwargs: A dictionary of filters on attribute values.

        :return: A PageElement.
        :rtype: bs4.element.Tag | bs4.element.NavigableString
        """
        ...

    findParents = ...
    fetchParents = ...

    @property
    def next(self):
        """The PageElement, if any, that was parsed just after this one.

        :return: A PageElement.
        :rtype: bs4.element.Tag | bs4.element.NavigableString
        """
        ...

    @property
    def previous(self):
        """The PageElement, if any, that was parsed just before this one.

        :return: A PageElement.
        :rtype: bs4.element.Tag | bs4.element.NavigableString
        """
        ...

    @property
    def next_elements(self):
        """All PageElements that were parsed after this one.

        :yield: A sequence of PageElements.
        """
        ...

    @property
    def next_siblings(self):
        """All PageElements that are siblings of this one but were parsed
        later.

        :yield: A sequence of PageElements.
        """
        ...

    @property
    def previous_elements(self):
        """All PageElements that were parsed before this one.

        :yield: A sequence of PageElements.
        """
        ...

    @property
    def previous_siblings(self):
        """All PageElements that are siblings of this one but were parsed
        earlier.

        :yield: A sequence of PageElements.
        """
        ...

    @property
    def parents(self):
        """All PageElements that are parents of this PageElement.

        :yield: A sequence of PageElements.
        """
        ...

    @property
    def decomposed(self):
        """Check whether a PageElement has been decomposed.

        :rtype: bool
        """
        ...

    def nextGenerator(self):
        ...

    def nextSiblingGenerator(self):
        ...

    def previousGenerator(self):
        ...

    def previousSiblingGenerator(self):
        ...

    def parentGenerator(self):
        ...


class NavigableString(str, PageElement):
    """A Python Unicode string that is part of a parse tree.

    When Beautiful Soup parses the markup <b>penguin</b>, it will
    create a NavigableString for the string "penguin".
    """
    PREFIX = ...
    SUFFIX = ...
    known_xml = ...

    def __new__(cls, value):
        """Create a new NavigableString.

        When unpickling a NavigableString, this method is called with
        the string in DEFAULT_OUTPUT_ENCODING. That encoding needs to be
        passed in to the superclass's __new__ or the superclass won't know
        how to handle non-ASCII characters.
        """
        ...

    def __copy__(self):
        """A copy of a NavigableString has the same contents and class
        as the original, but it is not connected to the parse tree.
        """
        ...

    def __getnewargs__(self):
        ...

    def __getattr__(self, attr):
        """text.string gives you text. This is for backwards
        compatibility for Navigable*String, but for CData* it lets you
        get the string without the CData wrapper."""
        ...

    def output_ready(self, formatter=...):
        """Run the string through the provided formatter.

        :param formatter: A Formatter object, or a string naming one of the standard formatters.
        """
        ...

    @property
    def name(self):
        """Since a NavigableString is not a Tag, it has no .name.

        This property is implemented so that code like this doesn't crash
        when run on a mixture of Tag and NavigableString objects:
            [x.name for x in tag.children]
        """
        ...

    @name.setter
    def name(self, name):
        """Prevent NavigableString.name from ever being set."""
        ...


class PreformattedString(NavigableString):
    """A NavigableString not subject to the normal formatting rules.

    This is an abstract class used for special kinds of strings such
    as comments (the Comment class) and CDATA blocks (the CData
    class).
    """
    PREFIX = ...
    SUFFIX = ...

    def output_ready(self, formatter=...):
        """Make this string ready for output by adding any subclass-specific
            prefix or suffix.

        :param formatter: A Formatter object, or a string naming one
            of the standard formatters. The string will be passed into the
            Formatter, but only to trigger any side effects: the return
            value is ignored.

        :return: The string, with any subclass-specific prefix and
           suffix added on.
        """
        ...


class CData(PreformattedString):
    """A CDATA block."""
    PREFIX = ...
    SUFFIX = ...


class ProcessingInstruction(PreformattedString):
    """A SGML processing instruction."""
    PREFIX = ...
    SUFFIX = ...


class XMLProcessingInstruction(ProcessingInstruction):
    """An XML processing instruction."""
    PREFIX = ...
    SUFFIX = ...


class Comment(PreformattedString):
    """An HTML or XML comment."""
    PREFIX = ...
    SUFFIX = ...


class Declaration(PreformattedString):
    """An XML declaration."""
    PREFIX = ...
    SUFFIX = ...


class Doctype(PreformattedString):
    """A document type declaration."""
    @classmethod
    def for_name_and_ids(cls, name, pub_id, system_id):
        """Generate an appropriate document type declaration for a given
        public ID and system ID.

        :param name: The name of the document's root element, e.g. 'html'.
        :param pub_id: The Formal Public Identifier for this document type,
            e.g. '-//W3C//DTD XHTML 1.1//EN'
        :param system_id: The system identifier for this document type,
            e.g. 'http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd'

        :return: A Doctype.
        """
        ...

    PREFIX = ...
    SUFFIX = ...


class Stylesheet(NavigableString):
    """A NavigableString representing an stylesheet (probably
    CSS).

    Used to distinguish embedded stylesheets from textual content.
    """
    ...


class Script(NavigableString):
    """A NavigableString representing an executable script (probably
    Javascript).

    Used to distinguish executable code from textual content.
    """
    ...


class TemplateString(NavigableString):
    """A NavigableString representing a string found inside an HTML
    template embedded in a larger document.

    Used to distinguish such strings from the main body of the document.
    """
    ...


class Tag(PageElement):
    """Represents an HTML or XML tag that is part of a parse tree, along
    with its attributes and contents.

    When Beautiful Soup parses the markup <b>penguin</b>, it will
    create a Tag object representing the <b> tag.
    """
    def __init__(self,
                 parser=...,
                 builder=...,
                 name=...,
                 namespace=...,
                 prefix=...,
                 attrs=...,
                 parent=...,
                 previous=...,
                 is_xml=...,
                 sourceline=...,
                 sourcepos=...,
                 can_be_empty_element=...,
                 cdata_list_attributes=...,
                 preserve_whitespace_tags=...) -> None:
        """Basic constructor.

        :param parser: A BeautifulSoup object.
        :param builder: A TreeBuilder.
        :param name: The name of the tag.
        :param namespace: The URI of this Tag's XML namespace, if any.
        :param prefix: The prefix for this Tag's XML namespace, if any.
        :param attrs: A dictionary of this Tag's attribute values.
        :param parent: The PageElement to use as this Tag's parent.
        :param previous: The PageElement that was parsed immediately before
            this tag.
        :param is_xml: If True, this is an XML tag. Otherwise, this is an
            HTML tag.
        :param sourceline: The line number where this tag was found in its
            source document.
        :param sourcepos: The character position within `sourceline` where this
            tag was found.
        :param can_be_empty_element: If True, this tag should be
            represented as <tag/>. If False, this tag should be represented
            as <tag></tag>.
        :param cdata_list_attributes: A list of attributes whose values should
            be treated as CDATA if they ever show up on this tag.
        :param preserve_whitespace_tags: A list of tag names whose contents
            should have their whitespace preserved.
        """
        ...

    parserClass = ...

    def __copy__(self):
        """A copy of a Tag is a new Tag, unconnected to the parse tree.
        Its contents are a copy of the old Tag's contents.
        """
        ...

    @property
    def is_empty_element(self):
        """Is this tag an empty-element tag? (aka a self-closing tag)

        A tag that has contents is never an empty-element tag.

        A tag that has no contents may or may not be an empty-element
        tag. It depends on the builder used to create the tag. If the
        builder has a designated list of empty-element tags, then only
        a tag whose name shows up in that list is considered an
        empty-element tag.

        If the builder has no designated list of empty-element tags,
        then any tag with no contents is an empty-element tag.
        """
        ...

    isSelfClosing = ...

    @property
    def string(self):
        """Convenience property to get the single string within this
        PageElement.

        TODO It might make sense to have NavigableString.string return
        itself.

        :return: If this element has a single string child, return
         value is that string. If this element has one child tag,
         return value is the 'string' attribute of the child tag,
         recursively. If this element is itself a string, has no
         children, or has more than one child, return value is None.
        """
        ...

    @string.setter
    def string(self, string):
        """Replace this PageElement's contents with `string`."""
        ...

    strings = ...

    @property
    def stripped_strings(self):
        """Yield all strings in the document, stripping them first.

        :yield: A sequence of stripped strings.
        """
        ...

    def get_text(self, separator=..., strip=..., types=...):
        """Get all child strings, concatenated using the given separator.

        :param separator: Strings will be concatenated using this separator.

        :param strip: If True, strings will be stripped before being
            concatenated.

        :types: A tuple of NavigableString subclasses. Any strings of
            a subclass not found in this list will be ignored. By
            default, this means only NavigableString and CData objects
            will be considered. So no comments, processing instructions,
            stylesheets, etc.

        :return: A string.
        """
        ...

    getText = ...
    text = ...

    def decompose(self):
        """Recursively destroys this PageElement and its children.

        This element will be removed from the tree and wiped out; so
        will everything beneath it.

        The behavior of a decomposed PageElement is undefined and you
        should never use one for anything, but if you need to _check_
        whether an element has been decomposed, you can use the
        `decomposed` property.
        """
        ...

    def clear(self, decompose=...):
        """Wipe out all children of this PageElement by calling extract()
           on them.

        :param decompose: If this is True, decompose() (a more
            destructive method) will be called instead of extract().
        """
        ...

    def smooth(self):
        """Smooth out this element's children by consolidating consecutive
        strings.

        This makes pretty-printed output look more natural following a
        lot of operations that modified the tree.
        """
        ...

    def index(self, element):
        """Find the index of a child by identity, not value.

        Avoids issues with tag.contents.index(element) getting the
        index of equal elements.

        :param element: Look for this PageElement in `self.contents`.
        """
        ...

    def get(self, key: str, default: str=...) -> str:
        """Returns the value of the 'key' attribute for the tag, or
        the value given for 'default' if it doesn't have that
        attribute."""
        ...

    def get_attribute_list(self, key, default=...):
        """The same as get(), but always returns a list.

        :param key: The attribute to look for.
        :param default: Use this value if the attribute is not present
            on this PageElement.
        :return: A list of values, probably containing only a single
            value.
        """
        ...

    def has_attr(self, key):
        """Does this PageElement have an attribute with the given name?"""
        ...

    def __hash__(self) -> int:
        ...

    def __getitem__(self, key):
        """tag[key] returns the value of the 'key' attribute for the Tag,
        and throws an exception if it's not there."""
        ...

    def __iter__(self):
        "Iterating over a Tag iterates over its contents."
        ...

    def __len__(self):
        "The length of a Tag is the length of its list of contents."
        ...

    def __contains__(self, x):
        ...

    def __bool__(self):
        "A tag is non-None even if it has no contents."
        ...

    def __setitem__(self, key, value):
        """Setting tag[key] sets the value of the 'key' attribute for the
        tag."""
        ...

    def __delitem__(self, key):
        "Deleting tag[key] deletes all 'key' attributes for the tag."
        ...

    def __call__(self, *args, **kwargs):
        """Calling a Tag like a function is the same as calling its
        find_all() method. Eg. tag('a') returns a list of all the A tags
        found within this tag."""
        ...

    def __getattr__(self, tag):
        """Calling tag.subtag is the same as calling tag.find(name="subtag")"""
        ...

    def __eq__(self, other) -> bool:
        """Returns true iff this Tag has the same name, the same attributes,
        and the same contents (recursively) as `other`."""
        ...

    def __ne__(self, other) -> bool:
        """Returns true iff this Tag is not identical to `other`,
        as defined in __eq__."""
        ...

    def __repr__(self, encoding=...):
        """Renders this PageElement as a string.

        :param encoding: The encoding to use (Python 2 only).
        :return: Under Python 2, a bytestring; under Python 3,
            a Unicode string.
        """
        ...

    def __unicode__(self):
        """Renders this PageElement as a Unicode string."""
        ...

    def __str__(self) -> str:
        """Renders this PageElement as a generic string.

        :return: Under Python 2, a UTF-8 bytestring; under Python 3,
            a Unicode string.        
        """
        ...

    if PY3K:
        __str__ = ...

    def encode(self,
               encoding=...,
               indent_level=...,
               formatter=...,
               errors=...):
        """Render a bytestring representation of this PageElement and its
        contents.

        :param encoding: The destination encoding.
        :param indent_level: Each line of the rendering will be
            indented this many spaces. Used internally in
            recursive calls while pretty-printing.
        :param formatter: A Formatter object, or a string naming one of
            the standard formatters.
        :param errors: An error handling strategy such as
            'xmlcharrefreplace'. This value is passed along into
            encode() and its value should be one of the constants
            defined by Python.
        :return: A bytestring.

        """
        ...

    def decode(self, indent_level=..., eventual_encoding=..., formatter=...):
        """Render a Unicode representation of this PageElement and its
        contents.

        :param indent_level: Each line of the rendering will be
             indented this many spaces. Used internally in
             recursive calls while pretty-printing.
        :param eventual_encoding: The tag is destined to be
            encoded into this encoding. This method is _not_
            responsible for performing that encoding. This information
            is passed in so that it can be substituted in if the
            document contains a <META> tag that mentions the document's
            encoding.
        :param formatter: A Formatter object, or a string naming one of
            the standard formatters.
        """
        ...

    def prettify(self, encoding=..., formatter=...):
        """Pretty-print this PageElement as a string.

        :param encoding: The eventual encoding of the string. If this is None,
            a Unicode string will be returned.
        :param formatter: A Formatter object, or a string naming one of
            the standard formatters.
        :return: A Unicode string (if encoding==None) or a bytestring 
            (otherwise).
        """
        ...

    def decode_contents(self,
                        indent_level=...,
                        eventual_encoding=...,
                        formatter=...):
        """Renders the contents of this tag as a Unicode string.

        :param indent_level: Each line of the rendering will be
           indented this many spaces. Used internally in
           recursive calls while pretty-printing.

        :param eventual_encoding: The tag is destined to be
           encoded into this encoding. decode_contents() is _not_
           responsible for performing that encoding. This information
           is passed in so that it can be substituted in if the
           document contains a <META> tag that mentions the document's
           encoding.

        :param formatter: A Formatter object, or a string naming one of
            the standard Formatters.
        """
        ...

    def encode_contents(self, indent_level=..., encoding=..., formatter=...):
        """Renders the contents of this PageElement as a bytestring.

        :param indent_level: Each line of the rendering will be
           indented this many spaces. Used internally in
           recursive calls while pretty-printing.

        :param eventual_encoding: The bytestring will be in this encoding.

        :param formatter: A Formatter object, or a string naming one of
            the standard Formatters.

        :return: A bytestring.
        """
        ...

    def renderContents(self, encoding=..., prettyPrint=..., indentLevel=...):
        """Deprecated method for BS3 compatibility."""
        ...

    def find(self, name=..., attrs=..., recursive=..., text=..., **kwargs):
        """Look in the children of this PageElement and find the first
        PageElement that matches the given criteria.

        All find_* methods take a common set of arguments. See the online
        documentation for detailed explanations.

        :param name: A filter on tag name.
        :param attrs: A dictionary of filters on attribute values.
        :param recursive: If this is True, find() will perform a
            recursive search of this PageElement's children. Otherwise,
            only the direct children will be considered.
        :param limit: Stop looking after finding this many results.
        :kwargs: A dictionary of filters on attribute values.
        :return: A PageElement.
        :rtype: bs4.element.Tag | bs4.element.NavigableString
        """
        ...

    findChild = ...

    def find_all(self,
                 name: str = ...,
                 attrs: Dict[str, str] = ...,
                 recursive: bool = ...,
                 text: str = ...,
                 limit: int = ...,
                 **kwargs: Any) -> ResultSet:
        """Look in the children of this PageElement and find all
        PageElements that match the given criteria.

        All find_* methods take a common set of arguments. See the online
        documentation for detailed explanations.

        :param name: A filter on tag name.
        :param attrs: A dictionary of filters on attribute values.
        :param recursive: If this is True, find_all() will perform a
            recursive search of this PageElement's children. Otherwise,
            only the direct children will be considered.
        :param limit: Stop looking after finding this many results.
        :kwargs: A dictionary of filters on attribute values.
        :return: A ResultSet of PageElements.
        :rtype: bs4.element.ResultSet
        """
        ...

    findAll = ...
    findChildren = ...

    @property
    def children(self):
        """Iterate over all direct children of this PageElement.

        :yield: A sequence of PageElements.
        """
        ...

    @property
    def descendants(self):
        """Iterate over all children of this PageElement in a
        breadth-first sequence.

        :yield: A sequence of PageElements.
        """
        ...

    def select_one(self, selector, namespaces=..., **kwargs):
        """Perform a CSS selection operation on the current element.

        :param selector: A CSS selector.

        :param namespaces: A dictionary mapping namespace prefixes
           used in the CSS selector to namespace URIs. By default,
           Beautiful Soup will use the prefixes it encountered while
           parsing the document.

        :param kwargs: Keyword arguments to be passed into SoupSieve's 
           soupsieve.select() method.

        :return: A Tag.
        :rtype: bs4.element.Tag
        """
        ...

    def select(self,
               selector: str,
               namespaces: Dict[str, str] = ...,
               limit: int = ...,
               **kwargs: Any) -> ResultSet:
        """Perform a CSS selection operation on the current element.

        This uses the SoupSieve library.

        :param selector: A string containing a CSS selector.

        :param namespaces: A dictionary mapping namespace prefixes
           used in the CSS selector to namespace URIs. By default,
           Beautiful Soup will use the prefixes it encountered while
           parsing the document.

        :param limit: After finding this number of results, stop looking.

        :param kwargs: Keyword arguments to be passed into SoupSieve's 
           soupsieve.select() method.

        :return: A ResultSet of Tags.
        :rtype: bs4.element.ResultSet
        """
        ...

    def childGenerator(self):
        """Deprecated generator."""
        ...

    def recursiveChildGenerator(self):
        """Deprecated generator."""
        ...

    def has_key(self, key):
        """Deprecated method. This was kind of misleading because has_key()
        (attributes) was different from __in__ (contents).

        has_key() is gone in Python 3, anyway.
        """
        ...


class SoupStrainer(object):
    """Encapsulates a number of ways of matching a markup element (tag or
    string).

    This is primarily used to underpin the find_* methods, but you can
    create one yourself and pass it in as `parse_only` to the
    `BeautifulSoup` constructor, to parse a subset of a large
    document.
    """
    def __init__(self, name=..., attrs=..., text=..., **kwargs) -> None:
        """Constructor.

        The SoupStrainer constructor takes the same arguments passed
        into the find_* methods. See the online documentation for
        detailed explanations.

        :param name: A filter on tag name.
        :param attrs: A dictionary of filters on attribute values.
        :param text: A filter for a NavigableString with specific text.
        :kwargs: A dictionary of filters on attribute values.
        """
        ...

    def __str__(self) -> str:
        """A human-readable representation of this SoupStrainer."""
        ...

    def search_tag(self, markup_name=..., markup_attrs=...):
        """Check whether a Tag with the given name and attributes would
        match this SoupStrainer.

        Used prospectively to decide whether to even bother creating a Tag
        object.

        :param markup_name: A tag name as found in some markup.
        :param markup_attrs: A dictionary of attributes as found in some markup.

        :return: True if the prospective tag would match this SoupStrainer;
            False otherwise.
        """
        ...

    searchTag = ...

    def search(self, markup):
        """Find all items in `markup` that match this SoupStrainer.

        Used by the core _find_all() method, which is ultimately
        called by all find_* methods.

        :param markup: A PageElement or a list of them.
        """
        ...


class ResultSet(list):
    """A ResultSet is just a list that keeps track of the SoupStrainer
    that created it."""
    def __init__(self, source, result=...) -> None:
        """Constructor.

        :param source: A SoupStrainer.
        :param result: A list of PageElements.
        """
        ...

    def __getattr__(self, key: int) -> Tag:
        """Raise a helpful exception to explain a common code fix."""
        ...

    def __getitem__(self, key: int) -> Tag:
        ...

    def __iter__(self) -> Iterator[Tag]: ...