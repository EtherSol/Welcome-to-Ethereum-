from brownie import accounts,config, SimpleStorage

def main():
    account = accounts[0]
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

main()