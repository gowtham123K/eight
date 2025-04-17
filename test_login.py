from login import log_in

def test_cases():
    assert((log_in("Asha","12")))=="login unsuccessfull"
    assert((log_in("Asha","1234")))=="login successfull"
    # assert((log_in("A","13"))) =="user doesn't exists"