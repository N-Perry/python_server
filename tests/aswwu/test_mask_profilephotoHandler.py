import requests
import json
from tests.utils import profile, archived_profile, gen_profiles

def test_profile_photo_handler_current_year_no_profile(testing_server, peopledb_conn):

    expected_data = {
        "error": "no profile found"
    }

    with profile(peopledb_conn, list(gen_profiles(number = 3))):
        url = "http://127.0.0.1:8888/profile_photo/1718/test.profile"
        resp = requests.get(url)
    assert (resp.status_code == 200)
    assert (json.loads(resp.text) == expected_data)


def test_profile_photo_handler_current_year(testing_server, peopledb_conn):

    expected_url = "https://aswwu.com/media/img-sm/profiles/1617/00000-9000001.jpg"


    with profile(peopledb_conn, list(gen_profiles(number = 3))):
        url = "http://127.0.0.1:8888/profile_photo/1718/test.profile1"
        resp = requests.get(url, allow_redirects=True)
    # this request is being redirected
    assert (resp.history[0].status_code == 302)
    assert (resp.url == expected_url)

def test_profile_photo_handler_current_year_another_profile(testing_server, peopledb_conn):

    expected_url = "https://aswwu.com/media/img-sm/profiles/1617/00000-9000002.jpg"


    with profile(peopledb_conn, list(gen_profiles(number = 3))):
        url = "http://127.0.0.1:8888/profile_photo/1718/test.profile2"
        resp = requests.get(url, allow_redirects=True)
    # this request is being redirected
    assert (resp.history[0].status_code == 302)
    assert (resp.url == expected_url)
