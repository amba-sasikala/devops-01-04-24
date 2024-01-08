from app import hello

#This catches a future bug
#############1=1##############

def test_hello():
    assert "bob" in hello("bob")