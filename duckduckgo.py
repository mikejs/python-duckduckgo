import urllib
import urllib2
from xml.etree import ElementTree

__version__ = 0.1


def query(query, useragent='python-duckduckgo 0.1'):
    """
    Query Duck Duck Go, returning a Results object.

    Here's a query that's unlikely to change:

    >>> result = query('1 + 1')
    >>> result.type
    'nothing'
    >>> result.answer.text
    '1 + 1 = 2'
    >>> result.answer.type
    'calc'
    """
    params = urllib.urlencode({'q': query, 'o': 'x'})
    url = 'http://duckduckgo.com/?' + params

    request = urllib2.Request(url, headers={'User-Agent': useragent})
    response = urllib2.urlopen(request)
    xml = ElementTree.fromstring(response.read())
    response.close()

    return Results(xml)


class Results(object):

    def __init__(self, xml):
        self.type = {'A': 'answer', 'D': 'disambiguation',
                     'C': 'category', 'N': 'name',
                     'E': 'exclusive', '': 'nothing'}[xml.findtext('Type', '')]

        self.api_version = xml.attrib.get('version', None)

        self.heading = xml.findtext('Heading', '')

        self.results = [Result(elem) for elem in xml.getiterator('Result')]
        self.related = [Result(elem) for elem in
                        xml.getiterator('RelatedTopic')]

        self.abstract = Abstract(xml)

        answer_xml = xml.find('Answer')
        if answer_xml is not None:
            self.answer = Answer(answer_xml)
            if not self.answer.text:
                self.answer = None
        else:
            self.answer = None

        image_xml = xml.find('Image')
        if image_xml is not None and image_xml.text:
            self.image = Image(image_xml)
        else:
            self.image = None


class Abstract(object):

    def __init__(self, xml):
        self.html = xml.findtext('Abstract', '')
        self.text = xml.findtext('AbstractText', '')
        self.url = xml.findtext('AbstractURL', '')
        self.source = xml.findtext('AbstractSource')


class Result(object):

    def __init__(self, xml):
        self.html = xml.text
        self.text = xml.findtext('Text')
        self.url = xml.findtext('FirstURL')

        icon_xml = xml.find('Icon')
        if icon_xml is not None:
            self.icon = Image(icon_xml)
        else:
            self.icon = None


class Image(object):

    def __init__(self, xml):
        self.url = xml.text
        self.height = xml.attrib.get('height', None)
        self.width = xml.attrib.get('width', None)


class Answer(object):

    def __init__(self, xml):
        self.text = xml.text
        self.type = xml.attrib.get('type', '')
