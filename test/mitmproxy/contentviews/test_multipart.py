from . import full_eval
from mitmproxy.contentviews import multipart


def test_view_multipart():
    view = full_eval(multipart.ViewMultipart())
    v = b"""
--AaB03x
Content-Disposition: form-data; name="submit-name"

Larry
--AaB03x
        """.strip()
    assert view(v, content_type="multipart/form-data; boundary=AaB03x")

    assert not view(v)

    assert not view(v, content_type="multipart/form-data")

    assert not view(v, content_type="unparseable")


def test_render_priority():
    v = multipart.ViewMultipart()
    assert v.render_priority(b"data", content_type="multipart/form-data")
    assert not v.render_priority(b"data", content_type="text/plain")
