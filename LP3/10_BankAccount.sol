// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract BankAccount {
    address public customer;
    uint public balance;

    constructor() {
        customer = msg.sender;
    }

    // Deposit ETH to contract
    function deposit() public payable {
        balance += msg.value;
    }

    // Withdraw ETH from contract
    function withdraw(uint amount) public {
        require(msg.sender == customer, "Not the account owner");
        require(amount <= balance, "Insufficient balance");

        balance -= amount;
        payable(msg.sender).transfer(amount);
    }

    // Display balance
    function getBalance() public view returns(uint) {
        return balance;
    }
}
