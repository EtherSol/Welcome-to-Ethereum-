from brownie import SimpleStorage, accounts 

def test_deploy():
    # Arrange
    account = accounts[0]
    # Act
    simple_storage = SimpleStorage.deploy({"from": account})
    starting_value = simple_storage.retrieve()
    expected = 15
    # Assert
    starting_value == expected

def test_updating_deploy():
    #Arrange
    account = accounts[0]
    #Act
    expected = 15
    simple_storage = SimpleStorage.store(expected, {"from":account})
    
    #Assert
    assert expected == simple_storage.retrieve()