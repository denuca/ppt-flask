import pytest
from app import app, send_email
from unittest.mock import patch
import io

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index(client):
    rv = client.get('/')
    assert rv.status_code == 200

def test_upload_no_text(client):
    rv = client.post('/upload', data={})
    assert rv.status_code == 400

def test_upload_with_text(client):
    rv = client.post('/upload', data={'text': 'Hello world'})
    assert rv.status_code == 302  # Redirect to download page

def test_upload_with_file(client):
    data = {
        'file': (io.BytesIO(b"Hello world"), 'test.txt')
    }
    rv = client.post('/upload', data=data, content_type='multipart/form-data')
    assert rv.status_code == 302  # Redirect to download page

def test_upload_with_text_and_file(client):
    data = {
        'text': 'Hello world',
        'file': (io.BytesIO(b"Hello world"), 'test.txt')
    }
    rv = client.post('/upload', data=data, content_type='multipart/form-data')
    assert rv.status_code == 400  # Should return an error because both text and file are provided

@patch('app.send_email')
def test_upload_with_email(mock_send_email, client):
    data = {
        'text': 'Hello world',
        'email': 'test@example.com',
        'send_email': '1'
    }
    rv = client.post('/upload', data=data)
    assert rv.status_code == 302  # Redirect to download page
    mock_send_email.assert_called_once()

@patch('app.send_email')
def test_upload_with_file_and_email(mock_send_email, client):
    data = {
        'file': (io.BytesIO(b"Hello world"), 'test.txt'),
        'email': 'test@example.com',
        'send_email': '1'
    }
    rv = client.post('/upload', data=data, content_type='multipart/form-data')
    assert rv.status_code == 302  # Redirect to download page
    mock_send_email.assert_called_once()

@patch('app.send_email')
def test_upload_with_email_no_address(mock_send_email, client):
    data = {
        'text': 'Hello world',
        'email': '',
        'send_email': '1'
    }
    rv = client.post('/upload', data=data)
    assert rv.status_code == 400  # Should return an error because email is checked but no address is provided
