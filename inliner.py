import logging
import argparse
import mimetypes
import base64

from lxml import html

logger = logging.getLogger(__name__)


def get_bytes(filename):
    with open(filename) as f:
        return f.read()


def process_file(filename):
    tree = html.fromstring(get_bytes(filename))
    for img in tree.xpath("//img"):
        src = img.get("src")
        img_data = get_bytes(src)
        encoded_img_data = base64.b64encode(img_data)
        mime_type = mimetypes.guess_type(src)[0] or "image/png"
        data_uri = "data:%s;base64,%s" % (mime_type, encoded_img_data)
        img.set("src", data_uri)
    for link in tree.xpath("//link[@rel='stylesheet']"):
        href = link.get("href")
        css = get_bytes(href)
        parent = link.getparent()
        style = html.Element("style")
        style.set("type", "text/css")
        style.text = css
        link.addnext(style)
        parent.remove(link)
    with open(filename, "w") as f:
        f.write(html.tostring(tree))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", nargs="+")
    args = parser.parse_args()

    for filename in args.filename:
        process_file(filename)


if __name__ == "__main__":
    main()
