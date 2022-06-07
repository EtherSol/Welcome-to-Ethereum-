from brownie import accounts,config, SimpleStorage, network

def main():
    account = get_account()
    # print(account)
    # account = accounts.add(config["wallets"]["from_key"])
    # print(account)
    simple_storage = SimpleStorage.deploy({"from":account})
    stored_value = simple_storage.retrieve()
    print(stored_value)

    # Transact
    transaction = simple_storage.store(15, {"from":account})
    transaction.wait(1)
    updated_stored_value = simple_storage.retrieve()
    print(updated_stored_value)
    # Call

def get_account():
    if network.show_active == "development":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


main()