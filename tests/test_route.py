import json


def test_get_accept_json(client):
    res = client.get('/', headers=[('Accept', 'application/json')])
    assert res.status_code == 200
    expected = {'message': 'Hello, World'}
    assert expected == json.loads(res.get_data(as_text=True))
    assert res.content_type == 'application/json'


def test_post_accept_json(client):
    res = client.post('/', headers=[('Accept', 'application/json')])
    assert res.status_code == 200
    expected = {'message': 'Hello, World'}
    assert expected == json.loads(res.get_data(as_text=True))
    assert res.content_type == 'application/json'


def test_get_accept_non_json(client):
    res = client.post('/', headers=[('Accept', '')])
    assert res.status_code == 200
    expected = "<p>Hello, World</p>"
    assert expected == res.get_data(as_text=True)
    assert 'text/html' in res.content_type
